---
name: synthesise-project
description: >
  Initialize, recover and maintain portable Synthesise project state, including
  PROJECT-BRIEF.md, append-only decisions, status, evidence provenance,
  milestones and artifact inventory. Use when resuming or updating a project.
license: MIT
compatibility: Agent Skills-compatible agents with authorized project filesystem access; otherwise provide templates and recovery guidance.
metadata:
  author: astisme
---

# Synthesise Project Continuity

Maintain portable, user-owned project state across sessions and harnesses. Owns `PROJECT-BRIEF.md`, `DECISIONS.md` and `PROJECT-STATUS.md`. It records decisions; it does not make specialist domain decisions.

## Scope
- Project initialization and recovery.
- Brief, decision log, status, milestones and artifact inventory.
- Evidence provenance and confirmed/hypothesis/rejected/unknown state.
- Conflict detection, missing-file recovery and continuation handoff.

## Non-goals
- Do not rely on hidden model memory or a proprietary database.
- Do not silently overwrite approved decisions or user-authored sections.
- Do not invent project identifiers, file writes, approvals or completed work.
- Do not resolve domain conflicts that belong to specialist owners.
- Do not store passwords, secrets or unnecessary personal data.

## Method
1. Identify the project root and confirm filesystem read/write authorization.
2. Inspect only named or relevant project files: brief, decisions, status and referenced artifacts.
3. Classify artifacts as missing, draft, approved, stale, conflicted or unknown; file existence alone is not approval.
4. Summarize recovered state, last approved decisions, evidence, open questions, blockers and next action.
5. Detect conflicts between artifacts and the decision log; surface them rather than choosing silently.
6. Update the brief while preserving unknown sections and user-authored content.
7. Append dated decision entries; never rewrite historical decisions.
8. Update status, milestones and artifact inventory with factual completion evidence.
9. Validate required sections and links; preserve portability and Markdown readability.
10. Return a continuation handoff naming the next specialist and bounded context.

Use `templates/PROJECT-BRIEF.md`, `templates/DECISIONS.md` and `templates/PROJECT-STATUS.md`.

## Canonical outputs
- `PROJECT-BRIEF.md`: portable source of truth for goal, creator, audience, UVZ, research, validation, product, offer, launch, risks and next actions.
- `DECISIONS.md`: append-only decision history with date, decision, rationale, evidence, approver and supersession link.
- `PROJECT-STATUS.md`: current stage, milestone status, blockers, artifact inventory and next actions.

## Quality gates
- Existing content and unknown sections are preserved.
- Decisions are append-only and approval status is explicit.
- Evidence includes provenance and status.
- No file is claimed created/updated unless the authorized filesystem action succeeded.
- Paths are portable; no hidden persistence assumption is made.
- Conflicts and missing files are surfaced.

## Progressive methodology reference

Load `references/project-state-and-continuity-methodology.md` whenever performing substantive project work. Use it to deepen the procedure, decision criteria and quality review; keep this `SKILL.md` as the concise entry point. The reference is additive and does not supersede shared contracts, approved decisions or the frozen v1.1.0 methodology.

## Shared evidence and handoff contract

- Distinguish verified facts, user-provided claims, external research, analytical interpretations, hypotheses, recommendations and unknowns. Never silently promote one state into another.
- Preserve evidence provenance and limitations: stable evidence ID, claim, type, source/locator, date, status, confidence, scope/segment, sample size where relevant, limitations and consuming artifacts. Reuse does not upgrade evidence strength.
- This skill owns its canonical artifact. Other specialists may propose changes but must not silently overwrite it; cross-owner changes require owner/user approval.
- Every handoff reports skill ID, project ID, objective, inputs used, outputs created, decisions proposed, decisions requiring approval, assumptions, evidence, limitations, next recommended skills and completion status.
- Before completion, check required sections, output names, evidence support, explicit assumptions/limitations, ownership, project continuity and actionable next steps. State blockers rather than claiming completion.

## Handoff
Return recovered state, files inspected/updated, conflicts, decisions requiring approval and next recommended specialist. If filesystem access is unavailable, provide templates and ask the user to place them in the project; do not claim persistence.
