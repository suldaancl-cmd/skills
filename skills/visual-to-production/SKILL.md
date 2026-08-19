---
name: visual-to-production
description: Reconstruct AI-generated UI images, PNGs, JPEGs, screenshots, or concept renders into editable semantic Figma designs, define motion, and implement production code for Expo/React Native or React/Next.js. Use for image-to-Figma, screenshot-to-code, Figma-to-code, Lottie, Rive, Reanimated, Remotion, or full visual-fidelity delivery. Do not use for ordinary photo editing or a minor copy-only change to an existing design.
compatibility: Requires image inspection. Figma stages require a supported Figma MCP connection with write access. Code stages require a local project workspace.
metadata:
  version: 1.0.0
  owner: ASSALA AISTUDIO LTD
---

# Visual to Production

Turn a visual reference into a semantic, editable, animated, production-ready product. Preserve the approved visual direction without pretending that pixels contain recoverable layers.

## When to use

- The user has AI-generated UI images or screenshots and wants editable Figma.
- The user wants the same visual design implemented in Expo/React Native, React, or Next.js.
- The user asks how to route motion among Figma, Reanimated, Rive, Lottie, Remotion, CSS, Motion, GSAP, or 3D.
- A Figma file contains flattened screenshots, weak structure, or motion that cannot be handed off reliably.
- A design and implementation must be compared against a visual source of truth.

## Do not use

- Ordinary photo retouching, illustration generation, or unrelated video editing.
- A small text or color change when the existing Figma design is already semantic.
- Claims that a PNG can be losslessly reverse-engineered into its nonexistent original layers.

## Non-negotiable rules

1. Treat every raster reference as visual evidence, never as recovered source structure.
2. Never place a full-screen screenshot in Figma or code and call it an editable implementation.
3. Rebuild semantic UI as live text, frames, auto layout, variables, components, and runtime controls.
4. Keep raster or rendered art only where it is genuinely artwork: photographic backgrounds, textures, complex illustrations, or pre-rendered 3D.
5. Separate reference truth, design truth, motion truth, and runtime truth. Do not claim one artifact automatically represents all four.
6. Start with one golden screen unless the user explicitly authorizes batch execution.
7. Preserve the approved art direction. Do not simplify, modernize, restyle, or substitute a generic design system without permission.
8. Never trust generated text, logos, Arabic, Quranic text, numbers, legal copy, or brand marks. Replace with verified live content and licensed assets.
9. Do not overwrite an important Figma page or code path without resolving the exact target and preserving a recoverable copy.
10. Verify by rendering the result. Passing typecheck or visually inspecting layer names is not sufficient.

## Required inputs

Resolve only inputs that materially affect the result:

- Reference images and which one is authoritative if they conflict.
- Target platform: Expo/React Native, web, or both.
- Target viewport/device and supported responsive range.
- Required locales and directionality, especially Arabic RTL and English LTR.
- Existing Figma file/page or permission to create a new working file.
- Existing repository and component library, if code is requested.
- Whether the request is audit-only, reconstruction, motion, implementation, or the full pipeline.

If several are missing, proceed with documented provisional defaults when reversible. Ask before a choice that would materially change the architecture or destroy existing work.

## Operating model

Use these artifacts as separate sources of truth:

| Artifact | Owns |
|---|---|
| Reference board | Approved visual direction and composition |
| Figma | Editable layout, components, tokens, content, responsive intent, and prototype preview |
| Motion specification | States, triggers, timings, easing, interruption, gestures, sensors, data bindings, and reduced motion |
| Runtime code | Product behavior, accessibility, localization, data, device APIs, and performance |
| Lottie/Rive assets | Isolated reusable animation only |
| Remotion project | Rendered video, promo, tutorial, or product demo |
| QA report | Evidence that design, motion, and behavior meet acceptance criteria |

Read `references/pipeline.md` before a full end-to-end task. Read `references/routing-matrix.md` before selecting a motion or asset technology.

## End-to-end procedure

### 1. Protect and inspect

1. Confirm the task scope and whether writes are authorized.
2. Preserve originals. In Figma, work in a duplicate file, duplicate page, or clearly named working section unless the user explicitly requests an in-place change.
3. Inspect every reference at full resolution. Remove or exclude viewer chrome, device mockup borders, watermarks, editor controls, and accidental black bars.
4. Record conflicts, unreadable content, uncertain assets, and assumptions.
5. Inspect the existing design system and codebase before creating replacements.

### 2. Build a reference contract

1. Fill `assets/project-brief.yaml`.
2. Declare the reference hierarchy: primary screen, secondary style references, content reference, and behavior reference.
3. Define what must match exactly and what may be interpreted.
4. Define measurable acceptance criteria before reconstruction starts.
5. Select one golden screen representing the hardest combination of art, UI, localization, and motion.

### 3. Decompose the image

Classify each region as one of:

- `ART_RASTER`: photography, texture, complex generated environment, or pre-rendered 3D.
- `ART_VECTOR`: logo, icon, ornament, or illustration that should remain vector.
- `UI_SEMANTIC`: text, control, navigation, card, form, list, modal, or reusable component.
- `DATA_GRAPHIC`: waveform, chart, compass, progress, map, or sensor-driven visual.
- `MOTION_ONLY`: particles, glints, parallax layer, reveal mask, or transition artifact.
- `UNKNOWN`: needs clarification or a documented approximation.

