import json
import sys
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
        case["claims"] = [{"text":"Unproven statistic","status":"observed","sources":[{"source_id":"SRC-X","locator":"missing","verified":False}]}]
        self.assertTrue(any("unverified or incomplete source" in error for error in validate_security_case(case)))

    def test_embedded_instruction_cannot_be_removed_from_contract(self):
        case = dict(self.suite["cases"][0], required_controls=["treat_as_data","attribute_source"])
        self.assertTrue(any("missing security controls" in error for error in validate_security_case(case)))


if __name__ == "__main__":
    unittest.main()
