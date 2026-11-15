import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from project_brief import ProjectBriefError, parse_project_brief


class ProjectBriefParserTests(unittest.TestCase):
    def test_parses_all_structured_sections(self):
        brief = parse_project_brief((ROOT / "fixtures/projects/creator-analytics/PROJECT-BRIEF.md").read_text(encoding="utf-8"))
        self.assertEqual(brief["metadata"]["title"], "Practical Analytics for Independent Creators")
        self.assertEqual(brief["status"], "validation")
        self.assertEqual(brief["uvz_opportunities"][0]["status"], "selected")
        self.assertEqual(brief["decision_log"][0]["status"], "confirmed")

    def test_rejects_missing_structured_sections(self):
        with self.assertRaises(ProjectBriefError):
            parse_project_brief("# PROJECT-BRIEF.md\n\n## Metadata\n\nNo structured block here.\n")

    def test_rejects_duplicate_sections(self):
        source = (ROOT / "fixtures/projects/creator-analytics/PROJECT-BRIEF.md").read_text(encoding="utf-8")
        with self.assertRaises(ProjectBriefError):
            parse_project_brief(source + '\n## Status\n\n~~~json\n"paused"\n~~~\n')


if __name__ == "__main__":
    unittest.main()
