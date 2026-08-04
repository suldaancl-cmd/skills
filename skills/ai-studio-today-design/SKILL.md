---
name: AI Studio Today-design
description: Design system skill for AI Studio Today. Activate when building UI components, pages, or any visual elements. Provides exact color tokens, typography scale, spacing grid, component patterns, and craft rules. Read references/DESIGN.md before writing any CSS or JSX. Includes ultra-mode visual journey: read references/ANIMATIONS.md, references/LAYOUT.md, references/COMPONENTS.md, and references/INTERACTIONS.md for full motion and layout details.
---

# AI Studio Today Design System

You are building UI for **AI Studio Today**. Light-themed, cool palette, sans-serif typography (Arial Black), compact density on a 4px grid.

## Visual Reference

**IMPORTANT**: Study ALL screenshots below before writing any UI. Match colors, typography, spacing, layout, and motion exactly as shown.

### Scroll Journey (Cinematic Visual States)

> These screenshots capture the website at different scroll depths. The design changes dramatically as you scroll — each frame shows a different cinematic state. Replicate these exact visual transitions.

#### 0% — Hero / Above the fold

![Scroll 0%](screens/scroll/scroll-000.png)

#### 17% — Mid-page at 17% scroll

![Scroll 17%](screens/scroll/scroll-017.png)

#### 33% — Mid-page at 33% scroll

![Scroll 33%](screens/scroll/scroll-033.png)

#### 50% — Mid-page at 50% scroll

![Scroll 50%](screens/scroll/scroll-050.png)

#### 67% — Mid-page at 67% scroll

![Scroll 67%](screens/scroll/scroll-067.png)

#### 83% — Mid-page at 83% scroll

![Scroll 83%](screens/scroll/scroll-083.png)

#### 100% — Footer / End of page

![Scroll 100%](screens/scroll/scroll-100.png)

> Read `references/DESIGN.md` for full token details. Read `references/ANIMATIONS.md` for motion specs. Read `references/LAYOUT.md` for layout structure. Read `references/COMPONENTS.md` for component patterns.

## Ultra Reference Files

This package includes extended documentation. **Read these files before implementing:**

| File | Contents |
|------|----------|
| `references/DESIGN.md` | Full design system tokens, colors, typography, spacing |
| `references/VISUAL_GUIDE.md` | **START HERE** — Master visual guide with all screenshots embedded |
| `references/ANIMATIONS.md` | CSS keyframes, scroll triggers, motion library stack, video specs |
| `references/LAYOUT.md` | Flex/grid containers, page structure, spacing relationships |
| `references/COMPONENTS.md` | DOM component patterns, HTML structure, class fingerprints |
| `references/INTERACTIONS.md` | Hover/focus states with before/after style diffs |
| `screens/scroll/` | 7 scroll journey screenshots showing cinematic states |

### Animation Stack Detected

- **Web Animations API (5 active)** — animation

## Design Philosophy

- **Layered depth** — use shadow tokens to create a sense of physical layering. Each elevation level has a specific shadow.
- **Solid colors only** — no gradients anywhere. Every surface is a single flat color.
- **Single typeface** — Arial Black carries all text. Hierarchy comes from size, weight, and color — never font mixing.
- **compact density** — 4px base grid. Every dimension is a multiple of 4.
- **cool palette** — the color temperature runs cool, matching the sans-serif typography.
- **Restrained accent** — `#a855f7` is the only pop of color. Used exclusively for CTAs, links, focus rings, and active states.
- **Minimal motion** — prefer instant state changes. Only use transitions for loading and page transitions.

## Color System

### Core Palette

| Role | Token | Hex | Use |
|------|-------|-----|-----|
| Background | `--background` | `#ffffff` | Page/app background |
| Surface | `--surface` | `#f0ebfa` | Cards, panels, modals |
| Text Primary | `--text-primary` | `#0b0712` | Headings, body text |
| Text Muted | `--text-muted` | `#a99fc2` | Captions, placeholders |
| Accent | `--accent` | `#a855f7` | CTAs, links, focus rings |

### Extended Palette

- `#c2b9d4`
- `#8b5cf6`
- `#b8c3dc`
- `#150e22` — Deep background layer or shadow color
- `#1e1430`

### CSS Variable Tokens

```css
--background: var(--color-bg-primary);
--foreground: var(--color-text-primary);
--shadow-accent-glow: 0 0 0 1px #8b5cf666,0 0 28px #8b5cf62e;
--color-bg-primary: #f8f4ec;
--color-bg-secondary: #f2ede1;
--color-text-primary: #050505;
--color-text-muted: #1f1f1f;
--color-border-subtle: #00000014;
--nav-capsule-text-muted: #b8c3dc;
--nav-capsule-border: #ffffff1a;
```

## Typography

### Font Stack

- **Arial Black** — Heading 1, Heading 2, Heading 3, Body, Caption

### Type Scale

| Role | Family | Size | Weight |
|------|--------|------|--------|
| Heading 1 | Arial Black | 48px / 3rem | 700 |
| Heading 2 | Arial Black | 32px / 2rem | 600 |
| Heading 3 | Arial Black | 24px / 1.5rem | 600 |
| Body | Arial Black | 16px / 1rem | 400 |
| Caption | Arial Black | 12px / 0.75rem | 400 |

### Typography Rules

- All text uses **Arial Black** — never add another font family
- Max 3-4 font sizes per screen
- Headings: weight 600-700, body: weight 400
- Use color and opacity for text hierarchy, not additional font sizes
- Line height: 1.5 for body, 1.2 for headings

## Spacing & Layout

### Base Grid: 4px

Every dimension (margin, padding, gap, width, height) must be a multiple of **4px**.

### Spacing Scale

`2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 24, 28` px

### Spacing as Meaning

| Spacing | Use |
|---------|-----|
| 4-8px | Tight: related items (icon + label, avatar + name) |
| 12-16px | Medium: between groups within a section |
| 24-32px | Wide: between distinct sections |
| 48px+ | Vast: major page section breaks |

### Border Radius

Scale: `4px, 8px, 12px, 16px, 20px, 22px, 24px, 30px, 693px`
Default: `20px`

## Component Patterns

### Card

```css
.card {
  background: #f0ebfa;
  border-radius: 20px;
  padding: 16px;
  box-shadow: rgba(139, 92, 246, 0.45) 0px 0px 6px 0px;
}
```

```html
<div class="card">
  <h3>Card Title</h3>
  <p>Card content goes here.</p>
</div>
```

### Button

```css
/* Primary */
.btn-primary {
  background: #a855f7;
  color: #0b0712;
  border-radius: 20px;
  padding: 8px 16px;
  font-weight: 500;
  transition: opacity 150ms ease;
}
.btn-primary:hover { opacity: 0.9; }

/* Ghost */
.btn-ghost {
  background: transparent;
  border: 1px solid #cccccc;
  color: #0b0712;
  border-radius: 20px;
  padding: 8px 16px;
}
```

```html
<button class="btn-primary">Get Started</button>
<button class="btn-ghost">Learn More</button>
```

### Input

```css
.input {
  background: #ffffff;
  border: 1px solid #cccccc;
  border-radius: 20px;
  padding: 8px 12px;
  color: #0b0712;
  font-size: 14px;
}
.input:focus { border-color: #a855f7; outline: none; }
```

```html
<input class="input" type="text" placeholder="Search..." />
```

### Badge / Chip

```css
.badge {
  display: inline-flex;
  align-items: center;
  padding: 4px 8px;
  border-radius: 9999px;
  font-size: 12px;
  font-weight: 500;
  background: #f0ebfa;
  color: #a99fc2;
}
```

```html
<span class="badge">New</span>
<span class="badge">Beta</span>
```

### Modal / Dialog

```css
.modal-backdrop { background: rgba(0, 0, 0, 0.6); }
.modal {
  background: #f0ebfa;
  border-radius: 693px;
  padding: 24px;
  max-width: 480px;
  width: 90vw;
  box-shadow: rgba(255, 255, 255, 0.12) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.2) 0px -1px 0px 0px inset, rgba(139, 92, 246, 0.12) 0px 0px 18px 0px;
}
```

```html
<div class="modal-backdrop">
  <div class="modal">
    <h2>Dialog Title</h2>
    <p>Dialog content.</p>
    <button class="btn-primary">Confirm</button>
    <button class="btn-ghost">Cancel</button>
  </div>
</div>
```

