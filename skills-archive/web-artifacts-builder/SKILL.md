---
name: web-artifacts-builder
description: Suite of tools for creating elaborate web artifacts — from React/shadcn multi-component apps to cinematic 3D-animated single-file HTML websites. Use for complex artifacts requiring state management, routing, or shadcn/ui components. Also use when the user asks for cinematic, dark-luxury, 3D animated, immersive websites with particles, scroll animations, glassmorphism, preloaders, CSS skylines, parallax, GSAP, Three.js, or premium motion design. Covers both React artifact pipeline and single-file cinematic HTML output.
license: Complete terms in LICENSE.txt
---

# Web Artifacts Builder

This skill has **two modes**:

1. **React Artifact Mode** — Multi-component apps with React + Tailwind + shadcn/ui, bundled to a single HTML artifact
2. **Cinematic HTML Mode** — Dark-luxury 3D animated single-file websites with particles, scroll animations, glassmorphism, and premium motion design

Choose the right mode based on the request:
- Need state management, routing, shadcn components? → **React Artifact Mode**
- Need cinematic experience, animations, 3D effects, dark luxury? → **Cinematic HTML Mode**
- Need both? → Start with Cinematic HTML Mode, add React interactivity where needed

---

# MODE 1: React Artifact Builder

To build powerful frontend claude.ai artifacts, follow these steps:
1. Initialize the frontend repo using `scripts/init-artifact.sh`
2. Develop your artifact by editing the generated code
3. Bundle all code into a single HTML file using `scripts/bundle-artifact.sh`
4. Display artifact to user
5. (Optional) Test the artifact

**Stack**: React 18 + TypeScript + Vite + Parcel (bundling) + Tailwind CSS + shadcn/ui

## Design & Style Guidelines

VERY IMPORTANT: To avoid what is often referred to as "AI slop", avoid using excessive centered layouts, purple gradients, uniform rounded corners, and Inter font.

## Quick Start

### Step 1: Initialize Project

Run the initialization script to create a new React project:
```bash
bash scripts/init-artifact.sh <project-name>
cd <project-name>
```

This creates a fully configured project with:
- ✅ React + TypeScript (via Vite)
- ✅ Tailwind CSS 3.4.1 with shadcn/ui theming system
- ✅ Path aliases (`@/`) configured
- ✅ 40+ shadcn/ui components pre-installed
- ✅ All Radix UI dependencies included
- ✅ Parcel configured for bundling (via .parcelrc)
- ✅ Node 18+ compatibility (auto-detects and pins Vite version)

### Step 2: Develop Your Artifact

To build the artifact, edit the generated files. See **Common Development Tasks** below for guidance.

### Step 3: Bundle to Single HTML File

To bundle the React app into a single HTML artifact:
```bash
bash scripts/bundle-artifact.sh
```

This creates `bundle.html` - a self-contained artifact with all JavaScript, CSS, and dependencies inlined. This file can be directly shared in Claude conversations as an artifact.

**Requirements**: Your project must have an `index.html` in the root directory.

**What the script does**:
- Installs bundling dependencies (parcel, @parcel/config-default, parcel-resolver-tspaths, html-inline)
- Creates `.parcelrc` config with path alias support
- Builds with Parcel (no source maps)
- Inlines all assets into single HTML using html-inline

### Step 4: Share Artifact with User

Finally, share the bundled HTML file in conversation with the user so they can view it as an artifact.

### Step 5: Testing/Visualizing the Artifact (Optional)

Note: This is a completely optional step. Only perform if necessary or requested.

To test/visualize the artifact, use available tools (including other Skills or built-in tools like Playwright or Puppeteer). In general, avoid testing the artifact upfront as it adds latency between the request and when the finished artifact can be seen. Test later, after presenting the artifact, if requested or if issues arise.

## Reference

- **shadcn/ui components**: https://ui.shadcn.com/docs/components

---

# MODE 2: Cinematic 3D Animation Web Designer

Build cinematic, immersive, dark-luxury animated websites that feel like premium experiences — particle effects, scroll-driven animations, glassmorphism, 3D transforms, CSS cityscapes, and cinematic motion — all in a single HTML file.

## When to Use Cinematic Mode

Use when the user wants:
- A dark, premium, animated landing page or full website
- A cinematic "experience" website (real estate, agency, fashion, tech)
- Night-themed websites with city lights, particles, or atmospheric effects
- 3D hover effects, parallax, or scroll-triggered reveals
- Websites inspired by luxury brands, commodity traders, or fashion houses
- Seedance 2.0 or Spline 3D prompt generation for web hero animations
- Any site described as "premium", "cinematic", "immersive", or "3D animated"

## Design Philosophy

**"Dark luxury meets technical precision"** — like a high-end CAD tool designed by a fashion house.

Three pillars:
1. **Cinematic Atmosphere** — Every scroll feels like a scene transition
2. **Technical Precision** — Grid overlays, crosshairs, corner brackets suggest engineering excellence
3. **Premium Typography** — Oversized display fonts, refined body text, generous spacing

