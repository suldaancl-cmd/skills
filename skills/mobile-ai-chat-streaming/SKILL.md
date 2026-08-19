---
name: mobile-ai-chat-streaming
description: Build or review an AI chat and streaming experience in Expo/React Native with authenticated server calls, message persistence, Markdown, attachments, cancellation, tool events, and provider abstraction. Use for conversational or short AI interactions; route durable workflows elsewhere.
---

# Mobile AI chat streaming

Create a resilient conversation product, not a text box wired directly to a provider key.

## Classify the request

- Use streaming request/response for short conversational work that can finish within the trusted API runtime.
- Create a durable job when the operation is long-running, asynchronous, costly, approval-gated, or must continue after the app closes.
- A chat UI may start and observe a durable job, but it must not pretend token streaming is durable execution.

## Client/server boundary

- The mobile app sends the user's authenticated session and a product-level request to a trusted endpoint.
- The server verifies the session, resource ownership, entitlement, rate limits, safety policy, and provider budget.
- Provider credentials and privileged database keys remain server-side.
- The client renders typed public stream events; it does not receive chain-of-thought, secrets, or raw tool credentials.

## Model conversation state explicitly

Separate conversation, message, content part, attachment, generation, citation, tool invocation, and durable job references. Preserve a stable client message ID so optimistic UI and server persistence converge without duplication.

Support:

- User, assistant, system-visible notice, and tool/result presentation roles appropriate to the product.
- Text, Markdown, images/files, citations, structured cards, progress, and recoverable errors.
- Pending, streaming, completed, stopped, failed, moderated, and superseded generation states.
- Editing/retry that creates a traceable branch or replacement rather than silently rewriting history.

## Streaming protocol

Use [references/mobile-stream-protocol.md](references/mobile-stream-protocol.md) when defining a transport. Requirements:

- Ordered event IDs and generation identity.
- Content deltas plus semantic state events.
- Abort/cancel behavior.
- Safe reconnect or a clear fallback to fetching the persisted final state.
- Backpressure and bounded payload/attachment sizes.
- An explicit terminal event.

Do not parse presentation from arbitrary provider-specific text. Normalize provider events on the server.

## Mobile experience

- Keep the list stable while tokens arrive; avoid re-rendering the entire transcript per token.
- Preserve drafts and optimistic messages across transient network failure.
- Keep stop, retry, copy, report, citation, and accessibility actions usable during and after generation.
- Render Markdown and links safely. Treat model-produced URLs, HTML, code, and tool arguments as untrusted.
- Handle keyboard, inverted/virtualized lists, long messages, RTL, selection, screen readers, and background/foreground transitions.
- Prefer cached server state for conversation history; do not make a global client store the permanent source of truth.

## Quality and safety

Test slow first token, mid-stream disconnect, duplicate event, cancellation race, provider error, moderated output, oversized response, attachment failure, session expiry, and app backgrounding. Capture latency to first token, completion latency, failure rate, stop rate, cost, and user feedback without logging private message contents by default.
