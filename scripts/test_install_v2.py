"""Cross-platform regression tests for the canonical modular v2 installer."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / "scripts" / "install.py"
PACKAGE_IDS = (
    "synthesise-orchestrator", "synthesise-discovery", "synthesise-audience",
    "synthesise-uvz", "synthesise-market-intelligence", "synthesise-validation",
    "synthesise-product-architecture", "synthesise-curriculum",
    "synthesise-monetization", "synthesise-launch", "synthesise-project",
)


class V2InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="synthesise v2 installer ")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.target = self.root / "agent skills with spaces"
        self.unrelated_skill = self.target / "existing-unrelated-skill"
        self.unrelated_skill.mkdir(parents=True)
        (self.unrelated_skill / "SKILL.md").write_text("---\nname: existing-unrelated-skill\n---\nunrelated installed skill data\n", encoding="utf-8")
        self.manifest = self.target / ".synthesise-v2.json"

    def run_installer(self, *args):
        return subprocess.run(
            [sys.executable, str(INSTALLER), "--target", str(self.target), *args],
            cwd=self.root, text=True, capture_output=True, check=False,
        )

    def test_full_install_preserves_unrelated_skills_and_records_all_packages(self):
        result = self.run_installer()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("unrelated installed skill data", (self.unrelated_skill / "SKILL.md").read_text(encoding="utf-8"))
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
            "---\nname: synthesise-orchestrator\nmetadata:\n  version: \"2.0.0\"\n---\n",
            encoding="utf-8",
        )
        result = self.run_installer("--package", "synthesise-orchestrator")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Duplicate skill identity", result.stderr)

    def test_remove_one_package_preserves_other_installed_skills(self):
        self.assertEqual(self.run_installer().returncode, 0)
        removed = self.run_installer("--package", "synthesise-audience", "--remove")
        self.assertEqual(removed.returncode, 0, removed.stderr)
        self.assertFalse((self.target / "synthesise-audience").exists())
        self.assertTrue((self.target / "synthesise-discovery").exists())
        self.assertTrue(self.unrelated_skill.exists())
        data = json.loads(self.manifest.read_text(encoding="utf-8"))
        self.assertNotIn("synthesise-audience", data["packages"])

    def test_remove_all_packages_leaves_unrelated_skills_untouched(self):
        self.assertEqual(self.run_installer().returncode, 0)
        removed = self.run_installer("--remove")
        self.assertEqual(removed.returncode, 0, removed.stderr)
        self.assertFalse(self.manifest.exists())
        self.assertEqual([p for p in self.target.iterdir() if p.is_dir()], [self.unrelated_skill])

    def test_verify_full_install_is_read_only_and_accepts_unrelated_skills(self):
        self.assertEqual(self.run_installer().returncode, 0)
        before = {p.name: p.read_bytes() for p in self.target.iterdir() if p.is_file()}
        verified = self.run_installer("--verify")
        self.assertEqual(verified.returncode, 0, verified.stderr)
        self.assertIn("Install verification passed (read-only).", verified.stdout)
        after = {p.name: p.read_bytes() for p in self.target.iterdir() if p.is_file()}
        self.assertEqual(before, after)
        self.assertIn("unrelated installed skill data", (self.unrelated_skill / "SKILL.md").read_text(encoding="utf-8"))

    def test_verify_detects_missing_package_directory(self):
        self.assertEqual(self.run_installer().returncode, 0)
        import shutil
        shutil.rmtree(self.target / "synthesise-launch")
        verified = self.run_installer("--verify")
        self.assertNotEqual(verified.returncode, 0)
        self.assertIn("synthesise-launch: installed package or SKILL.md is missing", verified.stderr)

    def test_verify_detects_identity_and_version_drift(self):
        self.assertEqual(self.run_installer("--package", "synthesise-discovery").returncode, 0)
        skill = self.target / "synthesise-discovery" / "SKILL.md"
        content = skill.read_text(encoding="utf-8")
        skill.write_text(content.replace('version: "2.0.0"', 'version: "2.0.0-alpha.3"'), encoding="utf-8")
        verified = self.run_installer("--package", "synthesise-discovery", "--verify")
        self.assertNotEqual(verified.returncode, 0)
        self.assertIn("manifest version 2.0.0 does not match installed version 2.0.0-alpha.3", verified.stderr)

    def test_verify_rejects_untracked_v2_package_directory(self):
        self.assertEqual(self.run_installer("--package", "synthesise-discovery").returncode, 0)
        untracked = self.target / "synthesise-launch"
        untracked.mkdir()
        (untracked / "SKILL.md").write_text("---\nname: synthesise-launch\nmetadata:\n  version: \"2.0.0\"\n---\n", encoding="utf-8")
        verified = self.run_installer("--verify")
        self.assertNotEqual(verified.returncode, 0)
        self.assertIn("synthesise-launch: directory exists but is not tracked", verified.stderr)

    def test_verify_requires_manifest_and_does_not_create_target(self):
        absent_target = self.root / "missing-target"
        result = subprocess.run(
            [sys.executable, str(INSTALLER), "--target", str(absent_target), "--verify"],
            cwd=self.root, text=True, capture_output=True, check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(absent_target.exists())


if __name__ == "__main__":
    unittest.main()
