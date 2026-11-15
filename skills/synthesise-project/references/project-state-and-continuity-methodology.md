# Project state and continuity methodology

## 1. Initialize a portable project

Confirm a user-approved project name/location and assign a stable, non-identifying project ID. Create or initialize `PROJECT-BRIEF.md`, `DECISIONS.md`, `PROJECT-STATUS.md` and an artifact registry. Record objective, scope, current stage, owners, assumptions and next actions. Never claim a file was written unless the filesystem action succeeded.

## 2. Maintain canonical state

The Markdown brief is the human-readable source of truth. Track creator/audience context, selected opportunity, evidence, validation, product, curriculum, commercial strategy, launch, constraints, open questions and next actions. Use structured sidecar metadata only to improve validation; do not require a database or convert the brief into an opaque format.

## 3. Record evidence provenance

Use stable evidence IDs and record claim, type, source locator, date, status, confidence, scope/segment, sample size, limitations, supporting hypotheses and consuming artifacts/skills. Reuse the record without upgrading its meaning or strength. Preserve the source's original qualification and limitations.

## 4. Keep decisions append-only

Each decision records ID, date, statement, context, alternatives, evidence IDs, assumptions, rationale, owner/approver, status and consequences. Supersede by adding a new decision that links to the prior one; never silently edit or delete history. Distinguish proposed, approved, rejected and superseded decisions.

## 5. Register artifact ownership and versions

For each canonical artifact record path, owning specialist, version, created/updated dates, status, dependencies, related decisions, checksum where practical and source project ID. One canonical artifact has one owner. Other skills submit patches; the owner or user approves application.

## 6. Synchronize a specialist handoff

Validate contract version, skill/project IDs, objective, inputs, outputs, proposed/required decisions, assumptions, evidence, limitations, next skills and completion status. Check files actually exist, names match canonical ownership, evidence IDs resolve and no decision conflicts are introduced. Do not infer approval from a completed handoff.

## 7. Resume a project safely

Read the brief, latest status, recent decisions and only relevant artifacts. Reconstruct completed work, stale/missing/conflicted items, open questions, blockers and next actions. Verify whether decisions remain approved and whether referenced files are available. Do not rerun completed work without a reason.

## 8. Resolve conflicts explicitly

Identify both conflicting records, owners, versions, dates and supporting decisions. Determine whether one is stale or whether the conflict is substantive. Preserve both, describe impact and request approval when authority or intent is unclear. Never choose a consequential resolution through silent inference.

## 9. Recovery and portability

Keep files human-readable and exportable. Support manual editing, backups, restore checks and relative paths. Record schema/skill versions needed to interpret artifacts. Avoid secrets and unnecessary personal data. A missing cloud service or agent memory must not prevent project recovery.

## 10. Quality review

Verify append-only decision history, canonical ownership, evidence links, file/version consistency, portable paths, truthful status and visible conflicts. Return a concise recovery/handoff summary with the next recommended specialist.
