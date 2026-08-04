---
name: papaya-smoke-hero
description: Build a cinematic dark-luxury hero section that combines an interactive WebGL fluid-smoke background with a McLaren-papaya / Lando Norris racing aesthetic — papaya orange, anthracite black, cyan accents, broadcast-style condensed typography, telemetry HUD microcopy, snappy GSAP entrance. Trigger on requests for "smoke hero", "fluid hero animation", "lando-style landing page", "mclaren hero", "papaya hero", "racing landing page", "f1 hero", or any cinematic dark hero with smoke/vapor/plume motion. Produces a complete vanilla HTML/CSS/JS scaffold (no build step).
---

# Papaya Smoke Hero

Cinematic hero scaffold = WebGL fluid smoke (Pavel Dobryakov's Navier-Stokes sim, MIT) + McLaren / Lando Norris broadcast aesthetic + GSAP intro. Vanilla HTML/CSS/JS, all libs from CDN.

## When to invoke

Any request for a dark, atmospheric hero with reactive smoke OR an F1 / racing / Lando / McLaren-themed landing page. Specifically:

- "smoke hero", "fluid hero animation", "vapor / plume hero"
- "make me a hero like xshack.app but in racing colors"
- "lando norris style landing page", "mclaren hero", "f1 brand site"
- "dark cinematic hero with motion"

If the request is **only** about the shader (no aesthetic specified), still use this skill — the user can override the palette via the design tokens.

## Tech stack

| Library | Version | Purpose |
|---|---|---|
| Pavel Dobryakov fluid sim | bundled | WebGL smoke shader |
| GSAP | 3.12+ | Timelines |
| ScrollTrigger | 3.12+ | Pin + scrub on scroll |
| SplitType | 0.3.4 | Word-by-word headline reveal |
| Lenis | 1.0+ | Smooth scroll |

All loaded via jsDelivr — no `npm install` required.

## Design tokens — Lando / McLaren palette

| Token | Hex | Use |
|---|---|---|
| `--papaya` | `#FF8000` | Primary action, accent line, halo, CTA |
| `--papaya-bright` | `#FF9933` | Hover state |
| `--lando-cyan` | `#47C7FC` | Secondary accent (Lando's helmet blue) |
| `--ink` | `#0A0A0A` | Page background |
| `--carbon` | `#1A1A1A` | Card / surface |
| `--graphite` | `#2D2D2D` | Border / divider |
| `--bone` | `#F5F1E8` | Body text on dark |
| `--white` | `#FFFFFF` | Headline |

## Typography

- **Display**: Druk Wide Bold (or `"Arial Black", "Helvetica Neue"` fallback). Uppercase. Letter-spacing `-0.025em`. Line-height `0.86`.
- **Body**: Inter / IBM Plex Sans / system sans.
- **Telemetry / mono**: JetBrains Mono / IBM Plex Mono — uppercase, tabular figures, `letter-spacing: 0.18em–0.32em` for HUD labels (`SECTOR 03`, `LAP 12/58`, `RPM 12,400`).

## Motion vocabulary

- **Entrance**: `expo.out`. Headline split into words → `gsap.from(words, { yPercent: 110, stagger: 0.05, duration: 1.0 })`.
- **Accent line**: `scaleX: 0 → 1`, `transformOrigin: left`, `duration: 1.1`, `expo.out`. This single moving papaya bar is the brand signature — never skip it.
- **Telemetry counter**: `gsap.to(obj, { v: 12, duration: 2.2, ease: 'power2.out', snap: { v: 1 } })`.
- **Scroll**: pin `.hero`, scrub `.hero-inner` opacity 1→0 + y -60 over `start: 'top top', end: 'bottom 30%'`.
- **Forbidden**: bouncy elastic / back eases (off-brand for racing). No spring physics.

## Workflow

1. **Confirm copy** with the user: headline (uppercase, 2–3 lines), subhead (≤ 24 words), CTA label (default `ENTER`), and optional telemetry string (e.g. `SECTOR 03 · BRAKE POINT`).
2. **Copy assets** from this skill folder into the target directory:
   - `smoke.js`
   - `template.html` → rename to `index.html`
   - `style.css`
   - `main.js`
3. **Replace placeholders** in `index.html`:
   - `__HEADLINE__` (use literal `<br>` for line breaks)
   - `__SUBHEAD__`
   - `__CTA__`
   - `__TELEMETRY__`
4. **Serve and verify**: `python -m http.server 5180` (or any static server). In a browser, confirm:
   - Smoke trails follow the cursor
   - Headline reveals word-by-word on load
   - Papaya accent line scales in
   - HUD telemetry counter ticks 00 → 12
   - No console errors
5. If the agent has `preview_*` tools, use the verification workflow — pixel-sample the canvas to confirm the shader paints (a real-mouse-trail screenshot may JPEG-compress to near-black; sample with `toDataURL` or `getImageData` after `drawImage(canvas, 0, 0)` for proof).

## Tuning knobs

In `smoke.js`, top of file:

```js
let config = {
  TEXTURE_DOWNSAMPLE: 1,        // 2 on mobile for perf
  DENSITY_DISSIPATION: 0.985,   // lower → smoke fades faster
  VELOCITY_DISSIPATION: 0.99,   // lower → motion stops faster
  PRESSURE_DISSIPATION: 0.8,
  PRESSURE_ITERATIONS: 25,      // 15 on mobile
  CURL: 30,                     // higher → more turbulent swirls
  SPLAT_RADIUS: 0.005,          // plume size
};
```

The papaya color palette for splats is defined further down in `smoke.js` — the `PAPAYA_PALETTE` array. Replace those vec3 entries to re-tint the smoke.

## Variants

- **Cyan/blue (Lando-helmet) variant**: swap `--papaya` for `--lando-cyan` on the accent line and CTA. Re-weight `PAPAYA_PALETTE` toward cyan.
- **Senna McLaren-red variant**: replace `#FF8000` with `#E10600` (Ferrari red) — but warn the user this drifts off-Lando-brand.
- **Static (low-power) variant**: drop `smoke.js` entirely and replace `<canvas>` with a still smoke photo + the rest of the GSAP intro intact.

## Files in this skill

| File | Purpose |
|---|---|
| `SKILL.md` | This file |
| `smoke.js` | Papaya-tinted WebGL fluid sim |
| `template.html` | HTML scaffold with placeholders |
| `style.css` | Palette + typography |
| `main.js` | GSAP intro + Lenis + SplitType + auto-seed |

## License

`smoke.js` is derived from PavelDoGreat/WebGL-Fluid-Simulation (MIT). Keep the license header intact in production builds.
