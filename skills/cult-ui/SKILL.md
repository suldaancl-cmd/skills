---
name: cult-ui
description: Cult UI — shadcn-based animated React components (texture cards/buttons, dynamic island, dock, neumorphic UI, shader backgrounds). Installs via the shadcn registry. Reach for it when an immersive/premium build needs tactile, animated UI pieces (cards, buttons, overlays, animated hero backgrounds) that drop into a shadcn + Tailwind + Framer Motion stack.
---

# Cult UI — animated component catalog

## What it is
A component registry built on **shadcn/ui + Tailwind + Framer Motion**. Tactile, "designed" pieces — textured cards and buttons, a macOS-style dynamic island and dock, neumorphic controls, and canvas/shader hero backgrounds. **MIT** (free component registry; the site also sells Pro templates separately). Pairs with the [[shadcn-ui]] skill for setup and the [[immersive-web-token-vault]] for palette/type before building.

## Install a component
Each component is a shadcn registry item:

```bash
npx shadcn@latest add "https://cult-ui.com/r/<slug>.json"
# example:
npx shadcn@latest add "https://cult-ui.com/r/texture-card.json"
```

Prereqs: a shadcn/ui-initialized project (`components.json`, the `cn` util from `lib/utils`), Tailwind, and `framer-motion`. Some backgrounds pull extra deps (canvas/shader helpers) declared in their registry JSON.

## Catalog (78 registry components — verified 2026-07-20)

**Buttons**
`cosmic-button`, `texture-button`, `bg-animate-button`, `border-beam-button`, `family-button`, `neumorph-button`, `metal-button`, `gradient-button-group`

**Cards & carousels**
`texture-card`, `shift-card`, `minimal-card`, `cutout-card`, `feature-carousel`, `three-d-carousel`, `logo-carousel`, `loading-carousel`

**Text & headings**
`text-animate`, `gradient-heading`, `typewriter`, `animated-number`, `text-gif`, `pixel-heading-character`, `pixel-heading-word`, `pixel-paragraph-words`, `pixel-paragraph-words-inverse`

**Hero & animated backgrounds**
`hero-dithering`, `hero-color-panel`, `hero-static-radial-gradient`, `hero-heatmap`, `hero-liquid-metal`, `bg-media`, `bg-image-texture`, `bg-animated-gradient`, `bg-animated-fractal-dot-grid`, `canvas-fractal-grid`, `stripe-bg-guides`, `grid-beam`, `texture-overlay`, `morph-surface`, `distorted-glass`

**Shader / blur effects**
`shader-lens-blur`, `edge-blur`, `dither-image`

**Navigation, overlays & panels**
`dynamic-island`, `direction-aware-tabs`, `dock`, `side-panel`, `floating-panel`, `popover`, `family-drawer`, `toolbar-expandable`, `intro-disclosure`, `expandable`, `expandable-screen`

**Media**
`hover-video-player`, `youtube-video-player`, `lightboard`

**Inputs & forms**
`color-picker`, `popover-form`, `sortable-list`, `onboarding`

**Polls & feedback widgets**
`choice-poll`, `feature-poll`, `feature-voting`, `vote-tally`, `poll-widget`, `prompt-library`, `ai-instructions`

**Dev & misc**
`code-block`, `mock-browser-window`, `terminal-animation`, `timer`, `squiggle-arrow`, `tweet-grid`, `neumorph-eyebrow`, `svg-shapes`, `svg-shapes-animated`, `svg-bands`

> Each `<slug>` above also has a `<slug>-demo` in the registry (type `registry:component`) if you want the usage example.

## When to use in a build
- Need a **tactile card or button** with real depth (texture/neumorph/metal) instead of a flat card → Buttons / Cards groups.
- Need an **animated hero background** without hand-writing a shader → Hero & backgrounds group (dithering, liquid-metal, heatmap, fractal-dot-grid).
- Building product UI chrome (dock, dynamic island, drawers, expandables) → Navigation & overlays.
- Feedback/voting/onboarding surfaces → Polls & widgets.

For award-tier restraint, still run the deck-first step: pick palette + type from [[immersive-web-token-vault]] before dropping these in, and write the surrounding code with [[frontend-design]].

## Source & freshness
Registry: `https://cult-ui.com/r/registry.json` · Docs: `https://www.cult-ui.com/docs/components` · Verified: 2026-07-20. Live registries change — re-run the registry fetch before quoting the list as current.
