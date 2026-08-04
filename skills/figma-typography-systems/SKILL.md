---
name: figma-typography-systems
description: >
  Build a premium TYPE system natively in Figma — a modular scale as number variables,
  text styles per role (display/heading/body/meta/eyebrow), disciplined pairings that
  honor the default-fonts ban, explicit line-height + letter-spacing, fluid type, and
  Arabic-safe RTL pairings. Use whenever a Figma file needs real typography rather than
  ad-hoc font sizes, or when setting up text styles, a type scale, or a font pairing.
  Triggers: "typography in Figma", "type scale", "text styles", "font pairing", "set up
  the type system", "Arabic typography in Figma", "fix the fonts". Load with `figma-use`
  (text styles/variables via `use_figma`) and after `premium-design-laws`. Pair with
  local `typography-scale`; for Arabic, also `rtl-arabic-i18n`.
disable-model-invocation: false
---

# Figma Typography Systems

Type is where premium is won or lost before color even registers. A system means a defined scale, strict role separation, and explicit metrics — not "I'll just size this heading to look right."

## Honor the default-fonts ban (premium-design-laws)

Do **not** default to Cormorant, Outfit, JetBrains Mono, or Noto Kufi Arabic. They're allowed only for a deliberate, named role (e.g. mono for code/meta), never as a lazy fallback. Choose a pairing intentionally per brief; lean on local `typography-scale` / `ui-ux-pro-max` font-pairing data.

## Role separation (the core discipline)

Three jobs, different families/treatments:
- **Display** — the hero/oversize moment. Tight tracking (≈ -0.02 to -0.03em), tight line-height (1.0–1.1), high weight. Often the character font.
- **Body** — readable at length. Comfortable line-height (1.5–1.65), measure 60–75ch, near-neutral tracking. A different family from display.
- **Meta / eyebrow** — labels, captions, kickers. Small, uppercase eyebrows with **positive** tracking (≈ 0.16–0.2em). This is the premium-design-laws replacement for `//`-style section labels and ASCII rules.

Never let one font at one weight do all three jobs — that's the template look.

## The modular scale

Pick a ratio (1.2 minor third for dense UI, 1.25–1.333 for editorial/marketing). Build steps as **number variables** off a base (16px):
`xs sm base lg xl 2xl 3xl 4xl 5xl 6xl`. Each step = previous × ratio, rounded sensibly.

Pair every size with its intended line-height and letter-spacing — store those as variables too where it helps. Large display sizes need *tighter* line-height and tracking than the scale math suggests; small text needs slightly *looser*.

## Text styles per role

Create published **text styles** combining family + weight + size + line-height + tracking + case:
`Display/XL`, `Display/L`, `Heading/1…3`, `Body/L`, `Body/M`, `Body/S`, `Eyebrow`, `Meta`, `Code` (the one allowed mono).

Bind sizes to the scale variables so retuning the scale updates every style.

## Fluid type

For responsive web hand-off, define min/max per role and let it interpolate (CSS `clamp()` on the code side). In Figma, set the desktop and mobile text styles as the two anchors; note the clamp in the design-system doc so the dev side matches.

## Arabic-first / RTL

For Arabic content (Karim ships Arabic-first):
- Use an Arabic-safe pairing — pick from the Arabic options in `typography-scale` / `ui-ux-pro-max`, not a Latin default with broken Arabic fallback.
- Arabic needs more line-height than Latin at the same size; don't reuse the Latin leading.
- Set text direction RTL and mirror layout; load `rtl-arabic-i18n`.
- Never mix AR + EN mid-line; one direction per text block (per Karim's bilingual-layout rule).

## Mechanics (via use_figma)

- Create number variables for the scale; create text styles bound to them.
- Set `fontName` (family + style), `fontSize`, `lineHeight`, `letterSpacing`, `textCase`, `textDecoration` explicitly on each style.
- Verify the fonts are available in the file/team before applying (missing-font = silent fallback).
- Read `figma-use/references/plugin-api-patterns.md` for text-style creation.

## Anti-patterns

- Default-ban fonts used as fallbacks; one family at one weight for everything.
- No scale (eyeballed sizes); no explicit line-height/tracking; positive tracking on display, or none on eyebrows.
- `//`-style or ASCII-rule section labels instead of real eyebrow styles (premium-design-laws symbol hygiene).
- Latin leading reused for Arabic; AR/EN mixed mid-line.
- Hardcoded sizes on text layers instead of styles/variables.

## Pairs with

`figma-immersive-premium` (router) · `figma-color-systems` (the other token half) · `figma-component-craft` (components consume these styles) · local `typography-scale`, `rtl-arabic-i18n`.
