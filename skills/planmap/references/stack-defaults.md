# Default stack for a Karim project

Source: Karim's own report, *تقرير اختيار المنصات والاشتراكات لتشغيل منصة B2B بوكلاء ذكاء
اصطناعي* (`D:\download chrome\download\...docx`, dated 2026-08-04), cross-read against the
same document open in ChatGPT. **Every price below is as stated in that report and has not
been re-checked against the vendors.** Label them `unverified` when you carry them into a
`PLANMAP.md`, or verify them first and say you did.

## The load-bearing rule

Separate the personal coding tools from the production infrastructure that serves customers.
`OpenCode Go`, `ChatGPT Plus`, `Claude Pro` and `Alibaba Coding Plan` help Karim build. None of
them is a licence to run customer traffic — Alibaba's Coding Plan documentation forbids
backends and automated scripts outright. Production model traffic goes through a gateway.

## Default choices

| Layer | Default | Price (per report) |
|---|---|---|
| Frontend, dashboard | Vercel Pro | `$20`/mo |
| Auth, database, CRM, CMS, bookings | Supabase Pro | `$25`/mo |
| Fast orchestration | Supabase Edge Functions | included |
| Long-running jobs | Trigger.dev Hobby + Contabo workers | `$10`/mo |
| Model layer | Kilo Gateway PAYG | `$20-50` starting credit |
| Mobile builds | Expo Free, then Starter | `$0`, then `$19`/mo |
| Rate limiting, cache | Upstash Redis | free tier |
| Transactional email | Resend Free, then Pro | `$0`, then `$20`/mo |
| DNS, WAF, media | Cloudflare Free + Contabo Object Storage | free |
| Source, CI | GitHub Free, Pro optional | `$0` / `$4`/mo |
| Personal coding agent | OpenCode Go or Claude Pro, not both | `$10` / `$20`/mo |

Baseline: about `$55`/mo for web, `$74`/mo with Expo Starter, on top of the Contabo box Karim
already pays for.

## Do not put these in a plan without a stated reason

`ChatGPT Pro`, `Claude Max`, `Ollama Pro`, `Alibaba Coding Plan`, `Kilo Pass`,
`Expo Production`, `Supabase Team`, `Redis Cloud Pro`. Each either duplicates something in the
table, cannot legally serve a backend, or is priced for a scale the project has not reached.
Redis question settled: Upstash is enough, skip Redis Cloud.

## Model routing default

Cheap model carries the load, expensive model is the escalation — never the default.

| Role | Model |
|---|---|
| Planner | `GLM-5.2` or `Qwen Max` |
| Web builder, database, mobile | `GLM-5.2` |
| Reviewer, hard cases | `Kimi K3`, escalation only |
| QA, classification, log summaries | a cheap flash model |

Per the report's assumption of `8,000` input + `2,000` output tokens per call, `GLM-5.2` runs
about `$0.020` per call against `Kimi K3` at about `$0.054` — which is the whole argument for a
router. Ten customers at 5K calls lands near `$115`/mo of model spend; a thousand customers at
500K calls lands near `$11,450`.

## Billing customers

Not per "model call" — that unit means nothing to a buyer and hides variance. Bill AI Credits:
input tokens, weighted output tokens, tool executions, build minutes, browser minutes, storage,
deploy operations. Add 30-50% margin over variable cost for retries, failures and support.

## Contabo, honestly

The 48GB box is a good Docker host, GitHub Actions runner, worker and build server. It has no
GPU. Serving the frontier models locally would need roughly `193 token/s` at a hundred
customers and `1,929 token/s` at a thousand — a GPU cluster, not this machine. Plan the gateway
in, do not plan it out.
