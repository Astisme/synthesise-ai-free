import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from workflow_integrity import validate_product_lifecycle, validate_project_resume


class WorkflowIntegrityTests(unittest.TestCase):
    def load(self, name):
        return json.loads((ROOT / "evaluations/workflows" / name).read_text(encoding="utf-8"))

    def test_discovery_to_monetization_handoff(self):
        self.assertEqual(validate_product_lifecycle(self.load("product-lifecycle.json")), [])

    def test_rejects_validation_without_evidence(self):
        errors = validate_product_lifecycle(self.load("invalid/missing-validation-evidence.json"))
        self.assertTrue(any("Completed validation" in error for error in errors))

    def test_rejects_broken_audience_handoff(self):
        errors = validate_product_lifecycle(self.load("invalid/broken-monetization-handoff.json"))
        self.assertTrue(any("preserve the charter audience" in error for error in errors))

    def test_project_resume_preserves_decisions(self):
        self.assertEqual(validate_project_resume(self.load("continuity/resume-preserves-decisions.json")), [])

    def test_project_resume_rejects_decision_loss(self):
        errors = validate_project_resume(self.load("invalid/decision-loss-on-resume.json"))
        self.assertTrue(any("dropped prior decision" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