### Table

```css
.table { width: 100%; border-collapse: collapse; }
.table th {
  text-align: left;
  padding: 8px 12px;
  font-weight: 500;
  font-size: 12px;
  color: #a99fc2;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  border-bottom: 1px solid #cccccc;
}
.table td {
  padding: 12px;
  border-bottom: 1px solid #cccccc;
}
```

```html
<table class="table">
  <thead><tr><th>Name</th><th>Status</th><th>Date</th></tr></thead>
  <tbody>
    <tr><td>Item One</td><td>Active</td><td>Jan 1</td></tr>
    <tr><td>Item Two</td><td>Pending</td><td>Jan 2</td></tr>
  </tbody>
</table>
```

### Navigation

```css
.nav {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 16px;
}
.nav-link {
  color: #a99fc2;
  padding: 8px 12px;
  border-radius: 20px;
  transition: color 150ms;
}
.nav-link:hover { color: #0b0712; }
.nav-link.active { color: #a855f7; }
```

```html
<nav class="nav">
  <a href="/" class="nav-link active">Home</a>
  <a href="/about" class="nav-link">About</a>
  <a href="/pricing" class="nav-link">Pricing</a>
  <button class="btn-primary" style="margin-left: auto">Get Started</button>
</nav>
```

## Animation & Motion

This project uses **subtle motion**. Transitions smooth state changes without calling attention.

### Motion Guidelines

- **Duration:** 150-300ms for micro-interactions, 300-500ms for page transitions
- **Easing:** `ease-out` for enters, `ease-in` for exits
- **Direction:** Elements enter from bottom/right, exit to top/left
- **Reduced motion:** Always respect `prefers-reduced-motion` — disable animations when set

## Depth & Elevation

### Shadow Tokens

- Subtle: `rgba(139, 92, 246, 0.28) 0px 0px 0px 1px inset`
- Subtle: `rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset`
- Raised (cards, buttons): `rgba(139, 92, 246, 0.45) 0px 0px 6px 0px`
- Floating (dropdowns, popovers): `rgba(255, 255, 255, 0.12) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.2) 0px -1px 0px 0px inset, rgba(139, 92, 246, 0.12) 0px 0px 18px 0px`
- Overlay (modals, dialogs): `rgba(255, 255, 255, 0.22) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.04) 0px -1px 0px 0px inset, rgba(0, 0, 0, 0.35) 0px 14px 40px 0px`
- Overlay (modals, dialogs): `rgba(139, 92, 246, 0.55) 0px 0px 36px -4px, rgba(255, 255, 255, 0.08) 0px 1px 0px 0px inset, rgba(139, 92, 246, 0.32) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0.32) 0px 10px 24px 0px`

## Anti-Patterns (Never Do)

- **No gradients** — solid colors only, everywhere
- **No blur effects** — no backdrop-blur, no filter: blur()
- **No zebra striping** — tables and lists use borders for separation
- **No invented colors** — every hex value must come from the palette above
- **No arbitrary spacing** — every dimension is a multiple of 4px
- **No extra fonts** — only Arial Black are allowed
- **No arbitrary border-radius** — use the scale: 4px, 8px, 12px, 16px, 20px, 22px, 24px, 30px, 693px
- **No opacity for disabled states** — use muted colors instead

## Workflow

1. **Read** `references/DESIGN.md` before writing any UI code
2. **Pick colors** from the Color System section — never invent new ones
3. **Set typography** — Arial Black only, using the type scale
4. **Build layout** on the 4px grid — check every margin, padding, gap
5. **Match components** to patterns above before creating new ones
6. **Apply elevation** — use shadow tokens
7. **Validate** — every value traces back to a design token. No magic numbers.

## Brand Spec

- **Site URL:** `https://aistudiotoday.com`
- **Brand color:** `#a855f7`
- **Brand typeface:** Arial Black

## Quick Reference

```
Background:     #ffffff
Surface:        #f0ebfa
Text:           #0b0712 / #a99fc2
Accent:         #a855f7
Border:         (not extracted)
Font:           Arial Black
Spacing:        4px grid
Radius:         20px
Components:     0 detected
```

## When to Trigger

Activate this skill when:
- Creating new components, pages, or visual elements for AI Studio Today
- Writing CSS, Tailwind classes, styled-components, or inline styles
- Building page layouts, templates, or responsive designs
- Reviewing UI code for design consistency
- The user mentions "AI Studio Today" design, style, UI, or theme
- Generating mockups, wireframes, or visual prototypes

---

# Full Reference Files

> Every output file is embedded below. Claude has full design system context from /skills alone.

## Design System Tokens (DESIGN.md)

# AI Studio Today DESIGN.md

> Auto-generated design system — reverse-engineered via static analysis by skillui.
> Frameworks: None detected
> Colors: 10 · Fonts: 1 · Components: 0
> Icon library: not detected · State: not detected
> Primary theme: light · Dark mode toggle: no · Motion: none

---

## 1. Visual Theme & Atmosphere

This is a **light-themed** interface with a cool, approachable feel. The light background emphasizes content clarity. Typography uses **Arial Black** throughout — a clean, modern choice that maintains consistency. Spacing follows a **4px base grid** (compact density), with scale: 2, 4, 6, 8, 10, 12, 14, 16px. The palette is predominantly monochromatic with **#a855f7** as the single accent color — used sparingly for interactive elements and emphasis.

---

## 2. Color Palette & Roles

| Token | Hex | Role | Use |
|---|---|---|---|
| background | `#ffffff` | background | Page background, darkest surface |
| surface | `#f0ebfa` | surface | Card and panel backgrounds |
| text-primary | `#0b0712` | text-primary | Headings and body text |
| text-muted | `#a99fc2` | text-muted | Captions, placeholders, secondary info |
| accent | `#a855f7` | accent | CTAs, links, focus rings, active states |
| info | `#8b5cf6` | info | Informational highlights |
| unknown | `#c2b9d4` | unknown | Palette color |
| unknown | `#b8c3dc` | unknown | Palette color |
| unknown | `#150e22` | unknown | Palette color |
| unknown | `#1e1430` | unknown | Palette color |

### CSS Variable Tokens

```css
--background: var(--color-bg-primary);
--foreground: var(--color-text-primary);
--shadow-accent-glow: 0 0 0 1px #8b5cf666,0 0 28px #8b5cf62e;
--color-bg-primary: #f8f4ec;
--color-bg-secondary: #f2ede1;
--color-text-primary: #050505;
--color-text-muted: #1f1f1f;
--color-border-subtle: #00000014;
--nav-capsule-text-muted: #b8c3dc;
--nav-capsule-border: #ffffff1a;
```


---

## 3. Typography Rules

**Font Stack:**
- **Arial Black** — Heading 1, Heading 2, Heading 3, Body, Caption

| Role | Font | Size | Weight |
|---|---|---|---|
| Heading 1 | Arial Black | 48px / 3rem | 700 |
| Heading 2 | Arial Black | 32px / 2rem | 600 |
| Heading 3 | Arial Black | 24px / 1.5rem | 600 |
| Body | Arial Black | 16px / 1rem | 400 |
| Caption | Arial Black | 12px / 0.75rem | 400 |

**Typographic Rules:**
- Use **Arial Black** for all text — do not mix font families
- Maintain consistent hierarchy: no more than 3-4 font sizes per screen
- Headings use bold (600-700), body uses regular (400)
- Line height: 1.5 for body text, 1.2 for headings
- Use color and opacity for secondary hierarchy, not additional font sizes


---

## 4. Component Stylings

No components detected. Scan `src/components/` or `components/` to populate this section.

---

## 5. Layout Principles

- **Base spacing unit:** 4px
- **Spacing scale:** 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 24, 28
- **Border radius:** 4px, 8px, 12px, 16px, 20px, 22px, 24px, 30px, 693px

**Spacing as Meaning:**
| Spacing | Use |
|---|---|
| 4-8px | Tight: related items within a group |
| 12-16px | Medium: between groups |
| 24-32px | Wide: between sections |
| 48px+ | Vast: major section breaks |


---

## 6. Depth & Elevation

### Flat — subtle depth hints

- `rgba(139, 92, 246, 0.28) 0px 0px 0px 1px inset`
- `rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset`

