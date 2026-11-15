---
name: synthesise-validation
description: Design and interpret customer, problem, demand, usability and willingness-to-pay experiments with explicit hypotheses, recruitment, thresholds and decision rules.
license: MIT
compatibility: Agent Skills-compatible agents; supporting workflow is loaded progressively.
metadata:
  author: astisme
  version: "2.0.0-alpha.2"
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

## Handoff
Pass validated/unvalidated hypotheses and evidence to Product Architecture. Product promises must not exceed what validation supports.