## Color Palettes

Choose ONE per project:

**Palette A — Gold & Midnight (Real estate, commodities, luxury)**
```css
:root {
  --bg: #050508; --bg-card: #0A0A0F;
  --gold: #D4A853; --gold-dim: #8B7335;
  --cyan: #4ECDC4; --warm: #FF6B35;
  --text: #E8E4DD; --text-dim: #8A8578;
  --glass: rgba(255,255,255,0.04);
  --glass-border: rgba(255,255,255,0.08);
}
```

**Palette B — Lime & Obsidian (Fashion-tech, SaaS, agencies)**
```css
:root {
  --bg: #0D0D12; --bg-card: #16161E;
  --accent: #C8E62E; --plum: #4A1942; --burgundy: #5C1A30;
  --text: #F0ECE4; --text-dim: #7A7670; --border: #2A2830;
}
```

**Palette C — Teal & Navy (Tech, corporate, sustainability)**
```css
:root {
  --bg: #0A1628; --bg-card: #0F1D30;
  --accent: #4ECDC4; --blue-glow: #1a3a5c;
  --text: #E0E8F0; --text-dim: #6B7C8E;
}
```

## Typography System

| Role | Fonts | Usage |
|------|-------|-------|
| Display | `Playfair Display`, `Anton`, `Bebas Neue`, `Oswald` | Hero text — OVERSIZED |
| Body | `Outfit`, `DM Sans`, `Space Grotesk` | Paragraphs — light weight |
| Mono | `Space Mono`, `JetBrains Mono` | Labels — uppercase letterspaced |

- Hero: `clamp(2.5rem, 8vw, 6rem)`
- Section labels: `0.65-0.75rem`, uppercase, `letter-spacing: 3px`, prefix `// `
- Body: `0.85-0.95rem`, `line-height: 1.7`, `font-weight: 300`

## Grid Overlay (Technical Precision Layer)

```css
body::before {
  content: ''; position: fixed; inset: 0;
  background-image:
    linear-gradient(rgba(212,168,83,0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(212,168,83,0.03) 1px, transparent 1px);
  background-size: 60px 60px;
  pointer-events: none; z-index: 0;
}
```

## Core Animation Components

Read `references/animations.md` for complete copy-paste code. Summary:

| Component | Description |
|-----------|-------------|
| **Preloader** | Branded loading screen with logo pulse + progress bar |
| **Particle System** | 40-80 floating dots, randomized colors/sizes/durations |
| **Scroll Reveal** | IntersectionObserver fade-up from `translateY(40px)` |
| **Counter Animation** | Numbers count up on scroll intersection |
| **3D Card Hover** | `perspective(1000px)` with rotateY/X on hover |
| **Parallax** | Background layers at different scroll speeds |
| **CSS Cityscape** | Pure-CSS night skyline with animated window lights |
| **Glassmorphism** | `backdrop-filter: blur(12px)` cards |
| **Text Stagger** | Line-by-line entrance with animation-delay |
| **Ambient Glow** | Blurred color blobs floating slowly |
| **Scanning Circle** | Pulsing animated circle (hero decoration) |
| **Fabric Textures** | Silk shimmer, velvet, linen CSS simulations |
| **Floating Ticker** | Infinite-scroll marquee bar |

## Page Architecture

```
1. PRELOADER → branded logo + progress bar
2. PARTICLES → fixed background layer
3. NAVIGATION → fixed, transparent, blur backdrop
4. HERO → full viewport, oversized text, ambient effects
5. CONTENT SECTIONS → alternating layouts with scroll reveals
6. FEATURE/SHOWCASE → full-width visual impact section
7. STATS → counter animations, grid layout
8. FOOTER → minimal, dark, accent-colored links
```

## Responsive Design

```css
@media (max-width: 900px) {
  .nav-links { display: none }
  .grid-2col { grid-template-columns: 1fr }
  .hero h1 { font-size: clamp(2rem, 6vw, 3rem) }
}
@media (max-width: 600px) {
  .particles { display: none }
  body::before { display: none }
}
```

## Seedance 2.0 / Spline 3D Prompts

Read `references/prompt-templates.md` for AI video and 3D web animation prompt structures.

## Single-File Output

Output as a **single HTML file** with everything inline:
- `<style>` block with all CSS (animations, responsive)
- `<script>` block with all JS (preloader, particles, scroll observers, counters)
- Google Fonts via `<link>` in `<head>`
- No external dependencies except fonts and optionally GSAP CDN

## Cinematic Mode Checklist

- [ ] Preloader works and auto-hides
- [ ] Particles render and float naturally
- [ ] Scroll reveals trigger on all sections
- [ ] Navigation has backdrop blur and scroll state
- [ ] Hero text is oversized and staggered
- [ ] At least one 3D hover effect on cards
- [ ] Counter animations trigger on scroll
- [ ] Responsive at 375px and 768px
- [ ] No horizontal overflow
- [ ] Color palette is consistent
- [ ] Footer is minimal and dark