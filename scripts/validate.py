#!/usr/bin/env python3
"""Dependency-free structural validator for the canonical Agent Skill and evaluation contracts."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []


def fail(message):
    errors.append(message)


# Validate the canonical modular v2 orchestrator package.
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
                    "Specialist availability", "Project continuity", "Completion response"):
        if "## " + heading not in orchestrator_content:
            fail("Orchestrator SKILL.md missing section: " + heading)
    for ref in re.findall(r"(?:references|workflows|templates|examples)/[A-Za-z0-9_./-]+\.md", orchestrator_content):
        if not (ORCHESTRATOR_DIR / ref).is_file():
            fail("Broken orchestrator reference: " + ref)

for folder in ("references", "examples"):
    if not (ORCHESTRATOR_DIR / folder).is_dir():
        fail("Missing orchestrator directory: " + folder)

EXPECTED_PLUGIN_SKILLS = [
    "./skills/synthesise-orchestrator",
    "./skills/synthesise-discovery",
    "./skills/synthesise-audience",
    "./skills/synthesise-uvz",
    "./skills/synthesise-market-intelligence",
    "./skills/synthesise-validation",
    "./skills/synthesise-product-architecture",
    "./skills/synthesise-curriculum",
    "./skills/synthesise-monetization",
    "./skills/synthesise-launch",
    "./skills/synthesise-project",
]
for relative in ("plugin.json", ".claude-plugin/plugin.json",
                 ".claude-plugin/marketplace.json", ".agents/plugins/marketplace.json"):
    path = ROOT / relative
    if not path.is_file():
        fail("Missing install manifest: " + relative)
        continue
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if relative in ("plugin.json", ".claude-plugin/plugin.json"):
            if data.get("name") != "synthesise-ai-free":
                fail("Canonical plugin name must be synthesise-ai-free in: " + relative)
            if data.get("version") != "2.0.0-alpha.4":
                fail("Canonical plugin version must be 2.0.0-alpha.4 in: " + relative)
            if data.get("skills") != EXPECTED_PLUGIN_SKILLS:
                fail("Canonical plugin must expose exactly the eleven modular v2 skills: " + relative)
        else:
            plugins = data.get("plugins", [])
            if len(plugins) != 1 or plugins[0].get("name") != "synthesise-ai-free":
                fail("Marketplace must expose exactly one canonical v2 plugin: " + relative)
            elif relative == ".claude-plugin/marketplace.json" and plugins[0].get("source") != "./":
                fail("Claude marketplace must source the repository root")
            elif relative == ".agents/plugins/marketplace.json":
                source = plugins[0].get("source", {})
                if source.get("source") != "url" or source.get("url") != "https://github.com/Astisme/synthesise-ai-free":
                    fail("Codex marketplace must source the canonical repository root")
    except (json.JSONDecodeError, OSError) as exc:
        fail("Invalid manifest " + relative + ": " + str(exc))

if (ROOT / "skills" / "plugin.json").exists() or (ROOT / "skills" / ".claude-plugin" / "plugin.json").exists():
    fail("Nested plugin manifests must not remain after canonical v2 consolidation")

required_files = (
    "schemas/project-brief.schema.json", "schemas/model-run.schema.json", "schemas/evidence-record.schema.json",
    "evaluations/baseline/v2.0.0-alpha.4.json", "evaluations/baseline/checksums.json",
    "fixtures/projects/minimal-project-brief.json", "fixtures/model-run.example.json",
    "scripts/project_brief.py", "scripts/test_project_brief.py",
    "scripts/workflow_integrity.py", "scripts/test_workflow_integrity.py",
    "scripts/security_fixtures.py", "scripts/test_security_fixtures.py", "scripts/install.py", "scripts/test_install_v2.py", "scripts/test_v2_plugin_distribution.py", "docs/native-plugin-distribution.md",
    "scripts/test_ci_contract.py", "scripts/test_specialist_methodologies.py", "scripts/test_evidence_record.py", "scripts/orchestration_integration.py", "scripts/test_orchestration_integration.py",
    "evaluations/workflows/product-lifecycle.json",
    "evaluations/workflows/continuity/resume-preserves-decisions.json",
    "evaluations/workflows/invalid/missing-validation-evidence.json",
    "evaluations/workflows/invalid/broken-monetization-handoff.json",
    "evaluations/workflows/invalid/decision-loss-on-resume.json",
    "evaluations/security/security-cases.json", "evaluations/specialists/methodology-cases.json", "evaluations/integration/orchestration-scenarios.json", "docs/evidence-record.md", "skills/synthesise-orchestrator/references/integration-contracts.md",
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
    "schemas/project-brief.schema.json", "schemas/model-run.schema.json", "schemas/evidence-record.schema.json",
    "evaluations/baseline/v2.0.0-alpha.4.json", "evaluations/baseline/checksums.json",
    "plugin.json", ".claude-plugin/plugin.json", ".claude-plugin/marketplace.json", ".agents/plugins/marketplace.json",
    "evaluations/specialists/methodology-cases.json",
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

# Enforce the complete modular catalog, specialist methodology references and fixture coverage.
EXPECTED_SPECIALISTS = {
    "synthesise-discovery": ("expertise-profile.md", "references/expertise-discovery-methodology.md"),
    "synthesise-audience": ("audience-intelligence.md", "references/audience-intelligence-methodology.md"),
    "synthesise-uvz": ("uvz-opportunity-report.md", "references/uvz-advanced-methodology.md"),
    "synthesise-market-intelligence": ("market-intelligence.md", "references/market-research-methodology.md"),
    "synthesise-validation": ("validation-report.md", "references/validation-and-experiment-design.md"),
    "synthesise-product-architecture": ("product-charter.md", "references/product-transformation-architecture.md"),
    "synthesise-curriculum": ("curriculum-blueprint.md", "references/instructional-design-methodology.md"),
    "synthesise-monetization": ("commercial-strategy.md", "references/commercial-and-pricing-methodology.md"),
    "synthesise-launch": ("go-to-market-plan.md", "references/go-to-market-methodology.md"),
    "synthesise-project": ("PROJECT-BRIEF.md", "references/project-state-and-continuity-methodology.md"),
}
actual_specialists = {
    path.name for path in SPECIALIST_ROOT.glob("synthesise-*")
    if path.is_dir() and path.name not in ("synthesise-ai-free", "synthesise-orchestrator")
}
for missing in sorted(set(EXPECTED_SPECIALISTS) - actual_specialists):
    fail("Missing modular specialist package: " + missing)
for unexpected in sorted(actual_specialists - set(EXPECTED_SPECIALISTS)):
    fail("Uncatalogued modular specialist package: " + unexpected)

for skill_id, (canonical_output, methodology_ref) in EXPECTED_SPECIALISTS.items():
    package_dir = SPECIALIST_ROOT / skill_id
    skill_path = package_dir / "SKILL.md"
    if not skill_path.is_file():
        continue
    content = skill_path.read_text(encoding="utf-8")
    if methodology_ref not in content:
        fail("Specialist does not declare its methodology reference: " + skill_id)
    if not (package_dir / methodology_ref).is_file():
        fail("Missing specialist methodology reference: " + skill_id + "/" + methodology_ref)
    if "## Handoff" not in content:
        fail("Specialist is missing a handoff section: " + skill_id)
    if canonical_output not in content:
        fail("Specialist does not declare its canonical output: " + skill_id)

# Local references must remain within their owning package; existence alone is insufficient.
for package_dir in sorted(SPECIALIST_ROOT.glob("synthesise-*")):
    if not package_dir.is_dir() or package_dir.name in ("synthesise-ai-free", "synthesise-orchestrator"):
        continue
    skill_path = package_dir / "SKILL.md"
    if not skill_path.is_file():
        continue
    content = skill_path.read_text(encoding="utf-8")
    for ref in re.findall(r"(?:references|workflows|templates|examples)/[A-Za-z0-9_./-]+\.md", content):
        target = (package_dir / ref).resolve()
        try:
            target.relative_to(package_dir.resolve())
        except ValueError:
            fail("Specialist reference escapes package directory: " + package_dir.name + "/" + ref)

# Every specialist has at least two deterministic methodology fixtures.
methodology_fixture = ROOT / "evaluations" / "specialists" / "methodology-cases.json"
if not methodology_fixture.is_file():
    fail("Missing specialist methodology fixture: evaluations/specialists/methodology-cases.json")
else:
    try:
        fixture_data = json.loads(methodology_fixture.read_text(encoding="utf-8"))
        cases = fixture_data.get("cases", []) if isinstance(fixture_data, dict) else []
        counts = {skill_id: 0 for skill_id in EXPECTED_SPECIALISTS}
        seen_case_ids = set()
        for case in cases:
            if not isinstance(case, dict):
                fail("Specialist methodology fixture case must be an object")
                continue
            case_id = case.get("id")
            skill_id = case.get("skill_id")
            if not isinstance(case_id, str) or not case_id or case_id in seen_case_ids:
                fail("Specialist methodology fixture has an empty or duplicate case id")
            else:
                seen_case_ids.add(case_id)
            if skill_id not in counts:
                fail("Unknown specialist in methodology fixture: " + str(skill_id))
                continue
            counts[skill_id] += 1
            for field in ("scenario", "task", "input_context", "expected_task", "required_invariants", "reject_if"):
                if field not in case or not case[field]:
                    fail("Methodology fixture case missing " + field + ": " + str(case_id))
        for skill_id, count in counts.items():
            if count < 2:
                fail("Specialist needs at least two methodology fixtures: " + skill_id)
    except (json.JSONDecodeError, OSError, AttributeError) as exc:
        fail("Invalid specialist methodology fixture: " + str(exc))

# The modular orchestration integration suite is a required alpha release gate.
integration_fixture = ROOT / "evaluations" / "integration" / "orchestration-scenarios.json"
if integration_fixture.is_file():
    try:
        integration_data = json.loads(integration_fixture.read_text(encoding="utf-8"))
        integration_cases = integration_data.get("scenarios", [])
        required_types = {"lifecycle", "parallelism", "evidence", "ownership",
                          "decision_conflict", "resume", "validation", "launch_readiness"}
        actual_types = {case.get("type") for case in integration_cases if isinstance(case, dict)}
        ids = [case.get("id") for case in integration_cases if isinstance(case, dict)]
        if len(integration_cases) != 8:
            fail("Orchestration integration suite must contain exactly eight scenarios")
        if actual_types != required_types:
            fail("Orchestration integration suite must cover all eight required scenario types")
        if len(ids) != len(set(ids)) or any(not item for item in ids):
            fail("Orchestration integration scenario IDs must be unique and non-empty")
        if integration_data.get("api_calls_made") is not False or integration_data.get("live_agent_behaviour_tested") is not False:
            fail("Orchestration fixture must disclose deterministic/non-live evaluation scope")
    except (json.JSONDecodeError, OSError, AttributeError) as exc:
        fail("Invalid orchestration integration fixture: " + str(exc))

# Catalog identity and canonical output ownership are checked against the actual packages.
catalog_path = ROOT / "docs" / "skill-catalog.md"
if catalog_path.is_file():
    catalog = catalog_path.read_text(encoding="utf-8")
    catalog_ids = set()
    for line in catalog.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) >= 2 and cells[0].isdigit():
            skill_cell = cells[1]
            if skill_cell.startswith("`") and skill_cell.endswith("`"):
                catalog_ids.add(skill_cell[1:-1])
    expected_catalog_ids = set(EXPECTED_SPECIALISTS) | {"synthesise-orchestrator"}
    if catalog_ids != expected_catalog_ids:
        fail("Skill catalog IDs do not match the eleven modular packages: " + str(sorted(catalog_ids)))
else:
    fail("Missing docs/skill-catalog.md")

canonical_outputs = [value[0] for value in EXPECTED_SPECIALISTS.values()]
if len(canonical_outputs) != len(set(canonical_outputs)):
    fail("Duplicate canonical specialist artifact ownership detected")

for skill_id in EXPECTED_SPECIALISTS:
    skill_path = SPECIALIST_ROOT / skill_id / "SKILL.md"
    if skill_path.is_file():
        content = skill_path.read_text(encoding="utf-8")
        if "## Shared evidence and handoff contract" not in content:
            fail("Specialist missing shared evidence/handoff contract: " + skill_id)

if errors:
    print("Validation failed:")
    for item in errors:
        print("- " + item)
    sys.exit(1)
print("Synthesise AI Free structure, install manifests and evaluation contracts: OK")
