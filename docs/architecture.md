# Architecture

## Canonical source

The canonical product is the modular v2 package under `skills/`: one orchestrator and ten specialist skills. The root plugin manifests enumerate these eleven skill directories explicitly. The orchestrator owns intent interpretation, routing, dependency-aware execution plans, handoffs, reconciliation and project-state coordination. Specialists own their domain methodologies and canonical artifacts.

The former monolithic skill package has been removed from the active repository tree. New work targets only the modular v2 packages.

## Progressive disclosure

Each specialist package contains a concise `SKILL.md` entry point and its own supporting methodology references, workflows, templates and examples where appropriate. The orchestrator contains routing, dependency, execution, quality-gate and integration references.

## Portable project memory

`PROJECT-BRIEF.md` is user-owned Markdown stored with the project. It captures facts, hypotheses, evidence, decisions and next actions. It is portable across agents and is not hidden model memory. The `synthesise-project` specialist owns project continuity and decision-state updates.

## Plugin distribution

The repository root is the single plugin root for Claude Code and Codex-compatible marketplaces. Root manifests expose the orchestrator and all ten specialists under one plugin identity, `synthesise-ai-free`. Do not register the nested `skills/` directory as a second plugin.

For compatible agents without native plugin support, use the cross-platform `scripts/install.py` installer or the host's documented Agent Skills installation flow.

## Quality and maintenance

The local quality pipeline has distinct layers: structural and manifest validation (`python scripts/validate.py`), Python regression tests (`python -m unittest discover -s scripts -p 'test_*.py' -v`), and deterministic scenario/fixture evaluation (`python scripts/evaluate.py --report-dir evaluations/reports`). GitHub Actions runs all three on Ubuntu for pushes and pull requests, uploads JSON/Markdown evaluation reports, and separately runs the modular v2 installer regression suite on Windows. None of these jobs executes a live agent or calls a model provider. Keep methodology canonical and update CHANGELOG for user-visible changes.
