---
name: template-color-typography
description: Color palette and typography systems for SELLABLE Webflow/Framer templates — palette archetypes with real hex values, font pairings actually used on premium 2025-26 sites, licensing reality (Google Fonts vs paid), and exact Webflow/Framer build notes. Invoke when designing a template's color system, picking fonts for a template, or building the style-guide/design-tokens page of a Webflow or Framer template meant for marketplace sale.
---

# Template color + typography

Extends `premium-design-laws` and the default-fonts ban — this skill does not replace either. Read `premium-design-laws/SKILL.md` first. Every rule below must comply with it: no `//` section-label decoration, no banned defaults (Cormorant, Outfit, JetBrains Mono, Noto Kufi Arabic) as a lazy fallback, real modular scale, semantic color tokens, WCAG-aware CTA contrast.

This skill adds the marketplace-specific layer premium-design-laws doesn't cover: which palette/font choices actually sell on Webflow and Framer template marketplaces, why, and the exact native-vs-code build technique in each tool. Sourced from a 112-site color study and a 140-site typography study (citations kept per pattern — see the two reference files).

## Workflow

1. Pick ONE color archetype from `references/color-palettes.md` and ONE typography pairing from `references/typography.md` that fit the brief's vertical (SaaS/AI, editorial/portfolio, hospitality/wellness, playful/consumer, events/streetwear).
2. Ship every color as a token (Webflow Variable / Framer Color Style) and every font role as a Text Style — never a hardcoded value. Buyers must be able to re-skin from one panel; marketplaces reward "customizable" templates.
3. Never ship a paid font in the template files. Design on the free clone, name the paid upgrade font in the template docs (see licensing table below). This is a hard marketplace rule (Webflow: Google/OFL only; Framer: library/Google fonts only), not a style preference.
4. Follow `premium-design-laws` Color & Font deck-first rule: present 3-4 archetype options before building, same as any other design work.
5. Build with `frontend-design` / `ui-ux-pro-max` as normal; this skill only supplies the palette+type decision layer.

## Non-negotiables (apply regardless of archetype)

- **Never pure `#FFF` or pure `#000`.** Every verified premium site offsets both ends (Linear `#08090A`/`#E2E4E9`, Stripe `#181818`, Aristotle `#F0ECE0`). Pure values are the fastest "unfinished/default" tell in a template preview.
- **Tint neutrals to the accent hue**, don't use flat gray. Build the gray/black ramp from the accent's hue at low saturation (formula and example in `references/color-palettes.md`).
- **Three type voices, not one:** display (character serif or oversized sans), body (neutral grotesk), and a mono/label voice for eyebrows and meta. See `references/typography.md`.
- **Ship tokens, not hardcoded values**, and say so in the template listing — "customizable color system" / "2 themes" is an observed purchase trigger.
- **Sellability score in this skill (1-10)** reflects marketplace evidence density (views, bestseller roundups, Awwwards frequency) from the source research, not personal taste — use it to break ties between archetypes that both fit the brief.

## Quick palette picker

| Vertical | Archetype (full detail in references/color-palettes.md) | Sellability |
|---|---|---|
| AI / SaaS / devtool (most crowded, highest discovery) | Near-black dark mode (`#08090A`-class base) | 10 |
| SaaS wanting one strong brand hook | Monochrome dark + one acid/electric accent | 10 |
| SaaS hero wanting max "wow" with zero assets | Aurora / mesh gradient hero | 10 |
| Multi-feature SaaS (bento sections) | Functional multi-accent set on dark (Linear trio) | 7 |
| Portfolio / studio / architecture / wellness (less crowded) | Warm off-white editorial paper base | 9 |
| Food / pets / events / kids / agency (Awwwards bait) | Paper base + muted retro brights | 6 |
| Health / HR / edtech / consumer fintech (friendly, less crowded than dark-SaaS) | Soft pastel washes on light | 7 |
| Any template needing broad buyer appeal | Dark hero → light body split | 9 |
| Any dark template (finishing touch) | Grain/noise overlay + neon micro-glow accents | 8 |

## Quick type picker

| Vertical | Pairing (full detail in references/typography.md) | Sellability |
|---|---|---|
| Default premium pairing, any vertical | Editorial serif display + neutral grotesk body | 10 |
| Any hero headline needing a personality lift | Italic serif accent word inside sans headline | 9 |
| Any template (system-signal layer) | Monospace eyebrow/label layer | 9 |
| Marketing/portfolio hero, zero imagery | Oversized full-bleed hero type | 9 |
| Any Awwwards-tier motion demo | Masked per-line kinetic text reveal | 10 |
| Safest SaaS/startup default | Single neo-grotesk system (Inter economy) | 8 |
| Hospitality / wellness / fashion | Quiet-luxury high-contrast serif | 8 |
| Sport / streetwear / event / esports | Ultra-condensed or ultra-extended uppercase | 7 |
| MENA / Arabic-facing (Karim's home market — underserved niche) | Arabic/RTL-ready dual-script system | 7 |
| AI / dev-tool "engineered" feel | Sans + matching-mono same-superfamily | 8 |

## Free-clone-then-upsell playbook (mandatory for legality)

Both marketplaces ban paid/Typekit fonts inside submitted templates. Design on the free clone, document the paid upgrade in the template's instructions page as a customization option:

| Paid font seen on premium sites | Free marketplace-legal clone |
|---|---|
| Editorial New / Editorial Old | Instrument Serif |
| Canela / GT Alpina | Fraunces (variable, SOFT/WONK axes) |
| Söhne / Suisse Int'l | Switzer |
| Diatype / Diatype Mono | DM Sans + DM Mono |
| Degular / Degular Mono | IBM Plex Sans + IBM Plex Mono |
| Monument Extended / Druk Wide | Archivo Black / Archivo Expanded |

Full pairing list, per-site citations, and Webflow/Framer build notes: `references/typography.md`.

## References

- `references/color-palettes.md` — 11 palette archetypes, exact hex values, why each works, Webflow build steps, Framer build steps, sellability score, source sites.
- `references/typography.md` — 11 typography patterns, verified pairings per site, licensing, Webflow/Framer build steps, sellability score, source sites.

Both files carry the original research's `sources` lists — cite them, don't re-derive claims from memory.
