# Architecture

## Canonical source

skills/synthesise-ai-free/ is the sole canonical skill package. Add harness-specific adapters only when a documented technical requirement exists; adapters must point to canonical content, not become methodology forks.

## Progressive disclosure

- SKILL.md: identity, operating contract, stage selection and workflow.
- references/: stable methods, rubrics, research standards and quality gates.
- workflows/: stage execution procedures.
- templates/: reusable deliverables.
- examples/: illustrative, clearly labelled examples.

## Portable project memory

PROJECT-BRIEF.md is user-owned Markdown stored with the project. It captures facts, hypotheses, evidence, decisions and next actions. It is portable across agents and is not hidden model memory.

## Compatibility

The package follows the Agent Skills convention: a skill directory containing SKILL.md with YAML frontmatter and relative supporting files. The Skills CLI can install it into supported harnesses. Manual installation is the fallback for Markdown-capable agents.

## Quality and maintenance

The local quality pipeline has distinct layers: structural and manifest validation (`python scripts/validate.py`), Python regression tests (`python -m unittest discover -s scripts -p 'test_*.py' -v`), and deterministic scenario/fixture evaluation (`python scripts/evaluate.py --report-dir evaluations/reports`). GitHub Actions runs all three on Ubuntu for pushes and pull requests, uploads JSON/Markdown evaluation reports, and separately runs the PowerShell installer regression suite on Windows. The CI contract is itself covered by a regression test to prevent accidental reduction to structural validation only. None of these jobs executes a live agent or calls a model provider. Keep methodology canonical and update CHANGELOG for user-visible changes.
