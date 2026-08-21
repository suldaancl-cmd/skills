---
name: langgraph-agent-orchestration
description: Design, implement, or audit LangGraph orchestration with explicit state, deterministic and agentic nodes, persistent checkpoints, stores, interrupts, subgraphs, streaming, and recovery. Use for advanced resumable agent workflows; not for a simple model-and-tools loop or queue transport alone.
---

# LangGraph agent orchestration

Use LangGraph when control flow, state, approval, and recovery must be explicit. Prefer a higher-level LangChain agent when a bounded model/tool loop is enough.

## Establish the runtime facts

- Inspect the installed LangGraph/LangChain packages, language, checkpoint adapters, schema library, and existing graph before changing architecture.
- Verify version-sensitive APIs in current official documentation; do not copy an older tutorial's imports or persistence setup.
- Map the graph to the surrounding durable job. A graph checkpoint does not replace job ownership, billing, provider webhook state, or queue delivery.

## Design the graph from state and side effects

- Define typed state with clear reducers/merge behavior before drawing nodes.
- Keep state minimal and serializable. Store large files, raw provider responses, and secrets externally and persist references.
- Separate deterministic validation/routing from LLM judgment.
- Give every node one observable responsibility and explicit input/output.
- Put irreversible or costly side effects behind deterministic authorization and idempotency boundaries.
- Use conditional edges for real routing decisions; avoid a graph that merely visualizes a fixed function chain.

## Persistence and identity

- Use a durable checkpointer in production. In-memory checkpointing is only for disposable development/tests.
- Give each independent conversation/run a stable `thread_id`; do not reuse one thread for unrelated users or jobs.
- Distinguish checkpointed thread state from long-term cross-thread memory stored through an application store.
- Select checkpoint durability/performance behavior deliberately and document the recovery window.
- Define retention, deletion, tenant isolation, encryption, and schema-migration behavior for checkpoints and stores.

## Human-in-the-loop

- Use interrupts when external input or approval must pause execution.
- Keep interrupt payloads JSON-serializable and safe to expose to the caller.
- Resuming may re-enter node logic; side effects before an interrupt must be idempotent or moved into a completed predecessor node.
- Bind approval to a fingerprint of the pending action. On resume, revalidate actor, scope, expiry, current state, and authorization.
- Never treat a free-form “yes” in conversation history as approval for a changed action.

## Subgraphs and agents

- Default to isolated per-invocation subgraph state for one-off specialists.
- Use per-thread state only when the subgraph genuinely needs continuity across calls.
- Prefer subagents-as-tools when a supervisor only needs a bounded specialist result.
- Do not create a multi-agent graph when deterministic nodes or ordinary functions provide clearer control.

## Errors, streaming, and recovery

- Classify retryable transport/provider errors separately from invalid input, policy blocks, budget exhaustion, and user-action requirements.
- Bound graph steps, recursion, tool calls, parallel branches, wall time, and provider spend.
- Stream semantic progress and final output, not hidden reasoning or checkpoint internals.
- Make cancellation and resume converge with the authoritative job state.

Use [references/langgraph-design-record.md](references/langgraph-design-record.md) for substantial work. Test crash/restart, duplicate resume, stale approval, node retry after side effect, checkpoint migration, and concurrent access to the same thread.
