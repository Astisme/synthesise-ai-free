"""Cross-platform regression tests for the isolated modular v2 preview installer."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / "scripts" / "install_v2_preview.py"
PACKAGE_IDS = (
    "synthesise-orchestrator", "synthesise-discovery", "synthesise-audience",
    "synthesise-uvz", "synthesise-market-intelligence", "synthesise-validation",
    "synthesise-product-architecture", "synthesise-curriculum",
    "synthesise-monetization", "synthesise-launch", "synthesise-project",
)


class V2PreviewInstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="synthesise v2 installer ")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.target = self.root / "agent skills with spaces"
        self.legacy = self.target / "synthesise-ai-free"
        self.legacy.mkdir(parents=True)
        (self.legacy / "SKILL.md").write_text("---\nname: synthesise-ai-free\n---\nlegacy user data\n", encoding="utf-8")
        self.manifest = self.target / ".synthesise-v2-preview.json"

    def run_installer(self, *args):
        return subprocess.run(
            [sys.executable, str(INSTALLER), "--target", str(self.target), *args],
            cwd=self.root, text=True, capture_output=True, check=False,
        )

    def test_full_install_isolated_from_v1_and_records_all_packages(self):
        result = self.run_installer()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("legacy user data", (self.legacy / "SKILL.md").read_text(encoding="utf-8"))
        data = json.loads(self.manifest.read_text(encoding="utf-8"))
        self.assertEqual(set(data["packages"]), set(PACKAGE_IDS))
        for package in PACKAGE_IDS:
            self.assertTrue((self.target / package / "SKILL.md").is_file(), package)

    def test_partial_install_can_be_resumed_without_overwriting_existing_package(self):
        first = self.run_installer("--package", "synthesise-discovery")
        self.assertEqual(first.returncode, 0, first.stderr)
        marker = self.target / "synthesise-discovery" / "user-note.txt"
        marker.write_text("preserve", encoding="utf-8")
        resumed = self.run_installer()
        self.assertEqual(resumed.returncode, 0, resumed.stderr)
        self.assertEqual(marker.read_text(encoding="utf-8"), "preserve")
        data = json.loads(self.manifest.read_text(encoding="utf-8"))
        self.assertEqual(set(data["packages"]), set(PACKAGE_IDS))

    def test_repeat_install_is_idempotent(self):
        self.assertEqual(self.run_installer().returncode, 0)
        again = self.run_installer()
        self.assertEqual(again.returncode, 0, again.stderr)
        self.assertIn("Already installed", again.stdout)

    def test_unmanaged_collision_is_refused_and_force_replaces_only_selected_package(self):
        destination = self.target / "synthesise-launch"
        destination.mkdir()
        (destination / "user-data.txt").write_text("unmanaged", encoding="utf-8")
        refused = self.run_installer("--package", "synthesise-launch")
        self.assertNotEqual(refused.returncode, 0)
        self.assertEqual((destination / "user-data.txt").read_text(encoding="utf-8"), "unmanaged")
        forced = self.run_installer("--package", "synthesise-launch", "--force")
        self.assertEqual(forced.returncode, 0, forced.stderr)
        self.assertFalse((destination / "user-data.txt").exists())
        self.assertTrue((destination / "SKILL.md").is_file())

    def test_duplicate_skill_identity_is_rejected(self):
        duplicate = self.target / "duplicate-copy"
        duplicate.mkdir()
        (duplicate / "SKILL.md").write_text(
            "---\nname: synthesise-orchestrator\nmetadata:\n  version: \"2.0.0-alpha.4\"\n---\n",
            encoding="utf-8",
        )
        result = self.run_installer("--package", "synthesise-orchestrator")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Duplicate installed skill name", result.stderr)

    def test_remove_one_package_preserves_legacy_and_other_preview_packages(self):
        self.assertEqual(self.run_installer().returncode, 0)
        removed = self.run_installer("--package", "synthesise-audience", "--remove")
        self.assertEqual(removed.returncode, 0, removed.stderr)
        self.assertFalse((self.target / "synthesise-audience").exists())
        self.assertTrue((self.target / "synthesise-discovery").exists())
        self.assertTrue(self.legacy.exists())
        data = json.loads(self.manifest.read_text(encoding="utf-8"))
        self.assertNotIn("synthesise-audience", data["packages"])

    def test_remove_all_preview_packages_leaves_v1_install_untouched(self):
        self.assertEqual(self.run_installer().returncode, 0)
        removed = self.run_installer("--remove")
        self.assertEqual(removed.returncode, 0, removed.stderr)
        self.assertFalse(self.manifest.exists())
        self.assertEqual([p for p in self.target.iterdir() if p.is_dir()], [self.legacy])


if __name__ == "__main__":
    unittest.main()
