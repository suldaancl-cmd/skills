# Mobile stream protocol

Choose SSE, fetch streaming, WebSocket, or a framework protocol based on the installed stack and runtime support. Keep event semantics transport-independent.

## Envelope

Each public event should include:

- protocol version
- conversation ID
- generation ID
- monotonically increasing event ID
- event type
- safe payload
- server timestamp when useful

## Event types

- `generation.started`
- `content.delta`
- `content.part.completed`
- `citation.added`
- `tool.started`
- `tool.progress`
- `tool.completed`
- `job.linked`
- `generation.completed`
- `generation.stopped`
- `generation.failed`
- `generation.moderated`

Expose only product-safe tool summaries. Keep raw tool input/output server-side unless the product explicitly needs and authorizes it.

## Persistence rules

- Persist the accepted user message before or atomically with generation creation.
- Deduplicate on client message ID and generation ID.
- Persist final normalized content independently of the transient stream.
- On reconnect, fetch persisted state and resume only when the transport and server support event replay.

## Error shape

Return a stable public code, recoverability, retry-after hint, and user-safe message. Keep provider error bodies and stack traces private.
