---
name: figma-motion-pipeline
description: The end-to-end pipeline for taking motion out of Figma (Config 2026 Figma Motion + the canvas agent) and shipping it as real code in a website OR a React Native app, driven by Claude through the Figma MCP. Routes each job to the right implementer and explains how Claude reads, authors, and verifies motion via MCP. Use this whenever the user wants to turn a Figma animation into code, asks how Claude controls Figma / generates motion through MCP, mentions Figma Motion / the Figma agent / Config 2026, or needs one animation to work across both apps and sites.
---

# Figma Motion Pipeline

The map for getting motion from Figma into shipped code — for **both sites and apps** — with Claude driving through the Figma MCP. This skill is the router; it hands the actual translation to the deep skills and exists so you pick the right one and understand the whole flow.

## What changed (Figma Config 2026, June 24 2026)

Figma stopped being a static-design tool. The wave that "totally changed" the workflow:

- **Figma Motion** — a real timeline on the design canvas: keyframes, presets, and **agent-assisted** starting points. Exports to **CSS, JSON, React, MP4, WebM, Animated SVG, GIF**.
- **MCP-compatible motion** — instead of a flat screenshot, the Figma MCP hands a coding agent **structured animation context** (`get_motion_context`): keyframe tracks, easing curves, timing, and pre-computed snippets, linked to design nodes by id.
- **Canvas design agent + Skills + Connectors** — Figma's own in-canvas agent now takes **Skills** (packaged team conventions/workflows, like coding-agent skills) and **Connectors** (live context from GitHub, Slack, Notion, Hex, etc. over MCP). So motion can be *authored* by an agent, then *implemented* by Claude.
- **Code Layers** — code living on the design file (early access from July 2026).

The important consequence: **Figma Motion's exports and Claude's existing bridge (`figma-implement-motion`) target React web + SwiftUI. Neither emits React Native.** That's why the app path routes through `react-native-motion`.

## The pipeline

```
Author (human or Figma canvas agent)
        │
        ▼
Claude reads via Figma MCP:
  get_design_context  → structure (layout, styles, data-node-id anchors)
  get_motion_context  → keyframes, easing, timing, snippets, timelineCohorts
        │
        ▼
Route by target ▼
```

| Target | Implementer skill | Output |
|---|---|---|
| **Website** (React) | `figma-implement-motion` | motion.dev (`motion/react`), verbatim snippets |
| **Website** (vanilla / non-React) | `figma-implement-motion` | CSS `@keyframes` |
| **iOS native** (SwiftUI) | `figma-implement-motion` (SwiftUI path) | `.animation(...)` modifiers, hand-translated |
| **App** (Expo / React Native) | **`react-native-motion`** | Reanimated / Moti — the bridge Figma doesn't emit |

`get_design_context` and `get_motion_context` are linked by node id — that linkage is the whole implementation workflow. Don't re-derive the node-merging mechanics here; `figma-implement-motion` owns them and `react-native-motion` reuses them for the RN case.

## How Claude actually drives Figma (MCP surface)

Claude both **reads from** and **writes to** Figma — it's bidirectional now:

- **Read:** `get_design_context`, `get_motion_context`, `get_screenshot`, `get_metadata`.
- **Author / control:** `use_figma` (Plugin API — create/edit nodes; add motion keyframes with `figma-use` + `figma-use-motion`), `generate_figma_design`, `create_new_file`, `upload_assets`.
- **Verify motion:** `get_screenshot` shows only the **resting state** — to see motion, `export_video` (slow/expensive; sample a few frames) or, better for the app case, run the generated code on a device and record it.
- **Preconditions:** the Figma MCP must be connected and the user needs the motion feature flag (`figma-use-motion` bails fast if not). Karim is on a Figma Pro/expert seat, so the full set is unlocked.

## Choosing per project

- **One design, both platforms?** Read the motion **once**, then implement twice — `figma-implement-motion` for the site, `react-native-motion` for the app. The *values* (durations, easing, offsets) stay identical across both so the brand motion feels the same; only the API differs.
- **Immersive static design** (shaders, gradients, depth) is a different axis — that's `figma-immersive-premium` and `figma-shader-recipes`. This skill owns the **time dimension**; those own the surface.
- **Authoring motion inside Figma** (not implementing it) → `figma-use` + `figma-use-motion`.

## Guardrails

- **Preserve the snippet's values exactly** — timing, easing curves, keyframe values. Regenerating from raw tracks loses fidelity on custom beziers and springs.
- **Honor `prefers-reduced-motion`** (web) / `useReducedMotion()` (RN) on everything.
- **Verify before done.** Motion is invisible in code review — sample `export_video` frames or record the running app. State plainly if you couldn't verify.
- **Premium bar.** Motion serves the design system, not the reverse. Keep it earned and intentional (`premium-design-laws`), never motion-for-motion's-sake.
