---
name: product-first-app-blueprint
description: Turn an app or AI product idea into an evidence-backed product brief, PRD, monetization model, and tightly scoped MVP before design or coding. Use for idea validation, product planning, feature prioritization, or rescuing an over-scoped app; do not use for implementation-only requests.
---

# Product-first app blueprint

Produce a buildable product decision, not a feature wishlist.

## Ground the decision

- Inspect the user's existing product notes, repository, analytics, customer evidence, and constraints before proposing a replacement direction.
- Separate **evidence**, **inference**, and **assumption**. Never invent market size, revenue, conversion, or competitor facts.
- If current data matters, verify it from primary sources. Cite the source and date.
- Prefer the narrowest paying user and repeatable job-to-be-done that can support an MVP.
- Preserve an existing stack, brand, or business choice unless changing it is part of the request and the tradeoff is demonstrated.

## Build the blueprint

Resolve these decisions:

1. Target user and urgent situation.
2. Current workaround and why it fails.
3. Product promise and differentiated wedge.
4. Primary success path from first open to achieved outcome.
5. Payment trigger, pricing hypothesis, and entitlement boundary.
6. AI unit economics: requests per outcome, provider cost, retries, storage, support, gross-margin target, and abuse ceiling.
7. MVP capabilities and explicit exclusions.
8. Domain objects and external integrations.
9. Trust, safety, privacy, compliance, and human-approval risks.
10. Activation, retention, revenue, reliability, and cost metrics.
11. Cheapest experiments that can invalidate the riskiest assumptions.

For AI products, distinguish what the model decides from what deterministic code must control. Money, permissions, deletion, publishing, entitlements, and irreversible actions stay deterministic.

## Scope the MVP

- Each MVP feature must support the primary success path, a required trust boundary, or measurement.
- Defer secondary personas, generalized marketplaces, autonomous multi-agent swarms, and speculative integrations.
- Define a visible fallback when AI is unavailable, slow, unsafe, or uncertain.
- Identify what can be manually operated during an early beta.
- Express later work as outcome-based increments, not a calendar promise.

## Deliverable

Use [references/product-blueprint-template.md](references/product-blueprint-template.md) for a full PRD or investment-grade plan. For a quick decision, return only the relevant sections.

End with one of these gates:

- **Proceed** — evidence and scope are sufficient to design.
- **Validate first** — name the experiment and pass/fail threshold.
- **Do not build yet** — name the missing economic or user proof.

Do not begin coding unless the user also asked for implementation.
