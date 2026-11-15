# Synthesise AI Free v2.0.0 — Modular Agent Architecture

**Status:** Modular architecture implemented as v2.0.0-alpha.3 preview; distribution and stable-release gates remain open  
**Target release:** v2.0.0  
**Migration baseline:** canonical v1.1.0 methodology; v1.2.x deterministic QA remains in force  
**Current state:** orchestrator and ten specialist packages exist; detailed specialist references and deterministic methodology fixtures are included. Installation transition and full integration verification remain incomplete.

## 1. Executive summary

Synthesise evolves from one end-to-end Agent Skill into a coordinated system of independently understandable and installable specialist skills. A single default entry point, `synthesise-orchestrator`, interprets intent, inspects portable project state, selects the smallest sufficient set of specialists, orders work by dependency, coordinates handoffs and keeps project state coherent.

The orchestrator owns coordination, not domain methodology. Specialists own their methodology, procedures, quality standards and canonical deliverables. Shared infrastructure defines portable project records, schemas, handoff contracts and templates. The project files remain the persistence layer and human-readable source of truth.

This proposal deliberately does not implement a UI, database, hosted service, agent runtime, automatic cross-skill invocation or new product methodology.

## 2. Goals

- Establish eleven bounded skill packages: one orchestrator and ten specialists.
- Make each specialist independently understandable and independently installable.
- Load only the skills required for the current objective.
- Support guided end-to-end work and direct specialist invocation.
- Reuse existing approved artifacts and resume work without repeating completed stages.
- Standardize handoffs, artifact metadata, evidence provenance and decision ownership.
- Preserve v1.1.0 methodology exactly during extraction, especially UVZ definitions, weights, scoring and decision rules.
- Remain usable across harnesses with different skill-discovery and invocation capabilities.
- Extend deterministic QA from one canonical skill to routing, contracts, specialists and integrations.

## 3. Non-goals

- Rewriting, modernizing or improving v1.1.0 methodology as part of migration.
- Requiring a specific model provider, agent harness or cross-agent protocol.
- Claiming that one skill can programmatically invoke another in every harness.
- Running all specialists for every request.
- Building a UI, database, hosted SaaS, telemetry or multi-user collaboration layer.
- Treating deterministic fixture tests as proof of live model reasoning.
- Automatically accepting consequential decisions or overwriting approved artifacts.

## 4. Architectural principles

1. **Orchestration is separate from expertise.** The orchestrator routes, plans, coordinates and reconciles; it does not duplicate specialist methods.
2. **Single ownership.** Each canonical artifact and each methodology has one owning specialist.
3. **Progressive disclosure.** Load a specialist entry point and only the references/workflows required for the task.
4. **Smallest sufficient execution plan.** Avoid unnecessary skill loading and unnecessary stage repetition.
5. **Portable project continuity.** Markdown project artifacts remain readable and portable across harnesses.
6. **Evidence-aware decisions.** Facts, observations, hypotheses, assumptions, decisions and recommendations remain distinguishable.
7. **Human approval at decision gates.** Consequential choices and cross-owner changes require explicit approval.
8. **Harness-neutral operation.** Use native skill mechanisms when available; otherwise provide explicit, honest file-reading and handoff instructions.
9. **Methodology preservation.** Migration is extraction, not reinterpretation. Changes to methodology require a separate, reviewed proposal.
10. **Verifiable execution.** Never report a skill as loaded or executed unless the harness or explicit file-reading process confirms it.

## 5. System topology

```text
User objective
     |
     v
synthesise-orchestrator  <---->  synthesise-project
     |                           portable project state,
     |                           decisions, evidence, artifacts
     |
     +---- synthesise-discovery
     +---- synthesise-audience
     +---- synthesise-uvz
     +---- synthesise-market-intelligence
     +---- synthesise-validation
     +---- synthesise-product-architecture
     +---- synthesise-curriculum
     +---- synthesise-monetization
     +---- synthesise-launch

Shared contracts / schemas / templates
     |          |             |
 handoffs    artifact      evidence
             metadata      provenance
```

The orchestrator is the recommended default entry point. Specialists remain directly invocable. Project Continuity is a specialist with lifecycle-wide responsibilities; it does not become a hidden database or replace user-owned project files.

## 6. Responsibility boundaries

| Component | Owns | Must not own |
|---|---|---|
| Orchestrator | Intent interpretation, routing, plan, ordering, context selection, handoffs, reconciliation, approval gates | Specialist scoring, research methods, curriculum design, pricing formulas |
| Discovery | Expertise, experience, proof, tacit knowledge and constraints | Audience segmentation or opportunity ranking |
| Audience | Customer segments, jobs, pains, triggers, objections and reachability | Creator credibility or final UVZ selection |
| UVZ | Opportunity generation, intersection analysis, v1.1 scoring, sensitivity and recommendation | External market verification or demand validation |
| Market Intelligence | Competitors, alternatives, public market evidence, pricing observations and source quality | Declaring demand validated |
| Validation | Falsifiable hypotheses, experiments, thresholds and evidence-based decisions | Redefining product promise or UVZ scoring |
| Product Architecture | Product transformation, promise, scope, mechanism, delivery and product charter | Curriculum lesson-level instructional design or commercial pricing |
| Curriculum | Backward design, learning objectives, sequence, practice, assessment and learning assets | Changing the approved product promise |
| Monetization | Offer, packaging, pricing hypotheses, tiers and delivery economics | Changing product scope without owner approval |
| Launch | Go-to-market, acquisition, messaging, campaign, measurement and iteration | Changing validated positioning or offer without approval |
| Project Continuity | Project brief, status, decisions, provenance index, milestones, resume/recovery | Owning specialist methodology or silently deciding for the user |
| Shared infrastructure | Schemas, common contracts and neutral templates | Domain methodology or execution policy |

