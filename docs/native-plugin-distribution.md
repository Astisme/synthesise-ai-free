# Native plugin distribution — modular v2 preview

**Channel:** `synthesise-v2-preview`  
**Package version:** `2.0.0-alpha.4`  
**Status:** Marketplace manifests and package contracts are committed for review. Manual installation in the native host applications remains a release acceptance gate; CI does not claim a live harness install or successful agent execution.

## Package layout

The existing repository-root plugin remains the stable v1.1.0 package:

- `plugin.json` — stable Codex-compatible plugin manifest
- `.claude-plugin/plugin.json` — stable Claude Code plugin manifest
- `skills/synthesise-ai-free/` — canonical v1.1.0 skill

The modular preview uses `skills/` as a separate plugin root:

- `skills/plugin.json` — Codex portable plugin manifest
- `skills/.claude-plugin/plugin.json` — Claude Code plugin manifest
- `skills/synthesise-orchestrator/`
- ten specialist directories under `skills/synthesise-*/`

Both preview manifests explicitly enumerate the orchestrator and ten specialists. They do not include `synthesise-ai-free`. This allows the stable and preview plugins to be discovered and installed independently.

## Marketplace entries

### Claude Code

The root `.claude-plugin/marketplace.json` retains the stable `synthesise-ai-free` entry and adds `synthesise-v2-preview` with source `./skills`.

Add the marketplace and install the preview:

```bash
claude plugin marketplace add Astisme/synthesise-ai-free
claude plugin install synthesise-v2-preview@synthesise-ai-free
claude plugin list
```

Invoke the orchestrator skill in Claude Code using its plugin-qualified skill name:

```text
/synthesise-v2-preview:synthesise-orchestrator
```

To use the stable plugin instead, install `synthesise-ai-free@synthesise-ai-free`. Do not install both versions into the same workflow unless you intentionally want both skill sets available.

### OpenAI Codex / ChatGPT desktop app

The root `.agents/plugins/marketplace.json` retains the stable root plugin and adds a Git-backed `git-subdir` entry. Its plugin root is `./skills`, selected from the repository's `main` branch.

Add or refresh the marketplace:

```bash
codex plugin marketplace add Astisme/synthesise-ai-free
codex plugin marketplace upgrade
codex plugin marketplace list
```

Then use the ChatGPT desktop app:

1. Open the Plugins Directory.
2. Select the **Synthesise AI Free** repository marketplace.
3. Install **synthesise-v2-preview**.
4. Confirm the plugin is enabled.
5. Start a new conversation and ask it to use `synthesise-orchestrator` for a small routing task.
6. Confirm the orchestrator identifies available specialist skills and does not claim a specialist was invoked unless the host actually makes it available.

The documented Codex repository-marketplace workflow uses the desktop Plugins Directory for installation. Marketplace registration in the CLI is not itself proof that the plugin was installed or loaded.

## Manual acceptance checklist

Record the host, host version, OS, date and observed result when running this checklist on real installations.

| Check | Claude Code | Codex desktop |
|---|---|---|
| Marketplace can be added/refreshed | `claude plugin marketplace add` | `codex plugin marketplace add` |
| Preview appears as separate entry | `claude plugin list` | Plugins Directory |
| Preview plugin installs | `claude plugin install` | Install from Plugins Directory |
| Orchestrator skill is discoverable | Invoke plugin-qualified skill name | Ask the host to use `synthesise-orchestrator` |
| Specialist skills are discoverable | Inspect/invoke a selected specialist | Ask the host to use a selected specialist |
| Stable v1 remains a separate option | `synthesise-ai-free` entry | `synthesise-ai-free` entry |
| Uninstall/reinstall works | Plugin manager / CLI | Plugins Directory |

A successful marketplace add is not sufficient. At minimum, verify install, discovery, one orchestrator invocation and one specialist invocation in each supported host before describing native integration as verified.

## CI coverage and limitations

The deterministic test suite validates:

- JSON syntax and plugin identities;
- explicit inclusion of exactly the eleven v2 skill paths;
- existence of each referenced `SKILL.md`;
- separate stable and preview marketplace entries;
- Codex `git-subdir` source path and required install policy;
- unchanged root v1 plugin identity/version and canonical skill presence.

CI does not currently install Claude Code or the Codex desktop application, authenticate a host session, or execute a live model. These package-contract tests therefore do not substitute for the manual acceptance checklist above. No native harness installation is claimed as completed by this PR.

## Methodology and release boundaries

This preview distribution does not change the frozen v1.1.0 methodology, UVZ scoring dimensions, weights, formulas or sensitivity rules. It does not mark v2 stable. Keep the local preview installer and native plugin marketplace paths separate from the stable v1 install route until cross-harness migration and live-install acceptance have passed.
