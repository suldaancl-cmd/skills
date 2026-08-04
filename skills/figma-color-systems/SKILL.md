---
name: figma-color-systems
description: >
  Build a complete, semantic COLOR system natively in Figma using variables — primitive
  ramps (50–950), semantic aliases (bg/surface/border/text/accent/cta/states), light +
  dark modes via variable modes, and WCAG-checked contrast. Use whenever a Figma file
  needs a real palette/token system rather than scattered hex values, or when adding dark
  mode, accent ramps, or state colors. Triggers: "color palette in Figma", "color
  variables/tokens", "dark mode in Figma", "semantic colors", "accent ramp", "fix
  contrast", "set up the palette". Load with `figma-use` (variables are created via
  `use_figma`) and after `premium-design-laws`. Pair with local `color-expert` /
  `color-system` to choose the hues; this skill structures them in Figma.
disable-model-invocation: false
---

# Figma Color Systems

A premium file has a color *system*, not colors. The system is two layers of variables: raw **primitives** (the ramp) and **semantic** aliases (what a color means). Components bind only to semantics — so the brand moves in one place and dark mode is a mode switch, not a re-paint.

## Layer 1 — primitive ramps

For each hue in the palette (neutral, accent, plus any secondary), build a ramp as color variables:
- Steps: `50 100 200 300 400 500 600 700 800 900 950`. 500 is the base; below = tints, above = shades.
- Keep perceptual evenness — equal *visual* steps, not equal hex math (lean on `color-expert` / OKLCH thinking).
- Neutrals: give them a subtle temperature (slightly warm or cool, often a hint of the accent hue) — pure greys read sterile.

Name them `color/neutral/700`, `color/accent/500`, etc. These are never used directly in designs.

## Layer 2 — semantic aliases

Create a second collection of variables that *alias* the primitives. These are what everything binds to:
- `bg` (page), `surface` (cards/panels), `surface-raised`, `border`, `border-strong`
- `text`, `text-muted`, `text-inverse`
- `accent`, `accent-hover`, `cta`, `cta-text`
- states: `success`, `warning`, `danger`, `info` (+ their `-bg` softer variants)

Each semantic = a reference to a primitive step (e.g. `text` → `neutral/900` in light mode).

## Light + dark via variable modes

Put the semantic collection on **two modes**: `Light` and `Dark`. Same variable names, different primitive references per mode:
- Light: `bg`→`neutral/50`, `surface`→`white`, `text`→`neutral/900`, `border`→`neutral/200`.
- Dark: `bg`→`neutral/950`, `surface`→`neutral/900`, `text`→`neutral/50`, `border`→`neutral/800`.
- Accents usually shift too — dark mode often wants a slightly brighter/desaturated accent to hold contrast.

Now switching a frame's mode reskins the whole design. This is the payoff of the two-layer structure.

## Contrast (non-negotiable)

- Body text vs its background: aim AA (4.5:1) minimum, AAA (7:1) where you can.
- CTA text vs CTA fill: AA minimum — premium-design-laws calls this out specifically.
- Don't rely on accent-on-accent; check muted text and borders too (borders failing contrast = invisible structure).
- Verify after building, per mode.

## Mechanics (via use_figma)

- Create a variable **collection** per layer; add **modes** to the semantic collection.
- Create `COLOR` variables; for semantics, set the value as an **alias** to the primitive variable (not a raw color) so the indirection holds.
- Bind fills/strokes/text to the semantic variables — never hardcode hex on a layer.
- Read `figma-use/references/variable-patterns.md` for collection/mode/alias creation patterns.

## Anti-patterns

- One flat list of named colors with no primitive/semantic split (brand can't move; dark mode means re-painting).
- Pure-grey neutrals; 60+ ad-hoc colors; accent bloat (premium-design-laws: one disciplined accent system).
- Hardcoded hex on layers instead of variable bindings.
- Dark mode built as a separate file/page instead of a mode.
- Shipping without a contrast pass.

## Pairs with

`figma-immersive-premium` (router) · `figma-gradient-systems` / `figma-shader-recipes` (gradients bind to these variables) · `figma-typography-systems` (the other half of the token system) · local `color-expert`, `color-system`, `design-token`.
