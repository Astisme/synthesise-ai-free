import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from evaluate import load_json, validate_scenarios, validate_schema


class EvaluatorInfrastructureTests(unittest.TestCase):
    def write_scenario(self, directory, filename, scenario):
        (directory / filename).write_text(json.dumps(scenario), encoding="utf-8")

    def valid_scenario(self, scenario_id="test-case"):
        return {
            "id": scenario_id,
            "input": "Test input",
            "input_conversation": [{"role": "user", "content": "Test input"}],
            "fixture_output": "A validated product hypothesis",
            "regression_status": {"introduced_in": "1.2.0", "mode": "fixture-only"},
            "expected": {
                "required_behaviours": ["validate"],
                "required_output_elements": ["product hypothesis"],
                "forbidden_behaviours": ["guaranteed revenue"],
                "acceptance_criteria": ["evidence is explicit"],
            },
        }

    def test_rejects_malformed_scenario_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            (directory / "broken.yaml").write_text('{"id": ', encoding="utf-8")
            scenario_ids, errors = validate_scenarios(directory)
        self.assertEqual(scenario_ids, set())
        self.assertTrue(any("broken.yaml" in error for error in errors))

    def test_rejects_duplicate_scenario_ids(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            self.write_scenario(directory, "first.yaml", self.valid_scenario())
            self.write_scenario(directory, "second.yaml", self.valid_scenario())
            scenario_ids, errors = validate_scenarios(directory)
        self.assertEqual(scenario_ids, {"test-case"})
        self.assertTrue(any("duplicate id test-case" in error for error in errors))

    def test_rejects_invalid_scenario_contract_types(self):
        scenario = self.valid_scenario()
        scenario["expected"]["required_output_elements"] = "not-a-list"
        scenario["input_conversation"] = [{"role": "user"}]
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            self.write_scenario(directory, "invalid.yaml", scenario)
            _, errors = validate_scenarios(directory)
        self.assertTrue(any("required_output_elements must be a non-empty list" in error for error in errors))
        self.assertTrue(any("input_conversation" in error for error in errors))

    def test_accepts_well_formed_scenario(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            self.write_scenario(directory, "valid.yaml", self.valid_scenario())
            scenario_ids, errors = validate_scenarios(directory)
        self.assertEqual(scenario_ids, {"test-case"})
        self.assertEqual(errors, [])

    def test_missing_baseline_file_fails_explicitly(self):
        with tempfile.TemporaryDirectory() as tmp:
            missing = Path(tmp) / "missing-baseline.json"
            with self.assertRaises(FileNotFoundError):
                load_json(missing)

    def test_schema_rejects_boolean_as_integer(self):
        errors = validate_schema(True, {"type": "integer"})
        self.assertTrue(errors)


if __name__ == "__main__":
    unittest.main()
