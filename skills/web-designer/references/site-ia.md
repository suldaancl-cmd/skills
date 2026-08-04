# Site architecture & landing page structure

A beautiful page with wrong architecture fails. Decide the story before the visuals.

## The narrative arc of a landing page

Every high-converting landing page answers these questions in order. Sections may combine them but the order rarely changes:

1. **What is this?** (hero) — 3 seconds to understand the product in human terms.
2. **Why should I care?** (problem / promise) — the pain or aspiration this hits.
3. **Prove it** (social proof, logos, stats, testimonials) — de-risk the claim.
4. **Show me how it works** (product demo, feature grid, flow) — make it concrete.
5. **What's different?** (differentiation, comparison) — why not a competitor or the status quo.
6. **What will it cost me?** (pricing or calculator) — set expectations before CTA.
7. **Am I convinced?** (objection handling, FAQ) — surface the doubts they're having right now.
8. **Do the thing** (final CTA) — single clear action.

Sites that skip step 3 feel like hype. Sites that skip step 5 feel like commodities. Sites that skip step 7 lose at the finish line.

## Hero section — the 3-second test

A new visitor should know, in 3 seconds:
1. **What** — one-sentence product description (what it is, not what it does)
2. **Who** — who it's for (explicit or implied)
3. **Why** — one reason it's different / worth attention
4. **How** — visual or demo hint

**Structure:**
```
┌──────────────────────────────────────────┐
│ [Eyebrow: category / tag]                 │
│                                            │
│   MASSIVE HEADLINE                         │
│   (one idea, no punctuation at end)       │
│                                            │
│   Sub-line that explains the what and who │
│   in 15–25 words.                          │
│                                            │
│   [Primary CTA]    [Secondary CTA]        │
│                                            │
│   [Demo / product visual / animation]     │
└──────────────────────────────────────────┘
```

**Headline patterns that work:**
- Outcome-first: "Ship React apps in seconds." (Vercel)
- Category-redefining: "A new home for Linux nerds." (Hetzner vibe)
- Contrast: "Everything you need. Nothing you don't." (Things-app)
- Specificity: "The fastest way to build React forms."
- Quote-able: "Say hello to the future of writing." (works only when you've earned it)

**Avoid:**
- Abstract claims: "Transform your business."
- Feature lists as headline: "AI-powered, real-time, scalable..."
- Asking questions: "Ready to grow?"
- Multiple headlines: pick one.

## Section patterns (reusable)

### Features grid
- 3 or 6 features (avoid 4 — feels like a bento miss, avoid 5 — asymmetric).
- Each: icon + short title (2–4 words) + 15–25 word description.
- Consistent visual weight per card. No "hero feature" unless by design.

### Feature walkthrough (alt. to grid)
- One feature per scroll-snap section with large visual + prose.
- Best when features are narrative-dependent ("first, then, finally").

### Social proof band
- Logo row: 4–7 recognizable logos, grayscale, equal optical size.
- OR a single large testimonial with name, title, company, photo.
- Avoid: vague testimonials ("great product!"), no attribution, no photo.

### Comparison table
- You vs. competitor / status quo.
- Max 5 rows. Check-marks + Xs or subtle visual encoding.
- Don't lie. Users research competitors; overclaiming loses trust.

### Pricing
- 3 tiers max. Middle tier is the recommended one — make it visually dominant.
- Show what's *included* clearly. Annual/monthly toggle if applicable.
- "Contact sales" is its own tier, not a note.
- FAQ under pricing addresses: cancellation, refunds, data ownership, billing.

### FAQ
- 5–8 questions. Use real questions from support / sales, not marketing.
- Order by frequency, not alphabetically.
- Each answer ≤ 3 sentences. Link to deeper docs if needed.

### CTA section (bottom of page)
- Restates the promise in 1 line.
- Single primary CTA (same as hero).
- No form on marketing pages unless conversion friction is desired (B2B often wants form).

## Information architecture — the nav

### Primary nav (visible)
- 4–7 items max. If you need 8+, your IA is wrong.
- Ordered by user value, not internal org: Product > Pricing > Resources > Customers.
- "Sign in" (secondary style) + CTA (primary style) on the right.

### Secondary nav (dropdown / mega menu)
- Only if you genuinely have sub-areas (product suite, industries).
- Structure with a clear hierarchy, not a flat list of links.

### Footer
- Full IA map. This is where you link to every page users might want: pricing, docs, blog, careers, legal, changelog, status.
- Group logically: Product, Company, Resources, Legal.
- Status link with a green/red indicator is a trust signal.

## Copy — do's and don'ts

**Do:**
- Use second person ("you") and active voice.
- Be specific: "Deploy in 8 seconds" > "Deploy fast."
- Lead with outcome, follow with mechanism.
- Use the words your users use (not your team's jargon).

**Don't:**
- "Seamless", "elevate", "unleash", "unlock", "supercharge", "revolutionize", "next-gen", "cutting-edge", "delve", "leverage" as a verb.
- "We believe that..." — nobody cares what you believe, they care what you ship.
- Stacked adjectives ("our innovative, powerful, intuitive platform").
- Past buzzwords as present claims (if "AI-powered" is in your hero in 2026, it better be actually novel).

## Page hierarchy beyond the landing

### Docs site
- Quick start / 5-minute tutorial must be discoverable from home.
- Concepts → Guides → Reference — in that order.
- Full-text search on every page. Keyboard shortcut to open.
- Sidebar is collapsible but not hidden by default.

### Pricing page (dedicated)
- Same 3-tier table as landing but more detail.
- Enterprise row with "Contact sales".
- Calculator if pricing is usage-based.
- Comparison table vs. competitors (optional, but powerful when honest).

### Changelog / Updates
- Reverse-chronological. Dates visible.
- Tag by type (feature, fix, breaking).
- RSS feed. Users care more than you think.

## Conversion principles

- **One primary action per page.** Multiple CTAs OK if they're the same action in different positions.
- **Reduce friction progressively.** First CTA → "Try free / See demo." Last CTA → "Create account."
- **Trust signals near the CTA.** Security badges, "No credit card", "30-day refund" — placed where the user is about to commit.
- **Form fields are a tax.** Every field reduces conversion. Ask for only what you need to deliver immediate value. Enrich the rest later.
- **Loading states matter.** Slow pages kill conversion; see performance in `code.md`.

## Common IA mistakes

- Home page is a kitchen-sink of every feature. Pick one main message.
- Nav item order reflects the org chart, not user priority.
- Pricing is buried (users look for it first — link from hero).
- "Learn more" as a CTA — what will I learn? Be specific.
- Modal on page load — disrespectful.
- Newsletter popup on page load — also disrespectful.
- Cookie banner so tall it covers the CTA — no.

## Before shipping

- Read every section out loud. If it sounds weird, it reads weird.
- Can you delete 30% of the copy and lose nothing? If yes, delete it.
- Does every section move the user forward, or are some just noise?
- Is the primary CTA the same in hero, mid-page, and footer? It should be.
