---
name: synthesise-discovery
description: >
  Extract a creator's credible expertise, achievements, repeatable methods,
  proof, assets, audience access and constraints. Use when establishing or
  updating the creator capability foundation for a product opportunity.
license: MIT
compatibility: Agent Skills-compatible agents; supporting files are loaded progressively.
metadata:
  author: astisme
  version: "2.0.0-alpha.2"
---

# Synthesise Discovery

Create an evidence-backed profile of what the creator can credibly teach, deliver, or enable. Discovery owns `expertise-profile.md`; it does not select a final market opportunity or design the commercial offer.

## Scope

- Domain knowledge, hard and soft skills, specialist methods and tacit knowledge.
- Career, project and lived experience relevant to the stated goal.
- Repeatable outcomes, achievements, proof, artifacts and credibility.
- Audience relationships, distribution, assets, interests, capacity and constraints.
- Evidence gaps and the most valuable next verification step.

## Non-goals

- Do not infer expertise from interest, job title or self-confidence alone.
- Do not invent credentials, outcomes, customer results, testimonials or portfolio evidence.
- Do not decide audience demand, UVZ ranking, product scope or pricing.
- Do not turn a creator's private or sensitive history into public positioning without explicit permission.

## Required inputs

Start with the creator's goal and any available work history, capability narrative, artifacts, proof, preferred audiences, resources and constraints. If information is incomplete, create a provisional profile and ask one high-value question at a time.

## Method

1. Clarify the creator's intended outcome and boundaries.
2. Inventory capabilities, experience, specialist knowledge and repeatable methods.
3. For each capability capture proficiency, recency, evidence, repeatability and ability to teach or deliver.
4. Record achievements with context: starting situation, creator contribution, observable result, timeframe and available corroboration.
5. Separate demonstrated strengths from aspirations and interests.
6. Identify assets, audience access, preferred delivery formats, capacity and constraints.
7. Mark each statement as confirmed, creator-reported, inferred, hypothesis or unknown.
8. Summarize the strongest credible advantages, gaps and next verification action.

Use `workflows/discovery.md` and `templates/expertise-inventory.md`.

## Canonical output: expertise-profile.md

Include:
- Creator goal and relevant context.
- Capability inventory with proficiency, recency, proof and confidence.
- Achievement and evidence register with provenance.
- Repeatable methods and teachable/deliverable outcomes.
- Assets, audience access and distribution.
- Interests, capacity, constraints and boundaries.
- Evidence gaps, open questions and next actions.
- A concise creator-advantage summary for downstream Audience and UVZ work.

## Quality gates

- Every claimed strength is distinguished from its supporting evidence.
- Interest is not represented as expertise.
- Outcomes are not attributed causally without support.
- Evidence includes source/context and date where available.
- Missing evidence remains unknown, not neutral or positive.
- Constraints and privacy boundaries are explicit.

## Handoff

Return a structured handoff identifying the canonical output path, evidence provenance, confidence, unresolved questions and any limitations. Audience and UVZ may consume the profile; they must not silently rewrite it.
