# Dependency Graph

## Default lifecycle

```text
Discovery -----------+
                     +--> UVZ --> Validation --> Product Architecture --> Curriculum
Audience ------------+              ^                    |
                                    |                    +--> Monetization --> Launch
Market Intelligence -+--------------+                         ^              ^
                     +-----------------------------------------+--------------+

Project Continuity coordinates project state across all stages.
```

## Dependency classes

- **Hard:** required to produce the requested output without misleading the user.
- **Soft:** improves quality/confidence; can be omitted with a visible limitation.
- **Conditional:** required only when a defined condition is true.
- **Independent:** can execute concurrently if inputs and ownership permit.

## Stage dependencies

| Specialist | Hard inputs / prerequisites | Soft or conditional inputs |
|---|---|---|
| Discovery | Creator-provided experience/capability context | Existing proof records, portfolio |
| Audience | A target context or customer/problem question | Discovery profile, interviews, market evidence |
| UVZ | Enough creator advantage and audience/problem context to compare opportunities | Market evidence; validation results |
| Market Intelligence | Defined market, audience or opportunity research question | UVZ selection, geography, customer language |
| Validation | Falsifiable opportunity/problem hypothesis and target segment | Market alternatives; existing customer evidence |
| Product Architecture | Selected or explicitly provisional opportunity and intended customer transformation | Validation evidence; creator constraints |
| Curriculum | Product charter or explicit provisional product scope with learning outcomes | Learner research, delivery constraints |
| Monetization | Defined offer scope and intended buyer | Market pricing evidence, willingness-to-pay evidence, cost data |
| Launch | Defined offer and target audience | Approved proof, channel research, conversion baseline |
| Project Continuity | Access to user-authorized project artifacts for read/update | All stage artifacts and decision records |

## Ordering constraints

- UVZ must not present a definitive ranking without sufficient expertise and audience/problem context.
- Market Intelligence and Validation may run in parallel after a candidate opportunity and target segment are defined, provided neither task depends on the other's output.
- Product Architecture must not silently convert an unvalidated assumption into a proven promise.
- Curriculum follows the product transformation and learning outcomes; it must not redefine the product promise.
- Monetization depends on a defined scope. Pricing research may be a separate parallel task when its question and output are independent.
- Launch follows an offer definition. It may prepare conditional plans while validation is incomplete, but must label assumptions.
- Project Continuity is cross-cutting; it records state and approvals but does not decide specialist questions.

## Parallel execution

Parallelize only if all conditions hold:
1. Required inputs are available to both tasks.
2. Neither task needs the other's output.
3. Outputs have distinct owners and paths.
4. No shared mutable artifact is being edited.
5. The harness explicitly supports parallel execution.

If any condition fails, run sequentially. Never claim parallel execution merely because two tasks are listed together.
