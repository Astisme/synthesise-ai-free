# Synthesise AI Free

An independent, open-source Agent Skill for turning expertise into a researched, validated and launch-ready digital product.

**Stable methodology:** v1.1.0 · **Deterministic QA:** v1.2.x · **Modular preview:** v2.0.0-alpha.4 · MIT

Inspired by publicly described product-development concepts, including the Unique Value Zone. This project is not affiliated with or endorsed by Synthesise AI.

## What it does

1. **Discovery engine** — extract capabilities, experience, proof, assets and constraints.
2. **UVZ engine** — generate, compare and rank opportunities with transparent weighted scoring.
3. **Market intelligence** — research customers, competitors, alternatives, positioning and unmet needs.
4. **Validation engine** — design experiments, pre-sales and paid pilots with explicit decision thresholds.
5. **Product architect** — generate product charters, curricula, workbooks, templates and delivery plans.
6. **Commercial strategist** — design positioning, pricing hypotheses, tiers, offers and unit economics.
7. **Launch strategist** — produce landing-page strategy, campaigns, roadmaps and metrics.
8. **Project memory** — maintain a portable `PROJECT-BRIEF.md` across sessions and harnesses.

The system distinguishes evidence from assumptions. A score is not proof of demand, and no commercial outcome is guaranteed.

## Modular v2.0 development

The modular v2 architecture is implemented in the repository as eleven Agent Skill packages: one orchestrator and ten specialists. Each specialist has a concise `SKILL.md`, a detailed progressive-disclosure methodology reference, shared evidence/handoff requirements and deterministic methodology fixtures. The catalog and architecture document describe the current package state.

**Distribution remains transitional.** The existing published installation routes and manifests continue to install the stable v1.1.0 canonical skill. The modular v2.0.0-alpha.3 package set is an explicit development preview; it is not yet the default plugin/marketplace installation and is not production-ready. Install or copy the orchestrator and selected specialist directories manually for preview work. Do not replace an existing v1 installation automatically. The orchestrator retains an explicitly labelled v1.1.0 methodology fallback for harnesses where a specialist is unavailable.

The modular package and methodology updates do not change the frozen v1.1.0 baseline, UVZ scoring rubric or existing installation manifests.

## Install

Choose **one installation route per agent**. Native plugins provide marketplace-based installation and update flows. The standalone Agent Skill route is available for agents that use the Skills CLI. Installing both into the same agent may create duplicate skills.

### Claude Code

```bash
claude plugin marketplace add Astisme/synthesise-ai-free
claude plugin install synthesise-ai-free@synthesise-ai-free
```

Update from the plugin manager or refresh the marketplace and reinstall/update the plugin. You can also open `/plugin` to browse and manage it.

### OpenAI Codex

```bash
codex plugin marketplace add Astisme/synthesise-ai-free
codex plugin add synthesise-ai-free@synthesise-ai-free
```

Use `codex plugin marketplace upgrade` to refresh marketplace metadata and `codex plugin list` to inspect installed plugins. The plugin is packaged with the canonical skill under `skills/`.

### GitHub Copilot CLI

```bash
copilot plugin marketplace add Astisme/synthesise-ai-free
copilot plugin install synthesise-ai-free@synthesise-ai-free
```

Use `copilot plugin update synthesise-ai-free` to update. In supported VS Code surfaces, use the plugin marketplace / install-from-source UI.

### Gemini CLI

```bash
gemini skills install https://github.com/Astisme/synthesise-ai-free.git --path skills/synthesise-ai-free
```

Re-run the command to update the installed skill.

### Other Agent Skills-compatible agents

Use the Vercel Skills CLI for Cursor, OpenCode, Windsurf, and other supported agents:

```bash
npx skills@latest add Astisme/synthesise-ai-free -a cursor
```

Replace `cursor` with the agent identifier supported by your installed Skills CLI. Omit `-a` to choose interactively. Check `npx skills@latest add --help` for the current supported agent list.

Update installed skills with:

```bash
npx skills@latest update
```

Re-run `add` when you want to select newly added skills from the repository.

### Claude Desktop and manual fallback

For Claude Desktop versions that support uploaded skills, package the complete `skills/synthesise-ai-free/` directory (including its references, workflows and templates) as an archive and import it through the skill interface.

For any Markdown-capable agent, clone the repository and copy the canonical folder into its documented skills directory:

```bash
git clone https://github.com/Astisme/synthesise-ai-free.git
mkdir -p .agents/skills
cp -R synthesise-ai-free/skills/synthesise-ai-free .agents/skills/
```

See [docs/installation.md](docs/installation.md) for the full harness matrix, update guidance and Windows instructions.

## Use it

