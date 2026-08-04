---
name: aceternity-ui
description: Aceternity UI — immersive/animated React components and full page blocks (3D cards, glare/spotlight, aurora, meteors, moving-border buttons, WebGL-ish effects). Installs via the shadcn registry. Reach for it when building award-tier immersive/marketing sites that need ready animated cards, buttons, hero backgrounds, and section blocks on a Tailwind + Framer Motion stack.
---

# Aceternity UI — immersive component catalog

## What it is
A large registry of **Tailwind + Framer Motion** components and pre-composed **blocks** (whole sections). The signature look is cinematic and immersive — spotlight, aurora, meteors, 3D card tilt, gradient/beam backgrounds — the "not-a-flat-card" aesthetic. Free component registry (the site also sells Pro templates). Pairs with [[immersive-web-token-vault]] for tokens and [[frontend-design]] for the surrounding code.

## Install a component
Every item is a shadcn registry entry:

```bash
npx shadcn@latest add "https://ui.aceternity.com/registry/<slug>.json"
# example:
npx shadcn@latest add "https://ui.aceternity.com/registry/3d-card.json"
```

Prereqs: Tailwind, `framer-motion` (a.k.a. `motion`), and the `cn` util (`clsx` + `tailwind-merge`). A few 3D/WebGL items pull `three` / `@react-three/fiber` — declared in their registry JSON.

## Catalog — components (verified 2026-07-20)

**Cards**
`3d-card`, `glare-card`, `evervault-card`, `card-stack`, `card-hover-effect`, `card-spotlight`, `wobble-card`, `comet-card`, `focus-cards`, `draggable-card`, `apple-cards-carousel`, `tooltip-card`, `bento-grid`, `layout-grid`

**Buttons**
`moving-border`, `hover-border-gradient`, `tailwindcss-buttons`, `magnetic-button`, `stateful-button`

**Backgrounds & atmosphere**
`aurora-background`, `background-beams`, `background-beams-with-collision`, `background-boxes`, `background-gradient`, `background-gradient-animation`, `background-lines`, `background-ripple-effect`, `wavy-background`, `vortex`, `meteors`, `shooting-stars`, `stars-background`, `sparkles`, `grid`, `dotted-glow-background`, `noise-background`, `spotlight`, `spotlight-new`, `glowing-effect`, `glowing-stars`, `lamp`, `hero-highlight`, `dither-shader`, `pixelated-canvas`, `webcam-pixel-grid`

**Text effects**
`text-generate-effect`, `text-hover-effect`, `text-reveal-card`, `typewriter-effect`, `flip-words`, `colourful-text`, `squiggly-text`, `container-text-flip`, `layout-text-flip`, `encrypted-text`, `text-flipping-board`, `canvas-text`, `ascii-art`

**Scroll & motion**
`tracing-beam`, `sticky-scroll-reveal`, `container-scroll-animation`, `parallax-scroll`, `parallax-scroll-2`, `hero-parallax`, `parallax-hero-images`, `macbook-scroll`, `timeline`, `google-gemini-effect`, `3d-marquee`

**Navigation**
`floating-navbar`, `navbar-menu`, `resizable-navbar`, `floating-dock`, `sidebar`, `tabs`, `sticky-banner`, `notch`

**3D & spatial**
`3d-pin`, `globe`, `3d-globe`, `world-map`, `lens`, `cover`, `svg-mask-effect`, `direction-aware-hover`, `compare`, `pointer-highlight`

**Media, inputs & utilities**
`images-slider`, `images-badge`, `infinite-moving-cards`, `animated-testimonials`, `following-pointer`, `animated-tooltip`, `moving-line`, `link-preview`, `animated-modal`, `multi-step-loader`, `loader`, `placeholders-and-vanish-input`, `gooey-input`, `input`, `label`, `file-upload`, `code-block`, `carousel`, `keyboard`, `terminal`, `scales`, `canvas-reveal-effect`

## Catalog — blocks (~180 pre-composed sections)
Aceternity also ships full **blocks** (registry type `registry:block`) — install the same way. They cover: **Heroes** (`hero-with-centered-image`, `hero-section-with-beams-and-grid`, `modern-hero-with-gradients`, `minimal-hero-section-with-parallax-images`, `hero-section-with-mesh-gradient`, …), **Features** (`features-section-demo-1..3`, `features-with-sticky-scroll`, `bento-grid-with-skeletons`, …), **CTAs**, **Pricing** (`simple-pricing-with-three-tiers`, `pricing-with-switch`, …), **Testimonials**, **Navbars**, **Footers**, **Auth/Login**, **Contact**, **Blog**, **Stats**, **Backgrounds**, **Team**, **Empty states**, and **shader sections** (`dot-distortion-shader`, `lines-gradient-shader`, `spotlight-shader`).

This is ~180 blocks — too many to list every slug here without them going stale. Fetch the live block list before choosing:

```bash
# lists every current UI component + block slug
curl -s https://ui.aceternity.com/registry | jq '.[].name'   # or WebFetch the same URL
```

## When to use in a build
- Immersive **hero / section** fast → pick a block, then restyle to the locked deck.
- A single spectacle element (spotlight, aurora, meteors, 3d-card, glare-card, moving-border) → components list above.
- Scroll storytelling (tracing-beam, sticky-scroll, container-scroll, hero-parallax) → Scroll & motion group.

Deck-first still applies: lock palette + type from [[immersive-web-token-vault]] before dropping these in; Aceternity's default demos lean purple-gradient, which is a non-award tell if kept unrestyled.

## Source & freshness
Registry: `https://ui.aceternity.com/registry` · Docs: `https://ui.aceternity.com/components` · Verified: 2026-07-20. Re-fetch the registry before quoting the list as current.
