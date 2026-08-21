---
name: figma-first-app-pipeline
description: 'Binding delivery contract for any app UI, onboarding flow, or animated screen sequence. Forces the order design in Figma, implement real components and images in Figma, author the motion in Figma, then extract to code and prove the match. Load it BEFORE writing any screen code. Use for onboarding flows, motion or animated UI, screenshot-to-app rebuilds, "make it like this reel", or whenever an agent is about to hand-code a screen that was never designed.'
---

# Figma-first app pipeline

## The law

**No screen code is written before its Figma frame and its motion spec exist.**

An agent that skips straight to code produces a screenshot-shaped page: absolute-positioned,
untokenized, unanimated, unlocalized, and impossible to review against anything. This skill exists
to stop that. Five gates, in order, each with an exit test you can point at.

You may run gates one screen at a time. You may not reorder them.

## Gate table

| Gate | Do | Call | Exit test — must be pointable |
|---|---|---|---|
| **G0 SYSTEM** | Lock tokens: color, type, spacing, radius, elevation | `premium-design-laws` → `figma-color-systems` / `figma-typography-systems` | A colors + fonts deck was shown and **Karim picked one**. Tokens exist as Figma variables. |
| **G1 DESIGN** | Lay out every screen in the flow | `onboarding-design` for flow order → `figma-generate-design` or `figma-use` | Every screen exists as a named Figma frame. The count matches the agreed flow. |
| **G2 IMPLEMENT** | Make it real, not a picture | `figma-component-craft` → `figma-use` | Live text, auto layout, components with variants, bound variables, **real images placed**. Zero flattened rasters standing in for UI. |
| **G3 MOTION** | Author motion **inside Figma** | `figma-use-motion` — needs the `metronome_plugin_api` flag, bail fast if absent | A motion spec per screen: what moves, from what, to what, duration, easing, trigger, stagger. |
| **G4 EXTRACT** | Figma → running code | `figma-motion-pipeline` routes it → `figma-to-production-code` + `figma-motion-to-runtime` → `reanimated` / `moti` / `rn-screen-transitions` | The flow runs on a device or simulator. Components use the G0 tokens, not literals. |
| **G5 VERIFY** | Prove it matches | `visual-fidelity-qa` | A pixel diff per screen — overlay, heatmap, MAE — plus RTL, dark mode, reduced-motion, and every data state. |

## Hard rules

1. **Deck first.** G0 does not exit until Karim picks a colors + fonts option. This extends the
   standing deck-first rule; it never replaces it.
2. **A screenshot is a spec, not a mood board.** When the brief arrives as an image, G1 is
   `reference-image-to-figma`, not "look at it and code". Rebuild it editable first.
3. **Motion is authored, not improvised.** If G3 produced no spec, G4 must not invent easing curves
   in code. No spec, no animation — say so and go back.
4. **Never ship a screenshot-shaped screen.** No absolute-positioned pixel layouts, no full-screen
   raster standing in for real UI, no Lottie or video substituting for semantic screens.
5. **Motion runs on the UI thread.** Reanimated/Moti worklets only, never `setState` per frame.
   `react-native-reanimated/plugin` stays LAST in `babel.config.js`; `npx expo start --clear` after
   any babel change. Honor `useReducedMotion()`.
6. **A clean build is not G5.** Compiling proves nothing about fidelity. The diff is the evidence.

## When Figma motion is unavailable

`figma-use-motion` needs the `metronome_plugin_api` feature flag. If it is not enabled, do **not**
silently skip G3 — that is exactly how motion gets improvised. Fall back in this order, and say
which one you used:

1. Write the spec as a table by hand: element, property, from, to, duration, easing, trigger,
   stagger. `micro-interaction-spec` gives the shape.
2. Prototype the transitions with Figma Smart Animate and read the timings off it.
3. Only then hand the table to `figma-motion-to-runtime`.

The deliverable of G3 is **the spec**, not the tool that produced it.

## Reading a reference reel

When Karim shares a design reel and says "like this", extract these five things before designing
anything. `references/worked-example-polle.md` walks a real one end to end.

- The **screen skeleton** that repeats across every frame
- The **hero object** per screen — the element carrying the proof
- What is **shared** across screens (background, chrome) versus what swaps
- The **motion inventory** — entrance only, or layout too? staggered? triggered by what?
- The **accent** — usually exactly one saturated color against neutrals

Detailed per-gate procedure: `references/gates.md`.

## Verifiable done

State which gate you are at. Never claim a later gate's outcome from an earlier gate's evidence.
Report like this: `G4 complete — flow runs on simulator, screenshot attached. G5 not started.`