- Help me discover my expertise and strongest proof.
- Generate and rank five UVZ opportunities for this audience.
- Research competitors and alternatives for this product.
- Design a validation experiment before I build.
- Create a complete product charter and course curriculum.
- Build my pricing tiers and unit economics assumptions.
- Create a launch plan and landing-page structure.
- Continue this project from PROJECT-BRIEF.md.

You can start at any stage; a full engagement does not require restarting discovery.

## Validate

Requires Python 3; no third-party dependencies:

```bash
python scripts/validate.py
python scripts/evaluate.py --report-dir evaluations/reports
```

The structural validator checks the skill and manifests. The deterministic evaluator checks the frozen v1.1.0 skill baseline, the extracted project-brief schema fixture and authored scenario fixtures. Fixture checks do not execute an agent and do not prove live model behaviour. See [evaluations/README.md](evaluations/README.md) for the optional captured-run evaluator and baseline update policy.

GitHub Actions runs two jobs on pushes and pull requests: (1) Ubuntu runs `python scripts/validate.py`, the complete `python -m unittest discover -s scripts -p 'test_*.py' -v` suite, and `python scripts/evaluate.py --report-dir evaluations/reports`, then uploads the deterministic JSON/Markdown reports; (2) Windows runs the PowerShell installer regression suite with `python -m unittest discover -s scripts -p 'test_install.py' -v`. The workflow contract itself is regression-tested so these checks cannot silently disappear while README coverage claims remain. These checks use no API keys or live model calls.

## Shared evidence provenance

The modular specialists use a common evidence-record convention so findings can be reused without silently upgrading their status, confidence or scope. See [the evidence-record contract](docs/evidence-record.md) and [schema](schemas/evidence-record.schema.json).

## Project memory

For ongoing work, ask the agent to create/update a `PROJECT-BRIEF.md` in your project. It stores audience, evidence, UVZ ranking, decisions, product architecture, commercial assumptions and next actions in portable Markdown. Keep secrets and unnecessary personal data out.

## Design principles

Evidence before assumptions. Customer outcomes before content volume. Validation before major production investment. Transparent scoring and uncertainty. One canonical skill, multiple compatible harnesses. Ethical marketing and realistic promises.

## Independence

This is an independent open-source implementation inspired by publicly described concepts. It does not reproduce proprietary software, private prompts, source code or internal algorithms and is not an official Synthesise AI release.

## Contributing and license

See [CONTRIBUTING.md](CONTRIBUTING.md). Licensed under the [MIT License](LICENSE).

## Deterministic QA roadmap

- v1.2.1 — Deterministic QA: parse real PROJECT-BRIEF.md examples, validate extracted sections and publish reproducible JSON/Markdown reports.
- v1.2.2 — Workflow integrity: test deterministic handoffs from discovery through monetization and preserve project decisions on resume.
- v1.2.3 — Security hardening: test prompt injection, malicious research documents, fabricated citations and untrusted instructions.
- v1.2.4 — CI and quality gate completion: harden evaluator input validation and regression-test malformed scenarios, duplicate IDs, baseline-file failures and schema edge cases; keep CI reports and artifacts mandatory.
- v1.2.5 — Installation and update regression tests: exercise Bash and PowerShell installers on their native CI platforms, including overwrite protection, forced updates and complete skill copies.
- v1.2.6 — Security and research provenance hardening: reject malformed security contracts and fixture path escapes; require auditable verification metadata for observed claims.
- v1.3.0 — Local-first product development workbench: architecture proposal published before implementation; see [the v1.3.0 workbench architecture proposal](docs/v1.3-workbench-architecture.md). Live model evaluation remains an optional, separately gated future capability and is not part of required CI.

### Modular orchestration integration

The v2.0.0-alpha.4 preview adds eight deterministic cross-specialist scenarios: expertise-to-charter lifecycle, capability-gated parallel research, evidence provenance, artifact ownership, approved-decision conflicts, project resume, negative validation and launch readiness. Mutation tests verify that representative contract violations are rejected. These tests validate portable handoff/state invariants; they do not invoke agents or prove live cross-harness execution.

### Workflow integrity fixtures

The deterministic integration suite uses controlled, ID-linked fixtures to check that discovery evidence and audience flow into UVZ selection; selected opportunities become falsifiable validation hypotheses; completed validation evidence bounds the product promise; curriculum modules support that promise; and the monetization offer preserves the product and audience. Resume fixtures assert that prior decisions remain unchanged and unresolved questions are not silently dropped. These checks verify data handoffs, not LLM reasoning.

### Security regression fixtures

The security fixture suite includes prompt-injection content, a malicious research attachment, an intentionally fabricated citation and quoted untrusted instructions. The evaluator treats these files as data, checks that each case is labelled untrusted, requires explicit handling controls, and rejects observed claims without verified source identifiers and locators. No fixture content is executed and no network lookup is attempted; source verification is represented by controlled fixture metadata.
