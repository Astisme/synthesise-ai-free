# Synthesise AI Free

An independent, open-source Agent Skill for turning expertise into a researched, validated and launch-ready digital product.

**v1.1.0** · MIT · Canonical skill: \`skills/synthesise-ai-free/\`

Inspired by publicly described product-development concepts, including the Unique Value Zone. This project is not affiliated with or endorsed by Synthesise AI.

## What it does

1. **Discovery engine** — extract capabilities, experience, proof, assets and constraints.
2. **UVZ engine** — generate, compare and rank opportunities with transparent weighted scoring.
3. **Market intelligence** — research customers, competitors, alternatives, positioning and unmet needs.
4. **Validation engine** — design experiments, pre-sales and paid pilots with explicit decision thresholds.
5. **Product architect** — generate product charters, curricula, workbooks, templates and delivery plans.
6. **Commercial strategist** — design positioning, pricing hypotheses, tiers, offers and unit economics.
7. **Launch strategist** — produce landing-page strategy, campaigns, roadmaps and metrics.
8. **Project memory** — maintain a portable \`PROJECT-BRIEF.md\` across sessions and harnesses.

The system distinguishes evidence from assumptions. A score is not proof of demand, and no commercial outcome is guaranteed.

## Install

Recommended:

\`\`\`bash
npx skills add astisme/synthesise-ai-free
\`\`\`

Select a harness:

\`\`\`bash
npx skills add astisme/synthesise-ai-free --agent codex
npx skills add astisme/synthesise-ai-free --agent claude-code
npx skills add astisme/synthesise-ai-free --agent cursor
npx skills add astisme/synthesise-ai-free --agent github-copilot
npx skills add astisme/synthesise-ai-free --agent gemini-cli
npx skills add astisme/synthesise-ai-free --agent opencode
\`\`\`

See [docs/installation.md](docs/installation.md) for Claude Desktop, Cline, Roo Code, OpenHands, Windsurf and manual installation. Agent identifiers and native support can change; check CLI help and current harness documentation.

Manual installation:

\`\`\`bash
git clone https://github.com/astisme/synthesise-ai-free.git
cd synthesise-ai-free
bash scripts/install.sh
\`\`\`

Windows PowerShell:

\`\`\`powershell
.\\scripts\\install.ps1
\`\`\`

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

## Repository structure

\`\`\`text
skills/synthesise-ai-free/
├── SKILL.md
├── references/
├── workflows/
├── templates/
└── examples/
docs/
scripts/
.github/workflows/
\`\`\`

## Validate

Requires Python 3; no third-party dependencies:

\`\`\`bash
python scripts/validate.py
\`\`\`

GitHub Actions runs the same check on pushes and pull requests.

## Project memory

For ongoing work, ask the agent to create/update a \`PROJECT-BRIEF.md\` in your project. It stores audience, evidence, UVZ ranking, decisions, product architecture, commercial assumptions and next actions in portable Markdown. Keep secrets and unnecessary personal data out.

## Design principles

Evidence before assumptions. Customer outcomes before content volume. Validation before major production investment. Transparent scoring and uncertainty. One canonical skill, multiple compatible harnesses. Ethical marketing and realistic promises.

## Independence

This is an independent open-source implementation inspired by publicly described concepts. It does not reproduce proprietary software, private prompts, source code or internal algorithms and is not an official Synthesise AI release.

## Contributing and license

See [CONTRIBUTING.md](CONTRIBUTING.md). Licensed under the [MIT License](LICENSE).
