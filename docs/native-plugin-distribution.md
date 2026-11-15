# Native plugin distribution — canonical modular v2

**Plugin identity:** `synthesise-ai-free`  
**Package version:** `2.0.0-alpha.4`  
**Distribution:** one root plugin for Codex-compatible and Claude Code marketplaces.

The modular architecture is the canonical product. The marketplace does not expose a separate legacy monolith or a preview-only alternative. The current package version remains alpha.4; this document does not claim stable-release readiness or verified live-host execution.

## Package layout

The repository root is the only plugin root:

- `plugin.json` — Codex-compatible plugin manifest.
- `.claude-plugin/plugin.json` — Claude Code plugin manifest.
- `skills/synthesise-orchestrator/` — default entry point.
- Ten specialist packages under `skills/synthesise-*/`: discovery, audience, UVZ, market intelligence, validation, product architecture, curriculum, monetization, launch and project continuity.

Both root manifests enumerate exactly these eleven skill directories. There is no nested `skills/plugin.json` package root.

## Claude Code

The root `.claude-plugin/marketplace.json` contains one plugin entry, `synthesise-ai-free`, sourced from `./`.

Add the marketplace and install:

```bash
claude plugin marketplace add Astisme/synthesise-ai-free
claude plugin install synthesise-ai-free@synthesise-ai-free
claude plugin list
```

Use the orchestrator as the default entry point:

```text
/synthesise-ai-free:synthesise-orchestrator
```

Then confirm it can discover and invoke a specialist skill. Do not claim that a specialist ran unless the host actually loaded it and the task execution supports that statement.

## OpenAI Codex / ChatGPT desktop app

The root `.agents/plugins/marketplace.json` contains one plugin entry, `synthesise-ai-free`, sourced from the repository root.

Register or refresh the marketplace:

```bash
codex plugin marketplace add Astisme/synthesise-ai-free
codex plugin marketplace upgrade
codex plugin marketplace list
```

Then:

1. Open the Plugins Directory in the ChatGPT desktop app.
2. Select the **Synthesise AI Free** repository marketplace.
3. Install **synthesise-ai-free**.
4. Confirm the plugin is enabled.
5. Ask the host to use `synthesise-orchestrator` for a narrow routing task.
6. Confirm that at least one relevant specialist can be discovered and used.

Marketplace registration in the CLI is not itself proof that the plugin is installed or loaded.

## Manual acceptance checklist

Record the host, host version, OS, date and observed result.

| Check | Claude Code | Codex desktop |
|---|---|---|
| Marketplace can be added/refreshed | `claude plugin marketplace add` | `codex plugin marketplace add` |
| Canonical plugin appears | `claude plugin list` | Plugins Directory |
| Plugin installs and enables | `claude plugin install` | Install from Plugins Directory |
| Orchestrator is discoverable | Invoke plugin-qualified orchestrator | Ask host to use orchestrator |
| At least one specialist is discoverable and invoked | Invoke a selected specialist | Ask host to use a selected specialist |
| Project brief can be inspected/resumed | Test with a copied project | Test with a copied project |
| Uninstall/reinstall works | Plugin manager / CLI | Plugins Directory |

A successful marketplace add is not sufficient. Verify installation, discovery, orchestrator use and at least one specialist invocation in each supported host before describing native integration as verified.

## CI coverage and limitations

The deterministic suite checks:

- JSON syntax and canonical plugin identity/version;
- exact inclusion of the orchestrator and ten specialists in both root manifests;
- existence of every referenced `SKILL.md`;
- one canonical marketplace entry in each marketplace catalog;
- root plugin source paths and package layout;
- absence of nested plugin manifests.

CI does not install Claude Code or the Codex desktop application, authenticate a host session, or execute a live model. Contract tests are not a substitute for the manual acceptance checklist.

## Methodology boundaries

The modular v2 package uses the established seven-dimension UVZ scoring rubric, including its weights, formulas, scales and sensitivity-analysis rules. Changes to that methodology require an explicit, separately reviewed change. The orchestrator owns routing and coordination; specialists own their respective methodology and canonical outputs.


## Machine-validated acceptance reports

Use one report per host and installation route. Start from [the incomplete report fixture](../fixtures/host-acceptance/incomplete.example.json), copy it into a dedicated evidence directory, and replace the example host/version/OS/date values with the actual environment.

The report requires eight checks:

1. Marketplace refresh.
2. Plugin installation and enablement.
3. Orchestrator discovery.
4. Orchestrator invocation.
5. Specialist discovery.
6. Specialist invocation.
7. Project resume from a real project brief.
8. Artifact ownership and non-overwrite behavior.

For each check, set `status` to `passed`, `failed`, `blocked` or `not_run`. A passed check must reference at least one evidence file relative to the report directory, such as a redacted CLI transcript or host session log. Failed, blocked and not-run checks require explanatory notes. Do not include API keys, credentials or unnecessary customer data in evidence.

Validate the report structure and evidence paths:

```bash
python scripts/validate_host_acceptance.py path/to/host-report.json
```

Enforce the complete release gate:

```bash
python scripts/validate_host_acceptance.py path/to/host-report.json --release-gate
```

The report validator checks host identity, plugin version, all eight required checks, evidence file existence and path containment. It does not run the host or manufacture evidence. The release gate passes only when every check is marked passed and backed by an evidence file. Keep one report for Claude Code and one for Codex Desktop; a successful CI run is not a substitute for either report.
