---
name: 3d-animation-web-designer
description: Build cinematic, dark-luxury 3D animated websites with particle systems, scroll animations, glassmorphism, preloaders, CSS skylines, and premium motion design. Use this skill whenever the user asks to create a 3D website, animated landing page, cinematic web experience, dark-theme luxury site, night-themed website, real estate showcase, fashion-tech platform, agency portfolio, or any website that should feel like "an experience, not just a webpage." Also trigger when the user mentions keywords like particles, preloader, glassmorphism, parallax scrolling, GSAP, Three.js, scroll animations, cinematic website, dark luxury design, night theme, gold/amber/cyan color schemes, 3D hover effects, CSS cityscape, Seedance prompts, Spline 3D, or premium web animation. This skill covers the full pipeline from design system to working HTML/CSS/JS code with all animations included.
---

# 3D Animation Web Designer

Build cinematic, immersive, dark-luxury animated websites that feel like premium experiences. This skill codifies a proven design system for creating websites with particle effects, scroll-driven animations, glassmorphism, 3D transforms, CSS cityscapes, and cinematic motion — all in a single HTML file.

## When to Use This Skill

Use when the user wants:
- A dark, premium, animated landing page or full website
- A cinematic "experience" website (real estate, agency, fashion, tech)
- Night-themed websites with city lights, particles, or atmospheric effects
- 3D hover effects, parallax, or scroll-triggered reveals
- Websites inspired by luxury brands, commodity traders, or fashion houses
- Seedance 2.0 or Spline 3D prompt generation for web hero animations
- Any site described as "premium", "cinematic", "immersive", or "3D animated"

## Design Philosophy

The core aesthetic is **"dark luxury meets technical precision"** — like a high-end CAD tool designed by a fashion house, or a commodity trading firm's website that feels like a cinematic trailer.

Three pillars:
1. **Cinematic Atmosphere** — Every scroll should feel like a scene transition in a film
2. **Technical Precision** — Grid overlays, crosshairs, measurement markers, corner brackets suggest engineering excellence
3. **Premium Typography** — Oversized display fonts paired with refined body text, generous spacing

## Design System

### Color Palettes

Choose ONE palette per project. Each has been battle-tested:

**Palette A — Gold & Midnight (Real estate, commodities, luxury)**
```css
:root {
  --bg: #050508;
  --bg-card: #0A0A0F;
  --gold: #D4A853;
  --gold-dim: #8B7335;
  --cyan: #4ECDC4;
  --warm: #FF6B35;
  --text: #E8E4DD;
  --text-dim: #8A8578;
  --glass: rgba(255,255,255,0.04);
  --glass-border: rgba(255,255,255,0.08);
}
```

**Palette B — Lime & Obsidian (Fashion-tech, SaaS, creative agencies)**
```css
:root {
  --bg: #0D0D12;
  --bg-card: #16161E;
  --accent: #C8E62E;
  --plum: #4A1942;
  --burgundy: #5C1A30;
  --text: #F0ECE4;
  --text-dim: #7A7670;
  --border: #2A2830;
}
```

**Palette C — Teal & Navy (Tech, corporate, sustainability)**
```css
:root {
  --bg: #0A1628;
  --bg-card: #0F1D30;
  --accent: #4ECDC4;
  --blue-glow: #1a3a5c;
  --text: #E0E8F0;
  --text-dim: #6B7C8E;
}
```

### Typography System

Always pair a **display font** with a **body font** and a **mono font**. Pick from the curated `premium-design-laws` set below by brief, and write the one-line justification first (name the brief, name the pairing, say why it fits) — defaulting is banned.

| Role | Recommended (from `premium-design-laws`) | Usage |
|------|------------------|-------|
| Display/Headlines | `Druk Wide Bold` (motion/cinematic), `Canela`, `GT Super Display`, `Domaine Display` | Hero text, section titles — OVERSIZED. Anchor weight ≥300; tracking −0.02 to −0.03em |
| Body | `PP Neue Montreal`, `Switzer`, `Aktiv Grotesk` | Paragraphs, descriptions — weight 400, tracking 0 |
| Mono/Technical | `IBM Plex Mono`, `Geist Mono`, `Space Mono` | HUD / telemetry / credits only — uppercase, letter-spacing ≤0.18em |
| Arabic (when needed) | `El Messiri` (display) / `Cairo` (body) | RTL text — tracking ALWAYS 0, 16px floor, per-block direction |

**Typography rules:**
- Hero text: `clamp(2.5rem, 8vw, 6rem)` — dominate the viewport
- Section labels: `0.65-0.75rem`, uppercase, `letter-spacing: 0.18em`, accent color — styled as an eyebrow micro-label; no symbol prefix (the styling signals the role)
- Body: `1rem` (16px floor — never smaller), `line-height: 1.6`, `font-weight: 400` (300 is display-only)
- Stats/numbers: italic bold display font, oversized

### Grid Overlay System (Technical Precision Layer)

Add a faint grid pattern as a fixed background to simulate a blueprint/CAD workspace:

