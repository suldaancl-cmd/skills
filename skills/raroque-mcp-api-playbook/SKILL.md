---
name: raroque-mcp-api-playbook
description: >-
  Chris Raroque's tactical playbook for making an existing app agent-accessible
  by adding an MCP server plus a public API — especially a mobile / iOS app that
  has no web presence. Use this whenever you need to expose an MCP for Claude /
  ChatGPT / Codex, ship a public API for a product, wire OAuth onto an app that
  only ever had native (in-app) login, design rate limits that stop agent-driven
  bulk-call abuse, or figure out the in-app UX for explaining and connecting an
  MCP to normal users. Walks the four problems in the order they actually bite:
  authentication, the missing API, security / rate-limiting, and mobile UX.
  Complements mcp-builder (which scaffolds the server code) by covering the
  product, auth, security, and UX decisions around it. Pairs with
  raroque-agent-ready-apps (the strategy).
---

# MCP + Public API Playbook (the Raroque method)

Derived from Chris Raroque ("How I'm Rebuilding My App for the AI Era", 2026-06-30). This is the **tactical build** companion to `raroque-agent-ready-apps`. Use it to bolt an MCP + public API onto an *existing* product. For the raw MCP server scaffolding, also use `mcp-builder`; this skill covers the decisions that scaffolding skill doesn't — auth, API shape, abuse, and how a normal person even turns it on.

## When to use

- You have a working app (often mobile/native) and want Claude/ChatGPT/Codex to act on the user's behalf.
- You're exposing a public API and an MCP together.
- The app currently authenticates only inside the native app and has **no web login**.
- You need rate limits that survive legitimate *bulk* agent calls without opening the door to abuse.

## Why it's harder than "just add an MCP"

Chris assumed this was ~a day (he'd built an MCP before for another app). It was substantially harder, because an MCP forces four separate problems to the surface in sequence. Do them in this order — each unblocks the next.

## Problem 1 — Authentication (do this first; it blocks everything)

- **The bite:** OAuth is the standard, recommended way to auth an MCP — but OAuth needs a **web** sign-in and authorization page. A mobile-only app has no web anything.
- **The fix:** Build a real web sign-in + authorization flow *before* the MCP can exist. Include the same providers your app already offers (Google, Apple sign-in), which adds complexity you must budget for.
- **The cheaper fallback:** API-key auth (user pastes a key when adding the MCP) avoids the web build. It's less slick than OAuth but ships far faster — reasonable for a v1 or a dev-only audience.
- **Gotcha:** if you already run auth through a backend-as-a-service, you still need the *authorization consent* page ("Allow <App> access?"), not just login.

## Problem 2 — The missing API

- **The bite:** Native apps often do device → private backend with **no API a third party can call**. An MCP is a third-party client, so there's nothing for it to talk to.
- **The fix:** Build proper REST endpoints. Decide **public vs private** early — Chris chose to make it a *public* API so outside developers can build on the product (distribution upside for near-zero extra work once it exists).
- **Design endpoints around real agent use, not the obvious case.** His instinct was a "get today's food" endpoint; real questions are broader ("what did I eat the last 2 weeks?"), so he had to rebuild it to accept **date ranges**. Before coding each endpoint, ask *how an agent-wielding user will actually phrase the request* and shape the endpoint to that. Most of the time here is spent on this modeling, not on writing code.

## Problem 3 — Security and rate-limiting

- **The bite:** An open MCP/API invites abuse, and every AI-backed action costs real money (~½¢ per entry in his case). On-device you can hide rate limits; an open surface can't.
- **The naive trap:** a fixed cap (e.g. "3 logs/minute") **breaks a legitimate use case** — someone telling ChatGPT "log everything I ate today" needs a burst of many calls at once. That's a real, common pattern, not abuse.
- **The fix: gradual cool-down.** Allow a genuine burst, then progressively throttle if bursts keep coming, forcing a slowdown/stop on sustained hammering. This is a standard, well-understood rate-limit shape and it serves both the honest bulk user and abuse defense.
- **Add monitoring** for abuse patterns on top of the limiter before you open the surface widely.

## Problem 4 — UX (usually the hardest, and least expected)

- **The bite:** How do you explain an MCP to a *normal person inside a phone app*? Essentially every existing MCP-connect example lives in a web or desktop settings page — almost no mobile app does this, so there's no pattern to copy.
- **The fix Chris landed on:** a **dedicated settings page** that
  - shows plainly what the user's AI tools will be able to do,
  - gives **dead-simple, copy-pasteable connect instructions**,
  - lets the user **copy or email the setup steps to themselves** to finish on desktop (where they'll actually paste into Claude/ChatGPT),
  - includes a separate **API section** to manage API keys and read the docs.
- **Expect heavy iteration here.** Condensing something that normally lives on desktop into a digestible mobile flow took the most tries. Budget for it; don't treat it as a last-minute settings toggle.

## Ordering rationale

Auth (1) gates the MCP existing at all. The API (2) is the thing the MCP and the world call. Security (3) only makes sense once the API's shape is known. UX (4) exposes the finished capability to humans — do it last, but budget the *most* iteration time for it.

## Paste-ready checklist for an IDE agent

```
Goal: make <APP> agent-accessible (MCP + public API).

1. AUTH
   [ ] Choose OAuth (web flow) or API-key (faster v1).
   [ ] If OAuth: build web sign-in + "Allow <APP> access?" consent page,
       incl. Google/Apple providers.
2. API
   [ ] Build REST endpoints; decide public vs private.
   [ ] For each endpoint, model the real agent phrasing first
       (support ranges/filters, not just the single obvious case).
3. SECURITY
   [ ] Implement gradual-cool-down rate limiting (allow burst, then throttle).
   [ ] Add abuse monitoring. Know your per-action cost.
4. UX
   [ ] Dedicated in-app settings page: what agents can do + copy/paste
       connect steps + copy/email-to-desktop + API-key mgmt + docs.
   [ ] Iterate — this is the hardest surface.
```

## Handoffs

- Strategy / whether to build this at all → `raroque-agent-ready-apps`.
- MCP server scaffolding / protocol details → `mcp-builder`.
