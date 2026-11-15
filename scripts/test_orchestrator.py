"""Structural regression tests for the modular orchestrator package."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "skills" / "synthesise-orchestrator"


class OrchestratorPackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = (PACKAGE / "SKILL.md").read_text(encoding="utf-8")

    def test_agent_skill_frontmatter_identity(self):
        self.assertTrue(self.skill.startswith("---\n"))
        frontmatter = self.skill.split("---", 2)[1]
        self.assertRegex(frontmatter, r"(?m)^name:\s*synthesise-orchestrator\s*$")
        for key in ("description:", "license:", "compatibility:"):
            self.assertIn(key, frontmatter)

    def test_required_operating_sections_exist(self):
        for heading in (
            "Operating contract", "Modes", "Execution protocol",
            "Migration-era package availability", "Project continuity",
            "Completion response",
        ):
            self.assertIn("## " + heading, self.skill)

    def test_all_progressive_disclosure_links_resolve(self):
        references = re.findall(
            r"(?:references|workflows|templates|examples)/[A-Za-z0-9_./-]+\.md",
            self.skill,
        )
        self.assertTrue(references)
        for relative in references:
            with self.subTest(reference=relative):
                self.assertTrue((PACKAGE / relative).is_file())

    def test_catalog_ids_are_not_claimed_as_installed_packages(self):
        routing = (PACKAGE / "references/routing-matrix.md").read_text(encoding="utf-8")
        self.assertIn("not a declaration that the packages are already installed", routing)
        self.assertIn("Package availability must be checked at runtime", routing)

    def test_legacy_fallback_is_explicit(self):
        self.assertIn("temporary methodology source", self.skill)
        self.assertIn("do not pretend it is a modular specialist", self.skill)

    def test_parallel_execution_is_capability_gated(self):
        dependency = (PACKAGE / "references/dependency-graph.md").read_text(encoding="utf-8")
        self.assertIn("harness explicitly supports parallel execution", dependency)


    def test_integration_contract_reference_is_linked_and_present(self):
        self.assertIn("references/integration-contracts.md", self.skill)
        self.assertTrue((PACKAGE / "references/integration-contracts.md").is_file())

    def test_handoff_contract_fields_are_documented(self):
        protocol = (PACKAGE / "references/orchestration-protocol.md").read_text(encoding="utf-8")
        for field in (
            "contract_version", "skill_id", "project_id", "objective",
            "completion_status", "inputs_used", "outputs_created",
            "decisions_proposed", "decisions_required", "assumptions",
            "evidence", "limitations", "next_recommended_skills",
        ):
            with self.subTest(field=field):
                self.assertIn(field, protocol)


if __name__ == "__main__":
    unittest.main()
