---
name: direct-immersive-color-light
description: Direct cinematic color, light, depth, texture, and palette transitions as a narrative system across DOM, video, WebGL, 3D, and scroll states. Use for immersive or Awwwards-level websites, color-scripted scrollytelling, dynamic themes, shader lighting, atmospheric gradients, product worlds, luxury/editorial art direction, palette selection, or projects where static color tokens are insufficient and the visual atmosphere must evolve over time while preserving contrast and brand recognition.
---

# Direct Immersive Color and Light

Treat color as narrative state and light as composition—not as decoration layered after layout.

## Create the deck first

Produce 3–4 clearly different Colors & Fonts routes before writing code. Use `references/color-light-deck.md`.

Use `immersive-web-token-vault` to seed or sanity-check routes against source-cited award-site tokens, then transform those observations into an original brand-specific system.

Each route must include:

- concept name and emotional promise
- base, surface, foreground, muted, accent, signal, and material colors
- warm/cool bias and tinted black/white endpoints
- gradient or light recipe with exact stops
- texture/grain/material behavior
- typography pairing and one-line justification
- hero, content, conversion, and footer mock states
- contrast evidence over the worst moving background frame
- CSS and WebGL token mapping

Do not default to generic black-and-gold luxury, neon-on-black cyberpunk, pure `#000`, or pure `#fff`. Derive the palette from the concept and brand.

For Karim's projects, stop after the deck and obtain a route selection before production code.

## Build a color script

Map the emotional arc to 4–7 visual states:

```text
arrival → orientation → tension → reveal → proof → conversion → afterimage
```

For each state define:

- background and foreground tokens
- dominant hue and accent allowance
- key-light direction, softness, and temperature
- rim/emission color and intensity
- fog/atmosphere density
- material roughness/metalness or CSS texture equivalent
- transition mechanism and duration/progress range
- contrast-safe text zone
- mobile/static fallback

Use quiet states between chromatic peaks. One accent should remain scarce enough to retain meaning.

## Connect DOM and 3D

Define shared semantic tokens rather than separate palettes:

```text
--color-world-bg
--color-surface
--color-text
--color-muted
--color-accent
--color-signal
--light-key
--light-rim
--fog-color
--emission-color
--grain-opacity
```

- Update tokens from a normalized scene progress value.
- Use perceptual interpolation where available; avoid muddy midpoint colors.
- Keep text as readable DOM above moving canvases.
- Ensure the canvas, poster fallback, OG image, and loading state share the same art direction.
- Treat grain, bloom, blur, and chromatic aberration as measured materials, not premium stickers.

## Contrast and accessibility

- Test text contrast on the brightest and darkest animation frames, not a hand-picked still.
- Provide a stable scrim or text-safe region when media cannot guarantee contrast.
- Do not encode state by hue alone; pair color with label, shape, motion, or position.
- Under reduced motion, move directly between stable palette states or use a short crossfade.
- Check high-contrast/forced-colors behavior and preserve visible focus rings.

## Performance boundaries

- Prefer CSS gradients and static textures when they deliver the concept.
- Animate compositor-friendly layers; avoid large full-screen filters on low-end mobile.
- Cap bloom, postprocessing passes, canvas DPR, and dynamic lights.
- Use compressed textures and a poster fallback for heavy worlds.
- Pause animated light and noise when off-screen or the tab is hidden.

## Required deliverable

1. 3–4 route deck
2. selected semantic token system
3. color/light script by scene
4. DOM ↔ WebGL mapping
5. texture and material rules
6. contrast evidence
7. mobile, reduced-motion, loading, and fallback states

## Quality gate

- A grayscale screenshot still has clear hierarchy.
- The palette is recognizable without the logo.
- The accent has a defined job and usage ceiling.
- Every atmospheric change supports an emotional or content beat.
- The conversion area is calmer and clearer than the spectacle preceding it.

## Evidence base

- Frequency Breathwork: https://tympanus.net/codrops/2025/12/29/frequency-breathwork-translating-the-invisible-rhythm-of-breath-into-digital-form/
- KODE Immersive: https://tympanus.net/codrops/2025/06/16/inside-the-frontier-of-ai-webxr-real-time-3d-crafting-kode-immersive/
- The Spark: https://tympanus.net/codrops/2026/01/09/the-spark-engineering-an-immersive-story-first-web-experience/
- Troa 25 Folio: https://tympanus.net/codrops/2025/03/28/case-study-troa-25-folio/
