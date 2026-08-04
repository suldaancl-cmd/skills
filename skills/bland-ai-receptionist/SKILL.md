---
name: bland-ai-receptionist
description: Build a production AI phone receptionist / voice agent on Bland AI — persona + voice, knowledge base, Norm auto-build with self-testing, Cal.com booking tools, pathways, web widget, Web Agent SDK, custom API tools, MCP + CLI for coding agents, self-hosting for compliance. Invoke when the task mentions AI receptionist, AI voice agent, AI phone agent, answering calls with AI, Bland AI, or booking-by-phone automation.
---

# bland-ai-receptionist — ship a working AI phone receptionist on Bland

Source: Sonny Sangha, "I Built an AI Voice Agent That Actually Works" (youtu.be/JSYOZvtkAx4, 2026-07-19, sponsored by Bland). Verified against video transcript + dashboard frames. Platform facts current as of that date — re-check pricing before quoting clients.

## Why Bland (the pitch in one breath)

- Most voice AI = 3 vendors in a trench coat (STT → LLM → TTS round trip) → robotic lag. Bland built the whole stack in-house for phone calls; target is **sub-half-second responses**, plus office-background sound effects and phone-line distortion so the brain accepts it as human.
- Scale proof: ~3.5M calls/week, 250+ enterprise customers, $100M+ raised (Series C).
- **Pricing: $0.14/min**, free tier to try. Phone numbers from **$15/month**. Real usage datapoint: 108 test calls ≈ $9.
- **Self-hosting on enterprise plan** — the differentiator for healthcare / finance / legal where docs can't hit a public LLM.

## Dashboard map (app.bland.ai)

- **Build:** Agents (Personas) · Pathways · Knowledge Base · Voices
- **Monitor:** Analytics · Alerts · Call Logs (with playback) · Triage (follow-ups/callbacks) · Compliance · Evals
- **Deploy:** Send Call · Batch Calls · Phone Numbers · SIP Trunks · Messaging (SMS) · Web Widget
- **Integrations:** Tools · Automations

## Build recipe (dental-clinic pattern — adapt per business)

### 1. Knowledge base FIRST
Knowledge Base → Add sources → drag-drop the business PDF (or website URL, raw text, Notion / Google Docs integration). It auto-scrapes into indexed sections. **Query Logs tab** shows every question agents asked against it, with answers + confidence scores — use it to audit hallucination.

### 2. Let Norm build the agent (don't hand-build first)
Norm = Bland's built-in AI builder agent. One chat prompt does persona + pathway + tools. Prompt pattern that worked:

> "Create an AI receptionist for my [business] [name]. Answer the phone as [agent name], greet the customer, ask how you can help. Answer questions from the knowledge base where I uploaded [doc]. Most importantly, book appointments using our [Cal.com/Calendly] setup."

Norm then: scans what's available (KB, tools, voices, secrets) → generates persona + pathway + tools → **runs the whole conversation flow itself as a test caller** → catches its own hallucinations ("not retrieving knowledge base") → self-diagnoses and fixes → re-tests. When it needs an input it can't know (API key, event-type ID) it pauses with a placeholder form.

### 3. Cal.com booking hookup
- In Cal.com: create the event type (e.g. "Dentist consultation", 60 min) → copy **API key** + **event type ID**.
- Give both to Norm when it asks. It generates two tools: `book_appointment_calcom` + `check_availability` — POST to api.cal.com v2, variables filled by the agent mid-call (patient name, visit reason, email, phone, preferred date/time).
- Tools can hit **any REST API** the same way (request URL + variables + connection or raw code route). Secure with bearer tokens so you can verify calls came from Bland.

### 4. Persona tuning (Agents tab)
- **Voice:** audition samples. Counterintuitive pick: the slightly *distorted, phone-realistic* voice ("Karen") beats HD-clear voices for believability.
- **Multilingual:** agent replies in the caller's language (best-supported list shown in dashboard; EN/ES/DE demoed). Arabic exists but quality is **unverified — test before selling into MENA**.
- **Behavior prompt:** personality, motivation, the 2-3 jobs (answer questions from KB; book appointments).
- **Interruption threshold:** lower = caller can cut the agent off faster = more human. Tune this.
- **Wait-for-hello** toggle for inbound. **Sound effects:** office background = authenticity.
- **Memories** toggle: repeat callers get remembered across calls/chats.
- **Human transfer** node: escalate to a real person (enterprise feature).

### 5. Pathways (the call flow graph)
Node graph: `Greeting (Start) → Answer Questions (KB-connected) ⇄ Collect Booking Details → Book Appointment (tool calls) → Wrap Up → End`. Edit in **draft**, then **promote to production** (production version is locked from edits). Add human-transfer / SMS nodes as needed.

### 6. Channels (same agent, four doors)
1. **Phone:** Inbound Numbers → purchase ($15/mo, pick area code) → publish the number. Use the built-in test-call button before buying.
2. **SMS:** customers text the same agent.
3. **Chat:** dashboard test chat.
4. **Web widget:** Web Widget → create → attach to a pathway → copy the `<script>` snippet into the site. Customize icon/colors/title, optional "powered by Bland" removal, **webhook** (end-of-conversation or every message → your endpoint), **allowed domains** so the widget only runs on your site.

### 7. Custom app integration (Web Agent SDK)
- Client library + `useWebChat` React hook.
- Token flow: frontend → your backend endpoint (Next.js API route / server action / Express / Convex) → Bland client creates a **session token** → returned to the web chat → start/stop call buttons + call state.
- Live-data pattern from the demo: Convex HTTP actions (`httpRouter` + `httpAction`) exposing e.g. `/api/crm/account` (runQuery checkAccount) and `/api/crm/membership` (runMutation updateMembership) on `*.convex.site` — registered as Bland tools, so the agent reads AND writes the production DB mid-call ("upgraded my plan while I watched the dashboard change").

### 8. Agent-native workflow (how WE should build these)
- **Bland MCP server:** search "MCP" in Bland docs → install → connect to Claude Code. Coding agent can then create agents, pathways, personas directly.
- **Bland CLI:** full account access for the coding agent (TTS route = lightweight changes only; CLI = full control). Pair with the stack CLI (e.g. Convex CLI) so one agent debugs both sides end-to-end.
- Docs are LLM-friendly ("agent friendly docs" page) — paste them at the agent.

### 9. Monitoring & compliance
Analytics (cost breakdown per call), Alerts, Call Logs with audio playback, Triage queue for follow-ups the agent flags, Compliance section. For regulated clients (healthcare/finance/legal): enterprise **self-hosted** deployment of the whole stack.

## Verifiable goals (done = provable)

- [ ] KB query log shows test questions answered with high confidence, zero hallucinated prices
- [ ] Norm's self-test passed (it books an appointment end-to-end in its own test run)
- [ ] A real chat/voice test booking **appears in Cal.com** with correct date/time
- [ ] Widget embedded and domain-locked; webhook fires to your endpoint
- [ ] Cost per call measured from Analytics before quoting a client

## Sibling skills
- `ai-receptionist-business` — sell/price/deliver this as a service (niches, pricing, MENA angle)
- `mcp-builder` — if wrapping Bland into our own MCP tooling
- `speech` / ElevenLabs voices — for content voiceovers, NOT phone agents (different stack)
