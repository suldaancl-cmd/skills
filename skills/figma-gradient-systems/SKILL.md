---
name: figma-gradient-systems
description: >
  Build premium, EARNED gradients in Figma — linear/radial/angular/diamond paints, mesh
  gradients (via shader fills), grain-over-gradient, and gradient tokens bound to color
  variables. Use whenever a Figma surface needs a gradient that reads expensive instead
  of cheap: hero washes, CTA fills, section atmospheres, glow behind a wordmark, dark
  editorial backgrounds. Triggers: "gradient in Figma", "make this gradient look
  premium/not cheap", "hero background wash", "CTA gradient", "fix banding", "mesh
  gradient", "gradient tokens". Load with `figma-use` (paints are set via `use_figma`)
  and after `premium-design-laws`. For generative mesh/aurora gradients, route to
  `figma-shader-recipes`.
disable-model-invocation: false
---

# Figma Gradient Systems

A gradient is the fastest way to look either premium or amateur. The difference is almost never the tool — it's restraint, color relationship, and finishing. premium-design-laws is explicit: gradients must be **earned** (same-family stops, or motivated by a real reference), never rainbow on headings.

## The premium gradient rules

1. **Same family, not the rainbow.** Stops should share a hue family or move hue by a small amount with a luminance/saturation shift. Big hue jumps (blue→pink→orange) read cheap unless there's a real brand reference for it.
2. **Move luminance, not just hue.** The most expensive gradients are mostly a dark-to-slightly-less-dark (or light-to-slightly-warmer) luminance ramp with a whisper of hue shift.
3. **Anchor to a foundation.** Dark project: start near-black (the `bg` token), drift toward a *desaturated* accent. Light project: start off-white, drift toward a warm or cool tint.
4. **Add grain to kill banding.** Smooth gradients band on real screens. A 2–5% noise/grain layer on top (a shader effect, or a noise fill) dithers it and adds texture. This single move separates premium from default.
5. **Tokenize it.** Save the gradient as a Figma style or bind its stops to color **variables** so the whole system shifts when the brand does.

## Gradient types in Figma and when to use each

- **Linear** — the workhorse. Diagonal (≈105–115°) reads more dynamic than flat horizontal/vertical. Use for hero washes, card surfaces, CTA fills.
- **Radial** — spotlight / focus. Behind a focal element or to vignette toward center. Soft, off-center radials feel organic.
- **Angular (conic)** — sweep / energy. Behind a wordmark, as a loader, or a metallic edge. Easy to overdo.
- **Diamond** — niche framing. Occasional.
- **Mesh (multi-point)** — the premium hero gradient. Figma does this via **shader fills** — route to `figma-shader-recipes`. 3–4 same-family control colors.

## Recipe: the dark premium hero wash

A reliable, expensive-looking default for dark immersive heroes:
- Base: `bg` (near-black, e.g. a deep neutral with a hint of the accent hue).
- Linear ≈110°: stop 1 = `bg`; stop 2 = accent at ~10–15% mixed into `bg` (desaturated, not full accent).
- Optional radial glow layer: low-opacity accent radial behind the focal/CTA area.
- Finishing: 3–4% film grain over the whole frame (shader effect).
- Text on top: ensure contrast stays WCAG-aware; if it dips, deepen the base or add a subtle scrim.

## Recipe: the premium CTA fill

- Two same-family stops with a clear luminance step (lighter top-left → deeper bottom-right) so the button reads slightly 3D.
- 1px inner highlight (inner shadow, white at low opacity, top) for a "lit" edge — see `figma-depth-and-light`.
- Hover variant: shift the stops brighter / rotate the angle slightly. Bind to variables so both states share tokens.

## Mechanics (via use_figma)

- Set paints as `GRADIENT_LINEAR` / `GRADIENT_RADIAL` / `GRADIENT_ANGULAR` / `GRADIENT_DIAMOND` with `gradientStops` (position 0–1, color RGBA) and a `gradientTransform`.
- Bind stop colors to variables where the API allows, or build the gradient as a published color style for reuse.
- For mesh/generative, use shader fills (`figma-shader-recipes`).
- Read `figma-use/references/plugin-api-patterns.md` for the exact paint/gradientTransform shapes.

## Anti-patterns

- Rainbow or complementary multi-stop gradients on headings or large surfaces.
- Pure-saturation gradients (full accent → full second hue) with no luminance logic.
- Smooth gradients with visible banding and no grain.
- Hardcoded hex stops repeated across files instead of a token/style.
- Angular gradients used decoratively everywhere (energy becomes noise).

## Pairs with

`figma-shader-recipes` (mesh/aurora) · `figma-color-systems` (the variables the stops bind to) · `figma-depth-and-light` (lit edges, glow) · local `color-expert` / `color-system`.