### Raised — cards, buttons, interactive elements

- `rgba(139, 92, 246, 0.45) 0px 0px 6px 0px`

### Floating — dropdowns, popovers, modals

- `rgba(255, 255, 255, 0.12) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.2) 0px -1px 0px 0px inset, rgba(139, 92, 246, 0.12) 0px 0px 18px 0px`

### Overlay — full-screen overlays, top-level dialogs

- `rgba(255, 255, 255, 0.22) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.04) 0px -1px 0px 0px inset, rgba(0, 0, 0, 0.35) 0px 14px 40px 0px`
- `rgba(139, 92, 246, 0.55) 0px 0px 36px -4px, rgba(255, 255, 255, 0.08) 0px 1px 0px 0px inset, rgba(139, 92, 246, 0.32) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0.32) 0px 10px 24px 0px`
- `rgba(255, 255, 255, 0.42) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.22) 0px -1px 0px 0px inset, rgba(255, 255, 255, 0.12) 0px 0px 0px 1px, rgba(139, 92, 246, 0.45) 0px 10px 24px 0px, rgba(168, 85, 247, 0.35) 0px 0px 40px 0px`



---

## 8. Do's and Don'ts

### Do's

- Use `#a855f7` for interactive elements (buttons, links, focus rings)
- Use `#ffffff` as the primary page background
- Use **Arial Black** for all UI text
- Follow the **4px** spacing grid for all margins, padding, and gaps
- Use the defined shadow tokens for elevation — see Section 6
- Use border-radius from the scale: 4px, 8px, 12px, 16px, 20px

### Don'ts

- Don't introduce colors outside this palette — extend the design tokens first
- Don't mix font families — use Arial Black consistently
- Don't use arbitrary spacing values — stick to multiples of 4px
- Don't create custom box-shadow values outside the system tokens
- Don't use gradients — the design uses solid colors only
- Don't use arbitrary border-radius values — pick from the defined scale
- Don't use backdrop-blur or blur effects

### Anti-Patterns (detected from codebase)

- No gradient backgrounds
- No blur or backdrop-blur effects
- No zebra striping on tables/lists


---

## 9. Responsive Behavior

No breakpoints detected. Consider adding responsive breakpoints to the design system.

---

## 10. Agent Prompt Guide

Use these as starting points when building new UI:

### Build a Card

```
Background: #f0ebfa
Border: 1px solid var(--border)
Radius: 20px
Padding: 16px
Font: Arial Black
Use shadow tokens from Section 6.
```

### Build a Button

```
Primary: bg #a855f7, text white
Ghost: bg transparent, border var(--border)
Padding: 8px 16px
Radius: 20px
Hover: opacity 0.9 or lighter shade
Focus: ring with #a855f7
```

### Build a Page Layout

```
Background: #ffffff
Max-width: 1280px, centered
Grid: 4px base
Responsive: mobile-first, breakpoints from Section 9
```

### Build a Stats Card

```
Surface: #f0ebfa
Label: #a99fc2 (muted, 12px, uppercase)
Value: #0b0712 (primary, 24-32px, bold)
Status: use success/warning/danger from Section 2
```

### Build a Form

```
Input bg: #ffffff
Input border: 1px solid var(--border)
Focus: border-color #a855f7
Label: #a99fc2 12px
Spacing: 16px between fields
Radius: 20px
```

### General Component

```
1. Read DESIGN.md Sections 2-6 for tokens
2. Colors: only from palette
3. Font: Arial Black, type scale from Section 3
4. Spacing: 4px grid
5. Components: match patterns from Section 4
6. Elevation: shadow tokens
```

## Visual Guide — Screenshots (VISUAL_GUIDE.md)

# AI Studio Today — Visual Guide

> Master visual reference. Study every screenshot carefully before implementing any UI.
> Match colors, layout, typography, spacing, and motion states exactly.

**Motion Stack:** **Web Animations API (5 active)**

**WebGL/3D:** Detected (1 canvas elements) — replicate with Three.js or CSS 3D transforms

## Scroll Journey

The page has cinematic scroll animations. Each screenshot below shows the exact visual state at that scroll depth.
**Replicate these transitions precisely** — the design changes dramatically as you scroll.

### Hero — Above the fold

*Scroll position: 0px of 11360px total*

![Hero — Above the fold](../screens/scroll/scroll-000.png)

### 17% scroll depth

*Scroll position: 1778px of 11360px total*

![17% scroll depth](../screens/scroll/scroll-017.png)

### 33% scroll depth

*Scroll position: 3452px of 11360px total*

![33% scroll depth](../screens/scroll/scroll-033.png)

### 50% scroll depth

*Scroll position: 5230px of 11360px total*

![50% scroll depth](../screens/scroll/scroll-050.png)

### 67% scroll depth

*Scroll position: 7008px of 11360px total*

![67% scroll depth](../screens/scroll/scroll-067.png)

### 83% scroll depth

*Scroll position: 8682px of 11360px total*

![83% scroll depth](../screens/scroll/scroll-083.png)

### Footer — End of page

*Scroll position: 10460px of 11360px total*

![Footer — End of page](../screens/scroll/scroll-100.png)

## Full Page Screenshots

### AI Studio Today — AI Growth Systems & AI Marketing Agency

*URL: `https://aistudiotoday.com`*

![AI Studio Today — AI Growth Systems & AI Marketing Agency](../screens/pages/home.png)

## Section Screenshots

Clipped sections showing individual components in context.

### Section 1 — `section`

*1440×990px*

![Section 1](../screens/sections/home-section-1.png)

## Animations & Motion (ANIMATIONS.md)

# Animation Reference

> Cinematic motion design extracted from live DOM. Follow these specs exactly to recreate the experience.

## Motion Technology Stack

| Library | Type | Notes |
|---------|------|-------|
| **Web Animations API (5 active)** | animation |  |
| Canvas (1 elements) | WebGL/3D | WebGL context detected — likely Three.js or custom shader |

## Scroll Journey

The page is **11,360px** tall. Each frame below shows what the user sees at that scroll depth.

> **Use these screenshots to understand WHAT animates, WHEN it animates, and HOW it moves.**

### 0% — Top / Hero
Scroll position: 0px

![Scroll 0%](../screens/scroll/scroll-000.png)

### 17% — Opening Section
Scroll position: 1,778px

![Scroll 17%](../screens/scroll/scroll-017.png)

### 33% — First Feature Section
Scroll position: 3,452px

![Scroll 33%](../screens/scroll/scroll-033.png)

### 50% — Mid-Page
Scroll position: 5,230px

![Scroll 50%](../screens/scroll/scroll-050.png)

### 67% — Lower Content
Scroll position: 7,008px

![Scroll 67%](../screens/scroll/scroll-067.png)

### 83% — Near Footer
Scroll position: 8,682px

![Scroll 83%](../screens/scroll/scroll-083.png)

### 100% — Bottom / Footer
Scroll position: 10,460px

![Scroll 100%](../screens/scroll/scroll-100.png)

## Scroll Animation Patterns

| Pattern | Library | Element Count | Duration | Delay | Easing |
|---------|---------|---------------|----------|-------|--------|
| parallax / sticky scroll | CSS | 1 | — | — | — |

### CSS Implementation

## CSS Keyframes (13 extracted)

### `@keyframes ambient-drift-a`

Duration: `18s` · Easing: `ease-in-out` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.hero-ambient-blob--a`, `.ambient-drift-a`

```css
@keyframes ambient-drift-a {
  0% {
    transform: translate(-6%, -3%) scale(1.06);
  }
  50% {
    transform: translate(7%, 4%) scale(1.12);
  }
  100% {
    transform: translate(-6%, -3%) scale(1.06);
  }
}
```

> Transform/motion animation

### `@keyframes ambient-drift-b`

Duration: `23s` · Easing: `ease-in-out` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.hero-ambient-blob--b`, `.ambient-drift-b`

```css
@keyframes ambient-drift-b {
  0% {
    transform: translate(5%, 4%) scale(1.1);
  }
  50% {
    transform: translate(-7%, -3%) scale(1.04);
  }
  100% {
    transform: translate(5%, 4%) scale(1.1);
  }
}
```

> Transform/motion animation

### `@keyframes liquid-pill-sheen`

