# v1 → modular v2 preview migration guide

**Current target:** v2.0.0-alpha.4  
**Release status:** preview only; v1.1.0 remains the stable methodology and installation channel.

This guide covers coexistence and a controlled evaluation of the modular preview. It does **not** convert a project, migrate agent configuration automatically, or certify native-host integration.

## 1. Identify the installation you already have

The stable v1 skill is the directory `synthesise-ai-free/`. The v2 preview consists of eleven separate skill directories:

- `synthesise-orchestrator/`
- ten specialists: discovery, audience, UVZ, market intelligence, validation, product architecture, curriculum, monetization, launch and project

The native marketplaces expose v1 and v2 as separate plugin entries. The filesystem installer also writes a separate `.synthesise-v2-preview.json` manifest and never manages the v1 directory.

## 2. Choose one v2 installation route per host

Do not install the same v2 preview through multiple routes in one host. Choose either:

- **Native plugin:** preferred when using Claude Code or Codex desktop. Follow [native plugin distribution](native-plugin-distribution.md).
- **Filesystem preview installer:** for a compatible agent skills directory when native marketplace installation is unavailable.

Example filesystem installation alongside v1:

```bash
python scripts/install_v2_preview.py --target .agents/skills
python scripts/install_v2_preview.py --target .agents/skills --verify
```

The expected layout keeps the packages separate:

```text
.agents/skills/
├── synthesise-ai-free/             # existing stable v1; leave untouched
├── synthesise-orchestrator/        # v2 preview
├── synthesise-discovery/           # v2 preview
├── ...                             # remaining v2 specialists
└── .synthesise-v2-preview.json
```

If a destination already exists and is not tracked by the preview install manifest, the installer refuses to replace it unless `--force` is explicitly supplied. Review and back up that directory before using `--force`.

## 3. Preserve project data; do not perform a destructive skill swap

The v2 preview is a new orchestration and package layout, not a project-data schema migration. Existing `PROJECT-BRIEF.md`, research files, deliverables, decision records and evidence files remain user-owned portable files.

Before evaluating v2:

1. Commit or back up the project directory.
2. Keep the existing v1 skill installed while evaluating v2.
3. Start with a copy of an existing project, or a small non-production project.
4. Ask the orchestrator to inspect the existing project brief and report what it can safely resume.
5. Require it to distinguish existing decisions/evidence from new assumptions and proposed changes.
6. Review proposed artifact changes before allowing writes.
7. Compare the output with the v1 workflow where methodology-sensitive results matter.

Do not assume that installing v2 imports, rewrites or upgrades project files. Do not discard v1 until the relevant workflows have been accepted in the target host.

## 4. Migration acceptance checks

A migration evaluation is successful only when all applicable checks have observable results:

- v1 remains installed and its canonical directory/content is unchanged.
- Exactly one v2 distribution route is active in the host.
- All eleven v2 skills are installed or discoverable through the selected route.
- The orchestrator is discoverable and can route a narrow task.
- At least one specialist can be invoked directly.
- A copied project brief can be resumed without losing decisions, evidence status, open questions or artifact ownership.
- UVZ output retains the frozen seven dimensions, weights, formula, rating scale and sensitivity rules.
- No claim is made that parallel specialists ran unless the host actually supports and performs that execution.
- Uninstalling v2 leaves v1 and project data intact.

For filesystem installs, run the read-only verifier before and after the evaluation:

```bash
python scripts/install_v2_preview.py --target .agents/skills --verify
```

For native installations, use the host's plugin manager and record the host/version/OS and observed discovery/invocation results. Contract tests in CI do not substitute for these live-host checks.

## 5. Rollback

For a filesystem preview installation, remove only the preview packages:

```bash
python scripts/install_v2_preview.py --target .agents/skills --remove
```

This removes the preview install manifest and its tracked v2 package directories; it does not remove `synthesise-ai-free/` or project files. For native plugins, uninstall only `synthesise-v2-preview` using the host plugin manager. Do not remove the stable `synthesise-ai-free` plugin unless that is a separate, intentional action.

## 6. Record real-host acceptance

Complete one record per host and operating system. Do not mark a check passed based only on a manifest test or marketplace registration.

| Field | Result |
|---|---|
| Host and version | |
| OS and version | |
| Date | |
| Distribution route | |
| Marketplace refresh / install | |
| Orchestrator discovery and invocation | |
| Specialist discovery and invocation | |
| Project resume / artifact preservation | |
| v1 coexistence / rollback | |
| Logs or reproducible evidence | |
| Overall result and known limitations | |

## Release boundary

Passing filesystem regression tests and static marketplace contract tests demonstrates only those deterministic contracts. It does not establish live Claude Code or Codex installation, skill discovery, cross-skill execution, migration safety for every user project, or stable v2 readiness. Keep v2 labelled alpha until the real-host acceptance records and migration checks are completed.
