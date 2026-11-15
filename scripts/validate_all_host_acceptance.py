#!/usr/bin/env python3
"""Require evidence-backed acceptance from both supported native hosts."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from validate_host_acceptance import (
    ALLOWED_HOSTS,
    AcceptanceReportError,
    load_json,
    validate_report,
)


def validate_all_reports(paths: list[Path]) -> list[str]:
    errors: list[str] = []
    if len(paths) != len(ALLOWED_HOSTS):
        return [f"Exactly {len(ALLOWED_HOSTS)} host reports are required (one per supported host)"]

    seen: set[str] = set()
    for path in paths:
        try:
            report = load_json(path.expanduser().resolve())
        except AcceptanceReportError as exc:
            errors.append(str(exc))
            continue
        host = report.get("host") if isinstance(report, dict) else None
        if not isinstance(host, str) or host not in ALLOWED_HOSTS:
            errors.append(f"{path}: host must be one of {', '.join(sorted(ALLOWED_HOSTS))}")
            continue
        if host in seen:
            errors.append(f"Duplicate host report: {host}")
            continue
        seen.add(host)
        try:
            report_errors, all_passed = validate_report(path, require_all_passed=True)
        except AcceptanceReportError as exc:
            errors.append(f"{host}: {exc}")
            continue
        errors.extend(f"{host}: {item}" for item in report_errors)
        if not all_passed and not any(item.startswith(f"{host}: Release gate not passed") for item in errors):
            errors.append(f"{host}: all eight checks must pass with evidence")

    missing = sorted(ALLOWED_HOSTS - seen)
    if missing:
        errors.append("Missing host reports: " + ", ".join(missing))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Require complete evidence-backed acceptance for Claude Code and Codex Desktop."
    )
    parser.add_argument("reports", nargs="+", type=Path, help="One JSON report for each supported host")
    args = parser.parse_args()
    try:
        errors = validate_all_reports(args.reports)
    except (AcceptanceReportError, OSError) as exc:
        print(f"Host release gate error: {exc}", file=sys.stderr)
        return 2
    if errors:
        print("Dual-host release gate failed:")
        for error in errors:
            print("- " + error)
        return 1
    print("Dual-host release gate passed: Claude Code and Codex Desktop have all eight evidence-backed checks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
