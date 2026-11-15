---
name: synthesise-curriculum
description: Design course and learning-product blueprints using backward design, measurable outcomes, practice, feedback, assessment and production specifications.
license: MIT
compatibility: Agent Skills-compatible agents; supporting files are loaded progressively.
metadata:
  author: astisme
  version: "2.0.0"
---

# Synthesise Curriculum

Translate an approved product transformation into a coherent learning experience. Owns `curriculum-blueprint.md`; it does not redefine the product promise or commercial scope.

## Inputs
An approved or explicitly provisional product charter, learner prerequisites, learning outcomes, delivery constraints and assessment requirements.

## Method — backward design
1. Confirm learner, context, prerequisites and overall learning outcome.
2. Define observable evidence that demonstrates completion.
3. Break the outcome into prerequisite capabilities and sequence them.
4. Design practice and feedback that produce the required evidence.
5. Add only the concepts/instruction necessary to perform the practice.
6. Specify module/lesson outcomes, activity, feedback, artifact and completion criteria.
7. Include assessment, remediation, learner support and accessibility.
8. Estimate effort and identify required assets and production dependencies.
9. Check that every module supports the approved transformation and promise.

The order is outcomes → evidence → activities → content. Do not start with a list of topics.

## Canonical output: curriculum-blueprint.md
Audience/prerequisites; overall outcome; completion evidence; module sequence; measurable objectives; lessons/concepts; practice; feedback; artifacts; completion criteria; effort; assessment; support/accessibility; production backlog; pilot feedback questions.

## Quality gates
Objectives use observable actions; each module supports an outcome; practice and assessment measure objectives; feedback/remediation are defined; workload is realistic; the blueprint does not expand the promise without approval.

## Progressive methodology reference

Load `references/instructional-design-methodology.md` whenever performing substantive curriculum work. Use it to deepen the procedure, decision criteria and quality review; keep this `SKILL.md` as the concise entry point. The reference is additive and does not supersede shared contracts, approved decisions or the frozen v1.1.0 methodology.

## Shared evidence and handoff contract

- Distinguish verified facts, user-provided claims, external research, analytical interpretations, hypotheses, recommendations and unknowns. Never silently promote one state into another.
- Preserve evidence provenance and limitations: stable evidence ID, claim, type, source/locator, date, status, confidence, scope/segment, sample size where relevant, limitations and consuming artifacts. Reuse does not upgrade evidence strength.
- This skill owns its canonical artifact. Other specialists may propose changes but must not silently overwrite it; cross-owner changes require owner/user approval.
- Every handoff reports skill ID, project ID, objective, inputs used, outputs created, decisions proposed, decisions requiring approval, assumptions, evidence, limitations, next recommended skills and completion status.
- Before completion, check required sections, output names, evidence support, explicit assumptions/limitations, ownership, project continuity and actionable next steps. State blockers rather than claiming completion.

## Handoff
Return curriculum scope, assumptions, production dependencies and acceptance criteria to Product Architecture/Project Continuity.
