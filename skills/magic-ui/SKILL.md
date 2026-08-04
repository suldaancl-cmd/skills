---
name: magic-ui
description: Magic UI — 75+ free animated React components and effects (border-beam, marquee, animated beams, text animations, shimmer/rainbow buttons, device mocks, backgrounds). Installs via the shadcn registry. Reach for it when an immersive/animated landing section needs a ready effect (text animation, animated background/pattern, animated button, or device mockup) on a Tailwind + Motion stack.
---

# Magic UI — immersive component catalog

## What it is
A large, **MIT-licensed** library of animated components and effects built on **Tailwind + Motion (Framer Motion)**, designed to sit alongside shadcn/ui. Strong on text animations, animated backgrounds/patterns, "wow" buttons, and device mockups for product shots. Pairs with [[shadcn-ui]] for setup, [[immersive-web-token-vault]] for tokens, [[frontend-design]] for code.

## Install a component
Each item is a shadcn registry entry; the **slug is the kebab-case of the name**:

```bash
npx shadcn@latest add "https://magicui.design/r/<slug>.json"
# examples:
npx shadcn@latest add "https://magicui.design/r/shimmer-button.json"
npx shadcn@latest add "https://magicui.design/r/animated-beam.json"
```

Prereqs: Tailwind, `motion` (Framer Motion), the `cn` util. Some items (Globe, Confetti, Icon Cloud) pull their own dep, declared in the registry JSON.

## Catalog (~76 components — verified 2026-07-20)

**Text animations**
Text Animate, Text Reveal, Dia Text Reveal, Hyper Text, Morphing Text, Kinetic Text, Spinning Text, Sparkles Text, Aurora Text, Comic Text, Line Shadow Text, Animated Gradient Text, Animated Shiny Text, Word Rotate, Typing Animation, Text 3D Flip, Video Text, Number Ticker, Highlighter, Scroll Based Velocity, Scroll Progress

**Buttons**
Shimmer Button, Shiny Button, Rainbow Button, Pulsating Button, Ripple Button, Interactive Hover Button

**Cards & data**
Magic Card, Neon Gradient Card, Bento Grid, Client Tweet Card, Tweet Card, File Tree, Code Comparison

**Backgrounds & patterns**
Animated Grid Pattern, Grid Pattern, Interactive Grid Pattern, Dot Pattern, Hexagon Pattern, Striped Pattern, Flickering Grid, Retro Grid, Ripple, Warp Background, Light Rays, Noise Texture, Backlight

**Effects & motion**
Border Beam, Shine Border, Animated Beam, Meteors, Particles, Orbiting Circles, Animated Circular Progress Bar, Animated List, Confetti, Cool Mode, Glare Hover, Progressive Blur, Smooth Cursor, Pointer, Globe, Icon Cloud, Lens, Marquee, Dotted Map, Glyph Matrix, Pixel Image, Avatar Circles, Theme Toggler

**Device & product mocks**
iPhone, Android, Safari, Terminal, Dock, Hero Video Dialog

## When to use in a build
- **Animated headline / kinetic type** → Text animations (Text Animate, Morphing Text, Aurora Text, Hyper Text).
- **Animated section background** without writing a shader → Backgrounds & patterns (Flickering Grid, Retro Grid, Warp Background, Dot Pattern).
- **"Integrations" / flow diagram** → Animated Beam + Orbiting Circles + Icon Cloud.
- **App screenshot in context** → Device mocks (iPhone/Safari/Android + Hero Video Dialog).
- **A single loud CTA** → Shimmer / Rainbow / Interactive Hover Button.

Deck-first still applies — restrain to one accent from [[immersive-web-token-vault]]; Magic UI demos lean on gradients, which read as non-award if left as-is.

## Source & freshness
Docs: `https://magicui.design/docs` · Registry item: `https://magicui.design/r/<slug>.json` · Verified: 2026-07-20 (names from `llms.txt`). Re-fetch before quoting as current.
