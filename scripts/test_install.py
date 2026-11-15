"""Regression tests for the copy-based Bash and PowerShell installers."""
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_SOURCE = ROOT / "skills" / "synthesise-ai-free"
BASH = shutil.which("bash")
POWERSHELL = shutil.which("pwsh") or shutil.which("powershell")


class InstallerRegressionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="synthesise installer tests ")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.target = self.base / "target directory with spaces"
        self.destination = self.target / "synthesise-ai-free"

    def run_bash(self, *args):
        return subprocess.run(
            [BASH, str(ROOT / "scripts" / "install.sh"), *map(str, args)],
            cwd=self.base, text=True, capture_output=True, check=False,
        )

    def run_powershell(self, *args):
        return subprocess.run(
            [POWERSHELL, "-NoProfile", "-File", str(ROOT / "scripts" / "install.ps1"), *map(str, args)],
            cwd=self.base, text=True, capture_output=True, check=False,
        )

    def assert_complete_install(self):
        self.assertTrue((self.destination / "SKILL.md").is_file())
        for folder in ("references", "workflows", "templates", "examples"):
            self.assertTrue((self.destination / folder).is_dir(), folder)
        source_files = {p.relative_to(SKILL_SOURCE) for p in SKILL_SOURCE.rglob("*") if p.is_file()}
        installed_files = {p.relative_to(self.destination) for p in self.destination.rglob("*") if p.is_file()}
        self.assertEqual(installed_files, source_files)

    @unittest.skipUnless(BASH, "Bash is not installed")
    def test_bash_fresh_install_preserves_complete_skill_and_space_path(self):
        result = self.run_bash("--target", self.target)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assert_complete_install()

    @unittest.skipUnless(BASH, "Bash is not installed")
    def test_bash_refuses_existing_install_without_force_and_preserves_it(self):
        self.destination.mkdir(parents=True)
        marker = self.destination / "user-data.txt"
        marker.write_text("keep me", encoding="utf-8")
        result = self.run_bash("--target", self.target)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(marker.read_text(encoding="utf-8"), "keep me")

    @unittest.skipUnless(BASH, "Bash is not installed")
    def test_bash_force_update_replaces_stale_files(self):
        self.destination.mkdir(parents=True)
        (self.destination / "stale.txt").write_text("stale", encoding="utf-8")
        result = self.run_bash("--target", self.target, "--force")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse((self.destination / "stale.txt").exists())
        self.assert_complete_install()

    @unittest.skipUnless(POWERSHELL, "PowerShell is not installed")
    def test_powershell_fresh_install_preserves_complete_skill_and_space_path(self):
        result = self.run_powershell("-Target", self.target)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assert_complete_install()

    @unittest.skipUnless(POWERSHELL, "PowerShell is not installed")
    def test_powershell_refuses_existing_install_without_force_and_preserves_it(self):
        self.destination.mkdir(parents=True)
        marker = self.destination / "user-data.txt"
        marker.write_text("keep me", encoding="utf-8")
        result = self.run_powershell("-Target", self.target)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(marker.read_text(encoding="utf-8"), "keep me")

    @unittest.skipUnless(POWERSHELL, "PowerShell is not installed")
    def test_powershell_force_update_replaces_stale_files(self):
        self.destination.mkdir(parents=True)
        (self.destination / "stale.txt").write_text("stale", encoding="utf-8")
        result = self.run_powershell("-Target", self.target, "-Force")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse((self.destination / "stale.txt").exists())
        self.assert_complete_install()


if __name__ == "__main__":
    unittest.main()
