"""Regression tests for deterministic modular orchestration integration fixtures."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from orchestration_integration import evaluate_integration_suite, validate_scenario

FIXTURE = ROOT / "evaluations" / "integration" / "orchestration-scenarios.json"


class OrchestrationIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(FIXTURE.read_text(encoding="utf-8"))
        cls.by_id = {item["id"]: item for item in cls.data["scenarios"]}

    def test_eight_end_to_end_contract_scenarios_pass(self):
        results = evaluate_integration_suite(self.data)
        self.assertEqual(len(self.data["scenarios"]), 8)
        self.assertTrue(all(item["passed"] for item in results), results)

    def test_expertise_to_charter_rejects_audience_or_opportunity_drift(self):
        case = copy.deepcopy(self.by_id["workflow-expertise-to-charter"])
        case["stages"]["charter"]["audience_id"] = "aud-other"
        self.assertTrue(validate_scenario(case))

    def test_parallel_research_rejects_shared_output_or_unsupported_parallelism(self):
        case = copy.deepcopy(self.by_id["parallel-market-validation"])
        case["tasks"][1]["output"] = case["tasks"][0]["output"]
        self.assertTrue(validate_scenario(case))
        case = copy.deepcopy(self.by_id["parallel-market-validation"])
        case["harness_supports_parallel"] = False
        self.assertTrue(validate_scenario(case))

    def test_evidence_reuse_rejects_status_upgrade_and_sample_loss(self):
        case = copy.deepcopy(self.by_id["evidence-provenance-through-handoffs"])
        case["consumers"][1]["status"] = "verified"
        case["consumers"][2]["sample_size"] = 12
        self.assertTrue(validate_scenario(case))

    def test_non_owner_cannot_overwrite_canonical_artifact(self):
        case = copy.deepcopy(self.by_id["artifact-owner-and-proposed-patch"])
        case["request"]["write_status"] = "updated"
        self.assertTrue(validate_scenario(case))

    def test_approved_decision_conflict_requires_user_resolution(self):
        case = copy.deepcopy(self.by_id["approved-decision-conflict"])
        case["resolution"]["automatic_replacement"] = True
        self.assertTrue(validate_scenario(case))

    def test_resume_rejects_lost_decision_or_evidence(self):
        case = copy.deepcopy(self.by_id["resume-preserves-project-state"])
        case["after"]["decisions"] = []
        case["after"]["evidence_ids"] = []
        self.assertTrue(validate_scenario(case))

    def test_failed_validation_cannot_be_promoted_to_validated_promise(self):
        case = copy.deepcopy(self.by_id["negative-validation-bounds-promise"])
        case["charter"]["promise_status"] = "validated"
        self.assertTrue(validate_scenario(case))

    def test_launch_cannot_complete_with_operational_blockers(self):
        case = copy.deepcopy(self.by_id["launch-readiness-blockers"])
        case["launch"]["completion_status"] = "complete"
        self.assertTrue(validate_scenario(case))


if __name__ == "__main__":
    unittest.main()
