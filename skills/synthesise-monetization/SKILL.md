---
name: synthesise-monetization
description: Design ethical positioning, offer architecture, tiers, pricing hypotheses, revenue models and unit economics grounded in product scope and buyer evidence.
license: MIT
compatibility: Agent Skills-compatible agents; supporting files are loaded progressively.
metadata:
  author: astisme
  version: "2.0.0-alpha.4"
---

# Synthesise Monetization

Translate a defined product into a commercially coherent, transparent offer. Owns `commercial-strategy.md`; it does not expand product scope or promise guaranteed revenue.

## Inputs
Approved product charter/scope, target buyer, evidence of willingness to pay, delivery/support costs and creator constraints. Missing cost or pricing evidence remains an assumption.

## Method
1. State audience, situation/problem, outcome, mechanism and proof.
2. Define the core offer: scope, format, delivery, support, prerequisites and exclusions.
3. Add tiers only when they serve materially different needs (self-serve, guided, implementation).
4. Define price hypotheses with currency, billing basis and rationale.
5. Triangulate alternatives, problem cost, buyer budget, delivery cost, support time, capacity, positioning and risk.
6. Model variable costs, contribution margin and break-even where inputs exist.
7. Include payment, refund/cancellation terms for legal review, bonuses and acquisition/retention logic.
8. For recurring billing, specify continuing value, servicing cost and churn assumptions.
9. Identify the highest-value pricing or offer experiment.
10. Review for ethical claims, hidden fees, misleading scarcity and unsupported proof.

## Canonical output: commercial-strategy.md
Positioning; buyer; offer scope; tier comparison; pricing hypotheses; economics assumptions/calculations; terms to review; delivery capacity; risks; validation questions.

## Quality gates
Estimates and assumptions are labelled; price includes currency and billing basis; scope aligns with the charter; recurring billing requires recurring value; no fabricated proof or deceptive scarcity; economics state excluded costs.

## Progressive methodology reference

Load `references/commercial-and-pricing-methodology.md` whenever performing substantive monetization work. Use it to deepen the procedure, decision criteria and quality review; keep this `SKILL.md` as the concise entry point. The reference is additive and does not supersede shared contracts, approved decisions or the frozen v1.1.0 methodology.

## Shared evidence and handoff contract

- Distinguish verified facts, user-provided claims, external research, analytical interpretations, hypotheses, recommendations and unknowns. Never silently promote one state into another.
- Preserve evidence provenance and limitations: stable evidence ID, claim, type, source/locator, date, status, confidence, scope/segment, sample size where relevant, limitations and consuming artifacts. Reuse does not upgrade evidence strength.
- This skill owns its canonical artifact. Other specialists may propose changes but must not silently overwrite it; cross-owner changes require owner/user approval.
- Every handoff reports skill ID, project ID, objective, inputs used, outputs created, decisions proposed, decisions requiring approval, assumptions, evidence, limitations, next recommended skills and completion status.
- Before completion, check required sections, output names, evidence support, explicit assumptions/limitations, ownership, project continuity and actionable next steps. State blockers rather than claiming completion.

## Handoff
Pass offer definition, pricing hypotheses, capacity constraints, economics and unresolved tests to Launch.