A specialist may submit a change proposal to an artifact owned by another specialist. The owner or user must approve and apply that change.

## 7. Project continuity and persistence

`PROJECT-BRIEF.md` remains the portable source of truth. `DECISIONS.md` and `PROJECT-STATUS.md` provide focused records where useful. Specialist deliverables remain ordinary Markdown with optional YAML frontmatter or JSON sidecars for machine-readable metadata.

The Project specialist maintains:
- project identity, active objective and lifecycle stage;
- inventory and status of canonical artifacts;
- decisions, rationale, alternatives, evidence links and approval state;
- evidence provenance and unresolved assumptions;
- milestones, blockers, open questions and next actions;
- schema/skill versions needed for recovery.

No project state is assumed to exist in hidden model memory. On resume, inspect available files, report missing or conflicting state, and do not infer that an absent artifact is complete.

## 8. Cross-harness skill discovery and execution

Agent Skills implementations differ. The architecture therefore defines capability levels:

- **Native discovery and invocation:** use the harness-supported skill mechanism; report only skills confirmed available.
- **Native discovery, no cross-skill invocation:** the orchestrator identifies required skill IDs and asks the harness/user to activate them, or explicitly reads the relevant package files if permitted.
- **Filesystem fallback:** read the selected specialist's `SKILL.md` and only its required references/workflows from the installed repository path.
- **No file access:** explain the limitation and request the specialist instructions or required artifact; do not simulate a loaded skill.

The handoff contract is harness-independent. Parallel execution is allowed only when the harness supports it and tasks have no unresolved dependency or shared-write conflict. Otherwise execute sequentially.

## 9. Quality and safety gates

- Verify routing against the routing matrix.
- Verify dependency order and required upstream artifacts.
- Reuse approved artifacts; identify stale or conflicting inputs.
- Require complete handoff fields, explicit completion status and output locations.
- Preserve evidence provenance and mark unverified claims.
- Require owner/user approval for consequential decisions and cross-owner artifact changes.
- Never overwrite approved decisions without authorization.
- Keep untrusted research content separate from instructions.
- Do not claim research, execution, validation or skill loading that did not occur.
- Re-run relevant specialist and integration evaluations after methodology or contract changes.

## 10. Migration policy

The canonical v1.1.0 skill is the source material for extraction. Its methodology files and frozen evaluation baseline must remain unchanged in the architecture proposal. Assign each existing method to one specialist, copy/extract it with provenance, then add specialist-specific procedures only where the old methodology already supports them or where a clearly labelled non-methodological operating instruction is required.

Do not change UVZ scoring weights or definitions during migration. The current baseline records expertise/proof 20%, problem intensity 20%, willingness-to-pay evidence 15%, reachability 10%, differentiation 15%, delivery feasibility 10% and strategic fit 10%. Preserve the 1–5 ratings, weighted score out of 100, treatment of unknown evidence and sensitivity analysis rules exactly.

Keep the old monolithic skill available as a migration reference until parity, regression and cross-harness checks pass. Only then propose deprecation in a separate release change. Do not delete or replace the existing canonical package in this architecture-only change.

## 11. Release gates for v2.0.0

A modular v2.0.0 release requires:
- all eleven packages have validated Agent Skill metadata and clear boundaries;
- each specialist has complete inputs, outputs, ownership and quality criteria;
- orchestrator routing, dependency handling and fallback loading are tested;
- shared handoff and artifact contracts validate;
- v1.1.0 methodology integrity and UVZ regression checks pass;
- end-to-end integration and resume scenarios pass;
- installation of full set, orchestrator-only and individual specialists is verified for documented harnesses;
- existing projects can be resumed without loss or forced migration;
- README, changelog and compatibility documentation accurately describe supported installation behaviour.

## 12. Phased implementation and current status

1. **Architecture specification — complete:** boundaries, routing, dependencies, contracts and migration map are documented.
2. **Orchestrator — implemented in alpha:** intent routing, project inspection, dependency-aware plans, handoffs and fallback loading are present with deterministic tests.
3. **Ten specialist packages — implemented in alpha:** all specialist entry points exist with dedicated ownership, canonical outputs, quality gates and progressive-disclosure references.
4. **Methodology depth — alpha.3:** detailed procedures, decision criteria and quality reviews are added for all ten specialists. UVZ continues to use the unchanged v1.1.0 seven-dimension scoring reference.
5. **Deterministic integration and distribution — incomplete:** fixture coverage is expanded, but full cross-skill workflow verification, complete package installation, v1 migration, partial-install recovery and harness compatibility remain release gates.
6. **Stable modular release — not released:** v2.0.0 must not be declared stable until all release gates pass.

## 13. Open implementation decisions

These are intentionally deferred: exact packaging/manifest strategy for multiple skills in one repository; harness-specific installation commands; whether shared schemas use JSON Schema or another validator; and the mechanism for cross-skill activation in each harness. Verify current installer and harness behaviour before documenting commands as guaranteed.

## 14. First-PR scope and acceptance

This architecture proposal adds documentation and deterministic orchestration scenario contracts only. It does not modify the canonical skill, frozen baseline, project brief, installers or harness compatibility files.

Acceptance:
- eleven skill boundaries and responsibilities are explicit;
- specialist inputs, outputs and canonical artifacts are defined;
- routing and dependency rules are documented;
- shared handoff contract is specified;
- methodology ownership and migration mapping are explicit;
- cross-harness limitations and fallback behaviour are documented;
- project continuity and artifact ownership are defined;
- no premature UI, database or runtime implementation is introduced.