Duration: `5s` · Easing: `ease-in-out` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.liquid-pill::after`

```css
@keyframes liquid-pill-sheen {
  0%, 8% {
    transform: translate(-200%);
  }
  50% {
    transform: translate(100%);
  }
  92%, 100% {
    transform: translate(300%);
  }
}
```

> Transform/motion animation

### `@keyframes nav-capsule-breath`

Duration: `4.5s` · Easing: `ease-in-out` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.nav-capsule-lit`

```css
@keyframes nav-capsule-breath {
  0%, 100% {
    box-shadow: inset 0 1px 0 var(--nav-capsule-highlight),inset 0 0 0 1px var(--nav-capsule-glow),inset 0 0 22px var(--nav-capsule-glow-fill);
  }
  50% {
    box-shadow: inset 0 1px 0 var(--nav-capsule-highlight-strong),inset 0 0 0 1px var(--nav-capsule-glow-strong),inset 0 0 30px var(--nav-capsule-glow-fill-strong);
  }
}
```

> Shadow pulse/glow effect

### `@keyframes nav-text-breath`

Duration: `4.5s` · Easing: `ease-in-out` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.nav-text-lit`

```css
@keyframes nav-text-breath {
  0%, 100% {
    text-shadow: 0 0 var(--nav-text-glow-spread-rest) var(--nav-text-glow);
  }
  50% {
    text-shadow: 0 0 var(--nav-text-glow-spread-peak) var(--nav-text-glow-strong);
  }
}
```

### `@keyframes swipe-out-left`

Used by: `[data-sonner-toast][data-swipe-out="true"][data-swipe-direction="left"]`

```css
@keyframes swipe-out-left {
  0% {
    transform: var(--y) translateX(var(--swipe-amount-x));
    opacity: 1;
  }
  100% {
    transform: var(--y) translateX(calc(var(--swipe-amount-x) - 100%));
    opacity: 0;
  }
}
```

> Fade + motion enter animation

### `@keyframes swipe-out-right`

Used by: `[data-sonner-toast][data-swipe-out="true"][data-swipe-direction="right"]`

```css
@keyframes swipe-out-right {
  0% {
    transform: var(--y) translateX(var(--swipe-amount-x));
    opacity: 1;
  }
  100% {
    transform: var(--y) translateX(calc(var(--swipe-amount-x) + 100%));
    opacity: 0;
  }
}
```

> Fade + motion enter animation

### `@keyframes swipe-out-up`

Used by: `[data-sonner-toast][data-swipe-out="true"][data-swipe-direction="up"]`

```css
@keyframes swipe-out-up {
  0% {
    transform: var(--y) translateY(var(--swipe-amount-y));
    opacity: 1;
  }
  100% {
    transform: var(--y) translateY(calc(var(--swipe-amount-y) - 100%));
    opacity: 0;
  }
}
```

> Fade + motion enter animation

### `@keyframes swipe-out-down`

Used by: `[data-sonner-toast][data-swipe-out="true"][data-swipe-direction="down"]`

```css
@keyframes swipe-out-down {
  0% {
    transform: var(--y) translateY(var(--swipe-amount-y));
    opacity: 1;
  }
  100% {
    transform: var(--y) translateY(calc(var(--swipe-amount-y) + 100%));
    opacity: 0;
  }
}
```

> Fade + motion enter animation

### `@keyframes sonner-fade-in`

Duration: `0.3s` · Easing: `ease` · Delay: `0s` · Iteration: `1` · Fill: `forwards`

Used by: `[data-sonner-toast][data-promise="true"] [data-icon] > svg`

```css
@keyframes sonner-fade-in {
  0% {
    opacity: 0;
    transform: scale(0.8);
  }
  100% {
    opacity: 1;
    transform: scale(1);
  }
}
```

> Fade + motion enter animation

### `@keyframes sonner-fade-out`

Duration: `0.2s` · Easing: `ease` · Delay: `0s` · Iteration: `1` · Fill: `forwards`

Used by: `.sonner-loading-wrapper[data-visible="false"]`

```css
@keyframes sonner-fade-out {
  0% {
    opacity: 1;
    transform: scale(1);
  }
  100% {
    opacity: 0;
    transform: scale(0.8);
  }
}
```

> Fade + motion enter animation

### `@keyframes sonner-spin`

Duration: `1.2s` · Easing: `linear` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.sonner-loading-bar`

```css
@keyframes sonner-spin {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0.15;
  }
}
```

> Opacity fade

### `@keyframes spin`

```css
@keyframes spin {
  100% {
    transform: rotate(1turn);
  }
}
```

> Transform/motion animation

## Motion Tokens (CSS Variables)

### Duration Tokens

```css
--default-transition-duration: .15s;
```

### Easing Tokens

```css
--ease-in: cubic-bezier(.4,0,1,1);
--default-transition-timing-function: cubic-bezier(.4,0,.2,1);
--ease-out: cubic-bezier(0,0,.2,1);
```

## Global Transition Declarations

These `transition` values were extracted from CSS rules across the site:

```css
transition: transform 0.4s, box-shadow 0.4s;
transition: opacity 0.4s;
transition: transform 0.2s, box-shadow 0.3s, filter 0.3s;
transition: border-color 0.3s, box-shadow 0.3s, color 0.3s;
transition: background 0.25s, box-shadow 0.25s, color 0.25s;
transition: border-color 0.25s, box-shadow 0.25s;
transition: opacity 0.24s ease-out, transform 0.24s ease-out;
transition: transform 0.22s ease-out, box-shadow 0.22s ease-out;
transition: border-color 0.3s, box-shadow 0.3s, background 0.3s;
transition: left 0.4s cubic-bezier(0.4, 0, 0.2, 1), background 0.4s, box-shadow 0.4s;
transition: transform 0.4s;
transition: transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s;
```

## How to Recreate This Motion Design

### Step 1 — Install Dependencies

```bash
```

### Step 2 — Scroll-Reveal Pattern

Elements that animate into view follow this pattern:

```css
/* Initial hidden state */
.reveal {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity .15s cubic-bezier(.4,0,1,1),
              transform .15s cubic-bezier(.4,0,1,1);
}
.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}
```

### Step 3 — Key Motion Principles

- **WebGL/3D layer detected** — product visualizations use Three.js or custom WebGL. Use `<canvas>` with Three.js for 3D product renders
- **Canvas elements (1)** — animated via requestAnimationFrame loop. Use canvas for particle effects, gradient animations, and WebGL scenes
- **Duration scale:** `.15s` · `0.4s` · `0.2s` · `0.3s` — use these values, never invent new durations
- **Always add** `@media (prefers-reduced-motion: reduce) { * { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; } }`

### Step 4 — Scroll Journey Reference

Match what happens at each scroll position:

- **0%** (`0px`) → `screens/scroll/scroll-000.png`
- **17%** (`1778px`) → `screens/scroll/scroll-017.png`
- **33%** (`3452px`) → `screens/scroll/scroll-033.png`
- **50%** (`5230px`) → `screens/scroll/scroll-050.png`
- **67%** (`7008px`) → `screens/scroll/scroll-067.png`
- **83%** (`8682px`) → `screens/scroll/scroll-083.png`
- **100%** (`10460px`) → `screens/scroll/scroll-100.png`

## Layout & Grid (LAYOUT.md)

# Layout Reference

> Auto-extracted from live DOM. Use this to understand how the site is structured spatially.

## Spacing System

**Base grid:** 4px

**Scale:** `2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 24, 28, 32, 40, 48` px

| Spacing | Semantic Use |
|---------|-------------|
| 4px | Tight — within a component |
| 8px | Medium — between sibling items |
| 16px | Wide — between sections |
| 32px | Vast — major section breaks |

## Flex Layouts

