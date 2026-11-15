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

The validator checks frontmatter basics, required sections and relative references. CI runs it on pushes and pull requests. Keep methodology canonical and update CHANGELOG for user-visible changes.
