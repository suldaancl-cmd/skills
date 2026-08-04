---
name: immersive-web-token-vault
description: A vault of REAL design tokens — palettes, typography pairings, spacing/radius, and gradient guidance — reverse-engineered from 15 award-winning / Awwwards-tier websites (Exo Ape, Unseen, Lusion, Igloo Inc SOTY, funkhaus, Scout Motors, Hatom, Clear Street, Studiogusto, Serious Business, Umault, X-Shack, Design Embraced, Zajno). Fire this whenever starting or art-directing an immersive / premium / award-tier website or landing page and you need a proven color palette, a display+body+mono font pairing, a spacing/radius system, or an honest answer on gradients — every value is source-cited to a named site (extracted via skillui static analysis, no guessing). Use it to seed a colors+fonts deck, sanity-check a palette against what actually wins awards, or find a free font that matches a commercial one. Pairs with premium-design-laws, ui-ux-pro-max, and the immersive builder skills.
---

# Immersive Web Token Vault

Real design tokens pulled from live award-winning sites, so a build can start from what demonstrably wins — not from taste alone. Every hex, font, and metric here was extracted with `skillui` (pure static analysis of shipped CSS, no AI, no guessing) on 2026-07-13 and is attributed to its source site.

This is a **reference vault**, not a builder. It feeds the colors+fonts deck step; it does not skip it. Karim still picks the direction.

## What's inside

- `references/palettes.md` — per-site palettes (background / surface / text / accent / semantic + extended swatches), split dark vs light, plus the synthesized **award palette recipe**.
- `references/typography.md` — per-site display×body×mono pairings, the four recurring patterns, and a **free-substitute table** (commercial face → premium free equivalent).
- `references/gradients-and-tokens.md` — the honest gradient finding, CSS gradients *constructed from* real accents, and the extracted spacing / border-radius / motion-density tokens.

Read the file that matches the decision in front of you. Don't load all three unless you're building a full deck.

## The award-tier cheatsheet (synthesized from all 15 sites)

Use this as the fast heuristic; go to the reference files for the receipts.

1. **Palette = base + text + ONE accent.** Pick one base (warm off-white like `#faf6f4`/`#e4e0db`, or near-black like `#000`–`#1c2928`), one high-contrast text, and exactly one saturated accent (electric blue `#0016ec`, coral-red `#ff4e4d`, hot pink `#ff7ec4`, acid green `#c1ff12`). Everything else is a low-chroma neighbor. Igloo Inc won Site of the Year 2024 on a **two-color** DOM.
2. **Warm your neutrals.** Award off-whites are warmed (`#faf6f4`, `#e4e0db`), not clinical `#f5f5f5`. Warm reads premium.
3. **Type: display + neutral body + a touch of mono.** Either an editorial serif (Saol, Times, Nib, Reyhan) *or* a statement grotesk (Aeonik, Matter, Acid Grotesk) for heads; a quiet grotesk for body; mono only for labels/timestamps. Two families max.
4. **System serif is a flex.** Exo Ape and Igloo ship Times New Roman on purpose — when WebGL carries the spectacle, a cost-free system serif reads as confidence.
5. **4px grid, committed.** 11/15 sites use a 4px base. Pick multiples and never use arbitrary spacing.
6. **One radius language.** Tight 8px everywhere, OR pills/circles (`100%`, `50–180px`). Never a fussy multi-value radius scale.
7. **Gradients come from shaders, not CSS.** ~Every site is "solid colors only." Atmospheric color is WebGL (noise/fluid/bloom). A flat CSS gradient hero is a non-award tell. See `ogl-webgl` / `webgl-effect-recipes` / `direct-immersive-color-light`.

## How to use it

**Seeding a colors+fonts deck** (the deck-first rule): open `palettes.md` and `typography.md`, pick 3–4 directions that fit the brief (e.g. "Lusion: white + electric blue + Aeonik" vs "Unseen: warm white + Saol Display editorial" vs "Hatom: black + acid neon"), and present those as deck options for Karim to choose. Do not write site code before he picks — this vault informs the deck, it is not the go-ahead.

**Sanity-checking a palette:** if a proposed palette has three loud colors and a 45° CSS gradient, this vault is the evidence that award-tier goes the other way — restrain to one accent, move color into a shader.

**Finding a free font:** the substitute table in `typography.md` maps each commercial face (Lausanne, Saol, Aeonik, Matter, Neue Montreal…) to a premium free equivalent (Fontshare Switzer / General Sans / Clash, Google Fraunces / Space Grotesk). These are NOT the banned lazy defaults.

## Provenance & refreshing the vault

Every value traces to a site named in the reference files. Live sites change — re-verify before quoting as current.

To refresh a site or add a new reference, re-run the extractor (already installed):

```bash
skillui --url https://exoape.com --format design-md --out ./tokens --name exoape
# then read ./tokens/exoape-design/DESIGN.md and fold new tokens into the reference files
```

Sites that render entirely through JS/canvas (e.g. Dorst & Lesser) ship no readable CSS tokens — skillui honestly returns zero rather than inventing. Treat those as canvas-driven and study their motion, not their tokens.

## Related skills

- `premium-design-laws` — the standing typography/color/gradient law; load it first.
- `mine-award-site-patterns` — turn reference URLs into a transferable design brief (the mechanism behind the effects).
- `ui-ux-pro-max` — lock the full design system once a direction is picked.
- `direct-immersive-color-light`, `direct-kinetic-typography` — take these static tokens and make them move.
- `ogl-webgl`, `webgl-effect-recipes`, `shader-dev` — where real gradients/atmosphere come from.
