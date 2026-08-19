---
name: agentic-app-orchestrator
description: Coordinate an AI-enabled Expo app from product decision through design, implementation, Supabase, durable agents, quality, and store release by routing to the focused skills in this suite. Use for whole-project plans, resets, or multi-domain delivery; not for a small isolated task.
---

# Agentic app orchestrator

Act as the lifecycle coordinator. Preserve the user's requested scope and load only the specialist guidance needed for the current gate.

## Route by decision

| Need | Skill |
|---|---|
| Idea, market, PRD, MVP, pricing | `$product-first-app-blueprint` |
| Repository instructions and agent workflow | `$agentic-coding-project-setup` |
| Screenshot/PNG/Figma to editable design and code | `$reference-to-native-design` |
| Motion, haptics, illustration, polish | `$premium-mobile-experience` |
| Expo/React Native structure and native behavior | `$expo-production-architecture` |
| Mobile server-state cache, mutations, and offline behavior | `$tanstack-query-mobile` |
| Supabase Auth/Postgres/Storage/Realtime/Queues | `$supabase-mobile-platform` |
| Neon Postgres connections, branching, roles, and pgvector | `$neon-postgres-platform` |
| LangChain model integration, typed tools, and bounded agent loops | `$langchain-agent-tooling` |
| LangGraph state, checkpoints, interrupts, and recovery | `$langgraph-agent-orchestration` |
| Durable job lifecycle, leases, approvals, and financial safety | `$durable-agent-worker` |
| Trigger.dev managed tasks, waits, retries, and deployment | `$trigger-dev-workflows` |
| Queue transport, idempotency, backpressure, and dead letters | `$durable-queue-architecture` |
| Knowledge ingestion, grounded RAG, citations, and memory | `$knowledge-rag-memory` |
| AI chat, streaming, Markdown, conversation UX | `$mobile-ai-chat-streaming` |
| Keys, JWT, webhooks, permissions, provider abuse | `$ai-provider-security` |
| Tests, devices, analytics, performance, AI evals | `$mobile-quality-observability` |
| EAS beta and App Store/Google Play submission | `$app-store-release-operations` |

If a specialist is unavailable, follow the same boundary and say which guidance could not be loaded. Do not invent tools or connectors.

## Establish mode and authority

Classify the request:

- **Advise/plan:** inspect and produce decisions; do not mutate the product or external services.
- **Build/change:** implement the requested slice, verify it, and preserve unrelated work.
- **Audit/diagnose:** gather evidence and report causes/risks; do not remediate unless requested.
- **Release/operate:** prepare first; obtain any required confirmation immediately before external side effects.

Clarify only choices that materially alter product scope, data ownership, billing, destructive changes, or external release. Otherwise state reasonable assumptions and proceed.

## Preserve the core architecture

For an Expo + Supabase + external worker product, default to:

- Expo as the untrusted client and device experience.
- Supabase as Auth and product system of record when already selected.
- TanStack Query as a client-side server-state cache, never as the durable source of truth.
- A trusted API/control plane for validation, entitlement, billing, and job creation.
- A durable worker for long-running agent/provider execution.
- One primary execution owner per job type: a Contabo worker, Trigger.dev, or another selected runtime—not duplicate consumers.
- Provider adapters instead of provider logic scattered across screens.
- Realtime or persisted polling for progress.

Do not replace Supabase with Neon, Clerk, Appwrite, InstantDB, or Convex merely because a tutorial used them. Introduce Neon only for a named data boundary and measured reason. Do not convert every named agent or provider into a microservice.

## Run lifecycle gates

Use [references/project-gates.md](references/project-gates.md) and start at the earliest gate affected by the request. Do not force the user through completed gates again.

At every gate:

1. Inspect current artifacts and evidence.
2. Identify the decision and acceptance criteria.
3. Load only relevant specialist references.
4. Make the smallest coherent change or deliverable.
5. Verify observable behavior.
6. Record known risks and the next gate.

For implementation, slice vertically: UI, backend contract, authorization, failure state, telemetry, and verification for one outcome before expanding breadth.

## Final handoff

Lead with the outcome. Include changed artifacts, checks run, evidence, unresolved risks, and the exact next decision. Never claim a Figma reconstruction, production build, database fix, or store submission was completed without observing the corresponding result.
