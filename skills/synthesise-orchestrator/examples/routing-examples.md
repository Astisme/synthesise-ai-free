# Orchestrator Routing Examples

These examples illustrate intended routing. They do not imply the specialist packages are installed or that a harness supports automatic skill invocation.

## Example 1 — Expertise, no product idea

**Request:** "I have expertise but no idea what to sell."

**Plan:** Discovery → Audience → UVZ.

**Reason:** establish creator advantage and proof, identify customer problems, then compare intersections. Do not load Curriculum, Monetization or Launch yet.

**Decision gate:** user reviews and approves the opportunity to investigate.

## Example 2 — Competitor research only

**Request:** "Research competitors for this audience."

**Plan:** Market Intelligence only, assuming the audience and research question are sufficiently defined.

**Conditional:** Audience only if target segment is unclear.

**Reason:** a narrow research task does not require creator discovery or UVZ ranking.

## Example 3 — Existing approved product, create a course curriculum

**Request:** "Create a detailed curriculum for this approved product."

**Plan:** Curriculum only, using the approved product charter.

**Conditional:** Project if the user wants project files updated.

**Gate:** if the charter has no measurable transformation or learning outcomes, report the gap before inventing them.

## Example 4 — Continue an existing project

**Request:** "Continue my project."

**Plan:** Project first, then route from the brief's current stage, approved artifacts, open decisions and next actions.

**Gate:** surface conflicts or missing state; never silently discard decisions.

## Example 5 — Migration fallback

**Request:** "Help me price my offer" while the modular Monetization package is not yet present.

**Plan:** check for `synthesise-monetization`. If absent, disclose that it is not yet implemented. If accessible, use only the relevant commercial-strategy reference in the canonical v1.1.0 skill and label this as legacy methodology fallback. Do not claim the specialist was loaded.

## Example 6 — Parallel research

**Request:** "Research the audience and competitors for this defined opportunity."

**Plan:** Audience and Market Intelligence may run in parallel only if each has sufficient independent inputs, separate output ownership and the harness supports parallel execution. Otherwise run sequentially.
