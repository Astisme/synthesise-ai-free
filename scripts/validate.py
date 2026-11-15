#!/usr/bin/env python3
"""Dependency-free structural validator for the canonical Agent Skill."""
from pathlib import Path
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
        if not re.search(r"(?m)^name:\\s*synthesise-ai-free\\s*$", frontmatter):
            fail("Frontmatter name must be synthesise-ai-free")
    for heading in ("Operating contract", "Engagement modes", "Project memory", "Deliverable standards"):
        if "## " + heading not in content:
            fail("SKILL.md missing section: " + heading)
    for ref in re.findall(r"(?:references|workflows|templates|examples)/[A-Za-z0-9_./-]+\\.md", content):
        if not (SKILL_DIR / ref).is_file():
            fail("Broken skill reference: " + ref)

for folder in ("references", "workflows", "templates", "examples"):
    if not (SKILL_DIR / folder).is_dir():
        fail("Missing directory: " + folder)

if errors:
    print("Validation failed:")
    for item in errors:
        print("- " + item)
    sys.exit(1)
print("Synthesise AI Free structure: OK")
