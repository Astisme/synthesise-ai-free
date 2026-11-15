#!/usr/bin/env python3
"""Validate evidence-backed native-host acceptance reports for modular v2."""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "host-acceptance.schema.json"
PLUGIN_PATH = ROOT / "plugin.json"
REQUIRED_CHECKS = (
    "marketplace_refresh",
    "plugin_install",
    "orchestrator_discovery",
    "orchestrator_invocation",
    "specialist_discovery",
    "specialist_invocation",
    "project_resume",
    "artifact_ownership",
)
ALLOWED_HOSTS = {"claude-code", "codex-desktop"}
ALLOWED_ROUTES = {"native-marketplace", "filesystem"}
ALLOWED_STATUSES = {"passed", "failed", "blocked", "not_run"}


class AcceptanceReportError(ValueError):
    pass


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise AcceptanceReportError(f"Cannot read JSON file {path}: {exc}") from exc


def validate_report(path: Path, require_all_passed: bool = False) -> tuple[list[str], bool]:
    report_path = path.expanduser().resolve()
    report = load_json(report_path)
    schema = load_json(SCHEMA_PATH)
    plugin = load_json(PLUGIN_PATH)
    errors = []

    if not isinstance(report, dict):
        raise AcceptanceReportError("Report root must be a JSON object")
    allowed_top = set(schema["properties"])
    if set(report) != set(schema["required"]):
        missing = sorted(set(schema["required"]) - set(report))
        extra = sorted(set(report) - allowed_top)
        if missing:
            errors.append("Missing top-level fields: " + ", ".join(missing))
        if extra:
            errors.append("Unexpected top-level fields: " + ", ".join(extra))

    if report.get("schema_version") != "1.0.0":
        errors.append("schema_version must be 1.0.0")

    report_plugin = report.get("plugin")
    if not isinstance(report_plugin, dict):
        errors.append("plugin must be an object")
    else:
        if set(report_plugin) != {"name", "version"}:
            errors.append("plugin must contain only name and version")
        if report_plugin.get("name") != plugin.get("name"):
            errors.append("plugin.name does not match the repository plugin manifest")
        if report_plugin.get("version") != plugin.get("version"):
            errors.append("plugin.version does not match the repository plugin manifest")

    if report.get("host") not in ALLOWED_HOSTS:
        errors.append("host must be claude-code or codex-desktop")
    for field in ("host_version", "os"):
        if not isinstance(report.get(field), str) or not report[field].strip():
            errors.append(field + " must be a non-empty string")
    try:
        tested_at = report.get("tested_at")
        if not isinstance(tested_at, str) or date.fromisoformat(tested_at).isoformat() != tested_at:
            raise ValueError
    except (TypeError, ValueError):
        errors.append("tested_at must be an ISO YYYY-MM-DD date")
    if report.get("install_route") not in ALLOWED_ROUTES:
        errors.append("install_route must be native-marketplace or filesystem")

    results = report.get("results")
    all_passed = True
    if not isinstance(results, dict):
        errors.append("results must be an object")
        results = {}
    missing_checks = sorted(set(REQUIRED_CHECKS) - set(results))
    extra_checks = sorted(set(results) - set(REQUIRED_CHECKS))
    if missing_checks:
        errors.append("Missing acceptance checks: " + ", ".join(missing_checks))
    if extra_checks:
        errors.append("Unexpected acceptance checks: " + ", ".join(extra_checks))

    evidence_root = report_path.parent.resolve()
    for check_id in REQUIRED_CHECKS:
        check = results.get(check_id)
        if not isinstance(check, dict):
            all_passed = False
            continue
        if set(check) - {"status", "evidence", "notes"}:
            errors.append(f"{check_id}: unexpected result fields")
        status = check.get("status")
        evidence = check.get("evidence")
        notes = check.get("notes")
        if status not in ALLOWED_STATUSES:
            errors.append(f"{check_id}: invalid status")
            all_passed = False
            continue
        if not isinstance(evidence, list) or not all(isinstance(item, str) and item.strip() for item in evidence):
            errors.append(f"{check_id}: evidence must be an array of non-empty relative paths")
            evidence = []
        if status == "passed" and not evidence:
            errors.append(f"{check_id}: passed checks require at least one evidence file")
        if status != "passed" and (not isinstance(notes, str) or not notes.strip()):
            errors.append(f"{check_id}: non-passed checks require explanatory notes")
        if "notes" in check and not isinstance(notes, str):
            errors.append(f"{check_id}: notes must be a string")
        for item in evidence:
            candidate = Path(item)
            if candidate.is_absolute() or ".." in candidate.parts:
                errors.append(f"{check_id}: evidence path must stay inside the report directory: {item}")
                continue
            resolved = (evidence_root / candidate).resolve()
            try:
                resolved.relative_to(evidence_root)
            except ValueError:
                errors.append(f"{check_id}: evidence path escapes the report directory: {item}")
                continue
            if not resolved.is_file():
                errors.append(f"{check_id}: evidence file does not exist: {item}")
        if status != "passed":
            all_passed = False

    if require_all_passed and not all_passed:
        errors.append("Release gate not passed: all eight host acceptance checks must pass")
    return errors, all_passed


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a modular v2 native-host acceptance report.")
    parser.add_argument("report", type=Path, help="Acceptance report JSON file")
    parser.add_argument("--release-gate", action="store_true", help="Fail unless all eight checks passed with evidence")
    args = parser.parse_args()
    try:
        errors, all_passed = validate_report(args.report, args.release_gate)
    except AcceptanceReportError as exc:
        print(f"Acceptance report error: {exc}", file=sys.stderr)
        return 2
    if errors:
        print("Acceptance report validation failed:")
        for error in errors:
            print("- " + error)
        return 1
    if all_passed:
        print("Host acceptance passed: all eight checks have evidence.")
    else:
        print("Host acceptance report is valid but incomplete; release gate remains open.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