| Element | Direction | Justify | Align | Gap | Children |
|---------|-----------|---------|-------|-----|----------|
| `body.flex.min-h-dvh` | column | — | — | — | 57 |
| `section.relative.isolate` | row | — | center | — | 3 |
| `div.relative.z-10` | row | center | — | — | 1 |
| `span.inline-flex.items-center` | row | — | center | 8px | 2 |
| `div.h-[60rem].md:h-[80rem]` | row | center | center | — | 1 |
| `div.flex.flex-col` | column | — | start | 16px | 1 |
| `div.mx-auto.max-w-5xl` | column | — | center | 32px | 4 |
| `div.mx-auto.max-w-4xl` | column | — | center | 24px | 3 |
| `div.flex.max-w-3xl` | column | — | start | 24px | 3 |
| `div.flex.flex-col` | column | — | center | 16px | 1 |
| `div.mt-16.flex` | row | center | — | 20px | 4 |
| `div.mx-auto.flex` | column | — | — | — | 3 |
| `div.flex.flex-col` | column | — | start | 16px | 1 |
| `ul.mt-10.flex` | column | — | — | 8px | 6 |
| `div.col-span-2.md:col-span-2` | column | — | — | 16px | 2 |

## Grid Layouts

| Element | Template Columns | Gap | Children |
|---------|-----------------|-----|----------|
| `div.grid.grid-cols-2` | `172px 172px 172px 172px 172px 172px` | 40px | 5 |
| `div.mt-14.grid` | `270px 270px 270px 270px` | 24px | 4 |
| `div.grid.gap-6` | `505.672px 702.328px` | 24px | 2 |
| `div.mt-12.grid` | `84.3281px 84.3281px 84.3281px 84.3281px 84.3281px ` | 20px | 4 |
| `ol.grid.grid-cols-1` | `240px 240px 240px 240px 240px` | 8px | 5 |

## Structural Containers

### `<header>` (`header.sticky.top-3`)

```
display:          block
children:         1
```

### `<footer>` (`footer.border-t.border-border-subtle`)

```
display:          block
children:         1
```

### `<section>` (`section.relative.isolate`)

```
display:          flex
flex-direction:   row
justify-content:  —
align-items:      center
children:         3
```

### `<section>` (`section.overflow-hidden.border-b`)

```
display:          block
children:         1
```

### `<section>` (`section.relative.py-24`)

```
display:          block
padding:          128px 0px
children:         1
```

### `<section>` (`section#industries.border-y.border-border-subtle`)

```
display:          block
children:         1
```

### `<section>` (`section.mx-auto.max-w-7xl`)

```
display:          block
padding:          128px 24px
max-width:        1280px
children:         2
```

### `<section>` (`section.border-b.border-border-subtle`)

```
display:          block
children:         1
```

### `<section>` (`section.dark-bg-flourish.relative`)

```
display:          block
children:         2
```

### `<section>` (`section.dark-bg-flourish.border-t`)

```
display:          block
children:         1
```

### `<section>` (`section#solution.relative.h-screen`)

```
display:          block
max-width:        1440px
children:         1
```

### `<article>` (`article.problem-card.group`)

```
display:          block
max-width:        260px
children:         3
```

## Layout Rules

- **Container max-width:** `1280px` — always center with `margin: auto`
- Primary layout system: **Flexbox**
- Secondary layout system: **CSS Grid** (used for card grids and multi-column layouts)
- Every spacing value must be a multiple of **4px**
- Never use arbitrary margin/padding values outside the spacing scale

## Component Patterns (COMPONENTS.md)

# Component Reference

> Repeated DOM patterns detected by structural analysis. Each component appeared 3+ times.

## Detected Components

| Component | Category | Instances | Key Classes |
|-----------|----------|-----------|-------------|
| **Nav Mega Item** | card | 8× | `.nav-mega-item` |
| **Flex** | unknown | 8× | `.flex`, `.gap-3`, `.group/mi` |
| **Min W 0** | unknown | 8× | `.min-w-0` |
| **Block** | unknown | 8× | `.block`, `.font-semibold`, `.text-sm` |
| **Block** | unknown | 8× | `.block`, `.leading-snug`, `.mt-0.5` |
| **Font Normal** | unknown | 5× | `.font-normal`, `.font-pro`, `.leading-[1.1]` |
| **Flex** | card | 5× | `.flex`, `.flex-col`, `.h-full` |
| **Flex** | card | 5× | `.flex`, `.flex-col`, `.gap-1` |
| **Font Display** | unknown | 5× | `.font-display`, `.font-semibold`, `.leading-tight` |
| **Leading 5** | unknown | 5× | `.leading-5`, `.text-sm`, `.text-text-muted` |
| **Aspect [3/4]** | card | 4× | `.aspect-[3/4]`, `.cursor-pointer`, `.group` |
| **Duration 700** | form-field | 4× | `.duration-700`, `.ease-out`, `.group-hover:scale-[1.06]` |
| **Absolute** | unknown | 4× | `.absolute`, `.bg-gradient-to-t`, `.from-black/85` |
| **Absolute** | unknown | 4× | `.absolute`, `.bottom-0`, `.inset-x-0` |
| **Font Display** | unknown | 4× | `.font-display`, `.font-semibold`, `.leading-snug` |
| **Leading [1.65]** | unknown | 4× | `.leading-[1.65]`, `.text-sm`, `.text-text-muted` |
| **Active:Scale [0.98]** | unknown | 3× | `.active:scale-[0.98]`, `.bg-transparent`, `.border` |
| **Flex** | card | 3× | `.flex`, `.gap-1`, `.items-center` |
| **Font Bold** | unknown | 3× | `.font-bold`, `.nav-text-lit`, `.px-4` |
| **Translate X 1/2** | badge | 3× | `.-translate-x-1/2`, `.absolute`, `.bottom-[58%]` |

## Cards

### Nav Mega Item

**Instances found:** 8

**CSS classes:** `.nav-mega-item`

**HTML structure:**

```html
<li class="nav-mega-item" style="transition-delay:60ms"><a role="menuitem" class="group/mi flex gap-3 rounded-xl p-3 transition-colors hover:bg-white/[0.06]" href="/en/ai-marketing-ugc"><span class="nav-mega-icon mt-0.5 inline-flex h-9 w-9 shrink-0 items-center justify-center rounded-lg"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-clapperboard size-[18px]" aria-hidden="true"><path d="M20.2 6 3 11l-.9-2.4c-.3-1.1.3-2.2 1.3-2.5l13.5-4c1.1-.
```

**Base styles (from design tokens):**

```css
.nav-mega-item {
  background: #f0ebfa;
  border-radius: 20px;
  padding: 8px;
}```

### Flex

**Instances found:** 5

**CSS classes:** `.flex` `.flex-col` `.h-full` `.items-center` `.justify-center` `.relative`

**HTML structure:**

```html
<li class="relative flex h-full flex-col items-center justify-center"><div class="flow-chip pointer-events-none absolute bottom-[58%] left-1/2 -translate-x-1/2" style="transform: translate(-67.4141px, 8px); translate: none; rotate: none; scale: none; opacity: 0;"><div class="flex flex-col items-center gap-1 rounded-xl liquid-glass px-4 py-2.5 whitespace-nowrap"><span class="font-mono text-xs uppercase tracking-[0.12em] text-text-dim">01</span><span class="font-display text-lg font-semibold leading-tight text-text-primary">AuditOS</span><span class="text-sm leading-5 text-text-muted">Score the 
```

**Base styles (from design tokens):**

```css
.flex {
  background: #f0ebfa;
  border-radius: 20px;
  padding: 8px;
}```

### Flex

**Instances found:** 5

**CSS classes:** `.flex` `.flex-col` `.gap-1` `.items-center` `.liquid-glass` `.px-4`

**HTML structure:**

```html
<div class="flex flex-col items-center gap-1 rounded-xl liquid-glass px-4 py-2.5 whitespace-nowrap"><span class="font-mono text-xs uppercase tracking-[0.12em] text-text-dim">01</span><span class="font-display text-lg font-semibold leading-tight text-text-primary">AuditOS</span><span class="text-sm leading-5 text-text-muted">Score the funnel</span></div>
```

**Base styles (from design tokens):**

```css
.flex {
  background: #f0ebfa;
  border-radius: 20px;
  padding: 8px;
}```

### Aspect [3/4]

**Instances found:** 4

**CSS classes:** `.aspect-[3/4]` `.cursor-pointer` `.group` `.max-w-[260px]` `.overflow-hidden` `.problem-card`

**HTML structure:**

