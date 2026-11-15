#!/usr/bin/env python3
"""Dependency-free structural validator for the canonical Agent Skill and evaluation contracts."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "synthesise-ai-free"
SKILL = SKILL_DIR / "SKILL.md"
errors = []


def fail(message):
    errors.append(message)


if not SKILL.is_file():
    fail("Missing canonical skills/synthesise-ai-free/SKILL.md")
else:
    content = SKILL.read_text(encoding="utf-8")
    if not content.startswith("---\n") or content.count("---") < 2:
        fail("SKILL.md must start with terminated YAML frontmatter")
    else:
        frontmatter = content.split("---", 2)[1]
        for key in ("name:", "description:", "license:", "compatibility:"):
            if not re.search(r"(?m)^" + re.escape(key), frontmatter):
                fail("Frontmatter missing " + key[:-1])
        if not re.search(r"(?m)^name:\s*synthesise-ai-free\s*$", frontmatter):
            fail("Frontmatter name must be synthesise-ai-free")
    for heading in ("Operating contract", "Engagement modes", "Project memory", "Deliverable standards"):
        if "## " + heading not in content:
            fail("SKILL.md missing section: " + heading)
    for ref in re.findall(r"(?:references|workflows|templates|examples)/[A-Za-z0-9_./-]+\.md", content):
        if not (SKILL_DIR / ref).is_file():
            fail("Broken skill reference: " + ref)

for folder in ("references", "workflows", "templates", "examples"):
    if not (SKILL_DIR / folder).is_dir():
        fail("Missing directory: " + folder)

for relative in ("plugin.json", ".claude-plugin/plugin.json",
                 ".claude-plugin/marketplace.json", ".agents/plugins/marketplace.json"):
    path = ROOT / relative
    if not path.is_file():
        fail("Missing install manifest: " + relative)
        continue
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if relative.endswith("marketplace.json") and not data.get("plugins"):
            fail("Marketplace has no plugins: " + relative)
        if relative.endswith("plugin.json") and data.get("name") != "synthesise-ai-free":
            fail("Unexpected plugin name in: " + relative)
    except (json.JSONDecodeError, OSError) as exc:
        fail("Invalid manifest " + relative + ": " + str(exc))

for relative in ("schemas/project-brief.schema.json", "schemas/model-run.schema.json",
                 "fixtures/projects/minimal-project-brief.json", "fixtures/model-run.example.json",
                 "scripts/project_brief.py", "scripts/test_project_brief.py",
                 "scripts/workflow_integrity.py", "scripts/test_workflow_integrity.py",
                 "evaluations/workflows/product-lifecycle.json",
                 "evaluations/workflows/continuity/resume-preserves-decisions.json",
                 "evaluations/workflows/invalid/missing-validation-evidence.json",
                 "evaluations/workflows/invalid/broken-monetization-handoff.json",
                 "evaluations/workflows/invalid/decision-loss-on-resume.json",
                 "fixtures/projects/creator-analytics/PROJECT-BRIEF.md",
                 "fixtures/projects/invalid/missing-sections.md"):
    path = ROOT / relative
    if not path.is_file():
        fail("Missing evaluation contract file: " + relative)
        continue
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        fail("Invalid JSON in " + relative + ": " + str(exc))

if errors:
    print("Validation failed:")
    for item in errors:
        print("- " + item)
    sys.exit(1)
print("Synthesise AI Free structure, install manifests and evaluation contracts: OK")
