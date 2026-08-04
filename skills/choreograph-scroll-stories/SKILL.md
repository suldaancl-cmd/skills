---
name: choreograph-scroll-stories
description: Turn content and an immersive concept into a cinematic, scene-by-scene scroll narrative with pacing, normalized progress, state transitions, interaction cues, quiet reading zones, mobile alternatives, reduced-motion behavior, and implementation handoff. Use for scrollytelling, pinned sequences, continuous 3D journeys, scroll-scrubbed video or typography, horizontal chapters, camera paths, narrative landing pages, product reveals, portfolio stories, or any site where scrolling must feel directed rather than a stack of entrance animations.
---

# Choreograph Scroll Stories

Treat scroll as time controlled by the visitor, not as a video timeline forced onto them.

## Route the work

- Start from `direct-immersive-concepts` when the central metaphor is unclear.
- Use `premium-motion-cookbook`, `gsap-scrolltrigger`, and `lenis-smooth-scroll` only after the cue sheet is approved.
- Use `three`, `threejs`, or `react-three-fiber` for camera/scene implementation, not story design.
- Read `references/scroll-cue-sheet.md` and complete it before coding.

## Build the narrative spine

1. Reduce the content to 5–9 beats. Give every beat one job and one emotional state.
2. Mark the change between beats: reveal, approach, collision, expansion, inversion, release, or return.
3. Alternate intensity. After every high-motion beat, provide a quiet reading or exploration zone.
4. Decide which beats are **triggered**, **scrubbed**, **pinned**, or **native-flow**. Do not scrub everything.
5. Assign normalized progress from `0` to `1`; keep layout values in CSS and let animation update progress variables where possible.
6. Allocate more scroll distance to comprehension and exploration, less to simple reveals.

## Use a motion grammar

Choose one primary transition family and at most two supporting families:

- **continuity:** morph, shared object, camera travel, persistent canvas
- **occlusion:** curtain, mask, wipe, foreground pass
- **focus:** blur, depth-of-field, scale, light isolation
- **assembly:** fragments, letters, particles, components converging
- **material change:** color, texture, roughness, shader state, typography axis

Repeat motifs with variation. Do not introduce a new easing, direction, or transition language in every section.

## Design the controller

Represent the experience as explicit scene state:

```text
scene = intro | discovery | tension | reveal | proof | conversion
progress = 0..1 within the active scene
velocity = smoothed signed scroll velocity
capability = full | reduced | static
```

- Keep one source of truth for scroll progress.
- Drive DOM, WebGL, type, and audio from the same normalized state.
- Load only the active scene plus the next scene for heavy experiences.
- Make scene entry/exit idempotent; dispose timers, listeners, media, geometry, and audio nodes.
- Preserve native anchors, focus movement, browser history, and keyboard scrolling.

## Responsive choreography

Do not shrink the desktop timeline. Recompose it.

- Desktop: full spatial choreography and optional smooth scroll.
- Tablet: fewer simultaneous layers and shorter pins.
- Mobile: native flow, shorter travel, static or video fallback for heavy WebGL, no hover dependencies.
- Reduced motion: remove scrubbed transforms, parallax, zoom, camera travel, and smooth-scroll interception; retain short opacity changes and immediate content access.

## Performance boundaries

- Paint meaningful DOM content before initializing heavy canvases.
- Prefer transforms and opacity; batch reads before writes.
- Keep active ScrollTriggers intentionally small; consolidate related sequences.
- Never create a second independent RAF loop when GSAP already owns the ticker.
- Pause off-screen loops and media.
- Test aggressive back-scroll, resize, orientation change, anchor jumps, focus navigation, and route return.

## Required output

Deliver:

1. narrative spine and emotional curve
2. completed scroll cue sheet
3. motion grammar and easing tokens
4. scene/state model
5. desktop, mobile, and reduced-motion choreography
6. asset/loading plan
7. acceptance tests for comprehension, performance, focus, and reversibility

## Quality gate

- Every pinned moment justifies why content cannot remain in normal flow.
- Every scrubbed change is reversible when scrolling backward.
- The visitor can pause and understand the current state.
- Navigation and conversion remain available without completing a theatrical sequence.
- The story still makes sense as a static document.

## Evidence base

- The Spark: https://tympanus.net/codrops/2026/01/09/the-spark-engineering-an-immersive-story-first-web-experience/
- KODE Immersive: https://tympanus.net/codrops/2025/06/16/inside-the-frontier-of-ai-webxr-real-time-3d-crafting-kode-immersive/
- Jitter website: https://tympanus.net/codrops/2025/09/02/a-behind-the-scenes-look-at-the-new-jitter-website/
- Dondre Green: https://tympanus.net/codrops/2025/01/07/case-study-dondre-green/
- Meet Your Legend: https://tympanus.net/codrops/2025/07/17/designing-momentum-the-story-behind-meet-your-legend/
