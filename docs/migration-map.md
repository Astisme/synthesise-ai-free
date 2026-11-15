# v1.1.0 to v2.0.0 Migration Map

**Status:** Proposed migration plan; no extraction performed in this change  
**Source of truth:** existing canonical package at `skills/synthesise-ai-free/`  
**Frozen baseline:** `evaluations/baseline/checksums.json`, source commit `3b70afb997a377fd555e9888cec912c96bf4ebd9`

## 1. Migration invariant

The first modular release is an architectural extraction, not a methodology rewrite. The v1.1.0 skill and its pinned files remain the canonical behavioural reference until each extracted specialist demonstrates parity. Do not update baseline hashes simply to make tests pass.

The current canonical UVZ scoring must remain exactly:
- expertise/proof: 20%;
- problem intensity: 20%;
- willingness-to-pay evidence: 15%;
- reachability: 10%;
- differentiation: 15%;
- delivery feasibility: 10%;
- strategic fit: 10%.

Ratings remain 1–5; weighted score remains `sum(weight × rating / 5)` out of 100. Preserve the definitions, unknown-evidence treatment, confidence explanation, shortlist/recommendation logic and sensitivity analysis instructions in the canonical references. This list is a preservation check, not a replacement for the full source method.

## 2. Methodology ownership mapping

| Existing source/method | New owner | Migration treatment |
|---|---|---|
| Creator capability, experience, proof and constraint inventory; `workflows/discovery.md`; `templates/expertise-inventory.md` | Discovery | Extract with definitions and prompts intact; produce expertise profile |
| Audience problem mapping and customer context in canonical skill | Audience | Extract and deepen operational detail without changing definitions |
| `references/uvz-scoring.md`, UVZ generation/ranking in canonical skill, `examples/uvz-example.md` | UVZ | Preserve formula, weights, rating anchors, unknown handling and sensitivity rules verbatim or semantically identical; add regression fixtures |
| `workflows/market-intelligence.md`, `references/research-protocol.md` | Market Intelligence | Preserve research hierarchy, evidence standards, citations and limitations |
| `workflows/validation.md` | Validation | Preserve hypothesis, experiment, threshold and decision procedures |
| `references/product-architecture.md`, `templates/product-charter.md`, product-building portions of `workflows/product-building.md` | Product Architecture | Preserve transformation-first design, scope, promise and delivery rules |
| `templates/curriculum.md`, curriculum/backward-design portions of product-building | Curriculum | Preserve backward design: outcomes → evidence → activities → content |
| `references/commercial-strategy.md` | Monetization | Preserve offer, pricing hypothesis, unit economics and recurring-value constraints |
| `workflows/launch.md`, `templates/launch-plan.md` | Launch | Preserve campaign, channel, roadmap and measurement methods |
| Portable project brief instructions and existing project continuity practices | Project Continuity | Preserve Markdown source of truth, dated decisions, evidence state and resume behaviour |
| Cross-stage sequencing and operating contract | Orchestrator | Extract coordination only; specialist methods remain in their owner package |

Some canonical files contain material for more than one specialist. Split by clearly bounded sections only after documenting source ranges and ensuring no rule is lost or duplicated with conflicting ownership. A source paragraph may be referenced by multiple specialists only when it is a neutral shared contract, not duplicated methodology.

## 3. Source inventory and provenance

Before extraction, create an inventory mapping every canonical methodology section to:
- source file and heading/line range;
- destination specialist and destination file;
- whether copied verbatim, reorganized without semantic change, or newly authored;
- regression scenario covering the rule;
- reviewer/approval status.

Retain a migration provenance note in each specialist reference for extracted methodology. Keep the frozen baseline file untouched during architecture and extraction unless a separately reviewed methodology change is explicitly approved.

## 4. Migration sequence

1. Approve architecture, catalog, orchestration and handoff contract.
2. Build orchestrator routing against planned package IDs; test deterministic routing without requiring live model calls.
3. Extract Discovery, Audience, UVZ and Validation. Run old and new methodology fixtures side-by-side.
4. Extract Product Architecture, Curriculum, Monetization, Market Intelligence, Launch and Project Continuity.
5. Run specialist, handoff, artifact ownership, integration, project-resume and harness installation tests.
6. Compare representative outputs against v1.1.0 reference cases. Investigate every material divergence; do not automatically change the expected output to fit the new implementation.
7. Mark the old monolithic package as a migration reference only after parity and installation checks pass.
8. Deprecate the monolithic entry point only in a separately reviewed release with a migration path for existing users/projects.

## 5. Regression requirements

- Verify frozen v1.1.0 file hashes remain unchanged during extraction.
- Verify UVZ weights sum to 100% and all source rating/decision rules are retained.
- Add positive and negative cases for each specialist's required inputs and outputs.
- Verify orchestrator selects the minimal sufficient skill set.
- Verify dependency ordering and parallel eligibility.
- Verify specialist handoffs satisfy the shared contract.
- Verify artifact ownership rejects unauthorized writes.
- Verify project resume preserves approved decisions, open questions and evidence provenance.
- Verify no skill claims native cross-invocation where the harness lacks it.
- Keep deterministic fixture checks clearly distinct from live-agent evaluations.

## 6. Existing project compatibility

Existing `PROJECT-BRIEF.md` files remain readable and user-owned. Do not require a database, hidden memory migration or mandatory schema rewrite. New fields should be optional or introduced through an explicit, backwards-compatible migration. Preserve unknown sections and user-authored content when updating briefs.

Existing installers and harness compatibility remain unchanged until new package layout and multi-skill installation have been verified. No installation command in the proposal is a guaranteed interface until tested against the current installer version and target harness.

## 7. Deprecation criteria

The v1.1.0 monolithic skill may be deprecated only when:
- all ten specialist packages are complete and validated;
- orchestrator routing and fallback loading work in documented harnesses;
- regression comparisons show no unapproved methodology drift;
- existing projects resume without loss;
- full, orchestrator-only and individual specialist installation paths are tested;
- README, changelog, migration guide and compatibility matrix are updated;
- a rollback path is documented.
