# LangChain harness record

## Task contract

- User outcome:
- Why an agent loop is needed:
- Stopping condition:
- Model capabilities required:
- Maximum steps/time/cost:

## Context map

| Context | Source | Trust level | Freshness | Size budget | Redaction/retention |
|---|---|---|---|---|---|

## Tool contract

| Tool | Read/mutate | Input schema | Server-injected context | Authorization | Idempotency | Output limit |
|---|---|---|---|---|---|---|

## Provider behavior

- Primary/fallback criteria:
- Structured output/tool-call compatibility:
- Timeout and retry ownership:
- Usage/cost capture:

## Evaluation cases

- Correct no-tool answer.
- Correct tool selection and valid arguments.
- Refusal/approval for consequential action.
- Injection inside retrieved/tool content.
- Provider timeout or unsupported capability.
- Loop and budget exhaustion.
- Same mutation requested twice.
