---
name: synthesise-audience
description: >
  Define and compare customer segments, ideal customer profiles, jobs-to-be-done,
  problem intensity, buying context, objections and reachability. Use when the
  target audience or customer problem needs to be understood or made actionable.
license: MIT
compatibility: Agent Skills-compatible agents; supporting files are loaded progressively.
metadata:
  author: astisme
  version: "2.0.0-alpha.4"
---

# Synthesise Audience

Translate a broad audience idea into evidence-labelled segment and problem intelligence. Audience owns `audience-intelligence.md`; it does not rank creator opportunities or claim an inferred persona is a real customer.

## Scope

- Segment definitions grounded in context and behaviour.
- Ideal customer profile (ICP) hypotheses and distinctions between user, buyer and beneficiary.
- Jobs-to-be-done, triggering situations, workarounds and switching context.
- Functional, emotional and social pains; desired outcomes and success criteria.
- Frequency, severity, urgency, consequences, buying authority, budget and objections.
- Reachability, channels and evidence gaps.

## Non-goals

- Do not invent customer interviews, quotes, market prevalence or willingness-to-pay evidence.
- Do not use demographics as a substitute for a meaningful segment.
- Do not treat likes, survey enthusiasm or hypothetical intent as purchase evidence.
- Do not choose a final UVZ opportunity or write the product promise.

## Required inputs

A target context, problem area or creator hypothesis is sufficient to begin. A discovery profile, customer records, interview notes and market evidence improve quality but are not mandatory for exploratory work. State what is missing.

## Method

1. Define the decision and candidate market context.
2. Generate distinct segments by situation, behaviour, need, constraints or buying context.
3. For each segment identify user, buyer and beneficiary; distinguish them where they differ.
4. Map trigger, job-to-be-done, current workaround, alternatives and switching costs.
5. Describe functional, emotional and social pains and desired outcomes.
6. Assess frequency, severity, urgency and consequences using observed evidence where possible.
7. Record buying authority, budget ownership, objections, procurement friction and evidence of existing spend.
8. Assess where the segment can be identified and reached; distinguish channel hypotheses from proven access.
9. Label every claim as observed, customer-reported, secondary-source evidence, inference, hypothesis or unknown.
10. Recommend the highest-value unresolved question or research step.

## Canonical output: audience-intelligence.md

Include segment comparison, ICP hypotheses, JTBD map, pain/outcome map, buying context, reachability assessment, source/evidence register, confidence and open questions.

## Quality gates

- Segment definitions describe context and behaviour, not demographic stereotypes.
- Personas inferred from limited evidence are labelled hypotheses.
- User, buyer and beneficiary are separated when relevant.
- Observations and interpretations are distinguishable.
- Problem intensity and willingness to pay are not conflated.
- Reachability is grounded in identifiable channels or explicitly labelled as a hypothesis.

## Progressive methodology reference

Load `references/audience-intelligence-methodology.md` whenever performing substantive audience work. Use it to deepen the procedure, decision criteria and quality review; keep this `SKILL.md` as the concise entry point. The reference is additive and does not supersede shared contracts, approved decisions or the frozen v1.1.0 methodology.

## Shared evidence and handoff contract

- Distinguish verified facts, user-provided claims, external research, analytical interpretations, hypotheses, recommendations and unknowns. Never silently promote one state into another.
- Preserve evidence provenance and limitations: stable evidence ID, claim, type, source/locator, date, status, confidence, scope/segment, sample size where relevant, limitations and consuming artifacts. Reuse does not upgrade evidence strength.
- This skill owns its canonical artifact. Other specialists may propose changes but must not silently overwrite it; cross-owner changes require owner/user approval.
- Every handoff reports skill ID, project ID, objective, inputs used, outputs created, decisions proposed, decisions requiring approval, assumptions, evidence, limitations, next recommended skills and completion status.
- Before completion, check required sections, output names, evidence support, explicit assumptions/limitations, ownership, project continuity and actionable next steps. State blockers rather than claiming completion.

## Handoff

Provide segment IDs/names consistently for downstream UVZ, Market Intelligence and Validation. Include evidence, confidence, unknowns and any sample limitations. Do not silently change an approved segment definition.
