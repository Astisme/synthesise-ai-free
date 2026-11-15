# Synthesise AI Free

An independent, open-source Agent Skill for turning expertise into a researched, validated and launch-ready digital product.

**Canonical architecture:** modular v2 · **Current package version:** 2.0.0-alpha.4 · MIT

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

## Modular v2 — canonical architecture

The canonical product is the modular v2 system: eleven Agent Skill packages consisting of one orchestrator and ten specialists. The root plugin manifests expose all eleven packages as one plugin named `synthesise-ai-free`. Claude Code and Codex marketplaces each publish one canonical plugin entry; there is no separate v1/v2 choice.

The orchestrator is the default entry point. It selects only the specialists needed for a task, respects dependencies, coordinates evidence and artifact ownership, and maintains portable project continuity. Each specialist has its own methodology reference, handoff contract and deterministic fixtures.

The seven-dimension UVZ scoring rubric remains explicit and consistent across the UVZ specialist, including its established weights, formulas, scales and sensitivity-analysis rules. The system distinguishes evidence from assumptions; a score is not proof of demand and no commercial outcome is guaranteed.

The old monolithic skill and old installer routes are no longer the recommended product or distribution path. They may remain in repository history or as archived material, but the active plugin manifests and installation instructions target modular v2 only.

## Install

Choose one installation route per agent. Native plugins provide marketplace-based installation and updates. The filesystem installer is available for compatible skills directories.

### Claude Code

```bash
claude plugin marketplace add Astisme/synthesise-ai-free
claude plugin install synthesise-ai-free@synthesise-ai-free
```

Use `/synthesise-ai-free:synthesise-orchestrator` as the default entry point. Manage the plugin with `claude plugin list`, `claude plugin update synthesise-ai-free@synthesise-ai-free` and `claude plugin uninstall synthesise-ai-free@synthesise-ai-free`.

### OpenAI Codex

```bash
codex plugin marketplace add Astisme/synthesise-ai-free
codex plugin marketplace upgrade
codex plugin marketplace list
```

Then open the Plugins Directory in the ChatGPT desktop app, select the Synthesise AI Free marketplace and install `synthesise-ai-free`. The documented repository-marketplace flow uses the desktop Plugins Directory for installation; marketplace registration in the CLI is not proof that a plugin is installed.

### GitHub Copilot CLI

```bash
copilot plugin marketplace add Astisme/synthesise-ai-free
copilot plugin install synthesise-ai-free@synthesise-ai-free
```

Update with `copilot plugin update synthesise-ai-free`.

### Gemini CLI

Install the orchestrator and specialists as separate skills from the repository:

```bash
gemini skills install https://github.com/Astisme/synthesise-ai-free.git --path skills/synthesise-orchestrator
```

Repeat for the specialist directories you want available. The full native plugin route is preferred where supported.

### Other Agent Skills-compatible agents

Use the Vercel Skills CLI to install the orchestrator and specialist directories from the repository. Check `npx skills@latest add --help` for the supported agent identifiers and source/path syntax. Install the complete eleven-skill set where the CLI supports selecting multiple skills.

### Filesystem installation

From a repository clone, install the complete modular package:

```bash
python scripts/install.py --target .agents/skills
python scripts/install.py --target .agents/skills --verify
```

See [docs/installation.md](docs/installation.md) for install, verify, upgrade and removal instructions, and [docs/native-plugin-distribution.md](docs/native-plugin-distribution.md) for package layout and host acceptance checks.

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

The structural validator checks all eleven modular skill packages, root plugin manifests and marketplace contracts. The deterministic evaluator checks the project-brief schema, specialist methodology fixtures and cross-specialist orchestration scenarios. Fixture checks do not execute an agent and do not prove live model behaviour. See [evaluations/README.md](evaluations/README.md) for the optional captured-run evaluator and baseline update policy.

GitHub Actions runs two jobs on pushes and pull requests: (1) Ubuntu runs `python scripts/validate.py`, the complete `python -m unittest discover -s scripts -p 'test_*.py' -v` suite, and `python scripts/evaluate.py --report-dir evaluations/reports`, then uploads the deterministic JSON/Markdown reports; (2) Windows runs the modular v2 installer regression suite with `python -m unittest discover -s scripts -p 'test_install_v2.py' -v`. The workflow contract itself is regression-tested so these checks cannot silently disappear while README coverage claims remain. These checks use no API keys or live model calls.

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

## Next milestones

- **v2.0.0 beta:** complete live Claude Code and Codex Desktop installation/discovery/invocation acceptance; verify end-to-end project resume and artifact ownership in real host sessions.
- **v2.0.0 release candidate:** add repeatable cross-harness smoke tests and migration-safe project fixtures; publish a release checklist with explicit evidence for each supported host.
- **v2.1:** prototype the local-first product-development workbench described in [the workbench architecture proposal](docs/v2.1-workbench-architecture.md), keeping the modular skill packages as the canonical methodology source.

### Modular orchestration integration

The v2.0.0-alpha.4 package includes eight deterministic cross-specialist scenarios: expertise-to-charter lifecycle, capability-gated parallel research, evidence provenance, artifact ownership, approved-decision conflicts, project resume, negative validation and launch readiness. Mutation tests verify that representative contract violations are rejected. These tests validate portable handoff/state invariants; they do not invoke agents or prove live cross-harness execution.

### Workflow integrity fixtures

The deterministic integration suite uses controlled, ID-linked fixtures to check that discovery evidence and audience flow into UVZ selection; selected opportunities become falsifiable validation hypotheses; completed validation evidence bounds the product promise; curriculum modules support that promise; and the monetization offer preserves the product and audience. Resume fixtures assert that prior decisions remain unchanged and unresolved questions are not silently dropped. These checks verify data handoffs, not LLM reasoning.

### Security regression fixtures

The security fixture suite includes prompt-injection content, a malicious research attachment, an intentionally fabricated citation and quoted untrusted instructions. The evaluator treats these files as data, checks that each case is labelled untrusted, requires explicit handling controls, and rejects observed claims without verified source identifiers and locators. No fixture content is executed and no network lookup is attempted; source verification is represented by controlled fixture metadata.
