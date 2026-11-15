# Synthesise Orchestration Specification

**Status:** Proposed; implementation not started  
**Default entry point:** `synthesise-orchestrator`

## 1. Purpose

The orchestrator translates a user objective into the smallest safe, dependency-correct specialist plan. It inspects portable project state, selects and loads skills using capabilities actually available in the current harness, passes bounded context, coordinates handoffs, surfaces consequential decisions and updates project state through the Project Continuity owner.

It coordinates expertise; it does not reproduce specialist methodology.

## 2. Operating modes

### Guided mode

Lead the user through a coherent product-development journey. Explain the current stage, identify missing prerequisites, ask one high-value question at a time, and pause at defined decision gates. Do not force completed or irrelevant stages.

### Direct mode

Invoke only the specialist needed for a specific deliverable. Inspect existing state and check only hard dependencies. If a dependency is missing, distinguish a true blocker from an optional input and ask whether to proceed with a labelled assumption.

### Resume mode

Invoke Project Continuity first when project artifacts are available or the user asks to continue. Reconstruct state from files, identify current stage, decisions, open questions, stale/conflicting artifacts and next action. Do not repeat completed work unless evidence is stale or the user asks to revisit it.

## 3. Request routing matrix

| User intent | Primary skills | Conditional skills |
|---|---|---|
| Expertise but no idea what to sell | Discovery → Audience → UVZ | Project when continuity is needed |
| Find a business opportunity | Audience → Market Intelligence → UVZ | Discovery if creator advantage is unknown |
| Is this idea worth building? | Market Intelligence → Validation | Audience if segment/problem unclear; UVZ if opportunity not selected |
| Build my digital product | Product Architecture | Discovery if expertise missing; UVZ if opportunity unselected; Validation if demand untested; Market Intelligence if alternatives unknown |
| Create an online course | Product Architecture → Curriculum | Project for existing project state; Validation if promise/demand is untested |
| Help me price this | Monetization | Market Intelligence for competitive pricing evidence; Product Architecture if scope/promise unclear |
| Launch my product | Monetization → Launch | Market Intelligence if channel/competitor context missing; Validation if offer/demand untested |
| Research competitors | Market Intelligence | Audience if target segment is undefined |
| Validate my idea | Validation | Audience if target segment/problem unclear; Market Intelligence if alternatives/context are unknown |
| Continue my project | Project first → relevant specialist | Determined from state, objective and unresolved work |

Routing is intent-aware, not a mandatory linear funnel. The table is a default policy; user instructions and existing approved artifacts take precedence unless a hard dependency or safety constraint prevents execution.

## 4. Dependency graph

Default lifecycle relationships:

```text
Discovery -----> UVZ <----- Audience
                    ^          |
                    |          v
Market Intelligence + Validation
                    |
                    v
          Product Architecture
                    |
                    v
               Curriculum

Product Architecture -----> Monetization -----> Launch
          |                       ^                 ^
          +-----------------------+-----------------+
                                  |
                         Market Intelligence

Project Continuity <---- every stage (state and artifact lifecycle)
```

Dependency semantics:

- **Hard dependency:** a required approved artifact or decision without which the requested output would be misleading or impossible.
- **Soft dependency:** improves confidence or quality; proceed if useful with a visible limitation.
- **Conditional dependency:** required only when a stated condition is true.
- **Independent task:** can run in parallel if inputs are available and no shared-write conflict exists.

Examples:
- UVZ requires enough creator advantage and audience/problem context to compare opportunities; missing inputs can be gathered by Discovery/Audience or explicitly treated as hypotheses.
- Product Architecture requires a selected opportunity or an explicit user-approved provisional concept.
- Curriculum requires an approved or explicitly provisional product charter and learning transformation.
- Monetization requires a defined offer scope; market pricing research is a soft/conditional dependency.
- Launch requires an offer and target audience; it must label unvalidated offer assumptions.
- Project Continuity is lifecycle-wide and is loaded on resume or when project state must be read/updated; it need not be loaded for every stateless one-off request.

## 5. Routing and execution algorithm

