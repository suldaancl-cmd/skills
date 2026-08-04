# Gradients, spacing & radius — from award-winning sites

Source: `skillui` static analysis, 2026-07-13.

## The honest gradient finding

skillui inspected 15 award/benchmark sites. On **essentially every one** it reported *"solid colors only — no gradient backgrounds."* This is a real signal, not a gap in the tool:

**Award-tier design leans on solid, restrained palettes. It does not lean on CSS gradients.** When these sites *do* show atmospheric color blends (Igloo, Lusion, Zajno), that depth is produced in **WebGL/shaders** — animated noise fields, fluid simulations, volumetric light — not `linear-gradient()`. A flat CSS gradient behind a hero is, if anything, a tell of a *non*-award build.

So this file does two honest things:
1. Points you to where premium "gradients" actually come from (shaders).
2. Gives CSS gradient recipes **constructed from the real accent colors** extracted in `palettes.md` — clearly labeled as constructed, for when a subtle CSS gradient genuinely helps (buttons, glows, section fades).

## Where premium gradients actually come from

For the fluid/atmospheric color you see on award sites, reach for a shader, not CSS:
- `ogl-webgl` — full-screen animated gradient/noise hero (tiny, fast).
- `webgl-effect-recipes` — drop-in fluid-cursor / gradient / noise backgrounds.
- `direct-immersive-color-light` — color *scripted over scroll* (palette that evolves scene to scene).
- `react-postprocessing` — Bloom over a dark scene reads as a glow-gradient without any gradient.
- `shader-dev` — write the mesh-gradient / flowmap yourself.

A mesh gradient (Stripe-style) is a shader interpolating 3–4 color points across a plane — do it in `ogl-webgl` with the accent hexes from `palettes.md`, not as a static PNG.

## Constructed CSS gradients (built FROM extracted accents)

Not extracted from the sites — *synthesized* from their real accent hexes so they stay on-brand with the source aesthetic. Use sparingly (button sheens, focus glows, subtle section transitions).

```css
/* Lusion electric-blue focus glow (from #0016ec) */
--glow-lusion: radial-gradient(120% 120% at 50% 0%, #1a2ffb 0%, #0016ec 45%, transparent 70%);

/* Serious Business candy sheen (from #ff7ec4 / #c3abff) */
--sheen-serious: linear-gradient(135deg, #ff7ec4 0%, #c3abff 100%);

/* Studiogusto coral CTA (from #ff4e4d) */
--cta-gusto: linear-gradient(180deg, #ff6a55 0%, #ff4e4d 100%);

/* Hatom acid-neon edge on black (from #c1ff12 / #007e2b) */
--edge-hatom: linear-gradient(90deg, #c1ff12 0%, #007e2b 100%);

/* X-Shack dark-teal atmosphere (from #1c2928 / #000) */
--atmo-xshack: radial-gradient(140% 100% at 50% 0%, #26403d 0%, #1c2928 55%, #000 100%);

/* Warm quiet-luxury paper fade (from Exo Ape #ffffff / #e4e0db) */
--paper-exoape: linear-gradient(180deg, #ffffff 0%, #e4e0db 100%);
```

Rule: a CSS gradient should be **barely perceptible** (two near-neighbors) OR clearly a deliberate brand device (Serious Business candy). The muddy mid-saturation 45° gradient is the thing to avoid.

## Spacing tokens (real, extracted)

The grid is remarkably consistent across the set:

| Base grid | Sites |
|---|---|
| **4px** | Clear Street, Design Embraced, Dorst&Lesser, funkhaus, Hatom, Igloo, Lusion, Scout Motors, Serious Business, Umault, Unseen (11/15 — the default) |
| **5px** | Studiogusto, X-Shack |
| **10px** | Exo Ape |

Takeaway: **commit to a 4px base grid** and use multiples (4, 8, 12, 16, 24, 32, 40, 48, 64). Exo Ape's 10px grid with a big jump scale (15/30/60/120) is the exception that produces its airy feel.

## Border-radius tokens (real, extracted)

Two dominant strategies:
- **Small + consistent:** `8px` everywhere (Design Embraced, Igloo, Studiogusto, Umault, Zajno).
- **Pill / full-round:** `100%` and large pills (`50px`, `100px`, `180px`) for buttons and media (Exo Ape, Lusion, Unseen, funkhaus, X-Shack).

Takeaway: pick ONE radius language — tight 8px *or* pills/circles. The extracted sites never mix a fussy 4-value radius scale; they commit.

## Motion density (real, extracted)

skillui flagged motion intensity: **expressive** on funkhaus, Hatom, Scout Motors; **none detected** (from static CSS) on the rest — because their motion lives in JS/WebGL, invisible to CSS analysis. Absence here means "not in CSS," not "no motion." For the motion layer, pair this vault with `gsap-scrolltrigger`, `lenis-smooth-scroll`, and `choreograph-scroll-stories`.
