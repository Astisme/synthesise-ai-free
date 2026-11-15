# Routing Matrix

**Status:** v2.0 proposed specialist catalog. Package availability must be checked at runtime.

## Intent routing

| User request / objective | Required specialists | Conditional specialists |
|---|---|---|
| I have expertise but no idea what to sell | Discovery → Audience → UVZ | Project when persistent state is needed |
| Find a business opportunity | Audience → Market Intelligence → UVZ | Discovery if creator advantage is unknown |
| Is this idea worth building? | Market Intelligence → Validation | Audience if segment/problem unclear; UVZ if no opportunity selected |
| Build my digital product | Product Architecture | Discovery if expertise missing; UVZ if opportunity unselected; Validation if demand is untested; Market Intelligence if alternatives are unknown |
| Create an online course | Product Architecture → Curriculum | Project for existing state; Validation if promise/demand is untested |
| Help me price this | Monetization | Market Intelligence for competitive pricing evidence; Product Architecture if offer scope is unclear |
| Launch my product | Monetization → Launch | Market Intelligence if competitor/channel evidence is missing; Validation if offer/demand is untested |
| Research competitors | Market Intelligence | Audience if target segment is undefined |
| Validate my idea | Validation | Audience if target segment/problem is unclear; Market Intelligence if alternatives/context are unknown |
| Continue my project | Project first → relevant specialist | Determined from project state and open work |

## Routing rules

1. The user's explicit objective takes precedence over the default lifecycle.
2. Reuse approved, current artifacts; do not reload upstream specialists just because they appear earlier in the lifecycle.
3. A missing hard prerequisite blocks downstream claims, not necessarily all useful work. Offer a bounded provisional result if safe.
4. Soft dependencies improve confidence but do not automatically expand the plan.
5. Do not add optional specialists unless they materially improve the requested outcome or the user asks.
6. If the request is narrow and its required inputs exist, load one specialist only.
7. Project Continuity is required for resume/recovery or explicit project-state updates, not every stateless question.
8. After each handoff, recompute the remaining skill set.

## Package identifiers

- `synthesise-discovery`
- `synthesise-audience`
- `synthesise-uvz`
- `synthesise-market-intelligence`
- `synthesise-validation`
- `synthesise-product-architecture`
- `synthesise-curriculum`
- `synthesise-monetization`
- `synthesise-launch`
- `synthesise-project`

The identifiers above are catalog entries, not a declaration that the packages are already installed.
