"""Deterministic contracts for the ten specialist methodology references.

These fixtures validate coverage and contract shape, not live agent reasoning.
"""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "evaluations" / "specialists" / "methodology-cases.json"
EXPECTED = {
    "synthesise-discovery", "synthesise-audience", "synthesise-uvz",
    "synthesise-market-intelligence", "synthesise-validation",
    "synthesise-product-architecture", "synthesise-curriculum",
    "synthesise-monetization", "synthesise-launch", "synthesise-project",
}


class SpecialistMethodologyFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(FIXTURE.read_text(encoding="utf-8"))
        cls.cases = cls.data["cases"]

    def test_every_specialist_has_two_meaningful_cases(self):
        counts = {skill: 0 for skill in EXPECTED}
        for case in self.cases:
            counts[case["skill_id"]] += 1
        self.assertEqual(set(counts), EXPECTED)
        self.assertEqual(counts, {skill: 2 for skill in EXPECTED})

    def test_case_ids_are_unique_and_contracts_are_actionable(self):
        ids = [case["id"] for case in self.cases]
        self.assertEqual(len(ids), len(set(ids)))
        for case in self.cases:
            with self.subTest(case=case["id"]):
                self.assertTrue(case["input_context"].strip())
                self.assertTrue(case["expected_task"].strip())
                self.assertGreaterEqual(len(case["required_invariants"]), 3)
                self.assertTrue(case["reject_if"])

    def test_each_case_points_to_a_real_skill_and_methodology(self):
        for skill in EXPECTED:
            package = ROOT / "skills" / skill
            with self.subTest(skill=skill):
                self.assertTrue((package / "SKILL.md").is_file())
                skill_text = (package / "SKILL.md").read_text(encoding="utf-8")
                self.assertIn("Progressive methodology reference", skill_text)
                self.assertRegex(skill_text, r"references/[A-Za-z0-9_-]+\.md")


if __name__ == "__main__":
    unittest.main()
