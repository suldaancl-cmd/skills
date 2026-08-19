---
name: langchain-agent-tooling
description: Design, implement, or audit a LangChain agent harness with models, typed tools, structured output, middleware, retrieval, dynamic context, and provider abstraction. Use for bounded agent/tool loops and integrations; use LangGraph for bespoke durable control flow.
---

# LangChain agent tooling

Treat LangChain as a harness around the model loop, not as the product's authorization, billing, queue, or database layer.

## Choose the right abstraction

- Use direct model calls for a deterministic single completion or structured extraction.
- Use a LangChain agent when the model must select among a bounded set of tools and iterate until a clear stopping condition.
- Use LangGraph when the application needs explicit state transitions, durable pause/resume, deterministic branches, or complex recovery.
- Do not add Deep Agents, subagents, retrieval, and memory by default; add only capabilities required by the product outcome.

## Verify the installed stack

- Inspect installed package versions, provider integrations, model capabilities, schema library, middleware, tracing, and existing abstractions.
- Verify current official documentation before using remembered constructors or imports.
- Keep provider-specific features behind an adapter when switching models is a real requirement; do not flatten away capabilities the product depends on.

## Engineer context

- Supply the minimum instructions, tools, user/tenant context, retrieved evidence, and recent state required for the current task.
- Prefer progressive disclosure and on-demand retrieval over placing every document, schema, or skill in the system prompt.
- Separate trusted policy/instructions from untrusted user content, retrieved pages, documents, and tool output.
- Define context budgets, compression/summarization ownership, freshness, and provenance.

## Define safe tools

- Give each tool a precise name, narrow purpose, typed schema, bounded output, timeout, and stable public error contract.
- Validate tool arguments and authorization in deterministic code. Never trust model-supplied `user_id`, price, recipient, file path, or permission scope.
- Inject verified runtime context outside model-controlled arguments where the framework supports it.
- Make read tools distinct from mutating tools. Require approval for consequential actions at execution time.
- Return concise model-facing results and keep large/raw artifacts outside context with references.
- Apply idempotency to costly or mutating calls and record correlation, latency, usage, and outcome.

## Control the loop

- Bound iterations, parallel tools, wall time, token/output size, and cost.
- Define what “done” means and when to abstain, ask the user, retry, or escalate.
- Use structured output when downstream code needs a contract; validate it before action.
- Do not allow the model to invent tools, providers, routes, or database operations.

## Retrieval and memory

Use retrieval only when knowledge is external, too large, private, or changes independently from code. Keep conversational thread state, durable workflow state, user memory, and knowledge-base documents as separate concerns. Load `$knowledge-rag-memory` for full design.

Use [references/langchain-harness-record.md](references/langchain-harness-record.md) for substantial work. Test tool selection, malformed arguments, unauthorized access, prompt injection in tool results, loop exhaustion, provider fallback, structured-output failure, and duplicate side effects.
