"""Regression tests for the dual-host native acceptance release gate."""
import json
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_all_host_acceptance import validate_all_reports

CHECKS = (
    "marketplace_refresh", "plugin_install", "orchestrator_discovery",
    "orchestrator_invocation", "specialist_discovery", "specialist_invocation",
    "project_resume", "artifact_ownership",
)


class DualHostAcceptanceTests(unittest.TestCase):
    def report(self, host):
        return {
            "schema_version": "1.0.0",
            "plugin": {"name": "synthesise-ai-free", "version": "2.0.0-alpha.4"},
            "host": host,
            "host_version": "test-version",
            "os": "test-os",
            "tested_at": "2026-11-15",
            "install_route": "native-marketplace",
            "results": {
                check: {"status": "passed", "evidence": [f"evidence/{check}.log"]}
                for check in CHECKS
            },
        }

    def write(self, root, host, report=None):
        folder = root / host
        evidence = folder / "evidence"
        evidence.mkdir(parents=True, exist_ok=True)
        for check in CHECKS:
            (evidence / f"{check}.log").write_text(f"Observed {check}\n", encoding="utf-8")
        path = folder / "report.json"
        path.write_text(json.dumps(report or self.report(host)), encoding="utf-8")
        return path

    def test_both_hosts_with_complete_evidence_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            claude = self.write(root, "claude-code")
            codex = self.write(root, "codex-desktop")
            self.assertEqual(validate_all_reports([claude, codex]), [])

    def test_single_host_is_not_enough(self):
        with tempfile.TemporaryDirectory() as tmp:
            report = self.write(Path(tmp), "claude-code")
            errors = validate_all_reports([report])
        self.assertTrue(any("Exactly 2 host reports" in item for item in errors))

    def test_duplicate_host_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            first = self.write(root, "claude-code")
            second = self.write(root, "claude-code")
            errors = validate_all_reports([first, second])
        self.assertTrue(any("Duplicate host report" in item for item in errors))
        self.assertTrue(any("Missing host reports" in item for item in errors))

    def test_incomplete_host_blocks_combined_gate(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            claude = self.write(root, "claude-code")
            incomplete = self.report("codex-desktop")
            incomplete["results"]["project_resume"] = {
                "status": "not_run", "evidence": [], "notes": "Not tested"
            }
            codex = self.write(root, "codex-desktop", incomplete)
            errors = validate_all_reports([claude, codex])
        self.assertTrue(any("codex-desktop: Release gate not passed" in item for item in errors))

    def test_report_host_must_match_supported_host(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            claude = self.write(root, "claude-code")
            invalid = self.report("other-host")
            codex = self.write(root, "codex-desktop", invalid)
            errors = validate_all_reports([claude, codex])
        self.assertTrue(any("host must be one of" in item for item in errors))


if __name__ == "__main__":
    unittest.main()
