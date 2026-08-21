---
name: ai-provider-security
description: Audit or implement the security boundary between mobile/web clients, trusted APIs, AI providers, databases, workers, and app-store credentials. Use for API keys, JWT validation, webhooks, tool permissions, rate limits, secret rotation, or suspected exposure; not for general UI work.
---

# AI provider security

Assume a shipped mobile or web client can be inspected. Visibility controls at build time do not make a client-consumed value secret.

## Inspect without leaking

- Identify secret sources and consumers through filenames, configuration structure, and secret scanners without printing values.
- Check committed history and built artifacts when exposure is suspected and authorized.
- Redact tokens, headers, user content, signed URLs, and provider responses from logs and reports.
- Do not rotate, revoke, or delete credentials during an audit unless the user explicitly requested remediation and the exact blast radius is known.

## Classify credentials

Use [references/credential-boundary-matrix.md](references/credential-boundary-matrix.md). At minimum distinguish:

- Public configuration and publishable client keys.
- User session/access tokens.
- Backend provider secrets.
- Database privileged keys and direct credentials.
- Webhook signing secrets.
- App signing, store API, CI/CD, and service-account credentials.

Never place backend provider, service-role, webhook, signing, or store credentials in `EXPO_PUBLIC_*`, client JavaScript, native resources, remote-config values readable by the client, analytics properties, or crash reports.

## Authenticate and authorize every server action

- Verify token issuer, audience, signature, expiry, and relevant session/revocation requirements using the supported server library.
- Derive user identity from the verified token, never from a request-body `user_id`.
- Check resource ownership/membership and entitlement on the server.
- Apply per-user, per-IP/device where appropriate, per-organization, and provider-spend limits.
- Validate request shape, media type, size, attachment ownership, and allowed model/tool choices.

## Protect provider calls and tools

- Give clients product operations such as `create-image-run`, not an unrestricted provider proxy.
- Keep allowed models, maximum tokens/duration/resolution, tool set, and cost ceiling server-controlled.
- Attach correlation and idempotency keys and record normalized usage.
- Treat prompts, retrieved documents, websites, and provider output as untrusted data.
- Validate tool arguments outside the model and enforce least-privilege credentials per integration.
- Require explicit approval for consequential actions at execution time, and bind approval to an action fingerprint.

## Webhooks and callbacks

- Verify signature against the raw request body as required by the provider.
- Validate timestamp/replay window, provider job ID, tenant/job ownership, and allowed state transition.
- Deduplicate events and tolerate out-of-order delivery.
- Never trust a callback URL, result URL, cost, or status merely because it appears in a provider payload; apply allowlists and server-side lookup where supported.

## Exposure response

When a real secret was exposed:

1. Contain access and stop further publication.
2. Identify credential scope, environments, logs, builds, and history affected.
3. Rotate/revoke through the provider with user authorization.
4. Replace trusted-runtime configuration and redeploy affected services.
5. Invalidate or rebuild shipped artifacts if needed.
6. Review usage, billing, and audit logs for abuse.
7. Add prevention and a verification test.

Do not treat removing a secret from the latest commit as containment; history and released binaries may still contain it.
