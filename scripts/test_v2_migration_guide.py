"""Guardrails for the documented v1-to-v2 preview migration contract."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "docs" / "v2-migration-guide.md"


class V2MigrationGuideTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = GUIDE.read_text(encoding="utf-8")

    def test_guide_discloses_preview_and_no_automatic_project_migration(self):
        self.assertIn("v2.0.0-alpha.4", self.content)
        self.assertIn("does **not** convert a project", self.content)
        self.assertIn("does not establish live Claude Code or Codex installation", self.content)

    def test_v1_and_v2_installations_are_kept_separate(self):
        self.assertIn("synthesise-ai-free/", self.content)
        self.assertIn(".synthesise-v2-preview.json", self.content)
        self.assertIn("never manages the v1 directory", self.content)
        self.assertIn("one v2 installation route per host", self.content)

    def test_project_continuity_and_uvz_frozen_baseline_are_acceptance_gates(self):
        for phrase in (
            "PROJECT-BRIEF.md",
            "decision records",
            "evidence status",
            "artifact ownership",
            "seven dimensions",
            "sensitivity rules",
        ):
            self.assertIn(phrase, self.content)

    def test_rollback_and_live_host_evidence_are_documented(self):
        self.assertIn("--remove", self.content)
        self.assertIn("host/version/OS", self.content)
        self.assertIn("Overall result and known limitations", self.content)


if __name__ == "__main__":
    unittest.main()
