# Changelog

## 1.1.0 — 2026-11-15
- Moved the canonical Agent Skill into skills/synthesise-ai-free/.
- Expanded the prompt sequence into an end-to-end product development system.
- Added transparent UVZ scoring, market intelligence and research protocol.
- Added validation, product architecture, curriculum, workbook, commercial and launch workflows.
- Added portable PROJECT-BRIEF.md methodology.
- Added native Claude Code, Codex and GitHub Copilot plugin manifests/marketplaces; Gemini CLI and Skills CLI install routes; shell and PowerShell fallback installers; and manifest-aware structural validation.
- Added GitHub Actions validation, architecture, methodology, FAQ and contribution guidance.

## Unreleased — v1.2.0 evaluation foundation

- Freeze the v1.1.0 canonical skill using Git blob SHA-1 checksums anchored to the merged v1.1.0 commit.
- Add deterministic scenario contracts and reference-fixture checks; explicitly distinguish these from live-agent behaviour.
- Add a structured-section schema for extracted PROJECT-BRIEF.md data while keeping Markdown as the portable source of truth.
- Add optional offline grading of captured model/harness runs with configuration hashes and rubric score capture.
- Extend CI to run structural validation and deterministic evaluation and upload a machine-readable report.
- No canonical skill methodology files are changed.

## Unreleased — v1.2.1 Deterministic QA

- Parse actual PROJECT-BRIEF.md Markdown fixtures into structured sections and validate extracted data against the project brief schema.
- Add positive/negative project brief parser unit tests.
- Generate JSON and Markdown deterministic evaluation reports.
- Run structural validation, unit tests and deterministic evaluation in pull-request and push CI.
- No external services, model calls, API keys or third-party Python packages.
