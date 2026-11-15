# Installation

Synthesise AI Free is distributed as one modular v2 plugin named `synthesise-ai-free`. Its root manifests expose the orchestrator and all ten specialists together. There is no separate legacy/v2 marketplace choice.

**Choose one installation route per agent.** Installing the same package through multiple routes can create duplicate skills.

## Claude Code — native plugin marketplace

```bash
claude plugin marketplace add Astisme/synthesise-ai-free
claude plugin install synthesise-ai-free@synthesise-ai-free
claude plugin list
```

Inside a Claude Code session, the equivalent commands are:

```text
/plugin marketplace add Astisme/synthesise-ai-free
/plugin install synthesise-ai-free@synthesise-ai-free
```

Use `/synthesise-ai-free:synthesise-orchestrator` as the default entry point. Invoke a specialist directly only when its task-specific workflow is needed. Update and remove with:

```bash
claude plugin update synthesise-ai-free@synthesise-ai-free
claude plugin uninstall synthesise-ai-free@synthesise-ai-free
```

## OpenAI Codex — native plugin marketplace

```bash
codex plugin marketplace add Astisme/synthesise-ai-free
codex plugin marketplace upgrade
codex plugin marketplace list
```

Then open the Plugins Directory in the ChatGPT desktop app, select the Synthesise AI Free marketplace and install `synthesise-ai-free`. Confirm the plugin is enabled before invoking `synthesise-orchestrator`.

Marketplace registration in the CLI is not proof that the plugin has been installed or loaded. The root Codex manifest lists the eleven skill directories explicitly.

## GitHub Copilot CLI

```bash
copilot plugin marketplace add Astisme/synthesise-ai-free
copilot plugin install synthesise-ai-free@synthesise-ai-free
```

Update with `copilot plugin update synthesise-ai-free`.

## Gemini CLI

Install the orchestrator and each specialist directory as individual skills using the supported Gemini CLI skill-install command. For example:

```bash
gemini skills install https://github.com/Astisme/synthesise-ai-free.git --path skills/synthesise-orchestrator
```

Repeat for the specialist directories required by your workflow. Prefer the complete native plugin package where the host supports it.

## Other Agent Skills-compatible agents

Use the Vercel Skills CLI or the host's documented install-from-source flow. Install all eleven directories when supported; at minimum install the orchestrator and the specialists it routes to. Agent identifiers and CLI syntax evolve, so check `npx skills@latest add --help` for the current supported syntax.

## Filesystem installer

For compatible agents that use a skills directory, clone the repository and install all eleven modular packages:

```bash
git clone https://github.com/Astisme/synthesise-ai-free.git
cd synthesise-ai-free
python scripts/install.py --target .agents/skills
python scripts/install.py --target .agents/skills --verify
```

The installer installs the canonical modular v2 package and records it in `.synthesise-v2.json`. The installer supports individual packages, safe collision refusal, explicit forced replacement, recovery of partial installs, read-only verification and removal. See the command help with:

```bash
python scripts/install.py --help
```

## Package layout

The canonical plugin manifests live at the repository root:

- `plugin.json` — Codex-compatible plugin manifest.
- `.claude-plugin/plugin.json` — Claude Code plugin manifest.
- `.agents/plugins/marketplace.json` — Codex repository marketplace catalog.
- `.claude-plugin/marketplace.json` — Claude Code marketplace catalog.

Both plugin manifests enumerate the orchestrator and all ten specialists. There are no nested plugin manifests; do not register `skills/` as a separate plugin root.

## Verification and host acceptance

Run the repository checks from a clone:

```bash
python scripts/validate.py
python -m unittest discover -s scripts -p 'test_*.py' -v
python scripts/evaluate.py --report-dir evaluations/reports
```

These deterministic checks validate package files, manifests, handoff contracts and authored scenarios. They do not prove that a particular host installed, discovered or executed the skills. For a real host, verify plugin installation, orchestrator discovery, at least one specialist invocation and project-continuity behavior. Record the host/version/OS and observed results; never infer live execution from a successful marketplace registration.

## Project continuity

Projects remain portable files, especially `PROJECT-BRIEF.md`, evidence records, decisions and generated deliverables. Installing the plugin does not rewrite project data. Ask the orchestrator to inspect an existing project before making changes, and review proposed writes through the host's available file-approval controls.
