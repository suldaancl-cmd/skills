---
name: raroque-agent-ready-apps
description: >-
  Chris Raroque's method for building and future-proofing apps for the AI-agent
  era: make your product drivable by Claude / ChatGPT / Codex / the new Siri
  through voice, an MCP, and a public API, all sitting on a text-first
  architecture. Use this whenever planning a new app or SaaS, deciding how to
  differentiate or "future-proof" a product, adding voice / Siri / agentic
  input, auditing whether an app is "agent-ready," designing a product's core
  action or input surface, or advising on indie-app strategy, subscription-app
  margins, or a content-to-product growth flywheel. Pairs with
  raroque-mcp-api-playbook (the tactical build) and mcp-builder (the server code).
---

# Agent-Ready Apps (the Raroque method)

Derived from Chris Raroque ("How I'm Rebuilding My App for the AI Era", 2026-06-30, ~92K-sub indie-dev channel; apps: Amy calorie tracker, Ellie planner). This is a **strategy / planning** skill — reach for it when deciding *what* to build and *why*, not when writing the code. For the actual build, see `raroque-mcp-api-playbook`.

## The thesis (why this matters now)

People are starting to live *inside* AI agents — Claude, ChatGPT, Codex, and (if Apple's revamp lands) Siri. As that happens, the moat stops being a prettier UI and becomes **whether an agent can operate your product on the user's behalf**. Users will increasingly prefer apps and services that "connect cleanly" to the agent they already use every day.

So the strategic move is to make your product **agent-accessible before the demand is obvious**. Being early and being *reachable by agents* is the differentiator — most competitors have no MCP, no public API, and no voice path.

Treat this thesis as a *lens*, not gospel: the strongest version is "reduce friction for agents and humans alike." The weakest version (betting everything on one unshipped platform like a future Siri) is speculative — see Honest caveats.

## The one diagnostic: the input-surface audit

The single highest-leverage question about any product:

> **Is the core action a single, low-friction, free-text (or voice) input that an agent could perform exactly the way a human does?**

- **Yes → you're agent-ready by construction.** Example: in Amy you type one line ("In-N-Out burger and fries") and the backend does all the AI work to return calories. An agent can send that same one line. Voice/Siri/MCP "come out of the box" because the human interface *is already* a text call.
- **No → that's your real work.** If logging an item means search → pick from a dropdown → set quantity → confirm (e.g. MyFitnessPal), an agent can't drive it, and neither can voice. Competitors like this are structurally stuck; the best they can do is "Hey Siri, open the app."

When auditing an existing product, find every core action and ask this question of each. The ones that fail the audit are where to invest.

## Design principles

1. **Text-first / single-input core.** Make the primary action one free-form string. Push all complexity into the backend. This is what makes voice, MCP, and API "free" later.
2. **Hide the machinery.** The user (or agent) shouldn't select or configure anything; the app is smart enough to interpret intent. Chris's app runs a multi-step AI pipeline in 1–2 seconds behind a single text field.
3. **Think ahead about input surfaces, not just features.** Voice (Siri), wearable (Watch), and *agentic* (MCP/API) are all inputs. If your product has no low-friction input path, inventing one is often worth more than a new feature.
4. **Low-friction beats feature-rich** for anything an agent will touch. Every extra required step is a place an agent breaks.

## The four agent-ready surfaces to ship

Ship these to make a product agent-accessible (build details in `raroque-mcp-api-playbook`):

1. **Voice / Siri** — for a text-first app this is often a near-one-shot with an IDE agent. Caveat: current Siri needs *static* pre-defined trigger phrases, so expect a two-step invocation ("Hey Siri, log food in Amy" → then the food) until dynamic phrases are supported.
2. **MCP** — lets Claude/ChatGPT/Codex read and act (log data, analyze patterns, make suggestions) safely on the user's behalf.
3. **Public API** — even if you only strictly need it internally, exposing it lets other developers build on you and compounds distribution.
4. **In-app UX to expose all of the above** — a normal user has to be able to discover and connect it (this is the *hardest* part; see the playbook).

## Economics notes (the model that makes it work)

- **High margin via cheap models.** Chris runs the per-entry AI on a low-cost model (Gemini 2.5 Flash Lite) and reports ~**85% profit margin** at ~$3K MRR — unusual for an "AI app," where 20–30% margins are common. Pick the cheapest model that clears the quality bar for the core action.
- **Know your per-action cost.** He estimates ~½¢ per text entry. Once you know this, you can price, rate-limit, and design abuse protection rationally (critical the moment an agent can call you in bulk).
- **Northstar = week-1 retention** (how many signups are still active 7 days later). Agent-readiness is a *future-proofing / differentiation* bet layered on top of a product that already retains — not a substitute for retention.

## Go-to-market flywheel

Chris's loop: **build-in-public content → app installs → subscription revenue → sponsorships** (the content is the distribution, and it also monetizes directly). Two reusable tactics:

- **Document the build as content.** Each hard problem you solve (e.g. "how I added an MCP to a mobile app") is both a video/post and a proof-of-competence sales asset.
- **Dictate your prompts to coding agents.** Speaking (vs typing) yields longer, more detailed prompts and better output from Claude Code / Cursor. Any dictation tool works.

## Honest caveats (say these out loud when advising)

- **The Siri bet is speculative.** It rides on an unshipped iOS Siri revamp and is US/English-first. For a MENA/Arabic audience, deprioritize Siri relative to MCP + API, which pay off regardless of platform.
- **Distribution is the hidden engine.** "Add an MCP" did not create Chris's growth — a ~92K-subscriber channel pushing the app did. Copy the *architecture*, but don't assume agent-readiness alone drives installs; you still need a distribution source.
- **"The AI one-shot it" undersells the work.** Behind the demo he built a web auth flow, a public API, rate limiting, abuse monitoring, and novel mobile UX — weeks of senior full-stack work. The agent accelerated an expert; it didn't replace the expertise. Don't promise clients magic.

## How to apply this skill

When asked to plan, differentiate, or future-proof a product:
1. Run the **input-surface audit** on every core action; name what fails.
2. Decide which of the **four surfaces** to ship and in what order (usually MCP + API before voice for non-US audiences).
3. State the **economics** (per-action cost, model choice, margin) and the **northstar** so the agent bet sits on a retaining product.
4. Deliver the **honest caveats** — especially distribution and the speculative parts — so the plan is a real decision, not hype.
5. Hand off to `raroque-mcp-api-playbook` for the build.
