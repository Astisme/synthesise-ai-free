"""Regression test for the frozen v1.1.0 UVZ weighted score fixture."""
from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "evaluations" / "specialists" / "uvz" / "scoring-parity.json"


class UvzScoringParityTests(unittest.TestCase):
    def test_fixture_matches_canonical_weighted_formula(self):
        fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
        weights = list(fixture["weights"].values())
        ratings = fixture["ratings"]
        self.assertEqual(sum(weights), fixture["expected"]["weight_sum"])
        self.assertEqual(len(weights), len(ratings))
        self.assertTrue(all(1 <= rating <= 5 for rating in ratings))
        score = sum(weight * rating / 5 for weight, rating in zip(weights, ratings))
        self.assertEqual(score, fixture["expected"]["weighted_score"])
        self.assertEqual(score, 69)


if __name__ == "__main__":
    unittest.main()
