"""Contract tests for the canonical modular v2 plugin distribution."""
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
EXPECTED_PATHS = [f"./skills/{name}" for name in V2_SKILLS]


def load_json(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


class CanonicalV2PluginDistributionTests(unittest.TestCase):
    def test_codex_root_manifest_exposes_exactly_all_v2_skills(self):
        manifest = load_json("plugin.json")
        self.assertEqual(manifest["name"], "synthesise-ai-free")
        self.assertEqual(manifest["version"], "2.0.0-beta.1")
        self.assertEqual(manifest["skills"], EXPECTED_PATHS)
        for name in V2_SKILLS:
            self.assertTrue((ROOT / "skills" / name / "SKILL.md").is_file(), name)

    def test_claude_root_manifest_exposes_exactly_all_v2_skills(self):
        manifest = load_json(".claude-plugin/plugin.json")
        self.assertEqual(manifest["name"], "synthesise-ai-free")
        self.assertEqual(manifest["version"], "2.0.0-beta.1")
        self.assertEqual(manifest["skills"], EXPECTED_PATHS)
        for name in V2_SKILLS:
            self.assertTrue((ROOT / "skills" / name / "SKILL.md").is_file(), name)

    def test_codex_marketplace_has_one_root_v2_plugin(self):
        marketplace = load_json(".agents/plugins/marketplace.json")
        entries = marketplace["plugins"]
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["name"], "synthesise-ai-free")
        self.assertEqual(entries[0]["source"]["source"], "url")
        self.assertEqual(entries[0]["source"]["url"], "https://github.com/Astisme/synthesise-ai-free")
        self.assertEqual(entries[0]["policy"]["installation"], "AVAILABLE")
        self.assertEqual(entries[0]["policy"]["authentication"], "ON_INSTALL")

    def test_claude_marketplace_has_one_root_v2_plugin(self):
        marketplace = load_json(".claude-plugin/marketplace.json")
        entries = marketplace["plugins"]
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["name"], "synthesise-ai-free")
        self.assertEqual(entries[0]["source"], "./")

    def test_nested_preview_plugin_roots_are_retired(self):
        self.assertFalse((ROOT / "skills" / "plugin.json").exists())
        self.assertFalse((ROOT / "skills" / ".claude-plugin" / "plugin.json").exists())

    def test_orchestrator_is_the_default_entry_point(self):
        orchestrator = (ROOT / "skills" / "synthesise-orchestrator" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("canonical v2 distribution", orchestrator)
        self.assertNotIn("Migration-era package availability", orchestrator)
        self.assertNotIn("legacy methodology fallback", orchestrator.lower())


if __name__ == "__main__":
    unittest.main()
