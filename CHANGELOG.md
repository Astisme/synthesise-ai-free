# Changelog

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
