---
name: figma-motion-to-runtime
description: Turn static or animated Figma designs and image-based motion concepts into an executable motion specification and production animation using Reanimated, Gesture Handler, Rive, Lottie, web motion, 3D runtime, or Remotion. Use for app transitions, gestures, compass/sensor motion, audio waveforms, microinteractions, interactive illustrations, or product videos. Do not use Lottie or video as a replacement for semantic full-screen UI.
compatibility: Figma motion extraction requires Figma MCP motion tools when available. Runtime implementation requires the target code workspace.
metadata:
  version: 1.0.0
  owner: ASSALA AISTUDIO LTD
---

# Figma Motion to Runtime

Design motion as behavior, not decoration. Assign each animation one runtime owner and preserve semantic UI, live data, localization, accessibility, and performance.

## When to use

- A Figma prototype or timeline must become production motion.
- A static generated UI image implies movement that has not been specified.
- The user asks whether to use Reanimated, Rive, Lottie, Remotion, web motion, canvas, or 3D.
- A sensor, audio input, gesture, route transition, or data stream drives the visual.

## Boundaries

- Do not export a full interactive screen as Lottie, video, or bitmap frames.
- Do not embed localized text, scripture, user data, prices, or live values in decorative animation assets.
- Do not treat Figma prototype playback as production-ready code.
- Do not invent motion as if it were approved. Label inferred motion and obtain approval for material behavior.
- Do not add a new animation library when the repository already has a suitable established stack.

## Required reading

- Read `references/technology-matrix.md` before selecting an engine.
- Read `references/motion-architecture.md` before implementation.
- Fill `assets/motion-spec.yaml` for every nontrivial animation.

## Procedure

### 1. Inspect the static and motion context

1. Inspect the exact Figma node and its rendered appearance.
2. Retrieve static design context first.
3. Retrieve motion/keyframe context recursively when the Figma node contains real animation.
4. Inspect prototypes, variants, interactions, component states, and navigation connections.
5. Identify which behaviors are explicit and which are inferred from a still image.

### 2. Classify each motion

Assign one class:

- `ROUTE`: screen entry/exit, modal, sheet, shared element.
- `STATE`: button, toggle, selection, loading, success, error.
- `GESTURE`: drag, swipe, pinch, rotate, scrub.
- `SCROLL`: parallax, reveal, sticky behavior, progress.
- `SENSOR`: compass, tilt, motion, orientation.
- `AUDIO`: waveform, recording level, speaking state.
- `DATA`: progress, chart, live status.
- `DECORATIVE`: shimmer, sparkle, logo reveal, ambient loop.
- `INTERACTIVE_VECTOR`: stateful illustration or character.
- `THREE_D`: camera/object/material animation.
- `VIDEO`: rendered promo, tutorial, or social output.

### 3. State the purpose

Every animation must serve at least one purpose:

- Explain spatial relationship.
- Confirm user input.
- Communicate system state.
- Direct attention.
- Visualize live data.
- Express brand without blocking usability.

Remove or reduce motion that has no clear purpose, creates latency, or competes with primary content.

### 4. Route to the runtime

Use the existing project stack first. Default routing:

- Expo/React Native UI and navigation: Reanimated.
- Touch interaction: Gesture Handler + Reanimated.
- Interactive vector state machine: Rive.
- Small finite decorative vector sequence: Lottie.
- Custom high-frequency waveform/shader/canvas graphic: existing canvas stack, often Skia or SVG depending complexity.
- Web UI: CSS transitions/animations or the existing Motion/GSAP stack.
- Web 3D: existing Three.js/R3F stack.
- Rendered product video: Remotion.
- Figma Smart Animate/timeline: prototype and handoff evidence.

Do not pick a tool based on novelty. Use `references/technology-matrix.md` for disqualifiers.

### 5. Write the motion specification

For each animation record:

- Stable ID and target layer/component.
- Purpose and classification.
- Trigger.
- From/to states.
- Delay, duration, easing, or spring parameters.
- Animated properties and value ranges.
- Stagger and coordination group.
- Loop behavior and stop condition.
- Interruption, reversal, and re-entry.
- Gesture/sensor/audio/data mapping.
- Reduced-motion fallback.
- Platform differences.
- Runtime owner and asset format.
- Acceptance evidence.

Use real values from Figma motion context when present. If absent, mark values as proposed.

### 6. Prototype in Figma when useful

Use Figma to communicate the transition and validate choreography, not to hide runtime complexity.

- Keep state names aligned with runtime state names.
- Use component variants for discrete states.
- Use timelines/keyframes for coordinated sequences where supported.
- Keep data-driven continuous behavior documented separately.
- Render or export a short approval video when the user needs visual sign-off.

### 7. Implement safely

1. Inspect package versions and existing patterns.
2. Keep animation state close to the owning component.
3. Separate product state from presentation progress.
4. Keep continuous work off the JavaScript thread where the selected runtime supports it.
5. Minimize bridge crossings and unnecessary React re-renders.
6. Make animations cancellable and resilient to rapid repeated input.
7. Handle backgrounding, navigation interruption, permission denial, and stale data.
8. Implement reduced motion before considering the task complete.

### 8. Verify motion

- Record the runtime at a stable frame rate.
- Compare start state, key poses, end state, timing, and easing against the specification.
- Test slow interaction, rapid repeated input, interruption, and reverse navigation.
- Test low-end/target hardware and measure dropped frames where tooling allows.
- Confirm touch targets and accessibility announcements remain correct while animated.
- Confirm text and UI remain live and selectable/announced as appropriate.

## Pattern guidance

### Compass

- Keep the dial or indicator as a runtime layer, not a video.
- Define heading source, calibration, smoothing, shortest-angle interpolation, update frequency, permission fallback, stale-data behavior, and reduced-motion mode.
- Separate decorative Kaaba/arch art from the mathematical heading indicator.

### Recording waveform

- Bind amplitude to live audio when permission is granted.
- Define idle, requesting permission, recording, paused, processing, success, and error states.
- Use a deterministic fallback waveform for previews, never to fake actual recording state.

### Glass and parallax

- Animate transforms and opacity before expensive blur or shadow properties.
- Use a small number of depth layers.
- Clamp sensor movement and disable it for reduced motion.

### Logo and ornament

- Use Lottie for a short deterministic vector reveal when it does not contain dynamic text.
- Use Rive when the ornament responds to user state or input.
- Keep the static fallback asset available.

### Remotion

- Use for exported MP4/WebM demos, onboarding explainers, store previews, and social/video marketing.
- Recreate UI from shared tokens/components when possible; do not make the Remotion composition the runtime application.

## Completion contract

Deliver:

1. Motion inventory.
2. Completed motion specifications.
3. Technology decision with rejected alternatives.
4. Figma prototype/timeline evidence when applicable.
5. Runtime implementation and static fallbacks.
6. Reduced-motion behavior.
7. Video or frame evidence plus performance findings.
8. Known deviations and inferred behaviors awaiting approval.

## Example

**Request:** “Animate the generated Qibla screen and export everything as Lottie.”

**Correct response:** Decompose the request. Keep buttons, labels, location, navigation, and compass data as live UI. Implement compass and interaction in Reanimated with sensor input; optionally use Rive for an interactive decorative center mark; use Lottie only for a small sparkle or logo reveal; use Remotion only if a promotional video is also requested.

