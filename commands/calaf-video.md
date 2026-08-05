---
description: Generate a 15s Arabic-first Calaf-branded video composition with Hyperframes V2. Pass a brief; auto-runs lint+validate+inspect.
argument-hint: <brief — e.g. "intro about Hermes 24/7 agents">
---

You are generating a Hyperframes V2 composition for the **Calaf brand**.

## Project location (fixed)

`C:\Users\user\.claude\_projects\hyperframes\` — overwrite `index.html` in place.
Fonts are already downloaded in `fonts/`:
- `ibm-plex-sans-arabic-300.woff2`
- `ibm-plex-sans-arabic-400.woff2`
- `ibm-plex-sans-arabic-700.woff2`

If `C:\Users\user\.claude\_projects\hyperframes\design.md` does not exist, the project is misconfigured — abort and tell the user to run `Skill: hyperframes` setup first.

## Mandatory workflow

1. **Load the hyperframes skill via the `Skill` tool.** Do not skip — the skill carries the non-negotiable scene/transition rules.
2. **Read `design.md`** at the project root. The palette tokens (`bg`, `fg`, `accent`, `accent-2`) are the ONLY colors allowed. Derived alpha variants are fine; new hex values are not.
3. **Plan the 15s composition** using the **BIT 3-scene** rhythm:
   - **Scene 1 (0–4.5s, track 0)** — hero title + Arabic tagline. Slow entrance (700-900ms title slam, staggered subtitle). Fully visible by ~2.5s. Class `clip`.
   - **Scene 2 (4.0–9.5s, track 1)** — content beats. Blur-crossfade entrance at t=4.0s (`filter: blur(22px)` → `0`, sine.inOut, 0.6s). Cards/stats with **120ms stagger**, `power3.out`. Class `clip`.
   - **Scene 3 (9.0–15s, track 2)** — closing + URL `calaf.app`. Push-slide entrance from right (`xPercent: 100 → 0`, power2.inOut, 0.7s). Final fade allowed at 14.4s.
4. **Write `index.html`** following the hyperframes skill's rules verbatim:
   - `<html lang="ar" dir="rtl">`
   - Standalone composition: NO `<template>` wrapper around the root
   - Root: `<div id="root" data-composition-id="main" data-start="0" data-duration="15" data-width="1920" data-height="1080">`
   - Each scene: `class="scene clip"` + `data-start` + `data-duration` + `data-track-index` (different track per scene)
   - Decorative glows that exceed scene bounds: `data-layout-allow-overflow`
   - Scene-3 wrapper: `data-layout-allow-overflow` (slide-in entrance)
   - `.scene-content` fills with `width:100%; height:100%; padding:Npx; box-sizing:border-box` — never `position:absolute; top:Npx`
   - GSAP timeline created synchronously in a `<script>` after the root div:
     ```js
     window.__timelines = window.__timelines || {};
     const tl = gsap.timeline({ paused: true, defaults: { ease: "power2.out" } });
     // ... entrances only via gsap.from / fromTo
     window.__timelines["main"] = tl;
     ```
5. **Hard rules — violating any one breaks the composition:**
   - Entrance animations on EVERY element (`gsap.from` / `fromTo`)
   - Exit animations BANNED on scenes 1 + 2 — the transition IS the exit
   - Final scene only may `gsap.to(opacity:0)` for fade-to-black
   - No `repeat: -1` anywhere
   - No `Math.random()`, `Date.now()`, no async timeline construction
   - No `transparent` keyword in gradients (use bg `#0A0A0F` at 0 alpha)
   - No `<br>` in content text — use `max-width` for natural wrap
6. **Typography:**
   - Display: `font-weight: 700`, `letter-spacing: -0.04em`, 160-220px for hero, 96-140px for headlines
   - Body: `font-weight: 400`, 26-32px, line-height 1.4
   - All Arabic blocks: natural RTL flow, no forced text-align overrides
7. **Run verification** — execute via Bash from the project:
   ```bash
   cd /c/Users/user/.claude/_projects/hyperframes && npm run check
   ```
   This runs `lint` + `validate` (WCAG AA) + `inspect` (9-sample layout audit).
8. **Fix any issues surgically** and re-run until clean:
   - `timed_element_missing_clip_class` → add `class="clip"` to scene divs
   - `container_overflow` on intentional decorative glows → add `data-layout-allow-overflow`
   - `canvas_overflow` from slide-in entrances → add `data-layout-allow-overflow` on the moving element or its scene wrapper
   - WCAG contrast warnings → bump muted text to fg (`#F4E4C1`) at higher alpha (≥0.65)
9. **Verify in the live preview** — if a Hyperframes Studio dev server is running on port 5174, navigate the preview iframe and `tl.time(<hero_t>)` to confirm hero frames render with correct palette. If not running, mention the launch command:
   ```bash
   cd C:\Users\user\.claude\_projects\hyperframes && npm run dev
   ```
10. **Final report to the user (in Arabic with English technical terms):**
    - 3 scene summary (one line each)
    - check results (errors/warnings/issues counts)
    - Render command: `npm run render`

## The brief

$ARGUMENTS

Now: invoke the hyperframes skill, plan the composition for the brief above, and execute the workflow end-to-end. Do not stop until `npm run check` is clean.
