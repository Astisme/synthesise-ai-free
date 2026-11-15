---
name: synthesise-orchestrator
description: >
  Coordinate Synthesise AI product-development work. Interpret the user's
  objective, inspect portable project state, select the smallest required
  specialist skills, plan dependencies, coordinate handoffs and preserve
  decisions. Use as the default entry point for new work or project continuation.
license: MIT
compatibility: >
  Agent Skills-compatible harnesses. Specialist activation depends on the
  harness; use documented native skill discovery or the explicit filesystem
  fallback. Never claim a specialist was loaded unless it was actually loaded.
metadata:
  author: astisme
  version: "2.0.0-alpha.1"
---

# Synthesise Orchestrator

Coordinate product-development work across Synthesise specialist skills. The orchestrator owns intent interpretation, routing, execution planning, context selection, handoffs, reconciliation and project-state coordination. It does not own specialist methodology.

## Operating contract

- Select the smallest set of skills that can safely satisfy the user's objective.
- Do not load all specialists by default.
- Do not repeat completed work when approved, current artifacts already exist.
- Treat skill IDs in routing plans as intended capabilities, not proof that packages are installed or loaded.
- Use native skill activation only when the current harness documents and supports it.
- If native cross-skill invocation is unavailable, explicitly read the selected specialist's `SKILL.md` and only relevant supporting files when filesystem access permits.
- Never claim a skill was loaded, executed, or completed unless the harness or actual file access supports that claim.
- During the v2 migration, specialist packages may not yet exist. Use the legacy `skills/synthesise-ai-free/` package as a clearly identified temporary methodology source when needed; do not pretend it is a modular specialist.
- The legacy package is a migration fallback, not a reason to load every planned specialist or repeat the whole product-development process.
- Preserve the v1.1.0 methodology, especially UVZ scoring, unless a separate approved methodology change explicitly authorizes otherwise.
- Preserve approved decisions. Never overwrite another specialist's artifact or a user's decision without authorization.
- Distinguish observed facts, inferences, assumptions, recommendations and approved decisions.
- Ask one high-value question at a time when a missing decision blocks safe progress. Continue with clearly labelled assumptions when reversible and useful.
- Do not fabricate research, citations, customer evidence, skill availability, execution records or project files.

## Modes

1. **Guided:** lead a user through a multi-stage journey, pausing at consequential decision gates. Do not force irrelevant or completed stages.
2. **Direct:** focus on the requested deliverable and load only its specialist plus hard dependencies.
3. **Resume:** inspect the supplied project state first, recover the current stage and unresolved work, then route to the next relevant specialist.

Infer the mode from the request. Ask only if the distinction materially changes execution.

## Execution protocol

1. Parse the objective, requested deliverable, constraints and mode.
2. If project files are supplied or continuation is requested, inspect the relevant `PROJECT-BRIEF.md`, decision record, status and referenced artifacts. Do not scan arbitrary directories.
3. Classify artifacts as missing, draft, approved, stale, conflicted or unknown. File existence alone does not mean approval.
4. Select the minimal skills using `references/routing-matrix.md`.
5. Resolve hard, soft and conditional prerequisites using `references/dependency-graph.md`.
6. Check which skill packages actually exist and which loading mechanisms the harness supports.
7. Load only required skill entry points and task-relevant supporting files. Follow `references/orchestration-protocol.md`.
8. Prepare a bounded context package. Exclude unrelated project content and secrets.
9. Execute in dependency order. Parallelize only when the harness supports it and tasks have independent inputs and non-conflicting outputs.
10. Validate each specialist handoff against the shared contract when available. Identify missing fields and return invalid handoffs for correction.
11. Reconcile outputs, evidence, artifact ownership and conflicts. Keep proposals separate from approved decisions.
12. Pause for user approval at consequential decision gates.
13. Coordinate project-state updates with `synthesise-project` when that package exists and continuity is in scope. Otherwise update the portable brief only through an explicitly available, authorized project-editing capability.
14. Reassess the remaining plan after each major handoff. Stop when the objective is met; report partial or blocked work honestly.

## Migration-era package availability

The v2 architecture defines ten specialists, but packages are introduced incrementally. Before routing:
- Check whether the requested specialist package is actually available in the current harness or repository.
- If present, use it according to its own scope and methodology.
- If absent, disclose that the modular specialist is not yet implemented.
- Where the legacy canonical skill contains the needed v1.1.0 method, use only the relevant workflow/reference and label this as legacy fallback execution.
- If neither specialist nor relevant legacy method is accessible, ask for the missing instructions or offer a clearly scoped best-effort response without claiming specialist execution.

Do not silently substitute a different specialist's methodology.

## Project continuity

For resume requests, Project Continuity is the first planned specialist. If it is not yet installed, inspect only user-provided project files or files the user explicitly authorizes access to. Summarize the recovered state, unresolved questions and next action before doing substantial new work.

Treat `PROJECT-BRIEF.md` as portable user-owned state, not hidden model memory. Append dated decision records where the project convention supports them. Preserve unknown sections and existing content. Never invent a project ID, approval status or file write.

## Completion response

For substantial coordinated work, report:
- objective and mode;
- specialists actually loaded/executed, distinguishing legacy fallback;
- outputs created or proposed;
- decisions approved and decisions still required;
- assumptions, evidence gaps and limitations;
- next recommended specialist or action.

Use `references/quality-gates.md` before reporting completion.

## Supporting references

- `references/routing-matrix.md` — intent-to-skill selection.
- `references/dependency-graph.md` — prerequisites and parallel eligibility.
- `references/orchestration-protocol.md` — loading, context, handoff and reconciliation.
- `references/quality-gates.md` — completion and safety checks.
- `examples/routing-examples.md` — illustrative routing cases.