```html
<article class="problem-card group relative w-[44vw] max-w-[260px] md:w-[200px] lg:w-[230px] aspect-[3/4] rounded-3xl overflow-hidden cursor-pointer" style="transform: translate(0px, 80px) scale(0.85, 0.85); transform-style: preserve-3d; transition: transform 0.6s cubic-bezier(0.22, 0.61, 0.36, 1); box-shadow: rgba(0, 0, 0, 0.35) 0px 12px 36px, rgba(0, 0, 0, 0.25) 0px 2px 8px; translate: none; rotate: none; scale: none; opacity: 0;" data-tilt="-22"><img alt="Red ink swirling in water — speed of reply" loading="lazy" decoding="async" data-nimg="fill" class="object-cover transition-transform dur
```

**Base styles (from design tokens):**

```css
.aspect-[3/4] {
  background: #f0ebfa;
  border-radius: 20px;
  padding: 8px;
}```

### Flex

**Instances found:** 3

**CSS classes:** `.flex` `.gap-1` `.items-center` `.relative`

**HTML structure:**

```html
<li class="relative flex items-center gap-1" role="none"><span aria-hidden="true" class="nav-item-dot"></span><a role="menuitem" class="px-4 py-1.5 nav-text-lit text-sm font-bold text-text-muted hover:text-text-primary transition-colors" href="/en/work">Work</a></li>
```

**Base styles (from design tokens):**

```css
.flex {
  background: #f0ebfa;
  border-radius: 20px;
  padding: 8px;
}```

## Badges & Chips

### Translate X 1/2

**Instances found:** 3

**CSS classes:** `.-translate-x-1/2` `.absolute` `.bottom-[58%]` `.flow-chip` `.left-1/2` `.pointer-events-none`

**HTML structure:**

```html
<div class="flow-chip pointer-events-none absolute bottom-[58%] left-1/2 -translate-x-1/2" style="transform: translate(-67.4141px, 8px); translate: none; rotate: none; scale: none; opacity: 0;"><div class="flex flex-col items-center gap-1 rounded-xl liquid-glass px-4 py-2.5 whitespace-nowrap"><span class="font-mono text-xs uppercase tracking-[0.12em] text-text-dim">01</span><span class="font-display text-lg font-semibold leading-tight text-text-primary">AuditOS</span><span class="text-sm leading-5 text-text-muted">Score the funnel</span></div></div>
```

**Base styles (from design tokens):**

```css
.-translate-x-1/2 {
  background: #f0ebfa;
  border-radius: 20px;
  padding: 2px 4px;
  font-size: 12px;
}```

## Form Fields

### Duration 700

**Instances found:** 4

**CSS classes:** `.duration-700` `.ease-out` `.group-hover:scale-[1.06]` `.object-cover` `.transition-transform`

**HTML structure:**

```html
<img alt="Red ink swirling in water — speed of reply" loading="lazy" decoding="async" data-nimg="fill" class="object-cover transition-transform duration-700 ease-out group-hover:scale-[1.06]" style="position:absolute;height:100%;width:100%;left:0;top:0;right:0;bottom:0;color:transparent" sizes="(min-width: 1024px) 230px, (min-width: 768px) 200px, 44vw" srcset="/_next/image?url=%2Fimages%2Fproblems%2F01-red-ink.webp&amp;w=384&amp;q=75 384w, /_next/image?url=%2Fimages%2Fproblems%2F01-red-ink.webp&amp;w=640&amp;q=75 640w, /_next/image?url=%2Fimages%2Fproblems%2F01-red-ink.webp&amp;w=750&amp;q=75 
```

**Base styles (from design tokens):**

```css
.duration-700 {
  background: #f0ebfa;
  padding: 4px;
}```

## Other Components

### Flex

**Instances found:** 8

**CSS classes:** `.flex` `.gap-3` `.group/mi` `.p-3` `.rounded-xl` `.transition-colors`

**HTML structure:**

```html
<a role="menuitem" class="group/mi flex gap-3 rounded-xl p-3 transition-colors hover:bg-white/[0.06]" href="/en/ai-marketing-ugc"><span class="nav-mega-icon mt-0.5 inline-flex h-9 w-9 shrink-0 items-center justify-center rounded-lg"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-clapperboard size-[18px]" aria-hidden="true"><path d="M20.2 6 3 11l-.9-2.4c-.3-1.1.3-2.2 1.3-2.5l13.5-4c1.1-.3 2.2.3 2.5 1.3Z"></path><path d="m6.2 5.3 3.1 3.9"></pa
```

**Base styles (from design tokens):**

```css
.flex {
  background: #f0ebfa;
  padding: 4px;
}```

### Min W 0

**Instances found:** 8

**CSS classes:** `.min-w-0`

**HTML structure:**

```html
<span class="min-w-0"><span class="block text-sm font-semibold text-text-primary">UGC Videos + AI Marketing</span><span class="mt-0.5 block text-xs leading-snug text-text-muted">Scroll-stopping AI video + paid creative…</span></span>
```

**Base styles (from design tokens):**

```css
.min-w-0 {
  background: #f0ebfa;
  padding: 4px;
}```

### Block

**Instances found:** 8

**CSS classes:** `.block` `.font-semibold` `.text-sm` `.text-text-primary`

**HTML structure:**

```html
<span class="block text-sm font-semibold text-text-primary">UGC Videos + AI Marketing</span>
```

**Base styles (from design tokens):**

```css
.block {
  background: #f0ebfa;
  padding: 4px;
}```

### Block

**Instances found:** 8

**CSS classes:** `.block` `.leading-snug` `.mt-0.5` `.text-text-muted` `.text-xs`

**HTML structure:**

```html
<span class="mt-0.5 block text-xs leading-snug text-text-muted">Scroll-stopping AI video + paid creative.</span>
```

**Base styles (from design tokens):**

```css
.block {
  background: #f0ebfa;
  padding: 4px;
}```

### Font Normal

**Instances found:** 5

**CSS classes:** `.font-normal` `.font-pro` `.leading-[1.1]` `.text-3xl` `.text-text-primary` `.tracking-tight`

**HTML structure:**

```html
<h2 class="font-pro font-normal tracking-tight text-3xl md:text-4xl leading-[1.1] text-text-primary">Why most businesses lose 60% of their leads</h2>
```

**Base styles (from design tokens):**

```css
.font-normal {
  background: #f0ebfa;
  padding: 4px;
}```

### Font Display

**Instances found:** 5

**CSS classes:** `.font-display` `.font-semibold` `.leading-tight` `.text-lg` `.text-text-primary`

**HTML structure:**

```html
<span class="font-display text-lg font-semibold leading-tight text-text-primary">AuditOS</span>
```

**Base styles (from design tokens):**

```css
.font-display {
  background: #f0ebfa;
  padding: 4px;
}```

### Leading 5

**Instances found:** 5

**CSS classes:** `.leading-5` `.text-sm` `.text-text-muted`

**HTML structure:**

```html
<span class="text-sm leading-5 text-text-muted">Score the funnel</span>
```

**Base styles (from design tokens):**

```css
.leading-5 {
  background: #f0ebfa;
  padding: 4px;
}```

### Absolute

**Instances found:** 4

**CSS classes:** `.absolute` `.bg-gradient-to-t` `.from-black/85` `.inset-0` `.to-transparent` `.via-black/30`

**HTML structure:**

```html
<div class="absolute inset-0 bg-gradient-to-t from-black/85 via-black/30 to-transparent"></div>
```

**Base styles (from design tokens):**

```css
.absolute {
  background: #f0ebfa;
  padding: 4px;
}```

### Absolute

**Instances found:** 4

**CSS classes:** `.absolute` `.bottom-0` `.inset-x-0` `.p-5`

**HTML structure:**

```html
<div class="absolute inset-x-0 bottom-0 p-5 md:p-6"><h3 class="font-display text-lg md:text-xl font-semibold text-white leading-snug">Slow replies kill deals</h3></div>
```

**Base styles (from design tokens):**

```css
.absolute {
  background: #f0ebfa;
  padding: 4px;
}```

### Font Display

**Instances found:** 4

**CSS classes:** `.font-display` `.font-semibold` `.leading-snug` `.text-lg` `.text-white`

**HTML structure:**

```html
<h3 class="font-display text-lg md:text-xl font-semibold text-white leading-snug">Slow replies kill deals</h3>
```

**Base styles (from design tokens):**

```css
.font-display {
  background: #f0ebfa;
  padding: 4px;
}```

### Leading [1.65]

**Instances found:** 4

**CSS classes:** `.leading-[1.65]` `.text-sm` `.text-text-muted`