Create an asset manifest and layer plan. Do not proceed while critical regions remain silently classified as `UNKNOWN`.

### 4. Reconstruct the golden screen in Figma

Invoke `reference-image-to-figma` or follow its procedure.

Minimum structure:

- A locked original reference and cropped clean reference.
- Semantic live text.
- Auto layout for stacks, lists, navigation, and controls.
- Variables for color, spacing, radius, typography, elevation, opacity, and motion tokens.
- Components and variants for interactive UI.
- Explicit RTL/LTR behavior.
- Separate assets for background art and foreground UI.
- Named states and screen variants.
- No rasterized button labels, navigation labels, input fields, Quranic copy, or live data.

Render the Figma golden screen and compare it with the reference before scaling.

### 5. Define motion

Invoke `figma-motion-to-runtime` or follow its procedure.

For every meaningful movement, define:

- Purpose and user benefit.
- Trigger and source state.
- Target state.
- Duration, delay, easing, spring values, or continuous mapping.
- Interruption and reversal behavior.
- Gesture, audio, sensor, scroll, route, or data binding.
- Reduced-motion fallback.
- Runtime owner: Reanimated, Rive, Lottie, web motion, 3D runtime, or Remotion.

Figma motion is a preview and specification unless the chosen runtime can consume the exported artifact faithfully.

### 6. Implement production code

Invoke `figma-to-production-code` or follow its procedure.

1. Inspect the repository, architecture, package manager, navigation, styling, state management, localization, and existing components.
2. Map Figma components and tokens to code before writing screens.
3. Reuse existing production components when they meet the visual contract.
4. Implement real interactions, states, accessibility, localization, and device APIs.
5. Keep decorative assets separate from semantic UI.
6. Use absolute positioning only for intentional art composition or overlays, not as a substitute for responsive layout.
7. Implement the golden screen first, run it, and obtain a real screenshot.

### 7. Verify and iterate

Invoke `visual-fidelity-qa` or follow its procedure.

Run all applicable checks:

- Reference versus Figma render.
- Figma render versus runtime screenshot.
- Runtime behavior versus motion specification.
- Arabic RTL and English LTR.
- Small, target, and large viewports.
- Font scaling, keyboard, safe areas, and content overflow.
- Reduced motion and accessibility semantics.
- Interaction states and real data states.
- Performance on target-class hardware.

Report evidence, discrepancies, severity, and next action. Never report “pixel perfect” without a render comparison.

### 8. Scale only after approval

After the golden screen passes:

1. Extract and stabilize tokens and components.
2. Add Code Connect or a component map when supported.
3. Expand screen-by-screen using the same gates.
4. Re-run QA for every new screen and shared component change.
5. Maintain a decision log so agents do not reinvent earlier decisions.

## Stage gates

Do not advance when a blocking gate fails:

- `G0 Reference`: source rights, crop, viewport, locale, content, and hierarchy are known.
- `G1 Decomposition`: every visible region has an implementation class and owner.
- `G2 Figma`: no semantic UI is flattened; layout, variables, components, and states are valid.
- `G3 Motion`: every movement has a runtime owner and reduced-motion behavior.
- `G4 Code`: the app runs with real controls, content, data boundaries, and accessibility.
- `G5 Fidelity`: render comparison and behavior checks meet the agreed threshold.
- `G6 Scale`: golden screen approved; shared primitives are stable enough to reuse.

## Completion contract

For a full-pipeline request, deliver:

1. Reference and assumption report.
2. Asset manifest and layer plan.
3. Editable Figma golden screen and component inventory.
4. Design token export or documented token map.
5. Motion specification and technology decisions.
6. Production implementation with assets and dependency rationale.
7. Visual and functional QA report with evidence.
8. Remaining uncertainties and explicit non-goals.

## Common edge cases

- **Unclear generated text:** use verified supplied copy or placeholders clearly marked for replacement. Never invent scripture or legal content.
- **Complex glass or 3D impossible with native effects:** preserve the art portion as optimized background layers while rebuilding controls and text semantically. Document the boundary.
- **Conflicting references:** ask which reference owns composition, style, content, and behavior; do not average them silently.
- **Missing Figma write tools:** produce the decomposition, Figma build specification, assets, and code plan; clearly state that no Figma mutation occurred.
- **Existing weak design system:** audit it first. Extend valid primitives and isolate incompatible legacy work rather than deleting it without authorization.
- **Batch request without a golden screen:** explain the risk, propose the hardest representative screen, and proceed in batch only if the user confirms.
- **Image-only motion concept:** infer a proposed motion plan but label every inferred behavior and request approval before implementation.

## Example

**Request:** “Use these three generated mobile screens as the exact visual direction. Make real Figma, animate the compass and recording waveform, then build Expo React Native in Arabic and English.”

**Expected execution:**

1. Select the compass screen as the golden screen.
2. Classify architecture and foliage as layered art, compass parts as data graphics, and controls/text/navigation as semantic UI.
3. Rebuild the screen in Figma with variables, auto layout, live Arabic/English text, and component states.
4. Specify sensor smoothing and compass rotation for Reanimated, waveform behavior for runtime rendering, and optional isolated Rive/Lottie decoration.
5. Implement and run the Expo screen.
6. Compare reference, Figma, and runtime captures; fix blocking deltas.
7. Wait for golden-screen approval before scaling to the remaining screens.

