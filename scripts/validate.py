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


# Validate the first modular v2 orchestrator package without changing the frozen v1.1 skill.
ORCHESTRATOR_DIR = ROOT / "skills" / "synthesise-orchestrator"
ORCHESTRATOR = ORCHESTRATOR_DIR / "SKILL.md"
if not ORCHESTRATOR.is_file():
    fail("Missing skills/synthesise-orchestrator/SKILL.md")
else:
    orchestrator_content = ORCHESTRATOR.read_text(encoding="utf-8")
    if not orchestrator_content.startswith("---\n") or orchestrator_content.count("---") < 2:
        fail("Orchestrator SKILL.md must start with terminated YAML frontmatter")
    else:
        orchestrator_frontmatter = orchestrator_content.split("---", 2)[1]
        for key in ("name:", "description:", "license:", "compatibility:"):
            if not re.search(r"(?m)^" + re.escape(key), orchestrator_frontmatter):
                fail("Orchestrator frontmatter missing " + key[:-1])
        if not re.search(r"(?m)^name:\s*synthesise-orchestrator\s*$", orchestrator_frontmatter):
            fail("Orchestrator frontmatter name must be synthesise-orchestrator")
    for heading in ("Operating contract", "Modes", "Execution protocol",
                    "Migration-era package availability", "Project continuity", "Completion response"):
        if "## " + heading not in orchestrator_content:
            fail("Orchestrator SKILL.md missing section: " + heading)
    for ref in re.findall(r"(?:references|workflows|templates|examples)/[A-Za-z0-9_./-]+\.md", orchestrator_content):
        if not (ORCHESTRATOR_DIR / ref).is_file():
            fail("Broken orchestrator reference: " + ref)

for folder in ("references", "examples"):
    if not (ORCHESTRATOR_DIR / folder).is_dir():
        fail("Missing orchestrator directory: " + folder)

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

required_files = (
    "schemas/project-brief.schema.json", "schemas/model-run.schema.json",
    "fixtures/projects/minimal-project-brief.json", "fixtures/model-run.example.json",
    "scripts/project_brief.py", "scripts/test_project_brief.py",
    "scripts/workflow_integrity.py", "scripts/test_workflow_integrity.py",
    "scripts/security_fixtures.py", "scripts/test_security_fixtures.py", "scripts/test_install.py",
    "scripts/test_ci_contract.py",
    "evaluations/workflows/product-lifecycle.json",
    "evaluations/workflows/continuity/resume-preserves-decisions.json",
    "evaluations/workflows/invalid/missing-validation-evidence.json",
    "evaluations/workflows/invalid/broken-monetization-handoff.json",
    "evaluations/workflows/invalid/decision-loss-on-resume.json",
    "evaluations/security/security-cases.json",
    "evaluations/security/fixtures/prompt-injection.md",
    "evaluations/security/fixtures/malicious-research-document.md",
    "evaluations/security/fixtures/fabricated-citations.md",
    "evaluations/security/fixtures/untrusted-instructions.md",
    "fixtures/projects/creator-analytics/PROJECT-BRIEF.md",
    "fixtures/projects/invalid/missing-sections.md",
)
for relative in required_files:
    if not (ROOT / relative).is_file():
        fail("Missing evaluation contract file: " + relative)

json_files = (
    "schemas/project-brief.schema.json", "schemas/model-run.schema.json",
    "fixtures/projects/minimal-project-brief.json", "fixtures/model-run.example.json",
    "evaluations/workflows/product-lifecycle.json",
    "evaluations/workflows/continuity/resume-preserves-decisions.json",
    "evaluations/workflows/invalid/missing-validation-evidence.json",
    "evaluations/workflows/invalid/broken-monetization-handoff.json",
    "evaluations/workflows/invalid/decision-loss-on-resume.json",
    "evaluations/security/security-cases.json",
)
for relative in json_files:
    path = ROOT / relative
    if path.is_file():
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as exc:
            fail("Invalid JSON in " + relative + ": " + str(exc))

# Validate every modular specialist package present in this checkout.
SPECIALIST_ROOT = ROOT / "skills"
for package_dir in sorted(SPECIALIST_ROOT.glob("synthesise-*")):
    if not package_dir.is_dir() or package_dir.name in ("synthesise-ai-free", "synthesise-orchestrator"):
        continue
    skill_path = package_dir / "SKILL.md"
    if not skill_path.is_file():
        fail("Missing specialist entry point: " + str(skill_path.relative_to(ROOT)))
        continue
    specialist_content = skill_path.read_text(encoding="utf-8")
    if not specialist_content.startswith("---\n") or specialist_content.count("---") < 2:
        fail("Specialist SKILL.md must start with terminated YAML frontmatter: " + package_dir.name)
        continue
    specialist_frontmatter = specialist_content.split("---", 2)[1]
    if not re.search(r"(?m)^name:\s*" + re.escape(package_dir.name) + r"\s*$", specialist_frontmatter):
        fail("Specialist frontmatter name mismatch: " + package_dir.name)
    for key in ("description:", "license:", "compatibility:", "version:"):
        if key not in specialist_frontmatter:
            fail("Specialist frontmatter missing " + key[:-1] + ": " + package_dir.name)
    for ref in re.findall(r"(?:references|workflows|templates|examples)/[A-Za-z0-9_./-]+\.md", specialist_content):
        if not (package_dir / ref).is_file():
            fail("Broken specialist reference in " + package_dir.name + ": " + ref)

if errors:
    print("Validation failed:")
    for item in errors:
        print("- " + item)
    sys.exit(1)
print("Synthesise AI Free structure, install manifests and evaluation contracts: OK")
