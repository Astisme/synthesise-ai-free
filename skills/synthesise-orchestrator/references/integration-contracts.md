# Modular orchestration integration contracts

This reference defines cross-specialist invariants for the v2 alpha integration suite. It complements (and does not replace) the specialist methodologies, routing matrix, dependency graph or shared handoff contract.

## 1. Expertise to product charter

Discovery establishes capability, audience/problem identity and source evidence. Audience may enrich segment context but cannot silently replace the source audience. UVZ may compare opportunities using the preserved canonical v1.1.0 rubric; it must retain capability/evidence links and unknowns. Market Intelligence and Validation investigate the selected opportunity without changing its identity. Product Architecture owns the charter and must keep its promise provisional when validation is incomplete, ambiguous or recommends revision.

## 2. Parallel research eligibility

Market Intelligence and Validation may be planned concurrently only when both have the same approved candidate and segment inputs, neither consumes the other's output, their canonical output paths/owners differ, and the current harness explicitly supports parallel execution. Otherwise sequence the work and describe the reason. A plan containing two tasks is not proof that parallel execution occurred.

## 3. Evidence identity across handoffs

Evidence IDs are stable across consumers. Status, confidence, source, scope/sample and limitations remain attached. An interpretation can be added by a consumer, but must be separately labelled and cannot upgrade the source record. Conflicting evidence is retained and surfaced.

## 4. Artifact ownership

Each canonical artifact has one specialist owner. A non-owner may submit a proposed patch with rationale and provenance, but cannot claim an update or write. The owner/user approval gate must be explicit. The orchestrator may reconcile and summarize but does not assume artifact ownership.

## 5. Approved decision conflicts

A new recommendation that contradicts an approved decision creates a conflict, not a replacement. Preserve the approved record, attach the new evidence and proposal, mark resolution pending and request the appropriate user/owner decision. Never infer approval from a specialist handoff.

## 6. Project resume

Resume retains stable project identity, prior decision records byte-for-byte/semantically unchanged, unresolved questions and evidence references. New actions and superseding decisions are appended. Missing artifacts, stale evidence and conflicts are reported rather than silently reconstructed.

## 7. Negative validation

A failed or inconclusive experiment cannot produce a validated promise or validated-demand claim. Product Architecture may retain a provisional concept only with the unresolved decision and evidence limitation explicit.

## 8. Launch readiness

Checkout, onboarding and fulfillment are critical operational gates. If any are blocked or untested, launch completion remains blocked; campaign preparation may continue only as conditional planning. Reach or engagement metrics do not override operational blockers.

## Deterministic coverage

`evaluations/integration/orchestration-scenarios.json` contains eight controlled scenarios for these invariants. `scripts/orchestration_integration.py` validates the fixture contracts and `scripts/test_orchestration_integration.py` includes mutation tests proving that representative contract violations are rejected.

These checks are API-free deterministic data-contract tests. They do not invoke Agent Skills, simulate a harness, evaluate generated prose or prove live cross-agent execution. Stable v2 still requires harness-specific installation and real workflow acceptance testing.
