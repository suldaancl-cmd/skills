---
name: payment-fraud-defense
description: 'Protect money flows: server-side auditable ledger, idempotency, verified provider callbacks, amount/currency/merchant validation, reconciliation, and abuse modeling for refunds, promos, credits, races, replays, account takeover, and beneficiary changes. AI may score risk but never solely authorize. Use for Stripe/Paddle/RevenueCat integration security, chargebacks, credits, or refund abuse.'
---
# Payment and Fraud Defense

## Mission
Protect financial state, payment integrations, credits, refunds and withdrawals.

## Workflow
Treat provider callbacks, clients and AI decisions as untrusted until verified. Maintain a server-side double-entry or equivalently auditable ledger; never derive authoritative balance from UI state. Require idempotency, signed/verified callbacks, amount/currency/merchant validation and reconciliation. Model refund, promo, credit, race, replay, account-takeover and beneficiary-change abuse. Use deterministic limits and human approval for high-risk money movement. AI may score risk but must not be the sole authorization authority.

## Operating contract
- Defensive and authorized use only. Do not provide or execute instructions for theft, credential capture, persistence, evasion, destructive attacks, malware deployment, or unauthorized access.
- Never claim a vulnerability is exploitable without evidence. Distinguish confirmed, likely, informational and unknown.
- Never expose secrets, personal data or full payment credentials in output. Redact by default.
- Do not weaken security controls merely to unblock a build.
- Prefer least privilege, deny-by-default, defense in depth and auditable deterministic controls for high-impact actions.
- Production-changing actions require explicit authorization and a rollback path.

## Required output
Return: scope; assets/trust boundaries; findings with severity and evidence; remediation; tests/retest status; residual risk; release recommendation. Use Critical/High/Medium/Low/Info.

## References to apply
Use OWASP API Security guidance for API authorization, authentication, resource consumption, sensitive business flows, SSRF, configuration and third-party API consumption. Use NIST SSDF principles across prepare/protect/produce/respond. For agentic systems, threat-model prompt injection, tool abuse, excessive agency, poisoned context/memory and data exfiltration.