```css
body::before {
  content: '';
  position: fixed;
  inset: 0;
  background-image:
    linear-gradient(rgba(212,168,83,0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(212,168,83,0.03) 1px, transparent 1px);
  background-size: 60px 60px;
  pointer-events: none;
  z-index: 0;
}
```

Optional decorative elements:
- **Crosshair markers** — pseudo-elements with 1px lines at intersection points
- **Corner brackets** — L-shaped border segments at card corners
- **Measurement rulers** — small tick marks along section edges
- **"×" markers** — accent-colored × at grid intersections

## Core Animation Components

Read `references/animations.md` for the full code library of all animation components. Here is a summary of what's available:

### 1. Preloader
A branded loading screen with logo pulse and progress bar animation. Hides after 2-2.5 seconds with opacity/visibility transition.

### 2. Particle System
Floating dots (40-80 particles) with randomized sizes (1-3px), positions, colors (from the accent palette), and float durations (10-25s). Fixed position, pointer-events: none.

### 3. Scroll Reveal
IntersectionObserver-based `.reveal` class that fades elements up from `translateY(40px)` to their natural position. Threshold: 0.15.

### 4. Counter Animation
Numbers count up from 0 to target value on scroll intersection. Use `setInterval` with 30ms steps, 60 frames total.

### 5. 3D Card Hover
Cards with `perspective(1000px)` and `rotateY(±5deg) rotateX(±3deg)` on hover, with box-shadow shifts for depth.

### 6. Parallax Background
Background layers that move at different scroll speeds using `transform: translateY(calc(var(--scroll) * 0.3))`.

### 7. CSS Cityscape/Skyline
A pure-CSS night cityscape with building silhouettes, window lights (animated opacity), stars, moon, and ambient city glow gradients.

### 8. Glassmorphism Cards
`backdrop-filter: blur(12px)` with semi-transparent backgrounds and subtle borders.

### 9. Text Reveal
Staggered line-by-line or word-by-word entrance using `animation-delay` increments of 0.1-0.2s.

### 10. Ambient Glow
Positioned `div` elements with large `border-radius: 50%`, blurred via `filter: blur(80-120px)`, with accent colors at 10-20% opacity. Slow floating animation.

## Page Architecture

Every cinematic website follows this structure:

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

### Navigation Pattern
Three-zone fixed top bar — left: menu toggle (`≡`); center: brand wordmark; right: CTA button with an accent-color border. Equal optical spacing between zones.
- Fixed top, `backdrop-filter: blur(12px)`
- Add `.scrolled` class on scroll to darken background
- CTA: border in accent color, hover fills solid

### Hero Section Pattern
- Full viewport height (`min-height: 100vh`)
- 3-4 lines of oversized display text, staggered reveal
- Small badge/tag above headline (monospace, accent color)
- Subtitle in lighter weight
- 1-2 CTA buttons (primary: filled accent, secondary: bordered)
- Optional: scanning circle animation, ambient glow, crosshairs

## Responsive Design

Desktop-first, mobile-adaptive:

```css
@media (max-width: 900px) {
  .nav-links { display: none }
  .nav-toggle { display: block }
  .grid-2col { grid-template-columns: 1fr }
  .hero h1 { font-size: clamp(2rem, 6vw, 3rem) }
}

@media (max-width: 600px) {
  .hero { padding: 100px 20px 60px }
  .section { padding: 60px 20px }
  /* Disable heavy effects on mobile */
  .particles { display: none }
  body::before { display: none }
}
```

Key rules:
- Grid layouts collapse to single column below 900px
- Particles and grid overlays hidden below 600px for performance
- Typography scales with `clamp()` — never fixed pixel sizes
- Touch targets minimum 44px

## Seedance 2.0 / Spline 3D Prompt Generation

When the user needs AI video or 3D web animation prompts, read `references/prompt-templates.md` for proven prompt structures for:
- Seedance 2.0 cinematic video generation
- Spline 3D web hero animations
- Scene composition, camera movement, lighting, and post-processing

## Single-File Output

Always output as a **single HTML file** with everything inline:
- `<style>` block with all CSS (including animations, responsive queries)
- `<script>` block with all JS (preloader, particles, scroll observers, counters)
- Google Fonts via `<link>` in `<head>`
- No external dependencies except fonts and optionally GSAP CDN

This ensures the file works immediately when opened in a browser or deployed anywhere.

## Checklist Before Delivery

Before presenting the final file, verify:
- [ ] Preloader works and auto-hides
- [ ] Particles render and float naturally
- [ ] Scroll reveals trigger on all sections
- [ ] Navigation has backdrop blur and scroll state
- [ ] Hero text is oversized and staggered
- [ ] At least one 3D hover effect on cards
- [ ] Counter animations trigger on scroll
- [ ] Responsive: test mental model at 375px and 768px
- [ ] No horizontal overflow at any breakpoint
- [ ] Custom cursor (crosshair or dot) set on body
- [ ] Color palette is consistent — no rogue colors
- [ ] Footer is minimal and dark
