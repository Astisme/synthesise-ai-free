# Specialist Skill Handoff Contract

**Contract version:** 1.0.0-draft  
**Status:** Proposed for Synthesise v2.0.0

## 1. Purpose

Every specialist returns a structured handoff so the orchestrator can reconcile outputs, preserve provenance, detect blockers and select the next appropriate skill. The handoff describes work performed; it does not imply that recommendations are validated or decisions approved.

## 2. Required fields

| Field | Type | Required | Contract |
|---|---|---:|---|
| `contract_version` | string | Yes | Version of this handoff contract |
| `skill_id` | string | Yes | Exact specialist package ID |
| `project_id` | string or null | Yes | Stable project identifier; null only for stateless work |
| `objective` | string | Yes | Task the specialist was asked to perform |
| `completion_status` | enum | Yes | `complete`, `partial` or `blocked` |
| `inputs_used` | array | Yes | Artifacts, evidence and user-provided inputs actually used |
| `outputs_created` | array | Yes | Deliverables created, proposed or returned inline |
| `decisions_proposed` | array | Yes | Recommendations not yet approved |
| `decisions_required` | array | Yes | Consequential questions requiring user/owner decision |
| `assumptions` | array | Yes | Unverified assumptions and their impact |
| `evidence` | array | Yes | Supporting evidence with provenance and epistemic status |
| `limitations` | array | Yes | Missing information, scope limits and uncertainty |
| `next_recommended_skills` | array | Yes | Suggested next specialist IDs and rationale |

Empty arrays are valid when there is nothing to report. Do not omit required fields.

## 3. Recommended YAML representation

```yaml
contract_version: "1.0.0-draft"
skill_id: synthesise-validation
project_id: example-project
objective: Assess whether the selected problem merits a paid pilot
completion_status: partial
inputs_used:
  - artifact_id: audience-intelligence
    path: audience-intelligence.md
    status: approved
outputs_created:
  - artifact_id: validation-plan
    path: validation-plan.md
    status: proposed
decisions_proposed:
  - decision_id: choose-pilot-segment
    recommendation: Start with segment A
    rationale: Stronger observed urgency in available interviews
decisions_required:
  - decision_id: approve-recruitment-budget
    question: Approve the proposed recruitment budget?
assumptions:
  - statement: The interview sample is representative of the initial niche
    impact: May overstate demand
evidence:
  - evidence_id: interview-01
    claim: Participants currently use manual workarounds
    status: observed
    source: interview-notes.md
    locator: section-2
limitations:
  - Only five interviews are available; no purchase behaviour observed
next_recommended_skills:
  - skill_id: synthesise-market-intelligence
    reason: Compare current alternatives before pilot positioning
```

Example values are illustrative and must not be treated as real project facts.

## 4. Field semantics

### Inputs

Each input identifies the exact source actually consulted. Include artifact ID/path, version or status where available. Do not list files that were merely available but not read.

### Outputs

Each output records a canonical artifact ID, path or inline-delivery identifier, status (`created`, `proposed`, `updated`, `not_written`) and owner. A proposed patch is not a committed file write. A specialist must not claim a file was saved unless the environment confirms it.

### Decisions

Proposals and required approvals are separate. A decision becomes approved only after an explicit user/authorized owner approval and a corresponding project decision record. Never convert a recommendation into an approved decision implicitly.

### Evidence

Evidence records should identify the claim, epistemic status (for example observed, inferred, assumed or unknown), source identifier, locator and verification metadata where applicable. Preserve the repository's existing research provenance requirements. An evidence entry is not independently verified merely because it appears in a handoff.

### Completion

- `complete`: requested specialist task and its required outputs are complete; open assumptions/limitations may remain and must be listed.
- `partial`: useful work exists but at least one requested output or required step remains incomplete.
- `blocked`: a missing prerequisite, permission, unavailable skill or unresolved decision prevents meaningful completion.

Completion status is separate from evidence strength, demand validation and project approval.

## 5. Ownership and write rules

- Specialists write only artifacts they own, or return proposed patches for another owner.
- The orchestrator may compose a summary but does not take ownership of specialist artifacts.
- Project Continuity owns project status and decision records; it records approvals but does not make domain decisions.
- Do not overwrite approved decisions or user-authored sections without explicit authorization.
- Use portable relative paths and preserve existing project content.

## 6. Orchestrator validation

The orchestrator must reject or mark invalid a handoff that:
- omits any required field;
- uses an unknown completion status;
- names a skill ID inconsistent with the executing specialist;
- claims an output was created without a path/inline result or execution evidence;
- treats an unapproved proposal as a decision;
- lacks provenance for material evidence claims;
- recommends a next skill that violates a hard dependency without explaining the missing prerequisite.

Invalid handoffs are returned for correction or reported as partial/blocked. They must not be silently normalized into complete work.
