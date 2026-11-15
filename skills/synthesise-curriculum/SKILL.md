---
name: synthesise-curriculum
description: Design course and learning-product blueprints using backward design, measurable outcomes, practice, feedback, assessment and production specifications.
license: MIT
compatibility: Agent Skills-compatible agents; supporting files are loaded progressively.
metadata:
  author: astisme
  version: "2.0.0-alpha.2"
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

## Handoff
Return curriculum scope, assumptions, production dependencies and acceptance criteria to Product Architecture/Project Continuity.
