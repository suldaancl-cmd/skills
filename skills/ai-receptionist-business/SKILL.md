---
name: ai-receptionist-business
description: Sell, price, and deliver AI phone receptionists as a service to appointment-driven businesses (clinics, dental, salons, restaurants, real estate, legal). Discovery questions, unit economics, pricing tiers, same-day delivery workflow, MENA/Arabic caveats, compliance upsell. Invoke when the task is about selling AI receptionists, voice-agent agency offers, pricing an AI answering service, or pitching missed-call recovery to a local business.
---

# ai-receptionist-business — the missed-call money printer

The service play on top of the `bland-ai-receptionist` build skill. Source stats from Sonny Sangha's Bland tutorial (youtu.be/JSYOZvtkAx4); economics marked [inference] are ours, not the video's.

## The pitch (why businesses buy)

- **62% of calls to small businesses go unanswered. 85% of people have hung up on a "press 1" menu.** (stats as quoted in the video — re-verify before putting in client-facing decks)
- Missed call = customer calls the competitor. The AI answers instantly, 24/7, no hold music, books the appointment mid-call, and texts confirmation.
- Cost anchor: **$0.14/min platform cost; 108 calls ≈ $9**. A part-time human receptionist costs orders of magnitude more — this is the whole spreadsheet for the client. [salary comparison = video's framing; localize numbers per market]

## Target niches (appointment-driven = tool-call-friendly)

Dental / medical clinics · salons & spas · restaurants (reservations) · real-estate agencies (viewings) · legal intake · car services. Pick niches where (a) every missed call has clear revenue value, (b) booking is calendar-shaped (Cal.com-compatible), (c) FAQ lives in one PDF (prices, hours, insurance).

## Discovery questions (before building anything)

1. How many calls/day, and what % missed? (their phone system usually knows)
2. What are the 10 questions callers actually ask? (becomes the KB test set)
3. What booking system today — calendar, pen-and-paper, WhatsApp? (pen-and-paper → set up Cal.com as part of the deal)
4. What must ALWAYS escalate to a human? (emergencies, complaints, VIPs → transfer node)
5. Languages callers use? (see MENA caveat below)
6. Any regulated data on calls? (health details → compliance / self-host conversation → enterprise, bigger deal)

## Offer structure [inference — adapt per market]

- **Setup fee** (one-time): KB build from their docs + persona + booking hookup + number + widget on their site. Same-day deliverable is credible — the video ships one in ~30 min of work.
- **Monthly retainer**: number rental + per-minute usage passed through with margin + monitoring (call-log review, KB updates, triage follow-ups from the dashboard).
- **Compliance tier**: regulated clients → Bland enterprise self-hosted — position as the premium tier, priced accordingly.
- Demo-as-proposal close: build the agent on THEIR real PDF before the sales call, let the owner call it live. The wow does the closing (same pattern as MotionSites prompt-shop economics).

## Delivery workflow (per client)

1. Collect: business PDF/site, Cal.com (or create it), escalation rules, voice preference.
2. Build per `bland-ai-receptionist` skill (KB → Norm → Cal.com tools → persona tune → pathway → promote).
3. Test gate (Verification Lock): 10 real FAQ questions answered from KB with zero invented prices + one end-to-end booking visible in Cal.com + one escalation test.
4. Ship: publish number + embed widget (domain-locked) + webhook into their CRM/sheet.
5. Retainer loop: weekly call-log + triage review, KB updates when prices/hours change, monthly cost report from Analytics.

## MENA / Karim-specific angle

- Fits the fleet's **WhatsApp AI concierge #1 opportunity** (see `reference_fleet_opportunity_convergence`): same buyer, same pain, phone instead of WhatsApp — bundle both in one offer.
- **Arabic voice quality on Bland is UNVERIFIED.** The video demoed EN and claimed broad multilingual support (EN/ES/DE named as best-supported). Before selling to a Saudi clinic: run a paid test call in Gulf Arabic, judge accent + interruption behavior yourself. If Arabic fails the bar, sell to English-serving niches (expat clinics, international schools) or web-widget-first, and re-test quarterly.
- Arabic-first content rule applies to all client-facing marketing; the agent's own language mix follows the client's callers.

## Red flags / what NOT to do

- Don't quote the 62%/85% stats or Bland's scale claims in client decks without re-verifying — they came from a sponsored video.
- Don't sell healthcare/legal on the cloud plan — that's the self-host conversation.
- Don't hand-build pathways before trying Norm; don't rebuild what its self-test already fixed.
- Don't promise "replaces your receptionist" — promise "answers the calls she misses" (easier close, truthful, keeps the human-transfer path).

## Verifiable goals

- [ ] Demo agent on the prospect's real docs exists before the pitch call
- [ ] Signed scope lists: KB sources, escalation rules, languages, booking calendar
- [ ] Test gate passed and screenshotted (KB query log + Cal.com booking + escalation)
- [ ] Client can call the live number and book — that call log is the acceptance artifact
