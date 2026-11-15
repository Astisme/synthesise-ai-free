import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from security_fixtures import validate_security_case, validate_security_suite


class SecurityFixtureTests(unittest.TestCase):
    def setUp(self):
        self.suite = json.loads((ROOT / "evaluations/security/security-cases.json").read_text(encoding="utf-8"))

    def test_all_adversarial_fixtures_are_safe_contracts(self):
        self.assertEqual(validate_security_suite(self.suite), [])

    def test_untrusted_source_cannot_be_promoted_to_trusted(self):
        case = dict(self.suite["cases"][0], trust_level="trusted")
        self.assertTrue(any("must be marked untrusted" in error for error in validate_security_case(case)))

    def test_observed_claim_requires_verified_provenance(self):
        case = dict(self.suite["cases"][2])
        case["claims"] = [{"text": "Unproven statistic", "status": "observed", "sources": [{"source_id": "SRC-X", "locator": "missing", "verified": False}]}]
        self.assertTrue(any("unverified or incomplete source" in error for error in validate_security_case(case)))

    def test_embedded_instruction_cannot_be_removed_from_contract(self):
        case = dict(self.suite["cases"][0], required_controls=["treat_as_data", "attribute_source"])
        self.assertTrue(any("missing security controls" in error for error in validate_security_case(case)))

    def test_fixture_path_cannot_escape_repository_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "repo"
            root.mkdir()
            outside = Path(tmp) / "outside.md"
            outside.write_text("sensitive local file", encoding="utf-8")
            case = dict(self.suite["cases"][0], fixture="../outside.md")
            errors = validate_security_case(case, root)
        self.assertTrue(any("escapes the repository root" in error for error in errors))

    def test_malformed_suite_and_case_shapes_return_errors(self):
        self.assertTrue(validate_security_suite([]))
        suite = dict(self.suite, cases=[None])
        errors = validate_security_suite(suite)
        self.assertTrue(any("must be an object" in error for error in errors))

    def test_invalid_claim_source_container_is_rejected(self):
        case = dict(self.suite["cases"][0])
        case["claims"] = [{"text": "A claim", "status": "hypothesis", "sources": "not-a-list"}]
        errors = validate_security_case(case)
        self.assertTrue(any("sources must be a list" in error for error in errors))

    def test_observed_claim_requires_verification_metadata(self):
        case = dict(self.suite["cases"][0])
        case["claims"] = [{
            "text": "A verified fact",
            "status": "observed",
            "sources": [{
                "source_id": "SRC-PRIMARY-01",
                "locator": "page 4, paragraph 2",
                "verified": True,
                "verification_method": "checked against the original publication",
                "verified_at": "2026-11-15",
            }],
        }]
        self.assertEqual(validate_security_case(case), [])

    def test_observed_claim_rejects_invalid_verification_date(self):
        case = dict(self.suite["cases"][0])
        case["claims"] = [{
            "text": "A verified fact",
            "status": "observed",
            "sources": [{
                "source_id": "SRC-PRIMARY-01",
                "locator": "page 4",
                "verified": True,
                "verification_method": "primary source review",
                "verified_at": "yesterday",
            }],
        }]
        errors = validate_security_case(case)
        self.assertTrue(any("valid YYYY-MM-DD date" in error for error in errors))

    def test_unhashable_claim_status_is_rejected_without_exception(self):
        case = dict(self.suite["cases"][0])
        case["claims"] = [{"text": "Malformed", "status": [], "sources": []}]
        errors = validate_security_case(case)
        self.assertTrue(any("invalid claim status" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
