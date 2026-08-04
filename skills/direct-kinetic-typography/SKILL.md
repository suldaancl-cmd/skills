---
name: direct-kinetic-typography
description: Design expressive, readable typography systems whose motion communicates brand meaning across load, scroll, hover, transitions, and variable-font states. Use for kinetic type, oversized editorial heroes, masked line reveals, SplitText choreography, scroll-scrubbed words, variable font axes, type-led portfolios, bilingual Arabic/English motion, or award-level sites where typography must act as an interface rather than static styling.
---

# Direct Kinetic Typography

Make type the protagonist without sacrificing reading, shaping, accessibility, or performance.

## Start with the type deck

Before writing CSS or animation code, produce 3–4 type routes. For each route show:

- display, body, utility/mono, and Arabic roles when required
- real sample headlines, body copy, numerals, CTA, and navigation
- license and delivery method
- weight, width, optical-size, slant, or custom axes actually available
- static composition and one motion motif
- one-line rationale tied to the brief

Do not default to Cormorant, Outfit, JetBrains Mono, or Noto Kufi. Do not select a font because it merely looks “premium.” Use `premium-design-laws`, `font-pairing-local`, and `variable-fonts-local` to validate the route.

For Karim's projects, stop after the Colors & Fonts deck and obtain a route selection before production code.

## Define roles and constraints

For each role specify:

- family, fallback, format, subset, and preload priority
- fluid size, line height, measure, tracking, and optical adjustments
- minimum and maximum viewport behavior
- axes and safe ranges
- split unit: block, line, word, or character
- semantic DOM and screen-reader text strategy
- mobile and reduced-motion behavior

Prefer standard properties such as `font-weight`, `font-stretch`, `font-style`, and `font-optical-sizing`. Use `font-variation-settings` for custom axes or precise multi-axis control.

## Choose one signature motif

Select one motif derived from the concept:

- assembly: fragments converge into a readable word
- pressure: width/weight responds to force or velocity
- reveal: lines emerge from a mask
- focus: blur/grade/contrast resolves into clarity
- relay: a word hands position or meaning to the next scene
- field: type bends, displaces, or lights around interaction

Repeat the motif across hero, transitions, labels, and footer with different intensity. Do not combine several unrelated showcase effects.

## Choreograph for reading

- Keep hero entrance finite and interruptible.
- Reveal the most important semantic unit first.
- Let users finish reading before the next scrubbed change.
- Reserve per-character motion for short Latin display text.
- Keep body copy stable; animate containers or emphasis, not every sentence.
- Use normalized progress for scrubbed typography so mobile can substitute simpler behavior.
- Pause loops and variable-axis animation when off-screen.

## Arabic and bilingual rules

- Never split Arabic into characters; it breaks connected shaping. Animate by line or word.
- Keep Arabic tracking at `0` and body text at least `16px`.
- Use one direction per block; do not mix RTL and LTR fragments inside one animated wrapper.
- Preserve logical DOM order and use visual transforms only.
- Test punctuation, numerals, ligatures, diacritics, line wrapping, and font fallback.
- Give Arabic and English equivalent hierarchy without forcing identical geometry.

## Accessibility and performance

- Keep a single accessible text node when visual duplicates are `aria-hidden`.
- Do not reveal essential copy only through canvas or SVG paths.
- Under `prefers-reduced-motion`, render the final readable state immediately or with a short opacity fade.
- Subset and self-host production fonts where licensing permits; preload only above-fold essentials.
- Avoid animating layout-dependent properties on long text.
- Test font swap, slow loading, zoom to 200%, and narrow widths.

## Required deliverable

Use `references/type-motion-spec.md` and provide:

1. selected type route and license notes
2. complete type scale and roles
3. signature motif with timing/progress rules
4. per-component motion table
5. Arabic/English behavior when applicable
6. mobile, no-font, and reduced-motion fallbacks
7. performance budget and acceptance tests

## Evidence base

- MDN variable fonts: https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts
- MDN `font-variation-settings`: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variation-settings
- Exat Microsite: https://tympanus.net/codrops/2026/04/10/the-exat-microsite-pushing-a-typography-showcase-to-new-creative-extremes/
- Stefan Vitasović Portfolio: https://tympanus.net/codrops/2025/03/05/case-study-stefan-vitasovic-portfolio-2025/
- LO2S: https://tympanus.net/codrops/2025/09/19/lo2s-x-snp-dashdigital-designing-a-website-full-of-movement-and-energy/