**HTML structure:**

```html
<p class="text-sm text-text-muted leading-[1.65] md:text-center">Leads expect a response in under 5 minutes. Most businesses take 5+ hours, and the lead is already someone else's customer.</p>
```

**Base styles (from design tokens):**

```css
.leading-[1.65] {
  background: #f0ebfa;
  padding: 4px;
}```

### Active:Scale [0.98]

**Instances found:** 3

**CSS classes:** `.active:scale-[0.98]` `.bg-transparent` `.border` `.border-white/15` `.disabled:cursor-not-allowed` `.disabled:opacity-50`

**HTML structure:**

```html
<a class="inline-flex items-center gap-2 font-medium transition-[transform,background-color,border-color,box-shadow,color] duration-200 ease-out focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent disabled:opacity-50 disabled:cursor-not-allowed disabled:pointer-events-none select-none rounded-full border border-white/15 bg-transparent text-text-primary hover:border-white/30 hover:bg-white/[0.04] hover:text-white active:scale-[0.98] h-9 px-4 justify-center text-xs" href="/en/services">See all Services</a>
```

**Base styles (from design tokens):**

```css
.active:scale-[0.98] {
  background: #f0ebfa;
  padding: 4px;
}```

### Font Bold

**Instances found:** 3

**CSS classes:** `.font-bold` `.nav-text-lit` `.px-4` `.py-1.5` `.text-sm` `.text-text-muted`

**HTML structure:**

```html
<a role="menuitem" class="px-4 py-1.5 nav-text-lit text-sm font-bold text-text-muted hover:text-text-primary transition-colors" href="/en/work">Work</a>
```

**Base styles (from design tokens):**

```css
.font-bold {
  background: #f0ebfa;
  padding: 4px;
}```

## Component Rules

- Match class names exactly from the patterns above
- Each component instance must be visually identical to others of its type
- Do not add extra wrappers or change the DOM structure
- Use `#a855f7` for all interactive/active states

## Interactions & States (INTERACTIONS.md)

# Interaction Reference

> Micro-interactions extracted from live DOM. Recreate these exactly for authentic feel.

## Coverage

| Component Type | Count | States Captured |
|----------------|-------|----------------|
| Button | 3 | default, hover, focus |
| Link | 3 | default, hover, focus |
| Input | 1 | default, hover, focus |

## Transition System

These transition declarations were extracted from interactive elements:

```css
transition: color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: color 0.2s cubic-bezier(0, 0, 0.2, 1), background-color 0.2s cubic-bezier(0, 0, 0.2, 1), border-color 0.2s cubic-bezier(0, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0, 0, 0.2, 1), fill 0.2s cubic-bezier(0, 0, 0.2, 1), stroke 0.2s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0, 0, 0.2, 1);
transition: transform 0.22s ease-out, box-shadow 0.22s ease-out;
transition: border-color 0.3s, box-shadow 0.3s, background 0.3s;
```

Apply these to all interactive elements. Never invent new durations or easings.

## Button Interactions

### Button 1 — `Services`

**States:**

- Default: `../screens/states/button-1-default.png`
- Hover: `../screens/states/button-1-hover.png`
- Focus: `../screens/states/button-1-focus.png`

**On hover:**

```css
/* color: rgb(184, 195, 220) → */ color: rgb(245, 245, 245);
/* border-color: rgb(184, 195, 220) → */ border-color: rgb(245, 245, 245);
/* outline: rgb(184, 195, 220) none 3px → */ outline: rgb(245, 245, 245) none 3px;
/* outline-color: rgb(184, 195, 220) → */ outline-color: rgb(245, 245, 245);
```

**On focus:**

```css
/* outline: rgb(184, 195, 220) none 3px → */ outline: rgb(139, 92, 246) solid 2px;
/* outline-color: rgb(184, 195, 220) → */ outline-color: rgb(139, 92, 246);
```

**Transition:** `color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1)`

### Button 2 — `Industries`

**States:**

- Default: `../screens/states/button-2-default.png`
- Hover: `../screens/states/button-2-hover.png`
- Focus: `../screens/states/button-2-focus.png`

**On hover:**

```css
/* color: rgb(184, 195, 220) → */ color: rgb(245, 245, 245);
/* border-color: rgb(184, 195, 220) → */ border-color: rgb(245, 245, 245);
/* outline: rgb(184, 195, 220) none 3px → */ outline: rgb(245, 245, 245) none 3px;
/* outline-color: rgb(184, 195, 220) → */ outline-color: rgb(245, 245, 245);
```

**On focus:**

```css
/* outline: rgb(184, 195, 220) none 3px → */ outline: rgb(139, 92, 246) solid 2px;
/* outline-color: rgb(184, 195, 220) → */ outline-color: rgb(139, 92, 246);
```

**Transition:** `color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1)`

### Button 3 — `ع`

**States:**

- Default: `../screens/states/button-3-default.png`
- Hover: `../screens/states/button-3-hover.png`
- Focus: `../screens/states/button-3-focus.png`

**On hover:**

```css
/* color: rgb(184, 195, 220) → */ color: rgb(245, 245, 245);
/* border-color: rgba(255, 255, 255, 0.1) → */ border-color: oklab(0.605616 0.0845671 -0.201916 / 0.4);
/* outline: rgb(184, 195, 220) none 3px → */ outline: rgb(245, 245, 245) none 3px;
/* outline-color: rgb(184, 195, 220) → */ outline-color: rgb(245, 245, 245);
```

**On focus:**

```css
/* outline: rgb(184, 195, 220) none 3px → */ outline: rgb(139, 92, 246) solid 2px;
/* outline-color: rgb(184, 195, 220) → */ outline-color: rgb(139, 92, 246);
```

**Transition:** `color 0.2s cubic-bezier(0, 0, 0.2, 1), background-color 0.2s cubic-bezier(0, 0, 0.2, 1), border-color 0.2s cubic-bezier(0, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0, 0, 0.2, 1), fill 0.2s cubic-bezier(0, 0, 0.2, 1), stroke 0.2s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0, 0, 0.2, 1)`

## Link Interactions

### Link 1 — `AIStudioToday — Home`

**States:**

- Default: `../screens/states/link-1-default.png`
- Hover: `../screens/states/link-1-hover.png`
- Focus: `../screens/states/link-1-focus.png`

**On hover:**

```css
/* transform: none → */ transform: matrix(1, 0, 0, 1, 0, -1);
```

**On focus:**

```css
/* outline: rgb(245, 245, 245) none 3px → */ outline: rgba(139, 92, 246, 0.6) solid 2px;
/* outline-color: rgb(245, 245, 245) → */ outline-color: rgba(139, 92, 246, 0.6);
```

**Transition:** `transform 0.22s ease-out, box-shadow 0.22s ease-out`

### Link 2 — `UGC Videos + AI Marketing
Scroll-stoppin`

**States:**

- Default: `../screens/states/link-2-default.png`
- Hover: `../screens/states/link-2-hover.png`
- Focus: `../screens/states/link-2-focus.png`

**On focus:**

```css
/* outline: rgb(245, 245, 245) none 3px → */ outline: rgb(139, 92, 246) solid 2px;
/* outline-color: rgb(245, 245, 245) → */ outline-color: rgb(139, 92, 246);
```

**Transition:** `color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1)`

### Link 3 — `WebsiteOS + WhatsApp
Bilingual conversio`

**States:**

- Default: `../screens/states/link-3-default.png`
- Hover: `../screens/states/link-3-hover.png`
- Focus: `../screens/states/link-3-focus.png`

**On focus:**

```css
/* outline: rgb(245, 245, 245) none 3px → */ outline: rgb(139, 92, 246) solid 2px;
/* outline-color: rgb(245, 245, 245) → */ outline-color: rgb(139, 92, 246);
```

**Transition:** `color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1)`

## Input Interactions

### Input 1 — `Toggle color theme`

**States:**

- Default: `../screens/states/input-1-default.png`
- Hover: `../screens/states/input-1-hover.png`
- Focus: `../screens/states/input-1-focus.png`

**On focus:**

```css
/* outline: rgb(245, 245, 245) none 3px → */ outline: rgb(139, 92, 246) solid 2px;
/* outline-color: rgb(245, 245, 245) → */ outline-color: rgb(139, 92, 246);
```

**Transition:** `border-color 0.3s, box-shadow 0.3s, background 0.3s`

## Interaction Rules

- Accent color `#a855f7` is used for focus rings, active states, and hover highlights
- Hover effects include **color transitions** — use the extracted values, not approximations
- Focus states use **outline** (not box-shadow) — always match the extracted focus ring
- Transition durations in use: `0.15s`, `0.2s`, `0.22s`, `0.3s`
- Always respect `prefers-reduced-motion` — set all transitions to `0s` when enabled

