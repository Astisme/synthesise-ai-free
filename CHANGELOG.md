# Changelog

## v2.0.0-beta.1-preview — Isolated distribution installer

- Add a separate cross-platform Python installer for the modular v2 preview, supporting complete or individual package installation.
- Add install-manifest tracking, duplicate identity detection, safe collision refusal, explicit forced upgrade, partial-install recovery and package removal.
- Preserve the stable v1.1.0 package, stable plugin identities and v1 installer scripts; the following distribution milestone adds separate preview-only marketplace entries.
- Add regression coverage for v1 isolation, idempotence, partial recovery, collision handling, duplicate detection and removal.
- Add separate Claude Code and Codex marketplace entries for the eleven-skill v2 preview package; retain the v1 marketplace entries as separate install choices.
- Add deterministic manifest/path contract tests and a manual real-host acceptance checklist. CI does not claim a live Claude Code or Codex desktop installation.
- This is a distribution preview, not a stable v2 release or proof of native harness execution.


## v2.0.0-alpha.4 — Orchestration integration contracts

- Add eight deterministic cross-specialist scenarios covering expertise-to-charter flow, capability-gated parallel research, evidence provenance, artifact ownership, approved-decision conflicts, project resume, negative validation and launch readiness.
- Add mutation tests that reject representative handoff, ownership, evidence, decision and readiness violations.
- Include the integration suite in the main deterministic evaluator and repository validator.
- Document the orchestrator's cross-specialist integration contracts and update architecture/catalog/specification status.
- Advance modular package metadata to alpha.4.
- Preserve the frozen v1.1.0 methodology, original seven-dimension UVZ scoring and stable v1 installation routes.
- These are API-free deterministic state/handoff tests, not live-agent or cross-harness execution tests. Installation and real workflow acceptance remain stable-release gates.

## v2.0.0-alpha.3 — Specialist methodology depth and repository synchronization

- Mark all ten specialist packages and the orchestrator as implemented in the repository preview; keep stable installation on the legacy v1.1.0 package.
- Add dedicated progressive-disclosure methodology references for all ten specialists, including tacit expertise extraction, JTBD and behavioural segmentation, UVZ interpretation, market research, experiment design, transformation architecture, instructional design, commercial economics, go-to-market operations and project continuity.
- Add shared evidence provenance and handoff requirements to every specialist entry point.
- Add two deterministic methodology scenarios per specialist and a dependency-free fixture contract test.
- Extend the main validator to enforce the exact ten-specialist catalog, canonical output ownership declarations, methodology reference availability, local-reference containment and fixture coverage.
- Synchronize README, skill catalog and architecture implementation status.
- Preserve the frozen v1.1.0 methodology, original seven-dimension UVZ scoring and existing plugin/marketplace installation manifests.
- This remains an alpha development preview; cross-harness installation and end-to-end integration are not yet a stable-release claim.

## v2.0.0-alpha.2 — Specialist package expansion

- Add the Discovery, Audience and UVZ specialist packages with creator evidence inventory, segment/JTBD intelligence and the preserved v1.1.0 UVZ rubric.
- Add Market Intelligence, Validation, Product Architecture, Curriculum and Monetization specialist packages with source provenance, predeclared experiments, bounded product promises, backward design and ethical offer economics.
- Add Launch and Project Continuity packages with operational readiness, portable project brief, append-only decisions and status tracking.
- Add deterministic specialist evaluation fixtures and package structure tests.
- Keep the v1.1.0 monolithic skill, frozen baseline and existing installation manifests unchanged; modular packages remain an alpha development preview.

## v2.0.0-alpha.1 — Orchestrator implementation preview

- Add the first modular package, `synthesise-orchestrator`, with guided/direct/resume modes, minimal-skill routing, dependency-aware planning, progressive disclosure, honest cross-harness loading fallbacks and project continuity rules.
- Add routing, dependency, orchestration protocol and quality-gate references plus worked routing examples.
- Add structural validator coverage and unit tests for package metadata, progressive-disclosure links, legacy fallback honesty, parallel-execution constraints and handoff fields.
- Preserve the canonical v1.1.0 skill, frozen methodology baseline, existing installers and current plugin manifests.
- This is a development preview, not a complete modular distribution: specialist packages and installer/marketplace integration are not included.

