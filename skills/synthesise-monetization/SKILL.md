---
name: synthesise-monetization
description: Design ethical positioning, offer architecture, tiers, pricing hypotheses, revenue models and unit economics grounded in product scope and buyer evidence.
license: MIT
compatibility: Agent Skills-compatible agents; supporting files are loaded progressively.
metadata:
  author: astisme
  version: "2.0.0-alpha.2"
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

## Handoff
Pass offer definition, pricing hypotheses, capacity constraints, economics and unresolved tests to Launch.