## Design Tokens — JSON Files

### tokens/colors.json
```json
{
  "$schema": "https://design-tokens.github.io/community-group/format/",
  "core": {
    "surface": {
      "value": "#f0ebfa",
      "role": "surface"
    },
    "background": {
      "value": "#ffffff",
      "role": "background"
    },
    "text-muted": {
      "value": "#a99fc2",
      "role": "text-muted"
    },
    "accent": {
      "value": "#a855f7",
      "role": "accent"
    },
    "text-primary": {
      "value": "#0b0712",
      "role": "text-primary"
    }
  },
  "status": {},
  "extended": {
    "color-c2b9d4": {
      "value": "#c2b9d4",
      "role": "unknown"
    },
    "color-8b5cf6": {
      "value": "#8b5cf6",
      "role": "info"
    },
    "color-b8c3dc": {
      "value": "#b8c3dc",
      "role": "unknown"
    },
    "color-150e22": {
      "value": "#150e22",
      "role": "unknown"
    },
    "color-1e1430": {
      "value": "#1e1430",
      "role": "unknown"
    }
  },
  "meta": {
    "theme": "light",
    "extracted": "2026-06-05"
  }
}
```

### tokens/spacing.json
```json
{
  "base": {
    "value": "4px",
    "description": "Grid unit — all spacing must be multiples of this"
  },
  "unit": "px",
  "scale": {
    "xs": {
      "value": "2px",
      "px": 2
    },
    "sm": {
      "value": "4px",
      "px": 4
    },
    "md": {
      "value": "6px",
      "px": 6
    },
    "lg": {
      "value": "8px",
      "px": 8
    },
    "xl": {
      "value": "10px",
      "px": 10
    },
    "2xl": {
      "value": "12px",
      "px": 12
    },
    "3xl": {
      "value": "14px",
      "px": 14
    },
    "4xl": {
      "value": "16px",
      "px": 16
    },
    "5xl": {
      "value": "18px",
      "px": 18
    },
    "6xl": {
      "value": "20px",
      "px": 20
    }
  },
  "multipliers": {
    "1x": {
      "value": "4px",
      "raw": 4
    },
    "2x": {
      "value": "8px",
      "raw": 8
    },
    "3x": {
      "value": "12px",
      "raw": 12
    },
    "4x": {
      "value": "16px",
      "raw": 16
    },
    "5x": {
      "value": "20px",
      "raw": 20
    },
    "6x": {
      "value": "24px",
      "raw": 24
    },
    "7x": {
      "value": "28px",
      "raw": 28
    },
    "8x": {
      "value": "32px",
      "raw": 32
    },
    "9x": {
      "value": "36px",
      "raw": 36
    },
    "10x": {
      "value": "40px",
      "raw": 40
    },
    "11x": {
      "value": "44px",
      "raw": 44
    },
    "12x": {
      "value": "48px",
      "raw": 48
    },
    "13x": {
      "value": "52px",
      "raw": 52
    },
    "14x": {
      "value": "56px",
      "raw": 56
    },
    "15x": {
      "value": "60px",
      "raw": 60
    },
    "16x": {
      "value": "64px",
      "raw": 64
    }
  },
  "meta": {
    "totalValues": 15,
    "min": 2,
    "max": 48
  }
}
```

### tokens/typography.json
```json
{
  "families": [
    "Arial Black"
  ],
  "scale": {
    "heading-1": {
      "fontFamily": "Arial Black",
      "fontSize": "48px / 3rem",
      "fontWeight": "700",
      "lineHeight": null,
      "source": "computed"
    },
    "heading-2": {
      "fontFamily": "Arial Black",
      "fontSize": "32px / 2rem",
      "fontWeight": "600",
      "lineHeight": null,
      "source": "computed"
    },
    "heading-3": {
      "fontFamily": "Arial Black",
      "fontSize": "24px / 1.5rem",
      "fontWeight": "600",
      "lineHeight": null,
      "source": "computed"
    },
    "body": {
      "fontFamily": "Arial Black",
      "fontSize": "16px / 1rem",
      "fontWeight": "400",
      "lineHeight": null,
      "source": "computed"
    },
    "caption": {
      "fontFamily": "Arial Black",
      "fontSize": "12px / 0.75rem",
      "fontWeight": "400",
      "lineHeight": null,
      "source": "computed"
    }
  },
  "fontFaces": [],
  "rules": {
    "maxSizesPerScreen": 4,
    "headingWeightRange": "600-700",
    "bodyWeight": 400,
    "lineHeightBody": 1.5,
    "lineHeightHeading": 1.2
  }
}
```

## Screenshots Inventory (screens/)

> Study all screenshots carefully before implementing any UI. Match every visual detail exactly.

### Scroll Journey (screens/scroll/)

*Cinematic scroll states — page visual at each scroll depth*

![scroll-000.png](screens/scroll/scroll-000.png)

![scroll-017.png](screens/scroll/scroll-017.png)

![scroll-033.png](screens/scroll/scroll-033.png)

![scroll-050.png](screens/scroll/scroll-050.png)

![scroll-067.png](screens/scroll/scroll-067.png)

![scroll-083.png](screens/scroll/scroll-083.png)

![scroll-100.png](screens/scroll/scroll-100.png)

### Full Page Screenshots (screens/pages/)

*Full-page screenshots of each crawled URL*

![home.png](screens/pages/home.png)

### Section Clips (screens/sections/)

*Clipped individual sections and components*

![home-section-1.png](screens/sections/home-section-1.png)

### Interaction States (screens/states/)

*Hover, focus, and active state captures*

![button-1-default.png](screens/states/button-1-default.png)

![button-1-focus.png](screens/states/button-1-focus.png)

![button-1-hover.png](screens/states/button-1-hover.png)

![button-2-default.png](screens/states/button-2-default.png)

![button-2-focus.png](screens/states/button-2-focus.png)

![button-2-hover.png](screens/states/button-2-hover.png)

![button-3-default.png](screens/states/button-3-default.png)

![button-3-focus.png](screens/states/button-3-focus.png)

![button-3-hover.png](screens/states/button-3-hover.png)

![input-1-default.png](screens/states/input-1-default.png)

![input-1-focus.png](screens/states/input-1-focus.png)

![input-1-hover.png](screens/states/input-1-hover.png)

![link-1-default.png](screens/states/link-1-default.png)

![link-1-focus.png](screens/states/link-1-focus.png)

![link-1-hover.png](screens/states/link-1-hover.png)

![link-2-default.png](screens/states/link-2-default.png)

![link-2-focus.png](screens/states/link-2-focus.png)

![link-2-hover.png](screens/states/link-2-hover.png)

![link-3-default.png](screens/states/link-3-default.png)

![link-3-focus.png](screens/states/link-3-focus.png)

![link-3-hover.png](screens/states/link-3-hover.png)

### Screenshot Index (screens/INDEX.md)

# Screenshot Index

## Scroll Journey

> Shows the cinematic state at each point of the page

| Scroll | Y Position | File |
|--------|-----------|------|
| 0% | 0px | `screens/scroll/scroll-000.png` |
| 17% | 1778px | `screens/scroll/scroll-017.png` |
| 33% | 3452px | `screens/scroll/scroll-033.png` |
| 50% | 5230px | `screens/scroll/scroll-050.png` |
| 67% | 7008px | `screens/scroll/scroll-067.png` |
| 83% | 8682px | `screens/scroll/scroll-083.png` |
| 100% | 10460px | `screens/scroll/scroll-100.png` |

## Pages

| Page | URL | File |
|------|-----|------|
| AI Studio Today — AI Growth Systems & AI Marketing Agency | `https://aistudiotoday.com` | `screens/pages/home.png` |

## Sections

| Page | Section | File |
|------|---------|------|
| home | #1 (section) | `screens/sections/home-section-1.png` |

