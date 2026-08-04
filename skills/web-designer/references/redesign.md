# Redesigning an existing site

Redesigns go wrong when you throw out the baby with the bathwater. Before rebuilding, audit what works, what doesn't, and why. Redesign with intent, not for its own sake.

## The audit — before any pixel changes

### 1. What's the brief, really?
- "Make it look better" is not a brief. Push for: what's failing? Conversion? Trust? Perception vs. competitors?
- If a metric is dropping, get the data. If a stakeholder is unhappy, get the specific complaint.
- If the answer is "I just don't like the old one", that's valid — but commit to a specific new direction, not "nicer".

### 2. Inventory the existing site
- **Pages** — list every page. Which get traffic? Which are zombies?
- **Components** — reusable UI, custom patterns, one-offs.
- **Content** — what's the voice, length, structure? Can it be reused?
- **Assets** — photography, illustrations, icons. Can be reused, need refresh, or retired?
- **Tech stack** — CMS? Framework? Any constraints on the redesign?
- **Analytics** — what do users do? Heatmaps, scroll depth, click maps if available.

### 3. What's actually working?
Before deleting:
- High-converting sections (keep the content, restyle).
- SEO-valuable pages (preserve URLs, meta, content hierarchy).
- Brand elements with equity (logo, signature color, tagline).
- Components your team knows how to use.

### 4. What's broken?

Categorize:
- **Strategic** — IA is wrong, positioning unclear, wrong audience.
- **Visual** — outdated aesthetic, inconsistent, cluttered.
- **UX** — flows are broken, friction at conversion points.
- **Performance** — slow, not mobile-optimized, broken on common devices.
- **Accessibility** — fails basic WCAG, bad contrast, keyboard traps.
- **Technical debt** — stack is holding back updates.

You probably can't fix all of these in one redesign. Prioritize based on what the brief demands.

## The decision: refactor, redesign, or rebuild?

### Refactor — keep IA and aesthetics, fix execution
- Use when: users and the brand are happy with the direction but execution is sloppy.
- Scope: improve component quality, clean up tokens, fix performance, a11y pass.
- Risk: low. Ship incrementally.

### Redesign — new aesthetic, same IA and content
- Use when: the site feels dated but the structure is right.
- Scope: new design language, tokens, motion. Content mostly reused.
- Risk: medium. One-shot deliverable, but content reduces risk.

### Rebuild — everything changes
- Use when: strategy has shifted (new audience, new positioning), or technical debt is blocking.
- Scope: IA, content, design, engineering.
- Risk: high. Takes 3–6 months minimum; don't underestimate content rewriting.

Most "redesigns" that clients ask for are actually refactors. Most proposals that agencies make are actually rebuilds. Be honest about which one you're doing.

## Preserving what matters

### URLs & SEO
- Keep URL slugs when possible. Changes = 301 redirects.
- Keep `<title>` and meta descriptions unless demonstrably better.
- Keep heading hierarchy and primary keywords in H1/H2.
- Maintain internal link structure.
- Test: does Search Console show a traffic drop post-launch? If yes, you broke something.

### Analytics & tracking
- Preserve event names for existing funnels. Renaming = losing historical comparison.
- If events must change, document the mapping. Keep old events firing for 30 days.

### Performance budget
- Don't launch a "premium" redesign that's 3× slower. Premium ≠ heavy.
- Core Web Vitals must hold or improve.

## The design process for a redesign

### Phase 1 — Strategy (1 week)
- Define success. Not "looks better" — specific metrics (bounce rate, conversion, NPS, page speed).
- Define the new positioning if it's changing. What's the one-sentence elevator pitch?
- Agree on aesthetic direction (see `aesthetics.md`). Commit.

### Phase 2 — Design system (1–2 weeks)
- Tokens first: color, type, spacing, radius, motion.
- Component primitives: button, input, card, nav. Get sign-off on these before composing pages.
- Component patterns: PricingTable, FeatureGrid, Hero variations.
- Document in Storybook or similar.

### Phase 3 — Page design (2–4 weeks)
- Start with highest-traffic / highest-value pages.
- Hero, features, pricing, signup flow before secondary pages.
- Responsive at each step, not as an afterthought.

### Phase 4 — Build (parallel with Phase 3, or after)
- Design-dev pairing. Design should not ship in isolation then "hand off".
- Weekly reviews of built vs. designed.
- A11y pass continuously, not at the end.

### Phase 5 — Launch
- **Staged rollout** if possible: 10% → 50% → 100%, with metric checks.
- **Holdout group** for 2–4 weeks: compare conversion rate old vs. new.
- **Redirects** verified. Sitemap submitted. Analytics intact.
- **Monitoring** the first 72 hours: Sentry errors, LCP regression, bounce-rate spike.

## Iterating on the redesigned site

Post-launch, resist the "we're done" mindset:
- Bug fixes and polish Week 1–2.
- Measure Week 2–4 against baseline.
- Identify weakest page; redesign iteration Week 5+.

Great sites are not launched; they're maintained. The site that never changes is either perfect (rare) or abandoned (common).

## Common redesign mistakes

- **Redesigning the wrong thing.** Stakeholder says "home page feels dated", but the conversion problem is on pricing. Fix the real issue.
- **Ignoring what worked.** Throwing out a high-converting section because "it looks old".
- **New design, same old content.** Copy is 50% of the site. If you redesign without rewriting, you've only done half the job.
- **Not testing on real users.** The team thinks the new design is "cleaner"; users find it harder to navigate. Test early and often.
- **Over-animation.** New design proves its "premium-ness" through 40 scroll animations. Users hate it. Restrain.
- **Different aesthetic, same IA.** Users are confused because the signposts changed. Keep navigation language consistent.
- **Accessibility regression.** Old site was AA-compliant; new one ships at AAA contrast but fails keyboard nav. Audit both.
- **Mobile shipped late.** Mobile-first from day one, not "we'll do mobile after desktop is done."

## The ask before starting

If the user says "redesign my site":

1. **What's the URL?** (Fetch it, look at it.)
2. **What specifically is failing?** (Conversion, perception, performance, accessibility, stale?)
3. **Who's the target user now?** (Same as before, or shifting?)
4. **What's the positioning sentence?** (One sentence, what the site claims.)
5. **What CANNOT change?** (Logo, URL structure, brand colors, specific sections?)
6. **What's the deadline and budget?** (Shapes scope.)

Don't start designing until these are answered. Half of redesign failures are scoping failures.
