---
name: motion-primitives
description: Motion Primitives — Motion (Framer Motion) + Tailwind animated UI primitives (text effects, morphing dialog/popover, transition panel, infinite slider, dock, tilt, glow, progressive blur). Installs via the shadcn registry. Reach for it when a build needs polished micro-interactions and animated UI chrome (overlays, sliders, kinetic text, cursor) rather than full hero spectacles.
---

# Motion Primitives — animated component catalog

## What it is
A **MIT-licensed** (free tier + a Pro tier) set of animated UI primitives built on **Motion (Framer Motion) + Tailwind**, by ibelick. Leans toward tasteful micro-interactions and animated chrome — text effects, morphing overlays, sliders, docks, tilt/glow — the polish layer rather than the WebGL hero layer. Pairs with [[frontend-design]] and the [[immersive-web-token-vault]].

## Install a component
Each component is a shadcn registry entry (the site also documents a dedicated CLI on each component page):

```bash
npx shadcn@latest add "https://motion-primitives.com/c/<slug>.json"
# example:
npx shadcn@latest add "https://motion-primitives.com/c/text-effect.json"
```

Prereqs: Tailwind, `motion` (Framer Motion), the `cn` util.

## Catalog (33 components — authoritative registry list, verified 2026-07-20)

**Text & numbers**
`text-effect`, `text-shimmer`, `text-shimmer-wave`, `text-morph`, `text-roll`, `text-scramble`, `text-loop`, `spinning-text`, `sliding-number`, `animated-number`

**Motion & interaction**
`animated-group`, `animated-background`, `in-view`, `tilt`, `magnetic`, `cursor`, `border-trail`, `glow-effect`, `progressive-blur`, `spotlight`, `infinite-slider`, `image-comparison`, `scroll-progress`

**Overlays & panels**
`dialog`, `morphing-dialog`, `morphing-popover`, `disclosure`, `accordion`, `transition-panel`, `toolbar-dynamic`, `toolbar-expandable`, `dock`, `carousel`

## When to use in a build
- **Kinetic headline / animated number** → Text group (`text-effect`, `text-shimmer`, `sliding-number`).
- **Focused overlay that morphs from a trigger** → `morphing-dialog` / `morphing-popover` (the signature MP move).
- **Staggered reveal of a list/grid** → `animated-group` + `in-view`.
- **Depth on hover / atmospheric glow** → `tilt`, `glow-effect`, `spotlight`, `progressive-blur`.
- **Marquee / logo strip / before-after** → `infinite-slider`, `image-comparison`.

Use MP for the polish layer; for full WebGL hero backgrounds reach for [[reactbits]] / [[ogl-webgl]] instead.

## Source & freshness
Docs: `https://motion-primitives.com/docs` · Registry item: `https://motion-primitives.com/c/<slug>.json` · Verified: 2026-07-20 (full list from the `public/c/` registry in the `ibelick/motion-primitives` repo; the live host index was 429-limited). Re-fetch before quoting as current.
