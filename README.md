# Synthesise AI Free

An independent, open-source Agent Skill for turning expertise into a researched, validated and launch-ready digital product.

**Canonical methodology v1.1.0** · Deterministic QA track v1.2.x · MIT · Canonical skill: `skills/synthesise-ai-free/`

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

GitHub Actions runs structural validation, Markdown brief parser unit tests and deterministic fixture evaluation on pushes and pull requests. It publishes JSON and Markdown reports as workflow artifacts. No API keys or model calls are used.

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
- v1.3.0 — Optional live model evaluation: only when explicitly enabled and credentials/budget are available. No provider SDK or API key is required by v1.2.x.

### Workflow integrity fixtures

The deterministic integration suite uses controlled, ID-linked fixtures to check that discovery evidence and audience flow into UVZ selection; selected opportunities become falsifiable validation hypotheses; completed validation evidence bounds the product promise; curriculum modules support that promise; and the monetization offer preserves the product and audience. Resume fixtures assert that prior decisions remain unchanged and unresolved questions are not silently dropped. These checks verify data handoffs, not LLM reasoning.

### Security regression fixtures

The security fixture suite includes prompt-injection content, a malicious research attachment, an intentionally fabricated citation and quoted untrusted instructions. The evaluator treats these files as data, checks that each case is labelled untrusted, requires explicit handling controls, and rejects observed claims without verified source identifiers and locators. No fixture content is executed and no network lookup is attempted; source verification is represented by controlled fixture metadata.
