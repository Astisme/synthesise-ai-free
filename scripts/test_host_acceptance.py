"""Regression tests for evidence-backed native-host acceptance reports."""
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "fixtures" / "host-acceptance" / "incomplete.example.json"

import sys
sys.path.insert(0, str(ROOT / "scripts"))
from validate_host_acceptance import validate_report

CHECKS = (
    "marketplace_refresh", "plugin_install", "orchestrator_discovery",
    "orchestrator_invocation", "specialist_discovery", "specialist_invocation",
    "project_resume", "artifact_ownership",
)


class HostAcceptanceReportTests(unittest.TestCase):
    def complete_report(self, evidence_status="passed"):
        return {
            "schema_version": "1.0.0",
            "plugin": {"name": "synthesise-ai-free", "version": "2.0.0"},
            "host": "claude-code",
            "host_version": "2.1.0",
            "os": "Ubuntu 26.04",
            "tested_at": "2026-11-15",
            "install_route": "native-marketplace",
            "results": {
                check: {
                    "status": evidence_status,
                    "evidence": [f"evidence/{check}.log"] if evidence_status == "passed" else [],
                    **({"notes": "Not yet executed"} if evidence_status != "passed" else {}),
                }
                for check in CHECKS
            },
        }

    def write_report(self, directory, report):
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "evidence").mkdir(exist_ok=True)
        for check in CHECKS:
            (directory / "evidence" / f"{check}.log").write_text(
                f"Observed host result for {check}\n", encoding="utf-8"
            )
        path = directory / "report.json"
        path.write_text(json.dumps(report, indent=2), encoding="utf-8")
        return path

    def test_example_fixture_is_valid_but_incomplete(self):
        errors, all_passed = validate_report(FIXTURE)
        self.assertEqual(errors, [])
        self.assertFalse(all_passed)

    def test_all_eight_passed_checks_with_evidence_pass_release_gate(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_report(Path(tmp), self.complete_report())
            errors, all_passed = validate_report(path, require_all_passed=True)
        self.assertEqual(errors, [])
        self.assertTrue(all_passed)

    def test_incomplete_report_is_valid_but_fails_release_gate(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_report(Path(tmp), self.complete_report("not_run"))
            errors, all_passed = validate_report(path)
            gate_errors, _ = validate_report(path, require_all_passed=True)
        self.assertEqual(errors, [])
        self.assertFalse(all_passed)
        self.assertTrue(any("Release gate not passed" in item for item in gate_errors))

    def test_passed_check_requires_evidence(self):
        report = self.complete_report()
        report["results"]["plugin_install"]["evidence"] = []
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_report(Path(tmp), report)
            errors, _ = validate_report(path)
        self.assertTrue(any("plugin_install: passed checks require" in item for item in errors))

    def test_evidence_paths_cannot_escape_report_directory(self):
        report = self.complete_report()
        report["results"]["plugin_install"]["evidence"] = ["../outside.log"]
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_report(Path(tmp), report)
            errors, _ = validate_report(path)
        self.assertTrue(any("evidence path must stay inside" in item for item in errors))

    def test_plugin_version_must_match_repository_manifest(self):
        report = self.complete_report()
        report["plugin"]["version"] = "2.0.0-alpha.3"
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_report(Path(tmp), report)
            errors, _ = validate_report(path)
        self.assertTrue(any("plugin.version does not match" in item for item in errors))

    def test_malformed_host_and_status_types_are_rejected_without_crashing(self):
        report = self.complete_report()
        report["host"] = ["claude-code"]
        report["results"]["plugin_install"]["status"] = ["passed"]
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_report(Path(tmp), report)
            errors, _ = validate_report(path)
        self.assertTrue(any("host must be" in item for item in errors))
        self.assertTrue(any("plugin_install: invalid status" in item for item in errors))

    def test_all_required_checks_must_be_present(self):
        report = self.complete_report()
        del report["results"]["artifact_ownership"]
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_report(Path(tmp), report)
            errors, _ = validate_report(path)
        self.assertTrue(any("Missing acceptance checks: artifact_ownership" in item for item in errors))


if __name__ == "__main__":
    unittest.main()
