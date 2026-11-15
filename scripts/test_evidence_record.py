"""Dependency-free checks for the shared evidence-record schema and guide."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "evidence-record.schema.json"
GUIDE_PATH = ROOT / "docs" / "evidence-record.md"


class EvidenceRecordContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        cls.guide = GUIDE_PATH.read_text(encoding="utf-8")

    def test_schema_requires_provenance_and_qualification(self):
        required = set(self.schema["required"])
        self.assertTrue({
            "evidence_id", "claim", "type", "status", "confidence",
            "scope", "limitations", "supports", "used_by",
        }.issubset(required))
        self.assertEqual(self.schema["additionalProperties"], False)

    def test_evidence_status_and_confidence_are_bounded(self):
        props = self.schema["properties"]
        self.assertEqual(
            set(props["status"]["enum"]),
            {"observed", "reported", "verified", "inferred", "hypothesis", "disputed", "superseded"},
        )
        self.assertEqual(set(props["confidence"]["enum"]), {"low", "medium", "high"})

    def test_guide_preserves_evidence_meaning_across_handoffs(self):
        self.assertIn("must not silently upgrade confidence or status", self.guide)
        self.assertIn("stable", self.guide)
        self.assertIn("limitations", self.guide)


if __name__ == "__main__":
    unittest.main()
