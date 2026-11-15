# Synthesise v2.0 Skill Catalog

**Status:** Canonical modular v2 package, currently version 2.0.0. All eleven packages (one orchestrator and ten specialists) are present and exposed by the root plugin manifests. Structural validation and deterministic contract fixtures cover package metadata, local references, specialist methodology depth and eight cross-specialist orchestration scenarios. The package is the default and only active distribution. Maintainer-reported end-to-end use has been confirmed across Claude Code and Codex Desktop; deterministic CI remains distinct from live-host evidence.  
**Default entry point:** `synthesise-orchestrator`

## Package conventions

Every package is an independently understandable Agent Skill with its own `SKILL.md` and progressive-disclosure support files (references, workflows, templates and examples as justified). Each package declares its scope, non-goals, required inputs, canonical outputs, quality gates, artifact ownership and handoff behaviour.

The catalog describes the packages present in this revision. Package presence does not guarantee native discovery, automatic cross-skill invocation or installation in every harness; availability must be checked at runtime.

## Skill catalog

| # | Skill ID | Responsibility | Canonical output | Owns |
|---:|---|---|---|---|
| 0 | `synthesise-orchestrator` | Intent, routing, plan, dependency order, skill loading, handoffs, reconciliation and approval gates | Execution plan and consolidated response | Overall execution plan |
| 1 | `synthesise-discovery` | Creator expertise, achievements, tacit knowledge, methods, proof, assets and constraints | `expertise-profile.md` | Expertise profile |
| 2 | `synthesise-audience` | ICP, segmentation, jobs-to-be-done, pains, desired outcomes, triggers, awareness, objections and reachability | `audience-intelligence.md` | Audience intelligence |
| 3 | `synthesise-uvz` | Expertise/problem intersection, opportunity generation, differentiation, seven-dimension UVZ scoring, sensitivity and ranking | `uvz-opportunity-report.md` | UVZ opportunity report and recommendation |
| 4 | `synthesise-market-intelligence` | Competitors, alternatives, positioning, market gaps, pricing observations, reviews and source quality | `market-intelligence.md` | Market intelligence |
| 5 | `synthesise-validation` | Hypotheses, problem/demand tests, interviews, experiments, thresholds and go/revise/stop decisions | `validation-report.md` | Validation plan and findings |
| 6 | `synthesise-product-architecture` | Transformation, promise, mechanism, scope, delivery model, customer journey and product structure | `product-charter.md` | Product charter |
| 7 | `synthesise-curriculum` | Backward design, learning objectives, sequencing, instruction, exercises, assessment and implementation assets | `curriculum-blueprint.md` | Curriculum blueprint |
| 8 | `synthesise-monetization` | Positioning, packaging, tiers, pricing hypotheses, bonuses, upsells, revenue model and delivery economics | `commercial-strategy.md` | Commercial strategy and offer architecture |
| 9 | `synthesise-launch` | Distribution, acquisition, messaging, sales assets, campaigns, content, metrics and iteration | `go-to-market-plan.md` | Go-to-market and launch plan |
| 10 | `synthesise-project` | Initialization, project brief, status, decisions, evidence provenance, artifact inventory, milestones and recovery | `PROJECT-BRIEF.md`, `DECISIONS.md`, `PROJECT-STATUS.md` | Portable project state and decision record |

## Specialist input and output contracts

### Orchestrator

- **Inputs:** user objective; harness capability information; available skill catalog; project location and available project artifacts.
- **Outputs:** intent summary; current-stage assessment; minimal skill set; dependency-aware execution plan; context packages; consolidated handoffs; unresolved decisions.
- **Quality:** route only necessary skills; do not invent skill availability; preserve approved decisions; identify missing dependencies; explain fallback limitations.

### Discovery

- **Inputs:** creator narrative, work history, capabilities, achievements, proof, assets, constraints and existing expertise records.
- **Outputs:** structured expertise inventory, evidence/proof inventory, repeatable methods, gaps and open questions in the expertise profile.
- **Quality:** distinguish claimed experience from verified proof; do not equate interest with expertise; preserve source/context for achievements.

### Audience

- **Inputs:** expertise profile where available; creator hypotheses; existing customer evidence; market/audience research.
- **Outputs:** segment definitions, ICP hypotheses, JTBD, pain/outcome maps, buying triggers, objections, alternatives and reachability assessment.
- **Quality:** label inferred personas; ground observed claims; distinguish user, buyer and beneficiary when they differ.

