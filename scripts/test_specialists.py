"""Structural tests for every modular Synthesise specialist package present in the checkout."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
EXCLUDED = {"synthesise-ai-free", "synthesise-orchestrator"}


class SpecialistPackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.packages = sorted(
            path for path in SKILLS.glob("synthesise-*")
            if path.is_dir() and path.name not in EXCLUDED
        )

    def test_at_least_one_specialist_package_is_present(self):
        self.assertTrue(self.packages, "No modular specialist packages found")

    def test_each_package_has_valid_skill_identity_and_metadata(self):
        for package in self.packages:
            with self.subTest(package=package.name):
                skill_path = package / "SKILL.md"
                self.assertTrue(skill_path.is_file())
                content = skill_path.read_text(encoding="utf-8")
                self.assertTrue(content.startswith("---\\n"))
                frontmatter = content.split("---", 2)[1]
                self.assertRegex(frontmatter, r"(?m)^name:\\s*" + re.escape(package.name) + r"\\s*$")
                for key in ("description:", "license:", "compatibility:", "version:"):
                    self.assertIn(key, frontmatter)

    def test_all_progressive_disclosure_links_resolve(self):
        pattern = r"(?:references|workflows|templates|examples)/[A-Za-z0-9_./-]+\\.md"
        for package in self.packages:
            content = (package / "SKILL.md").read_text(encoding="utf-8")
            for relative in re.findall(pattern, content):
                with self.subTest(package=package.name, reference=relative):
                    self.assertTrue((package / relative).is_file())

    def test_uvz_package_preserves_canonical_weights_when_present(self):
        package = SKILLS / "synthesise-uvz"
        if not package.is_dir():
            self.skipTest("UVZ package is introduced by its own specialist PR")
        scoring = (package / "references/uvz-scoring.md").read_text(encoding="utf-8")
        for weight in ("20%", "20%", "15%", "10%", "15%", "10%", "10%"):
            with self.subTest(weight=weight):
                self.assertIn(weight, scoring)
        self.assertIn("sum(weight × rating / 5)", scoring)
        self.assertIn("Unknown", scoring)


if __name__ == "__main__":
    unittest.main()
