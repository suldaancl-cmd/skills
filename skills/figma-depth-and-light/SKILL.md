---
name: figma-depth-and-light
description: >
  Premium depth, light, and material in Figma — layered soft shadow elevation systems,
  glassmorphism (background blur + low-opacity surface + lit 1px border), inner-shadow
  lit edges, colored (not pure-black) shadows, ambient+key light logic, and dark-mode
  depth via surface lightness. Use whenever a Figma surface needs to feel three-
  dimensional, lit, glassy, or layered instead of flat. Triggers: "add depth in Figma",
  "shadows / elevation", "glassmorphism / frosted glass", "make this less flat", "premium
  card depth", "blur panel", "neumorphism". Load with `figma-use` (effects via use_figma)
  and after `premium-design-laws`. The cure for Karim's rejected "flat cards" look.
disable-model-invocation: false
---

# Figma Depth & Light

Flat-card-on-dark-panel is the look Karim explicitly rejected as "so bad." Depth is how you fix it — but depth done with one harsh drop shadow is just as cheap. Premium depth imitates real light: soft, layered, colored, directional.

## Elevation = layered soft shadows (never one harsh drop)

Real objects cast more than one shadow. An elevation system stacks 2–3 shadows per level:
- A **tight, darker** shadow close to the element (contact).
- A **wider, softer, lighter** shadow further out (ambient).
- Optionally a very wide, very faint one for high elevations.

Define levels as a system (`elevation/1…5`); higher level = larger blur + larger Y-offset + slightly more total opacity. Save as effect styles so cards, modals, menus pull from the same ladder.

Rule of thumb per level: Y-offset ≈ blur × 0.5; opacity goes *down* as blur goes *up* (big soft shadows are faint). Spread usually 0 or slightly negative.

## Color in shadows (the expensive tell)

Pure-black shadows (`#000`) look cheap and muddy on color. Tint the shadow toward the background's hue or a deep cool/warm neutral, and use opacity rather than grey. On a colored surface, the shadow should carry a hint of that color's deep shade. This one change reads instantly more premium.

## Lit edges (inner shadow as highlight)

A 1px **inner shadow** in white at low opacity on the top edge makes a surface look lit from above — buttons, cards, inputs gain a subtle bevel without skeuomorphism. Pair a faint top highlight with the drop shadow below for a real "object in light" feel.

## Glassmorphism (done right)

Frosted glass is premium when restrained:
- **Background blur** (layer blur on the backdrop) — the frost.
- **Low-opacity surface fill** (8–20%) over it — usually white in light mode, a light tint in dark mode.
- **1px border** with a subtle top-lit gradient (lighter at top) — the glass edge catching light.
- A faint inner highlight + soft outer shadow for lift.
- Needs something textured/colorful *behind* it to refract — glass over flat color is pointless. Pair with a `figma-shader-recipes` fill behind.

## Ambient + key light logic

Pick one light direction (usually top, slightly left) and keep it consistent across the whole file — highlights on top, shadows below. Inconsistent light direction is a subconscious "amateur" signal. Brighter/larger highlight = stronger key light; soft fill on the opposite side = ambient.

## Dark-mode depth (shadows barely read — use lightness)

On dark backgrounds, drop shadows are nearly invisible. Convey elevation with **surface lightness** instead: higher elevation = lighter surface (`surface` → `surface-raised` → lighter still). Keep a faint shadow for separation, but lightness does the lifting. Add a subtle top border-highlight to catch the implied light.

## Mechanics (via use_figma)

- Effects: `DROP_SHADOW`, `INNER_SHADOW`, `LAYER_BLUR`, `BACKGROUND_BLUR` — set `color` (RGBA, tinted not pure black), `offset {x,y}`, `radius`, `spread`.
- Stack multiple effects on one node for layered elevation.
- Save as **effect styles** (`elevation/1…5`, `glass`) for reuse; bind surface colors to variables (`figma-color-systems`).
- Read `figma-use/references/plugin-api-patterns.md` for effect shapes.

## Anti-patterns

- One harsh `#000` drop shadow at high opacity (the flat-card tell).
- Pure-black shadows on colored/dark surfaces; uniform shadow on everything (no elevation hierarchy).
- Inconsistent light direction across the file.
- Glass over flat color (nothing to refract); blur used everywhere until it's mush.
- Relying on drop shadows for elevation in dark mode instead of surface lightness.

## Pairs with

`figma-immersive-premium` (router) · `figma-shader-recipes` (texture behind glass; glow) · `figma-color-systems` (tinted shadows + surface tokens) · `figma-component-craft` (elevation/effect styles on components) · local `refactor-ui-08-use-shadows-appropriately`.