### UVZ

- **Inputs:** expertise profile; audience intelligence; relevant constraints; prior UVZ decisions and evidence.
- **Outputs:** distinct opportunity hypotheses, complete scorecards, sensitivity analysis, ranked portfolio, recommended opportunity, rationale and unresolved assumptions.
- **Quality:** preserve the established seven-dimension UVZ scoring methodology exactly; show evidence and confidence; unknowns are not confirmed neutral facts.

### Market Intelligence

- **Inputs:** selected or candidate opportunity; audience and geography; research questions; prior evidence and source constraints.
- **Outputs:** competitor/alternative landscape, dated pricing observations, positioning comparison, review-language themes, gaps, source register and limitations.
- **Quality:** distinguish verified observations from interpretation; cite material claims; never invent competitor performance or market size.

### Validation

- **Inputs:** opportunity/product hypotheses; riskiest assumptions; target segment; available resources and constraints.
- **Outputs:** prioritized hypotheses, experiment protocols, recruitment plan, thresholds, bias/limitations, results and proceed/iterate/pivot/stop recommendation.
- **Quality:** define decision rules before execution; distinguish intent from observed behaviour; never call an unrun experiment validated.

### Product Architecture

- **Inputs:** selected opportunity; audience evidence; validation findings; creator constraints and existing product decisions.
- **Outputs:** product promise, transformation map, mechanism, scope/exclusions, delivery model, customer journey and product charter.
- **Quality:** promise must be supported by evidence and delivery feasibility; preserve approved audience/opportunity choices unless explicitly reopened.

### Curriculum

- **Inputs:** approved product charter, learner prerequisites, learning outcomes, delivery constraints and assessment requirements.
- **Outputs:** curriculum blueprint, module/lesson sequence, measurable objectives, practice, assessments, assignments and production specifications.
- **Quality:** use backward design; each module supports an observable outcome; flag gaps between promise and learning evidence.

### Monetization

- **Inputs:** approved product charter, audience, evidence of willingness to pay, delivery/support costs and creator constraints.
- **Outputs:** positioning, offer stack, tiers, pricing hypotheses, unit economics assumptions, bonuses and commercial validation questions.
- **Quality:** label estimates and assumptions; preserve scope; recurring billing requires recurring value; no guaranteed revenue claims.

### Launch

- **Inputs:** approved product and offer, target audience, proof, channel access, budget/capacity and launch constraints.
- **Outputs:** acquisition/channel plan, messaging architecture, sales-page structure, campaign calendar, email/content plan and measurement framework.
- **Quality:** claims must be supportable; plans include owners, dependencies and metrics; do not imply a launch occurred when only planned.

### Project Continuity

- **Inputs:** project root; existing brief, decisions, status, evidence and artifact files; current specialist handoff.
- **Outputs:** synchronized portable project brief, append-only decision entries, status/milestone updates, artifact inventory and recovery report.
- **Quality:** never silently rewrite approved decisions; detect conflicts and missing files; keep paths portable; preserve provenance and unresolved questions.

## Orchestration integration

The orchestrator reference [integration contracts](../skills/synthesise-orchestrator/references/integration-contracts.md) defines eight deterministic cross-specialist scenarios. They validate state/handoff invariants, not live agent execution.

## Shared evidence record

All specialists preserve evidence identity, claim status, confidence, scope and limitations when reusing findings. See [the shared evidence-record contract](evidence-record.md) and its machine-readable [JSON Schema](../schemas/evidence-record.schema.json). Reuse must never silently upgrade evidence strength.

## Cross-skill ownership rules

- Each canonical artifact has exactly one owner as listed above.
- The orchestrator may assemble a consolidated view but does not become the canonical owner of specialist artifacts.
- A non-owner may propose a patch; it must not silently write it.
- Project Continuity records approved decisions and state; it does not decide domain questions for specialist owners.
- Shared schemas and contracts are neutral infrastructure and cannot redefine a specialist method.
- A change to a specialist's methodology is reviewed by that specialist's owner and requires regression coverage.

## Package maturity

All eleven packages are implemented and exposed through the canonical root plugin manifests. The ten specialists include detailed methodology references and two deterministic evaluation fixtures each. Fixtures validate authored contracts and coverage; they are not proof of live-agent behaviour. Live discovery and invocation in each supported host remain acceptance checks outside CI.
