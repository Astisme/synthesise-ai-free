---
name: synthesise-uvz
description: >
  Generate, compare and rank Unique Value Zone opportunity hypotheses at the
  intersection of creator advantage, audience demand, differentiation,
  deliverability and commercial logic. Preserves the established weighted scoring
  method. Use when selecting or revisiting a product opportunity.
license: MIT
compatibility: Agent Skills-compatible agents; supporting scoring reference is canonical.
metadata:
  author: astisme
  version: "2.0.0-alpha.4"
---

# Synthesise UVZ

Generate a small portfolio of distinct opportunity hypotheses and compare them transparently. UVZ owns `uvz-opportunity-report.md` and the opportunity recommendation. It does not claim that a score validates demand.

## Methodology preservation — mandatory

This package extracts the canonical UVZ scoring methodology. The weights, 1–5 ratings, formula, interpretation bands, treatment of unknown evidence, confidence explanation and sensitivity-analysis rules must not drift without a separately approved methodology change.

Use `references/uvz-scoring.md` as the scoring source of truth and `examples/uvz-example.md` for the expected reasoning format.

## Required inputs

- Creator expertise/proof profile, or a clearly provisional creator-advantage hypothesis.
- Audience segment and problem context, or clearly provisional audience hypotheses.
- Relevant capacity, delivery and strategic constraints.
- Existing opportunity decisions and evidence, if this is a continuation.

If upstream evidence is missing, do not fabricate it. Produce a provisional analysis only when useful and state which ratings are weakly supported.

## Method

1. Confirm creator advantage and candidate audience/problem context.
2. Generate 3–7 distinct opportunity hypotheses before selecting a favourite.
3. Define each opportunity as a specific creator advantage × audience/job/problem × distinctive mechanism × deliverable transformation × commercial hypothesis.
4. Score every candidate on all seven canonical dimensions using the fixed weights and 1–5 scale.
5. For every rating record evidence, confidence (high/medium/low), unknowns and rationale.
6. Calculate the weighted score out of 100 using the canonical formula.
7. Compare candidates using the same rubric; do not change weights to favour a preferred idea.
8. Run sensitivity analysis when scores are within five points or low-confidence ratings could change the ranking.
9. Identify the shortlist, risks, strongest evidence gap and cheapest discriminating next test.
10. Recommend a bet or explicitly recommend more discovery rather than forcing a winner.

## Canonical output: uvz-opportunity-report.md

Include:
- Inputs and provenance.
- 3–7 distinct opportunity hypotheses.
- Full scorecard with ratings, weights, weighted contributions, evidence and confidence.
- Ranked shortlist and rationale.
- Sensitivity analysis where triggered.
- Recommended opportunity, risks and unresolved assumptions.
- Cheapest next test and decision criteria.

## Quality gates

- All seven dimensions and original weights are present and sum to 100%.
- Ratings remain 1–5 and formula remains `sum(weight × rating / 5)`, out of 100.
- Unknown evidence is not represented as a confirmed neutral fact.
- Evidence and confidence accompany scores.
- Similar opportunities are not disguised duplicates.
- Highest score is not automatically selected if reachability or delivery makes it impractical.
- Score is explicitly described as a prioritization aid, not validation.

## Progressive methodology reference

Load `references/uvz-advanced-methodology.md` whenever performing substantive uvz work. Use it to deepen the procedure, decision criteria and quality review; keep this `SKILL.md` as the concise entry point. The reference is additive and does not supersede shared contracts, approved decisions or the established UVZ methodology.

## Shared evidence and handoff contract

- Distinguish verified facts, user-provided claims, external research, analytical interpretations, hypotheses, recommendations and unknowns. Never silently promote one state into another.
- Preserve evidence provenance and limitations: stable evidence ID, claim, type, source/locator, date, status, confidence, scope/segment, sample size where relevant, limitations and consuming artifacts. Reuse does not upgrade evidence strength.
- This skill owns its canonical artifact. Other specialists may propose changes but must not silently overwrite it; cross-owner changes require owner/user approval.
- Every handoff reports skill ID, project ID, objective, inputs used, outputs created, decisions proposed, decisions requiring approval, assumptions, evidence, limitations, next recommended skills and completion status.
- Before completion, check required sections, output names, evidence support, explicit assumptions/limitations, ownership, project continuity and actionable next steps. State blockers rather than claiming completion.

## Handoff

Pass selected opportunity identifiers, full score rationale, assumptions, confidence and unresolved tests to Market Intelligence and Validation. Approved opportunity decisions are not reopened unless the user asks or material new evidence warrants a proposed review.
