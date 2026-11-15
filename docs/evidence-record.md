# Shared evidence record

Synthesise specialists may reuse evidence, but they must preserve its meaning and strength. This record is a portable convention for customer interviews, observations, experiments, creator-reported claims and external research.

## Required discipline

- Assign a stable `evidence_id`; do not mint a new identity merely because another specialist consumes the record.
- Preserve the original claim, source/locator, date, status, confidence, scope, sample size and limitations.
- Keep reported, observed, verified, inferred and hypothetical states distinct. Verification is claim- and scope-specific.
- Record which hypotheses and artifacts the evidence supports and which specialists consume it.
- A downstream summary may add an interpretation, but it must cite the evidence ID and must not silently upgrade confidence or status.
- When evidence is contradicted or superseded, append a new record or status transition with provenance; do not erase history.

## Example

```yaml
evidence_id: E-001
claim: "The target audience struggles with onboarding."
type: customer_interview
source: interview-03.md
date: 2026-11-15
status: reported
confidence: low
scope:
  description: "One interview with an early-stage consultant"
  segment: early-stage-consultants
  sample_size: 1
limitations:
  - Single interview
  - No behavioural validation
supports:
  - hypothesis-onboarding-problem
used_by:
  - synthesise-audience
  - synthesise-validation
```

The JSON Schema at `schemas/evidence-record.schema.json` defines a machine-checkable envelope. It intentionally allows specialist-specific scope metadata while requiring the evidence identity and qualification fields. Schema validity does not independently verify a source or prove a claim.