## v1.2.0 — Evaluation foundation (merged to main)

- Freeze the v1.1.0 canonical skill using Git blob SHA-1 checksums anchored to the merged v1.1.0 commit.
- Add deterministic scenario contracts and reference-fixture checks; explicitly distinguish these from live-agent behaviour.
- Add a structured-section schema for extracted PROJECT-BRIEF.md data while keeping Markdown as the portable source of truth.
- Add optional offline grading of captured model/harness runs with configuration hashes and rubric score capture.
- Extend CI to run structural validation, unit tests and deterministic evaluation and upload a machine-readable report.
- No canonical skill methodology files are changed.

## v1.2.1 — Deterministic QA (merged to main)

- Parse actual PROJECT-BRIEF.md Markdown fixtures into structured sections and validate extracted data against the project brief schema.
- Add positive/negative project brief parser unit tests.
- Generate JSON and Markdown deterministic evaluation reports.
- Run structural validation, unit tests and deterministic evaluation in pull-request and push CI.
- No external services, model calls, API keys or third-party Python packages.

## v1.2.2 — Workflow integrity (merged to main)

- Add deterministic product lifecycle handoff fixtures from discovery through monetization.
- Verify selected opportunities map to validation hypotheses, completed validation evidence bounds the product promise, curriculum supports that promise, and the offer preserves the product/audience IDs.
- Add project-resume fixtures that reject dropped or silently modified prior decisions and dropped open questions.
- Add negative fixtures for missing validation evidence, broken monetization handoffs and decision loss.

## v1.2.3 — Security hardening (merged to main)

- Add adversarial prompt-injection, malicious research-document, fabricated-citation and untrusted-instruction fixtures.
- Add deterministic checks for trust labels, handling controls, claim-state separation and verified provenance requirements for observed claims.
- Add negative tests for trusted promotion, missing controls and unverified citations.
- Security fixtures are never executed; no network calls, API keys or external scanners are required.

## v1.2.4 — CI and quality gate completion (merged to main)

- Harden deterministic scenario validation against malformed JSON, non-object roots, duplicate/empty IDs and invalid contract field types.
- Add evaluator infrastructure unit tests for valid and malformed scenarios, duplicate IDs, missing baseline inputs and schema type edge cases.
- Keep the dependency-free CI pipeline, JSON/Markdown reports and artifact upload; no methodology or canonical skill files are changed.

## v1.2.5 — Installation and update regression tests (merged to main)

- Add automated Bash and PowerShell installer tests for fresh installs, safe refusal to overwrite, forced updates, complete nested skill copies and paths containing spaces.
- Run the PowerShell installer suite on Windows CI and the Bash installer suite on the existing Ubuntu CI job.
- Extend structural validation to require the installer regression suite.
- No new runtime dependencies and no changes to canonical product methodology.

## v1.2.6 — Security and research provenance hardening (merged to main)

- Reject malformed suite, case, claim and source structures without uncaught type errors.
- Resolve security fixture paths and reject absolute paths or paths escaping the repository root, including symlink escapes.
- Require explicit verification method and ISO date metadata for observed claims in addition to a verified source ID and locator.
- Add regression tests for path traversal, malformed contracts, invalid claim statuses and positive/negative provenance cases.
- Keep fixture handling offline and data-only; no external scanners, network calls, model calls or third-party dependencies.

## v1.2.7 — Public-source alignment (this PR)

- Make the changelog status of merged v1.2.x work explicit without implying that GitHub Releases or version tags were published.
- Document the actual Ubuntu and Windows CI jobs and add a regression test that fails if the workflow is reduced to structural validation alone.
- Publish the v1.3.0 local-first workbench architecture proposal before implementation.
