---
name: synthesise-validation
description: Design and interpret customer, problem, demand, usability and willingness-to-pay experiments with explicit hypotheses, recruitment, thresholds and decision rules.
license: MIT
compatibility: Agent Skills-compatible agents; supporting workflow is loaded progressively.
metadata:
  author: astisme
  version: "2.0.0-alpha.4"
---

# Synthesise Validation

Reduce the most consequential uncertainty with the smallest credible experiment. Validation owns `validation-report.md`; a plan is not evidence that an experiment ran.

## Scope
Customer, problem, solution, delivery and payment hypotheses; assumption ranking; interviews, smoke tests, prototypes, concierge pilots, paid pilots and transparent pre-sales; recruitment, sample, timeframe, cost, bias, thresholds and decision rules.

## Inputs
A falsifiable hypothesis and target segment. If either is unclear, route to Audience or create an explicitly provisional hypothesis.

## Method
1. Write customer, problem, solution, delivery and payment hypotheses separately.
2. Rank assumptions by impact × uncertainty.
3. Choose the smallest experiment that can falsify the riskiest assumption.
4. Before execution, define segment, recruitment, method, sample, timeframe, cost, success/failure thresholds, bias and decision rule.
5. Match method to uncertainty: interviews for problem context; landing-page tests for qualified interest; concierge pilots for delivery; paid pilots or transparent pre-sales for willingness to pay; prototypes for usability.
6. Run the experiment and preserve raw observations with consent and provenance.
7. Separate observations from interpretation; note recruitment bias, sample limits and protocol deviations.
8. Decide proceed, iterate, pivot or stop. Explain remaining uncertainty and next test.

## Canonical output: validation-report.md
Hypothesis register; prioritized assumptions; experiment protocol; recruitment/sample; predeclared thresholds; observed results; limitations/bias; decision and rationale; next experiment.

## Quality gates
- Proposed and executed experiments are clearly distinguished.
- Decision rules were defined before execution or deviations are disclosed.
- Behavioural/payment evidence is weighted more strongly than hypothetical intent.
- Sample and recruitment limitations are explicit.
- Conclusions match evidence strength; no unsupported market-wide claims.

## Progressive methodology reference

Load `references/validation-and-experiment-design.md` whenever performing substantive validation work. Use it to deepen the procedure, decision criteria and quality review; keep this `SKILL.md` as the concise entry point. The reference is additive and does not supersede shared contracts, approved decisions or the frozen v1.1.0 methodology.

## Shared evidence and handoff contract

- Distinguish verified facts, user-provided claims, external research, analytical interpretations, hypotheses, recommendations and unknowns. Never silently promote one state into another.
- Preserve evidence provenance and limitations: stable evidence ID, claim, type, source/locator, date, status, confidence, scope/segment, sample size where relevant, limitations and consuming artifacts. Reuse does not upgrade evidence strength.
- This skill owns its canonical artifact. Other specialists may propose changes but must not silently overwrite it; cross-owner changes require owner/user approval.
- Every handoff reports skill ID, project ID, objective, inputs used, outputs created, decisions proposed, decisions requiring approval, assumptions, evidence, limitations, next recommended skills and completion status.
- Before completion, check required sections, output names, evidence support, explicit assumptions/limitations, ownership, project continuity and actionable next steps. State blockers rather than claiming completion.

## Handoff
Pass validated/unvalidated hypotheses and evidence to Product Architecture. Product promises must not exceed what validation supports.
