---
name: synthesise-launch
description: >
  Turn an approved product and offer into an executable go-to-market plan,
  including channel strategy, messaging, campaign calendar, sales assets,
  operational readiness and measurement.
license: MIT
compatibility: Agent Skills-compatible agents; research and publishing capabilities vary by harness.
metadata:
  author: astisme
---

# Synthesise Launch

Create a practical launch and operating plan grounded in an approved product, offer and target audience. Owns `go-to-market-plan.md`; planning is not evidence that a launch occurred.

## Inputs
Approved or explicitly provisional product charter and commercial offer, target audience, proof, channel access, budget/capacity, delivery readiness and launch constraints. Identify any missing prerequisite.

## Method
1. Confirm offer scope, price hypothesis, delivery capacity and audience.
2. Define launch objective and decision; choose one or more measurable outcomes.
3. Form channel and message hypotheses based on audience reachability and available proof.
4. Design positioning, core message, objection handling and supportable claims.
5. Prepare landing page/sales assets, checkout, onboarding, fulfilment and support.
6. Build a dated campaign calendar with owner, dependency, effort, deliverable and acceptance criteria.
7. QA the end-to-end customer journey, accessibility, payment, confirmation, onboarding and support escalation.
8. Launch with transparent claims, beta/pre-sale terms and realistic delivery dates.
9. Track qualified reach, leads, conversion, revenue, refunds, activation, completion, support load and customer outcomes.
10. Review evidence, interview customers where possible and prioritize the next iteration.

Use `workflows/launch.md` and `templates/launch-plan.md`.

## Canonical output: go-to-market-plan.md
Objective; audience/offer; message architecture; channel rationale; campaign calendar; sales/onboarding assets; readiness checklist; risks; metrics with definition/source/cadence; post-launch review and decision.

## Quality gates
- Claims are supportable and proof is permissioned.
- Owners, dependencies, dates and acceptance criteria are explicit.
- Checkout, onboarding and support are ready or visibly blocked.
- Metrics have definitions, sources and review cadence.
- Plans, drafts and completed activities are clearly distinguished.
- Post-launch learning loop is included.

## Progressive methodology reference

Load `references/go-to-market-methodology.md` whenever performing substantive launch work. Use it to deepen the procedure, decision criteria and quality review; keep this `SKILL.md` as the concise entry point. The reference is additive and does not supersede shared contracts, approved decisions or the frozen v1.1.0 methodology.

## Shared evidence and handoff contract

- Distinguish verified facts, user-provided claims, external research, analytical interpretations, hypotheses, recommendations and unknowns. Never silently promote one state into another.
- Preserve evidence provenance and limitations: stable evidence ID, claim, type, source/locator, date, status, confidence, scope/segment, sample size where relevant, limitations and consuming artifacts. Reuse does not upgrade evidence strength.
- This skill owns its canonical artifact. Other specialists may propose changes but must not silently overwrite it; cross-owner changes require owner/user approval.
- Every handoff reports skill ID, project ID, objective, inputs used, outputs created, decisions proposed, decisions requiring approval, assumptions, evidence, limitations, next recommended skills and completion status.
- Before completion, check required sections, output names, evidence support, explicit assumptions/limitations, ownership, project continuity and actionable next steps. State blockers rather than claiming completion.

## Handoff
Pass launch readiness, blockers, owners, metrics and next operating cycle to Project Continuity. Do not mark a task complete without evidence.
