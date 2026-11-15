# Orchestrator Quality Gates

Before presenting a coordinated result, verify the following.

## Routing
- Is every selected skill relevant to the stated objective?
- Were unnecessary specialists excluded?
- Were approved/current artifacts reused?
- Are hard dependencies satisfied or clearly identified as blockers?
- Were optional dependencies treated as optional?

## Loading and execution honesty
- Is every claimed loaded specialist actually available and activated/read?
- Is native activation distinguished from filesystem fallback and legacy fallback?
- Were unsupported harness capabilities avoided?
- Is parallel execution claimed only when it actually occurred?

## Handoffs and artifacts
- Does each specialist handoff include all required fields?
- Are outputs real, proposed or inline, with status clearly stated?
- Is artifact ownership respected?
- Are unapproved recommendations kept separate from decisions?
- Are evidence sources and limitations traceable?

## Project continuity
- Were existing decisions and open questions preserved?
- Were conflicting or stale artifacts surfaced?
- Were writes authorized and confirmed?
- Are file paths portable and secrets excluded?

## Completion
- Are all requested deliverables complete, or are partial/blocked conditions explicit?
- Are remaining assumptions, risks and evidence gaps visible?
- Is the next action useful and dependency-correct?
- Does the response avoid implying that a plan is validated, executed or commercially proven?

A failed critical gate means do not report the overall task as complete.