1. **Parse objective:** identify requested outcome, scope, urgency, constraints and whether the request is direct, guided or resume.
2. **Inspect project state:** if a project is supplied or continuity is requested, read relevant project artifacts through Project Continuity or its documented fallback. Do not scan arbitrary directories.
3. **Assess stage and artifact status:** classify artifacts as missing, draft, approved, stale, conflicted or unknown. Never infer approval from file existence alone.
4. **Resolve prerequisites:** map objective to routing matrix; classify dependencies as hard, soft or conditional.
5. **Minimize skill set:** choose the smallest skill set sufficient for the request and its quality gates. Do not load all specialists by default.
6. **Build dependency plan:** topologically order required work; identify independent branches.
7. **Check harness capabilities:** determine whether native skill discovery, invocation, filesystem reading and parallel execution are available.
8. **Load honestly:** use native mechanism if supported. Otherwise explicitly read specialist `SKILL.md` and only necessary references/workflows. If unavailable, disclose and request required material.
9. **Prepare bounded context:** provide objective, relevant approved artifacts, evidence, decisions, constraints, required output and ownership restrictions. Exclude unrelated project data and secrets.
10. **Execute and hand off:** each specialist returns the standard handoff contract and named artifacts.
11. **Reconcile:** verify required fields, provenance, output ownership, conflicts and dependency completion. Return incomplete/blocked work as such.
12. **Decision gates:** request user approval for consequential choices, unresolved trade-offs, scope changes and cross-owner artifact changes.
13. **Persist:** ask/route Project Continuity to update project brief, decision log, status and artifact inventory when project continuity is in scope.
14. **Reassess:** after each major handoff, recompute remaining skills and stop when the objective is satisfied.

## 6. Skill loading protocol

Each specialist package is a directory with `SKILL.md` and optional references/workflows/templates/examples. Loading is progressive:

- Read the specialist `SKILL.md` first.
- Follow its explicit reference-loading instructions.
- Read only the task-relevant supporting files.
- Do not bulk-load every reference unless the specialist explicitly requires it.
- Keep loaded context bounded to the objective and dependencies.

Never claim a package is installed, available, loaded or executed without a supporting harness signal or actual file read. A skill identifier in a routing table is a plan, not evidence of availability.

### Harness fallback levels

| Capability | Behaviour |
|---|---|
| Native skill activation supported | Activate the specialist using documented harness syntax |
| Skill files discoverable, no invocation API | Ask harness/user to activate, or explicitly read files if supported |
| Repository/filesystem access only | Read package files directly and follow their instructions as a bounded specialist procedure |
| No skill or file access | State limitation; request skill content or provide a clearly-labelled best-effort response without claiming specialist execution |

Do not assume Codex, Claude, Cursor, Gemini CLI or other harnesses share the same invocation semantics. Maintain compatibility notes with tested versions and dates in a later implementation phase.

## 7. Parallel execution policy

Parallel work is allowed only when:
- all required inputs are available;
- tasks have no hard dependency on each other's outputs;
- outputs have distinct owners/paths or an explicit merge protocol;
- the harness actually supports parallel execution;
- the orchestrator can reconcile all results.

Example: Audience and Market Intelligence research may run concurrently when both have the same defined target segment and independent output artifacts. UVZ ranking must wait for required expertise and audience inputs. Curriculum must wait for product architecture. If parallel execution is unsupported, run sequentially without implying concurrency.

## 8. Standard specialist context package

```yaml
project_id: example-project
objective: Create an online course
current_stage: product_architecture
mode: direct
available_artifacts:
  - path: expertise-profile.md
    status: approved
  - path: audience-intelligence.md
    status: approved
  - path: uvz-opportunity-report.md
    status: approved
required_outputs:
  - product-charter.md
constraints:
  preserve_approved_decisions: true
  preserve_methodology: true
  flag_unverified_claims: true
  do_not_overwrite_non_owned_artifacts: true
```

This is illustrative. A real context package must use actual project identifiers, paths and artifact statuses; never copy example values as facts.

## 9. Handoff and reconciliation

Every specialist returns the shared contract in `shared/contracts/skill-handoff.md`. The orchestrator checks:
- skill ID and project ID match the task;
- objective and inputs are traceable;
- outputs exist or are clearly marked proposed/not written;
- artifact owner is respected;
- decisions proposed and decisions requiring user approval are distinguished;
- assumptions, evidence, limitations and completion status are explicit;
- next skill recommendations are consistent with the dependency graph.

A handoff marked complete is not automatically a validated outcome. Completion describes task execution; evidence strength and validation status are separate.

## 10. Decision gates and conflict resolution

Pause for user input when:
- selecting or materially changing the primary UVZ opportunity;
- accepting/rejecting validation findings with consequential investment implications;
- changing product promise, scope or audience;
- accepting pricing or commercial assumptions that materially affect the offer;
- approving a launch claim that lacks evidence;
- changing an approved decision or an artifact owned by another specialist.

When artifacts conflict, preserve both source records, identify owner and timestamps/versions, explain impact and request resolution. Do not silently choose the newest file or overwrite an approved decision.

## 11. Completion criteria

The orchestrator may report the objective complete only when:
- all required specialists have returned complete handoffs or the user has accepted a documented limitation;
- required outputs are present or clearly delivered in the response;
- hard dependencies are satisfied;
- conflicts and approval gates are resolved or explicitly pending;
- project state is updated when requested and available;
- remaining assumptions, evidence gaps and next actions are visible.

Otherwise report partial or blocked with a concrete reason.
