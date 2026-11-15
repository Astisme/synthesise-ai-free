# Orchestration Protocol

## 1. Intent and plan

Translate the request into:
- objective and expected deliverable;
- guided, direct or resume mode;
- constraints and user preferences;
- known project and artifact state;
- minimal required specialists;
- hard/soft/conditional prerequisites;
- decision gates and completion criteria.

Do not expose an internal plan longer than useful. Explain specialist selection when it materially helps the user understand scope.

## 2. Skill discovery and loading

Use this order:

1. Check the current harness's documented skill-discovery and activation capabilities.
2. If a native mechanism exists, use its documented invocation and verify activation.
3. If cross-skill invocation is unavailable but files are accessible, read the selected specialist's `SKILL.md` and only the references/workflows it identifies as relevant.
4. If specialist package is absent, disclose that fact and use only the corresponding legacy v1.1.0 method when accessible.
5. If no method is accessible, ask for the needed instructions or return a clearly labelled best-effort response.

Do not infer support from another harness's behaviour. Do not invent tool commands or installation paths.

## 3. Bounded context package

Provide each specialist only what it needs:

```yaml
project_id: actual-project-id-or-null
objective: Specific requested outcome
mode: direct
current_stage: product_architecture
available_artifacts:
  - artifact_id: audience-intelligence
    path: audience-intelligence.md
    status: approved
    version: known-version-or-null
required_outputs:
  - product-charter.md
constraints:
  preserve_approved_decisions: true
  preserve_methodology: true
  flag_unverified_claims: true
  do_not_overwrite_non_owned_artifacts: true
```

This is a schema illustration, not a literal project record. Populate only with verified values. Do not include unrelated artifacts, secrets, credentials or unnecessary personal data.

## 4. Specialist handoff

Use `shared/contracts/skill-handoff.md` when available. Required fields:
- contract_version
- skill_id
- project_id
- objective
- completion_status (`complete`, `partial`, `blocked`)
- inputs_used
- outputs_created
- decisions_proposed
- decisions_required
- assumptions
- evidence
- limitations
- next_recommended_skills

Empty arrays are valid. Missing required fields are not. Do not convert a partial handoff into complete by filling gaps with guesses.

## 5. Output and artifact handling

For every output identify:
- canonical artifact ID and owner;
- path or inline delivery;
- status: created, proposed, updated or not_written;
- source inputs and provenance;
- whether a write actually occurred.

A specialist may write only its own canonical artifact, subject to the environment's write permissions and user authorization. A non-owner returns a proposed patch. The orchestrator may summarize artifacts but does not become their owner.

## 6. Reconciliation

After each specialist:
1. Verify skill identity and objective.
2. Check required handoff fields.
3. Check outputs and ownership.
4. Verify hard dependencies and whether their artifacts are approved/current.
5. Separate observed evidence from assumptions and recommendations.
6. Detect conflicts with approved project decisions.
7. Record limitations and unresolved questions.
8. Recompute the smallest remaining skill set.

If a handoff is invalid, ask for correction or report partial/blocked. Do not silently normalize.

## 7. Decision gates

Ask for explicit user approval before:
- selecting or materially changing the primary UVZ opportunity;
- accepting consequential validation findings or investment decisions;
- changing audience, product promise or product scope;
- accepting material pricing/offer assumptions;
- publishing or relying on claims without adequate evidence;
- changing an approved decision;
- writing to an artifact owned by another specialist.

A recommendation is not an approval. Project Continuity records the decision after approval; it does not approve on the user's behalf.

## 8. Conflict handling

When artifacts disagree:
- preserve both sources;
- identify owner, status and available timestamps/versions;
- explain the practical conflict;
- do not choose the newest artifact automatically;
- request resolution if the conflict affects the outcome.

## 9. Project state

On resume, read the portable brief and relevant decision/status records before proposing work. Preserve unknown sections, user-authored content and prior decisions. Use relative project paths. Do not claim persistence unless an authorized write actually succeeds.

## 10. Harness limitations

- Native activation, filesystem fallback and copy/paste handoff are different execution modes; label which was used.
- If parallel execution is unavailable, execute sequentially.
- If filesystem access is unavailable, request the package or artifact from the user.
- If only the legacy monolithic skill exists, use it as a temporary source and identify the exact relevant legacy method; do not describe it as a specialist package.
