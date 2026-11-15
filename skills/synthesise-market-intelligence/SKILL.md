---
name: synthesise-market-intelligence
description: Research customers, competitors, alternatives, public pricing, positioning and market whitespace with source provenance.
license: MIT
compatibility: Agent Skills-compatible agents; research tool availability varies by harness.
metadata:
  author: astisme
  version: "2.0.0"
---

# Synthesise Market Intelligence

Produce a source-backed view of the alternatives customers use and the market context for a defined opportunity. Owns `market-intelligence.md`; does not invent market size, competitor performance or customer demand.

## Inputs
A defined decision/research question, target segment or candidate opportunity, geography/category and time horizon. State assumptions if any are missing.

## Method
1. Define the decision, segment, geography, category, time horizon and exclusions.
2. Identify direct competitors, indirect alternatives, DIY and status quo.
3. Prioritize primary sources: provider pages, documentation, public filings and customer evidence.
4. Capture audience, job, promise, mechanism, format, scope, public price/currency/billing basis/date, proof, distribution and limitations.
5. Review customer language and counterexamples; anecdotes do not establish prevalence.
6. Compare alternatives consistently and identify underserved jobs as hypotheses.
7. Cite material claims near the claim; record title, publisher, URL and publication/access date.
8. Translate findings into product implications and next research steps.

## Canonical output: market-intelligence.md
Decision/context; competitor and alternative matrix; customer-language themes; positioning comparison; pricing observations; whitespace hypotheses; source register; confidence and limitations; implications.

## Quality gates
- Material claims have traceable sources or are labelled unverified.
- Public list price is not represented as realized transaction price.
- Revenue, market share, conversion and satisfaction are not inferred from marketing copy.
- Recent sources are preferred for changing prices/features.
- Observations are distinguished from interpretation.

## Progressive methodology reference

Load `references/market-research-methodology.md` whenever performing substantive market intelligence work. Use it to deepen the procedure, decision criteria and quality review; keep this `SKILL.md` as the concise entry point. The reference is additive and does not supersede shared contracts, approved decisions or the frozen v1.1.0 methodology.

## Shared evidence and handoff contract

- Distinguish verified facts, user-provided claims, external research, analytical interpretations, hypotheses, recommendations and unknowns. Never silently promote one state into another.
- Preserve evidence provenance and limitations: stable evidence ID, claim, type, source/locator, date, status, confidence, scope/segment, sample size where relevant, limitations and consuming artifacts. Reuse does not upgrade evidence strength.
- This skill owns its canonical artifact. Other specialists may propose changes but must not silently overwrite it; cross-owner changes require owner/user approval.
- Every handoff reports skill ID, project ID, objective, inputs used, outputs created, decisions proposed, decisions requiring approval, assumptions, evidence, limitations, next recommended skills and completion status.
- Before completion, check required sections, output names, evidence support, explicit assumptions/limitations, ownership, project continuity and actionable next steps. State blockers rather than claiming completion.

## Handoff
Provide source provenance, access dates, geography, limitations and open questions. If browsing is unavailable, state that research is unverified and provide a research plan.
