---
name: immersive-components
description: Index/router for the immersive React component libraries installed as skills (Aceternity UI, Magic UI, React Bits, Motion Primitives, Cult UI). Use FIRST when a build needs a ready immersive card, button, animated background, kinetic text, or section block — it routes the need to the right library skill and names the runners-up not yet cataloged.
---

# Immersive components — library index & router

Five immersive/animated React component libraries are cataloged as skills. This is the router: match the need, open the library skill, install the component. All five are **Tailwind + Motion/WebGL** and install through a CLI registry, so components drop into any React/Next build.

## Pick a library by need

| You need… | Reach for | Skill |
| --- | --- | --- |
| A full **hero / section block** ready to restyle | Aceternity UI (~180 blocks) | [[aceternity-ui]] |
| A single **spectacle** element (spotlight, aurora, meteors, 3D/glare card, moving-border) | Aceternity UI | [[aceternity-ui]] |
| **Animated effects & text** for landing sections (border-beam, marquee, beams, shimmer button, device mocks) | Magic UI (~76) | [[magic-ui]] |
| A **GPU / shader background** (galaxy, aurora, liquid, iridescence) or signature cursor/scroll effect | React Bits (139, WebGL) | [[reactbits]] |
| **Micro-interaction polish** — morphing dialog/popover, transition panel, kinetic text, tilt/glow, sliders | Motion Primitives (~27) | [[motion-primitives]] |
| A **tactile card/button** with real depth (texture, neumorph, metal) or product chrome (dynamic island, dock) | Cult UI (78) | [[cult-ui]] |

Overlap is fine — e.g. Dock exists in Magic UI, React Bits, Motion Primitives and Cult UI. Pick the one whose aesthetic matches the locked deck.

## Install pattern (all libraries)
Four of five publish a **shadcn registry**; React Bits uses **jsrepo** (and also shadcn). General flow:

```bash
# shadcn-registry libraries (Aceternity, Magic UI, Cult UI, Motion Primitives)
npx shadcn@latest add "<library-registry-url>/<slug>.json"

# React Bits
npx jsrepo add https://reactbits.dev/<variant>/<Category>/<Name>
```

Exact URL per library is in each skill's "Install a component" section. Shared prereqs: Tailwind, `motion`/`framer-motion`, the `cn` util (shadcn projects already have it).

## Hard rules when using any of these
- **Deck-first.** These libraries do NOT replace the colors+fonts deck step. Lock palette + type from [[immersive-web-token-vault]] first; restyle every component off its default demo (most ship purple/gradient demos, which is a non-award tell).
- **One shader per section.** WebGL backgrounds (React Bits, Aceternity canvas items) are GPU-heavy — never stack two in a viewport. See [[gsap-performance]] / [[premium-motion-cookbook]].
- **Restraint over quantity.** One accent, one spectacle per section (award-tier finding, [[immersive-web-token-vault]]). Pulling ten animated components into one page is the opposite of the bar Karim wants.
- Write the surrounding code with [[frontend-design]]; audit with [[impeccable]].

## Runners-up (not cataloged yet — install on request)
Other quality immersive/animated registries, addable the same way if a build needs them: **Animata**, **Fancy Components**, **HextaUI**, **Eldora UI**, **Syntax UI**, **Skiper UI**, **Indie UI**, **Kokonut UI**, **Luxe**, **Page UI**. Say the word and each becomes a sibling skill with a verified catalog.

## Freshness
All five catalogs verified 2026-07-20 from live registries/docs. These libraries add components frequently — re-fetch a library's registry before quoting its list as current (each skill carries its refresh URL).
