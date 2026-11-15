"""Contract tests for the separate native v2 preview plugin packages."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
V2_SKILLS = (
    "synthesise-orchestrator",
    "synthesise-discovery",
    "synthesise-audience",
    "synthesise-uvz",
    "synthesise-market-intelligence",
    "synthesise-validation",
    "synthesise-product-architecture",
    "synthesise-curriculum",
    "synthesise-monetization",
    "synthesise-launch",
    "synthesise-project",
)


def load_json(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


class V2NativePluginDistributionTests(unittest.TestCase):
    def test_codex_plugin_manifest_is_a_separate_v2_package(self):
        manifest = load_json("skills/plugin.json")
        self.assertEqual(manifest["name"], "synthesise-v2-preview")
        self.assertEqual(manifest["version"], "2.0.0-alpha.4")
        self.assertEqual(
            manifest["skills"],
            [f"./{name}" for name in V2_SKILLS],
        )
        for name in V2_SKILLS:
            self.assertTrue((ROOT / "skills" / name / "SKILL.md").is_file(), name)

    def test_claude_plugin_manifest_is_a_separate_v2_package(self):
        manifest = load_json("skills/.claude-plugin/plugin.json")
        self.assertEqual(manifest["name"], "synthesise-v2-preview")
        self.assertEqual(manifest["version"], "2.0.0-alpha.4")
        self.assertEqual(manifest["skills"], [f"./{name}" for name in V2_SKILLS])
        for name in V2_SKILLS:
            self.assertTrue((ROOT / "skills" / name / "SKILL.md").is_file(), name)

    def test_codex_marketplace_keeps_v1_and_exposes_v2_git_subdirectory(self):
        marketplace = load_json(".agents/plugins/marketplace.json")
        entries = {entry["name"]: entry for entry in marketplace["plugins"]}
        self.assertEqual(set(entries), {"synthesise-ai-free", "synthesise-v2-preview"})
        self.assertEqual(entries["synthesise-ai-free"]["source"]["source"], "url")
        preview = entries["synthesise-v2-preview"]
        self.assertEqual(preview["source"]["source"], "git-subdir")
        self.assertEqual(preview["source"]["path"], "./skills")
        self.assertEqual(preview["source"]["ref"], "main")
        self.assertEqual(preview["policy"]["installation"], "AVAILABLE")
        self.assertEqual(preview["policy"]["authentication"], "ON_INSTALL")
        self.assertEqual(preview["category"], "Productivity")

    def test_claude_marketplace_keeps_v1_and_exposes_v2_subdirectory(self):
        marketplace = load_json(".claude-plugin/marketplace.json")
        entries = {entry["name"]: entry for entry in marketplace["plugins"]}
        self.assertEqual(set(entries), {"synthesise-ai-free", "synthesise-v2-preview"})
        self.assertEqual(entries["synthesise-ai-free"]["source"], "./")
        self.assertEqual(entries["synthesise-v2-preview"]["source"], "./skills")

    def test_v1_root_plugin_and_canonical_skill_are_unchanged(self):
        root_plugin = load_json("plugin.json")
        self.assertEqual(root_plugin["name"], "synthesise-ai-free")
        self.assertEqual(root_plugin["version"], "1.1.0")
        self.assertEqual(root_plugin["skills"], ["./skills/synthesise-ai-free"])
        self.assertNotIn("./skills/synthesise-orchestrator", root_plugin["skills"])
        self.assertEqual(root_plugin["version"], "1.1.0")
        canonical = (ROOT / "skills" / "synthesise-ai-free" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("name: synthesise-ai-free", canonical)


if __name__ == "__main__":
    unittest.main()
