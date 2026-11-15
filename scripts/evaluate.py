#!/usr/bin/env python3
"""Dependency-free deterministic fixture and frozen-baseline evaluator.

This validates authored fixtures and repository invariants. It does not run an
agent and must never be interpreted as proof of live model behaviour.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / "evaluations/baseline/v1.1.0.json"
CHECKSUMS = ROOT / "evaluations/baseline/checksums.json"
SCENARIOS = ROOT / "evaluations/scenarios"
SCHEMA = ROOT / "schemas/project-brief.schema.json"
BRIEF_FIXTURE = ROOT / "fixtures/projects/minimal-project-brief.json"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def validate_schema(value, schema, path="$"):
    errors = []
    expected = schema.get("type")
    types = expected if isinstance(expected, list) else [expected] if expected else []
    type_map = {"object": dict, "array": list, "string": str, "integer": int,
                "number": (int, float), "boolean": bool, "null": type(None)}
    if types and not any(
        isinstance(value, type_map[t]) and not (t == "integer" and isinstance(value, bool))
        for t in types
    ):
        return [f"{path}: expected {' or '.join(types)}"]
    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                errors.append(f"{path}: missing required property {key}")
        for key, child in schema.get("properties", {}).items():
            if key in value:
                errors.extend(validate_schema(value[key], child, f"{path}.{key}"))
        if schema.get("additionalProperties") is False:
            allowed = set(schema.get("properties", {}))
            for key in value.keys() - allowed:
                errors.append(f"{path}: unexpected property {key}")
    if isinstance(value, list) and len(value) < schema.get("minItems", 0):
        errors.append(f"{path}: fewer than minItems")
    if isinstance(value, list) and "items" in schema:
        for index, item in enumerate(value):
            errors.extend(validate_schema(item, schema["items"], f"{path}[{index}]"))
    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0):
            errors.append(f"{path}: shorter than minLength")
        if "enum" in schema and value not in schema["enum"]:
            errors.append(f"{path}: value not in enum")
    if isinstance(value, int) and not isinstance(value, bool):
        if value < schema.get("minimum", value) or value > schema.get("maximum", value):
            errors.append(f"{path}: integer outside permitted range")
    return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", type=Path, help="Write machine-readable report JSON")
    args = parser.parse_args()
    checks, failures = [], []

    def check(name, ok, detail):
        checks.append({"name": name, "status": "passed" if ok else "failed", "detail": detail})
        if not ok:
            failures.append(name)

    baseline = {}
    try:
        baseline = load_json(BASELINE)
        checksums = load_json(CHECKSUMS)
        check("baseline_metadata", baseline["source_commit"] == checksums["source_commit"],
              "Baseline commit references agree")
        pinned, changed, missing = checksums["files"], [], []
        for relative, expected in pinned.items():
            path = ROOT / relative
            if not path.is_file():
                missing.append(relative)
                continue
            actual = git_blob_sha1(path.read_bytes())
            if actual != expected:
                changed.append({"path": relative, "expected": expected, "actual": actual})
        check("frozen_v1_1_skill", not missing and not changed,
              {"pinned_files": len(pinned), "missing": missing, "changed": changed})
    except (OSError, KeyError, json.JSONDecodeError) as exc:
        check("frozen_v1_1_skill", False, str(exc))

    try:
        schema, brief = load_json(SCHEMA), load_json(BRIEF_FIXTURE)
        schema_errors = validate_schema(brief, schema)
        check("project_brief_schema_fixture", not schema_errors,
              schema_errors or "Structured extraction fixture conforms")
        model_schema = load_json(ROOT / "schemas/model-run.schema.json")
        model_fixture = load_json(ROOT / "fixtures/model-run.example.json")
        model_errors = validate_schema(model_fixture, model_schema)
        check("model_run_schema_fixture", not model_errors,
              model_errors or "Captured model-run fixture conforms")
    except (OSError, json.JSONDecodeError) as exc:
        check("project_brief_schema_fixture", False, str(exc))

    scenario_files = sorted(SCENARIOS.glob("*.yaml"))
    scenario_ids, fixture_failures = set(), []
    for path in scenario_files:
        try:
            scenario = load_json(path)
            scenario_id = scenario["id"]
            if scenario_id in scenario_ids:
                fixture_failures.append(f"{path.name}: duplicate id {scenario_id}")
            scenario_ids.add(scenario_id)
            expected = scenario["expected"]
            conversation = scenario.get("input_conversation", [])
            regression = scenario.get("regression_status", {})
            if not conversation or not all(message.get("role") and message.get("content") for message in conversation):
                fixture_failures.append(f"{scenario_id}: input_conversation must contain role/content messages")
            if regression.get("introduced_in") != "1.2.0" or regression.get("mode") != "fixture-only":
                fixture_failures.append(f"{scenario_id}: regression_status must identify the 1.2.0 fixture-only baseline")
            fixture = scenario["fixture_output"].casefold()
            for phrase in expected["required_output_elements"]:
                if phrase.casefold() not in fixture:
                    fixture_failures.append(f"{scenario_id}: fixture missing required marker {phrase!r}")
            for phrase in expected["forbidden_behaviours"]:
                if phrase.casefold() in fixture:
                    fixture_failures.append(f"{scenario_id}: fixture contains forbidden marker {phrase!r}")
            for key in ("required_behaviours", "required_output_elements",
                        "forbidden_behaviours", "acceptance_criteria"):
                if not isinstance(expected.get(key), list) or not expected[key]:
                    fixture_failures.append(f"{scenario_id}: expected.{key} must be a non-empty list")
            if not scenario.get("input") or not scenario.get("fixture_output"):
                fixture_failures.append(f"{scenario_id}: input and fixture_output are required")
        except (OSError, KeyError, json.JSONDecodeError, TypeError) as exc:
            fixture_failures.append(f"{path.name}: {exc}")
    required = {"discovery", "uvz-analysis", "market-research", "validation",
                "product-architecture", "monetization", "project-continuity",
                "security-prompt-injection", "non-triggering"}
    check("scenario_contracts", required.issubset(scenario_ids),
          {"scenario_count": len(scenario_ids), "missing": sorted(required - scenario_ids)})
    check("reference_fixture_assertions", not fixture_failures,
          fixture_failures or "Authored fixture markers pass; this is not a live-agent evaluation")

    report = {
        "evaluation_version": "1.0.0",
        "evaluation_type": "deterministic-fixture-and-baseline",
        "live_agent_behaviour_tested": False,
        "skill_version": baseline.get("skill_version", "unknown"),
        "baseline_commit": baseline.get("source_commit", "unknown"),
        "scenario_set": "1.0.0",
        "evaluation_date": datetime.now(timezone.utc).date().isoformat(),
        "results": {"passed": sum(c["status"] == "passed" for c in checks),
                    "failed": len(failures), "checks": checks},
        "failures": failures
    }
    rendered = json.dumps(report, indent=2) + "\n"
    print(rendered, end="")
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(rendered, encoding="utf-8")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
