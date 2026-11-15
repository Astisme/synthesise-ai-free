"""Regression guard for the public GitHub Actions quality-gate contract."""
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "validate.yml"


class WorkflowContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.workflow = WORKFLOW.read_text(encoding="utf-8")

    def test_ubuntu_job_runs_all_quality_layers(self):
        for required in (
            "deterministic:",
            "runs-on: ubuntu-latest",
            "python scripts/validate.py",
            "python -m unittest discover -s scripts -p 'test_*.py' -v",
            "python scripts/evaluate.py --report-dir evaluations/reports",
            "actions/upload-artifact@v4",
            "evaluations/reports/deterministic.json",
            "evaluations/reports/deterministic.md",
        ):
            with self.subTest(required=required):
                self.assertIn(required, self.workflow)

    def test_windows_job_runs_powershell_installer_regressions(self):
        for required in (
            "windows-installers:",
            "runs-on: windows-latest",
            "shell: pwsh",
            "python -m unittest discover -s scripts -p 'test_install*.py' -v",
        ):
            with self.subTest(required=required):
                self.assertIn(required, self.workflow)

    def test_workflow_is_not_structural_validation_only(self):
        self.assertIn("python scripts/validate.py", self.workflow)
        self.assertIn("python -m unittest discover", self.workflow)
        self.assertIn("python scripts/evaluate.py", self.workflow)


if __name__ == "__main__":
    unittest.main()
