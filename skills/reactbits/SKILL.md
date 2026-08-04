---
name: reactbits
description: React Bits — a large library of animated React "bits" across Text Animations, Animations, Components, and Backgrounds (WebGL/GLSL backgrounds, cursor effects, kinetic text, glass/tilt cards). Ships in JS/TS × CSS/Tailwind variants; installs via the jsrepo CLI or shadcn. Reach for it when a build needs immersive hero text, a GPU background (galaxy/aurora/liquid), or a signature cursor/scroll effect.
---

# React Bits — immersive component catalog

## What it is
An open-source (**MIT**) collection of animated React components. Each bit ships in four variants — **JS or TS**, and **CSS or Tailwind** — so it drops into most stacks. Many of the Backgrounds and some Animations are **WebGL/GLSL** (three.js / OGL) or **GSAP**-driven, which is where the real "shader atmosphere" comes from (the award-tier move — see [[immersive-web-token-vault]] rule 7). Pairs with [[ogl-webgl]], [[gsap]], [[frontend-design]].

## Install a component
React Bits supports two install paths; the exact command per component/variant is shown on that component's page:

```bash
# jsrepo CLI — path is <variant>/<Category>/<Name>
npx jsrepo add https://reactbits.dev/ts/tailwind/TextAnimations/SplitText

# it also publishes a shadcn registry — copy the exact URL from the component page:
npx shadcn@latest add "https://reactbits.dev/r/<Name>-<VARIANT>"
```

Or just copy the source from the site. Per-component deps vary: Backgrounds usually need `ogl` or `three`; some Animations/Text need `gsap` or `framer-motion` — each page lists its own.

## Catalog (139 items across 4 categories — verified 2026-07-20)

**Text Animations (23)**
Split Text, Blur Text, Shiny Text, Gradient Text, Text Type, Text Cursor, Text Pressure, Curved Loop, Fuzzy Text, Scrambled Text, Rotating Text, Glitch Text, Scroll Reveal, True Focus, Scroll Float, Scroll Velocity, ASCII Text, Decrypted Text, Falling Text, Circular Text, Shuffle, Count Up, Variable Proximity

**Animations (31)**
Animated Content, Fade Content, Pixel Transition, Glare Hover, Magnet, Magnet Lines, Noise, Crosshair, Image Trail, Ribbons, Splash Cursor, Blob Cursor, Star Border, Metallic Paint, Meta Balls, Click Spark, Electric Border, Pixel Trail, Cubes, Ghost Cursor, Shape Blur, Gradual Blur, Laser Flow, Logo Loop, Sticker Peel, Target Cursor, Antigravity, Cursor Grid, Magic Rings, Orbit Images, Strands

**Components (40)**
Animated List, Stepper, Dock, Gooey Nav, Bounce Cards, Card Swap, Carousel, Stack, Flying Posters, Card Nav, Bubble Menu, Staggered Menu, Pill Nav, Masonry, Chroma Grid, Magic Bento, Spotlight Card, Reflective Card, Tilted Card, Decay Card, Pixel Card, Profile Card, Circular Gallery, Dome Gallery, Flowing Menu, Infinite Menu, Fluid Glass, Glass Icons, Glass Surface, Elastic Slider, Counter, Folder, Model Viewer, Lanyard, Scroll Stack, Specular Button, Option Wheel, Curved Input, Line Sidebar, Bubble Menu

**Backgrounds (45)**
Aurora, Silk, Threads, Beams, Waves, Iridescence, Liquid Chrome, Liquid Ether, Balatro, Ballpit, Dither, Galaxy, Orb, Grid Motion, Grid Distortion, Grid Scan, Hyperspeed, Squares, Letter Glitch, Lightning, Light Rays, Light Pillar, Lightfall, Dark Veil, Dot Grid, Dot Field, Ripple Grid, Faulty Terminal, Prism, Prismatic Burst, Plasma, Plasma Wave, Pixel Blast, Pixel Snow, Particles, Color Bends, Grainient, Ferrofluid, Floating Lines, Line Waves, Radar, Shape Grid, Side Rays, Soft Aurora, Evil Eye

## When to use in a build
- **GPU / shader hero background** (the award-tier atmosphere source) → Backgrounds (Aurora, Silk, Liquid Ether, Galaxy, Iridescence, Threads, Plasma).
- **Kinetic / decrypted / variable-proximity headline** → Text Animations.
- **Signature cursor or scroll effect** → Animations (Splash/Blob/Ghost Cursor, Image Trail, Scroll Stack).
- **Glassy/tilt/reflective card or a bento** → Components (Fluid Glass, Tilted Card, Magic Bento, Spotlight Card).

Because many bits are WebGL, keep to ONE per section — stacking shaders kills performance (see [[gsap-performance]] / [[premium-motion-cookbook]]).

## Source & freshness
Docs: `https://reactbits.dev` · Categories: Text Animations, Animations, Components, Backgrounds · Verified: 2026-07-20. Re-fetch before quoting as current.
