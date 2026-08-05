---
name: chargebee-design
description: Design system skill for chargebee. Activate when building UI components, pages, or any visual elements. Provides exact color tokens, typography scale, spacing grid, component patterns, and craft rules. Read references/DESIGN.md before writing any CSS or JSX. Includes ultra-mode visual journey: read references/ANIMATIONS.md, references/LAYOUT.md, references/COMPONENTS.md, and references/INTERACTIONS.md for full motion and layout details.
---

# chargebee Design System

You are building UI for **chargebee**. Light-themed, warm palette, sans-serif typography (Sora), compact density on a 4px grid, expressive motion.

## Visual Reference

**IMPORTANT**: Study ALL screenshots below before writing any UI. Match colors, typography, spacing, layout, and motion exactly as shown.

### Homepage

![chargebee Homepage](screenshots/homepage.png)

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

- **Web Animations API (12 active)** — animation

## Design Philosophy

- **Layered depth** — use shadow tokens to create a sense of physical layering. Each elevation level has a specific shadow.
- **Gradient accents** — gradients are used thoughtfully for emphasis, not decoration.
- **Type pairing** — Sora for body/UI text, Inter for headings/display. Never introduce a third typeface.
- **compact density** — 4px base grid. Every dimension is a multiple of 4.
- **warm palette** — the color temperature runs warm, matching the sans-serif typography.
- **Restrained accent** — `#ff5722` is the only pop of color. Used exclusively for CTAs, links, focus rings, and active states.
- **Expressive motion** — animations are an integral part of the experience. Use spring physics and layout animations.

## Color System

### Core Palette

| Role | Token | Hex | Use |
|------|-------|-----|-----|
| Background | `--background` | `#ffffff` | Page/app background |
| Surface | `--surface` | `#e8f4f5` | Cards, panels, modals |
| Text Primary | `--text-primary` | `#012a38` | Headings, body text |
| Text Muted | `--text-muted` | `#57606a` | Captions, placeholders |
| Accent | `--accent` | `#ff5722` | CTAs, links, focus rings |

### Status Colors

| Status | Hex | Use |
|--------|-----|-----|
| Danger | `#ff3300` | Errors, destructive actions |

### Extended Palette

- `#e0e0e0`
- `#9ca3af`
- `#bff90b`
- **cb-teal-muted:** `#22748b` — Secondary text, placeholder text
- **iti-hover-color:** `#000000` — Deep background layer or shadow color
- `#84e4ee`
- **cb-ticker-muted:** `#d3d9dc` — Secondary text, placeholder text
- `#d5f4f7` — Light surface or highlight color

### CSS Variable Tokens

```css
--primary-color: var(--blue-900);
--secondary-color: var(--white);
--primary-color: var(--white);
--secondary-color: var(--blue-900);
--primary-color: var(--lime-500);
--secondary-color: var(--opal-100);
--ff_primary: Inter,sans-serif;
--cb-teal-muted: #22748b;
--cb-text-muted: #4f6169;
--cb-ticker-muted: #d3d9dc;
--cb-border-soft: #e5edf5;
--cb-border-light: #efefef;
--navigation-border-radius: var(--cb-radius);
--primary-color: var(--blue-900);
--secondary-color: var(--white);
--primary-color: var(--white);
--secondary-color: var(--blue-900);
--primary-color: var(--lime-500);
--secondary-color: var(--opal-100);
--ff_primary: Inter,sans-serif;
```

## Typography

### Font Stack

- **Sora** — Heading 1, Heading 2, Heading 3
- **Inter** — Body, Caption
- **SF Mono** — Code

### Font Sources

```css
@font-face {
  font-family: "Inter";
  src: url("fonts/Inter-Bold.ttf") format("truetype");
  font-weight: 700;
}
@font-face {
  font-family: "Inter";
  src: url("fonts/Inter-Regular.ttf") format("truetype");
  font-weight: 400;
}
@font-face {
  font-family: "Sora";
  src: url("fonts/Sora-Bold.ttf") format("truetype");
  font-weight: 700;
}
@font-face {
  font-family: "Sora";
  src: url("fonts/Sora-Regular.ttf") format("truetype");
  font-weight: 400;
}
```

### Type Scale

| Role | Family | Size | Weight |
|------|--------|------|--------|
| Heading 1 | Sora | 250px | 700 |
| Heading 2 | Sora | 200px | 700 |
| Heading 3 | Sora | 190px | 700 |
| Body | Inter | 14px | 400 |
| Caption | Inter | 16px | 400 |
| Code | SF Mono | 14px | 400 |

### Typography Rules

- Body/UI: **Sora**, Headings: **Inter** — these are the only display fonts
- Max 3-4 font sizes per screen
- Headings: weight 600-700, body: weight 400
- Use color and opacity for text hierarchy, not additional font sizes
- Line height: 1.5 for body, 1.2 for headings

## Spacing & Layout

### Base Grid: 4px

Every dimension (margin, padding, gap, width, height) must be a multiple of **4px**.

### Spacing Scale

`2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24` px

### Spacing as Meaning

| Spacing | Use |
|---------|-----|
| 4-8px | Tight: related items (icon + label, avatar + name) |
| 12-16px | Medium: between groups within a section |
| 24-32px | Wide: between distinct sections |
| 48px+ | Vast: major page section breaks |

### Border Radius

Scale: `0px 12px 12px 0px, .25rem, .375rem, .5rem, .75rem, 1rem, 1.5rem, 2px, 3px, 4px, 6px, 8px, 9px, 10px, 11px, 12px, 13px, 14px, 15px, 16px, 18px, 19px, 20px, 22px, 24px, 25%, 25px, 26px, 28px, 29px, 30px, 32px, 33px, 34px, 35px, 36px, 38px, 40px, 40px 40px 0px 0px, 42px, 48px, 50px, 52px, 60px, 67.788px, 68px, 70px, 80px, 100%, 100px, 120px, 320px, inherit, 150px, 160px, 280px, 800px, 999px`
Default: `29px`

### Container

Max-width: `960px`, centered with auto margins.

### Breakpoints

| Name | Value |
|------|-------|
| sm | 500px |
| sm | 600px |
| sm | 639px |
| sm | 640px |
| md | 767px |
| md | 768px |
| lg | 1023px |
| lg | 1024px |
| xl | 1028px |
| xl | 1200px |
| xl | 1279px |
| xl | 1280px |
| 2xl | 1440px |
| 2xl | 1600px |
| 2xl | 1920px |
| 2xl | 2500px |

Mobile-first: design for small screens, layer on responsive overrides.

## Component Patterns

### Card

```css
.card {
  background: #e8f4f5;
  border-radius: 29px;
  padding: 16px;
  box-shadow: 0 2px 8px #012a382e;
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
  background: #ff5722;
  color: #012a38;
  border-radius: 29px;
  padding: 8px 16px;
  font-weight: 500;
  transition: opacity 150ms ease;
}
.btn-primary:hover { opacity: 0.9; }

/* Ghost */
.btn-ghost {
  background: transparent;
  border: 1px solid #cccccc;
  color: #012a38;
  border-radius: 29px;
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
  border-radius: 29px;
  padding: 8px 12px;
  color: #012a38;
  font-size: 14px;
}
.input:focus { border-color: #ff5722; outline: none; }
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
  background: #e8f4f5;
  color: #57606a;
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
  background: #e8f4f5;
  border-radius: 999px;
  padding: 24px;
  max-width: 480px;
  width: 90vw;
  box-shadow: 0 1px 1px #5a7abe1a,0 10px 20px #5a7abe33;
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
  color: #57606a;
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
  color: #57606a;
  padding: 8px 12px;
  border-radius: 29px;
  transition: color 150ms;
}
.nav-link:hover { color: #012a38; }
.nav-link.active { color: #ff5722; }
```

```html
<nav class="nav">
  <a href="/" class="nav-link active">Home</a>
  <a href="/about" class="nav-link">About</a>
  <a href="/pricing" class="nav-link">Pricing</a>
  <button class="btn-primary" style="margin-left: auto">Get Started</button>
</nav>
```

### Extracted Components

These components were found in the codebase:

**Button** (`html`)
- Variants: `-primary`

**Input** (`html`)

**Card** (`html`)
- Variants: `-hub`, `-newsletter`, `-vibe`, `-second-acts`, `logo`

**Navigation** (`html`)

**Modal** (`html`)

**Footer** (`html`)

**List** (`html`)

## Page Structure

The following page sections were detected:

- **Navigation** — Top navigation bar (6 items)
- **Hero** — Hero/banner section with headline and CTAs
- **Faq** — FAQ/accordion section
- **Footer** — Page footer with links and info (48 items)
- **Cta** — Call-to-action section
- **Testimonials** — Testimonials/reviews section
- **Cards** — Grid of 35 card elements (35 items)
- **Features** — Feature/benefit cards grid (20 items)

When building pages, follow this section order and structure.

## Animation & Motion

This project uses **expressive motion**. Animations are part of the design language.

### CSS Animations

- `anime`
- `splide-loading`
- `skeletonShimmer`
- `agent-shimmer-962d5e26`
- `rc-bounce`

### Motion Tokens

- **Duration scale:** `0ms`, `0.01ms`, `.1s`, `.15s`, `0.15s`, `.2s`, `.25s`, `.3s`, `.32s`, `.5s`, `.52s`, `.7s`, `.8s`, `1s`, `1.5s`, `50ms`, `100ms`, `120ms`, `150ms`, `200ms`, `250ms`, `280ms`, `300ms`, `350ms`, `400ms`, `500ms`, `1000ms`
- **Easing functions:** `cubic-bezier(.4,0,.2,1)`, `ease-out`, `ease`, `linear`, `cubic-bezier(.34,1.56,.64,1)`, `cubic-bezier(.8,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `ease-in-out`, `cubic-bezier(.22,1,.36,1)`, `ease-in`, `cubic-bezier(0.6,0,0.2,0.5)`, `cubic-bezier(0.4,0,0.2,1)`

### Motion Guidelines

- **Duration:** Use values from the duration scale above. Short (0ms) for micro-interactions, long (1000ms) for page transitions
- **Easing:** Use `cubic-bezier(.4,0,.2,1)` as the default easing curve
- **Direction:** Elements enter from bottom/right, exit to top/left
- **Reduced motion:** Always respect `prefers-reduced-motion` — disable animations when set

## Depth & Elevation

### Shadow Tokens

- Subtle: `1.165px 1.165px #00000040`
- Subtle: `inset 0 0 0 1px #012a38`
- Subtle: `0 0 0 1px rgba(255,255,255,0.18)`
- Subtle: `0px 0px 1px 0px #888`
- Subtle: `inset 0 0#0000001a,0 0 0 2px #92a1a8`
- Raised (cards, buttons): `0 2px 8px #012a382e`

### Z-Index Scale

`0, 1, 2, 3, 5, 9, 10, 20, 30, 40, 50, 60, 90, 95, 99, 100, 999, 1060, 9998, 9999, 99999, 999999, 999999999`

Use these exact values — never invent z-index values.

## Anti-Patterns (Never Do)

- **No blur effects** — no backdrop-blur, no filter: blur()
- **No zebra striping** — tables and lists use borders for separation
- **No invented colors** — every hex value must come from the palette above
- **No arbitrary spacing** — every dimension is a multiple of 4px
- **No extra fonts** — only Sora and Inter and SF Mono are allowed
- **No arbitrary border-radius** — use the scale: .25rem, .375rem, .5rem, .75rem, 1rem, 1.5rem, 2px, 3px, 4px, 6px
- **No opacity for disabled states** — use muted colors instead

## Workflow

1. **Read** `references/DESIGN.md` before writing any UI code
2. **Pick colors** from the Color System section — never invent new ones
3. **Set typography** — Sora, Inter, SF Mono only, using the type scale
4. **Build layout** on the 4px grid — check every margin, padding, gap
5. **Match components** to patterns above before creating new ones
6. **Apply elevation** — use shadow tokens
7. **Validate** — every value traces back to a design token. No magic numbers.

## Brand Spec

- **Favicon:** `/static/resources/brand/favicon.png`
- **Site URL:** `https://www.chargebee.com`
- **Brand color:** `#ff5722`
- **Brand typeface:** Sora

## Quick Reference

```
Background:     #ffffff
Surface:        #e8f4f5
Text:           #012a38 / #57606a
Accent:         #ff5722
Border:         (not extracted)
Font:           Sora
Spacing:        4px grid
Radius:         29px
Components:     10 detected
```

## When to Trigger

Activate this skill when:
- Creating new components, pages, or visual elements for chargebee
- Writing CSS, Tailwind classes, styled-components, or inline styles
- Building page layouts, templates, or responsive designs
- Reviewing UI code for design consistency
- The user mentions "chargebee" design, style, UI, or theme
- Generating mockups, wireframes, or visual prototypes

---

# Full Reference Files

> Every output file is embedded below. Claude has full design system context from /skills alone.

## Design System Tokens (DESIGN.md)

# chargebee DESIGN.md

> Auto-generated design system — reverse-engineered via static analysis by skillui.
> Frameworks: None detected
> Colors: 20 · Fonts: 3 · Components: 10
> Icon library: not detected · State: not detected
> Primary theme: light · Dark mode toggle: no · Motion: expressive

## Visual Reference

**Match this design exactly** — study colors, fonts, spacing, and component shapes before writing any UI code.

![chargebee Homepage](../screenshots/homepage.png)

---

## 1. Visual Theme & Atmosphere

This is a **light-themed** interface with a warm, approachable feel. The light background emphasizes content clarity. Typography pairs **Inter** for display/headings with **Sora** for body text, creating clear visual hierarchy through type contrast. Spacing follows a **4px base grid** (compact density), with scale: 2, 4, 6, 8, 10, 12, 14, 16px. The palette is predominantly monochromatic with **#ff5722** as the single accent color — used sparingly for interactive elements and emphasis. Motion is expressive — spring physics, layout animations, and staggered reveals are part of the visual language.

---

## 2. Color Palette & Roles

| Token | Hex | Role | Use |
|---|---|---|---|
| tw-ring-offset-color | `#ffffff` | background | Page background, darkest surface |
| tw-ring-offset-color | `#e8f4f5` | surface | Card and panel backgrounds |
| theme-color | `#012a38` | text-primary | Headings and body text |
| cb-text-muted | `#57606a` | text-muted | Captions, placeholders, secondary info |
| text-muted | `#a2c1c4` | text-muted | Captions, placeholders, secondary info |
| cb-text-subtle | `#8a9aa1` | text-muted | Captions, placeholders, secondary info |
| accent | `#ff5722` | accent | CTAs, links, focus rings, active states |
| tw-ring-color | `#ff3300` | danger | Error states, destructive actions |
| cb-teal-muted | `#22748b` | info | Informational highlights |
| unknown | `#e0e0e0` | unknown | Palette color |
| unknown | `#9ca3af` | unknown | Palette color |
| unknown | `#bff90b` | unknown | Palette color |
| iti-hover-color | `#000000` | unknown | Palette color |
| unknown | `#84e4ee` | unknown | Palette color |
| cb-ticker-muted | `#d3d9dc` | unknown | Palette color |
| unknown | `#d5f4f7` | unknown | Palette color |
| unknown | `#03779e` | unknown | Palette color |
| unknown | `#90c2c7` | unknown | Palette color |
| unknown | `#335466` | unknown | Palette color |
| unknown | `#174350` | unknown | Palette color |

### CSS Variable Tokens

```css
--tw-border-opacity: 1;
--tw-border-opacity: 1;
--tw-border-opacity: 1;
--tw-border-spacing-x: 0;
--tw-border-spacing-y: 0;
--tw-border-spacing-x: 0;
--tw-border-spacing-y: 0;
--tw-border-opacity: 1;
--tw-border-opacity: 1;
--tw-border-opacity: 1;
--tw-border-opacity: 1;
--tw-border-opacity: 1;
--tw-border-opacity: 1;
--tw-border-opacity: 1;
--tw-border-opacity: 1;
--tw-border-opacity: 1;
--tw-border-opacity: 1;
--tw-border-opacity: 1;
--tw-border-opacity: 1;
--tw-border-opacity: 1;
```


---

## 3. Typography Rules

**Font Stack:**
- **Sora** — Heading 1, Heading 2, Heading 3
- **Inter** — Body, Caption
- **SF Mono** — Code

**Font Sources:**

```css
@font-face {
  font-family: "Inter";
  src: url("fonts/Inter-Bold.ttf") format("truetype");
  font-weight: 700;
}
@font-face {
  font-family: "Inter";
  src: url("fonts/Inter-Regular.ttf") format("truetype");
  font-weight: 400;
}
@font-face {
  font-family: "Sora";
  src: url("fonts/Sora-Bold.ttf") format("truetype");
  font-weight: 700;
}
@font-face {
  font-family: "Sora";
  src: url("fonts/Sora-Regular.ttf") format("truetype");
  font-weight: 400;
}
```

| Role | Font | Size | Weight |
|---|---|---|---|
| Heading 1 | Sora | 250px | 700 |
| Heading 2 | Sora | 200px | 700 |
| Heading 3 | Sora | 190px | 700 |
| Body | Inter | 14px | 400 |
| Caption | Inter | 16px | 400 |
| Code | SF Mono | 14px | 400 |

**Typographic Rules:**
- Limit to 3 font families max per screen
- Use **Sora** for body/UI text, **Inter** for display/headings
- Maintain consistent hierarchy: no more than 3-4 font sizes per screen
- Headings use bold (600-700), body uses regular (400)
- Line height: 1.5 for body text, 1.2 for headings
- Use color and opacity for secondary hierarchy, not additional font sizes


---

## 4. Component Stylings

### Layout (1)

**Footer** — `html`

### Navigation (1)

**Navigation** — `html`

### Data Display (3)

**Card** — `html`
- Variants: `-hub`, `-newsletter`, `-vibe`, `-second-acts`, `logo`

**Badge** — `html`

**List** — `html`

### Data Input (2)

**Button** — `html`
- Variants: `-primary`
- Animation: 

**Input** — `html`
- State: :focus, :placeholder

### Overlay (1)

**Modal** — `html`

### Media (2)

**Image** — `html`

**Icon** — `html`



---

## 5. Layout Principles

- **Base spacing unit:** 4px
- **Spacing scale:** 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24
- **Border radius:** 0px 12px 12px 0px, .25rem, .375rem, .5rem, .75rem, 1rem, 1.5rem, 2px, 3px, 4px, 6px, 8px, 9px, 10px, 11px, 12px, 13px, 14px, 15px, 16px, 18px, 19px, 20px, 22px, 24px, 25%, 25px, 26px, 28px, 29px, 30px, 32px, 33px, 34px, 35px, 36px, 38px, 40px, 40px 40px 0px 0px, 42px, 48px, 50px, 52px, 60px, 67.788px, 68px, 70px, 80px, 100%, 100px, 120px, 320px, inherit, 150px, 160px, 280px, 800px, 999px
- **Max content width:** 960px

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

- `1.165px 1.165px #00000040`
- `inset 0 0 0 1px #012a38`
- `0 0 0 1px rgba(255,255,255,0.18)`

### Raised — cards, buttons, interactive elements

- `0 2px 8px #012a382e`
- `var(--cb-shadow)`
- `inset 1px 2px 3px rgba(0,0,0,0.25)`

### Floating — dropdowns, popovers, modals

- `0 1px 1px #5a7abe1a,0 10px 20px #5a7abe33`
- `2px 0 12px #012a384d`
- `0 0 0 3px #bff90b33,0 0 12px #bff90b80`

### Overlay — full-screen overlays, top-level dialogs

- `0 4px 54px #00000040`
- `0 6px 34px #0000003b`
- `0 25px 80px #0000004d`

### Z-Index Scale

`0, 1, 2, 3, 5, 9, 10, 20, 30, 40, 50, 60, 90, 95, 99, 100, 999, 1060, 9998, 9999, 99999, 999999, 999999999`



---

## 7. Animation & Motion

This project uses **expressive motion**. Animations are an integral part of the experience.

### CSS Animations

- `@keyframes anime`
- `@keyframes splide-loading`
- `@keyframes skeletonShimmer`
- `@keyframes agent-shimmer-962d5e26`
- `@keyframes rc-bounce`
- `@keyframes rc-ping`
- `@keyframes rc-tv-toaster-shimmer`
- `@keyframes rc-tv-toaster-chevron`

### Animated Components

- **Button**: 

### Motion Guidelines

- Duration: 150-300ms for micro-interactions, 300-500ms for page transitions
- Easing: `ease-out` for enters, `ease-in` for exits
- Always respect `prefers-reduced-motion`


---

## 8. Do's and Don'ts

### Do's

- Use `#ff5722` for interactive elements (buttons, links, focus rings)
- Use `#ffffff` as the primary page background
- Pair **Sora** (body) with **Inter** (display) — these are the only allowed fonts
- Follow the **4px** spacing grid for all margins, padding, and gaps
- Use the defined shadow tokens for elevation — see Section 6
- Use border-radius from the scale: 0px 12px 12px 0px, .25rem, .375rem, .5rem, .75rem
- Reuse existing components from Section 4 before creating new ones

### Don'ts

- Don't introduce colors outside this palette — extend the design tokens first
- Don't introduce additional font families beyond Sora and Inter and SF Mono
- Don't use arbitrary spacing values — stick to multiples of 4px
- Don't create custom box-shadow values outside the system tokens
- Don't use arbitrary border-radius values — pick from the defined scale
- Don't duplicate component patterns — check Section 4 first
- Don't use backdrop-blur or blur effects

### Anti-Patterns (detected from codebase)

- No blur or backdrop-blur effects
- No zebra striping on tables/lists


---

## 9. Responsive Behavior

| Name | Value | Source |
|---|---|---|
| sm | 500px | css |
| sm | 600px | css |
| sm | 639px | css |
| sm | 640px | css |
| md | 767px | css |
| md | 768px | css |
| lg | 1023px | css |
| lg | 1024px | css |
| xl | 1028px | css |
| xl | 1200px | css |
| xl | 1279px | css |
| xl | 1280px | css |
| 2xl | 1440px | css |
| 2xl | 1600px | css |
| 2xl | 1920px | css |
| 2xl | 2500px | css |

**Approach:** Use `@media (min-width: ...)` queries matching the breakpoints above.


---

## 10. Agent Prompt Guide

Use these as starting points when building new UI:

### Build a Card

```
Background: #e8f4f5
Border: 1px solid var(--border)
Radius: 29px
Padding: 16px
Font: Sora
Use shadow tokens from Section 6.
```

### Build a Button

```
Primary: bg #ff5722, text white
Ghost: bg transparent, border var(--border)
Padding: 8px 16px
Radius: 29px
Hover: opacity 0.9 or lighter shade
Focus: ring with #ff5722
```

### Build a Page Layout

```
Background: #ffffff
Max-width: 960px, centered
Grid: 4px base
Responsive: mobile-first, breakpoints from Section 9
```

### Build a Stats Card

```
Surface: #e8f4f5
Label: #57606a (muted, 12px, uppercase)
Value: #012a38 (primary, 24-32px, bold)
Status: use success/warning/danger from Section 2
```

### Build a Form

```
Input bg: #ffffff
Input border: 1px solid var(--border)
Focus: border-color #ff5722
Label: #57606a 12px
Spacing: 16px between fields
Radius: 29px
```

### General Component

```
1. Read DESIGN.md Sections 2-6 for tokens
2. Colors: only from palette
3. Font: Sora, type scale from Section 3
4. Spacing: 4px grid
5. Components: match patterns from Section 4
6. Elevation: shadow tokens
```

## Visual Guide — Screenshots (VISUAL_GUIDE.md)

# chargebee — Visual Guide

> Master visual reference. Study every screenshot carefully before implementing any UI.
> Match colors, layout, typography, spacing, and motion states exactly.

**Motion Stack:** **Web Animations API (12 active)**

## Scroll Journey

The page has cinematic scroll animations. Each screenshot below shows the exact visual state at that scroll depth.
**Replicate these transitions precisely** — the design changes dramatically as you scroll.

### Hero — Above the fold

*Scroll position: 0px of 10042px total*

![Hero — Above the fold](../screens/scroll/scroll-000.png)

### 17% scroll depth

*Scroll position: 1554px of 10042px total*

![17% scroll depth](../screens/scroll/scroll-017.png)

### 33% scroll depth

*Scroll position: 3017px of 10042px total*

![33% scroll depth](../screens/scroll/scroll-033.png)

### 50% scroll depth

*Scroll position: 4571px of 10042px total*

![50% scroll depth](../screens/scroll/scroll-050.png)

### 67% scroll depth

*Scroll position: 6125px of 10042px total*

![67% scroll depth](../screens/scroll/scroll-067.png)

### 83% scroll depth

*Scroll position: 7588px of 10042px total*

![83% scroll depth](../screens/scroll/scroll-083.png)

### Footer — End of page

*Scroll position: 9142px of 10042px total*

![Footer — End of page](../screens/scroll/scroll-100.png)

## Full Page Screenshots

### Chargebee: Billing & Monetization for SaaS and AI Companies

*URL: `https://www.chargebee.com`*

![Chargebee: Billing & Monetization for SaaS and AI Companies](../screens/pages/home.png)

### Plans and Pricing - Chargebee

*URL: `https://www.chargebee.com/pricing/`*

![Plans and Pricing - Chargebee](../screens/pages/pricing.png)

### Chargebee for Startups | Get Started for Free

*URL: `https://www.chargebee.com/startups/`*

![Chargebee for Startups | Get Started for Free](../screens/pages/startups.png)

### Sign Up - Get Your Free Sandbox - Chargebee

*URL: `https://www.chargebee.com/trial-signup/`*

![Sign Up - Get Your Free Sandbox - Chargebee](../screens/pages/trial-signup.png)

### Get a demo of Chargebee's Recurring Billing Platform Today

*URL: `https://www.chargebee.com/schedule-a-demo/`*

![Get a demo of Chargebee's Recurring Billing Platform Today](../screens/pages/schedule-a-demo.png)

### AI Billing Infrastructure with MCP Server | Chargebee

*URL: `https://www.chargebee.com/mcp/`*

![AI Billing Infrastructure with MCP Server | Chargebee](../screens/pages/mcp.png)

## Section Screenshots

Clipped sections showing individual components in context.

### Section 8 — `[class*="hero"]`

*1440×251px*

![Section 8](../screens/sections/home-section-8.png)

### Section 9 — `[class*="hero"]`

*1440×481px*

![Section 9](../screens/sections/home-section-9.png)

### Section 4 — `[class*="pricing"]`

*1440×1200px*

![Section 4](../screens/sections/pricing-section-4.png)

### Section 5 — `[class*="pricing"]`

*1440×790px*

![Section 5](../screens/sections/pricing-section-5.png)

### Section 1 — `section`

*1440×477px*

![Section 1](../screens/sections/startups-section-1.png)

### Section 2 — `section`

*1440×772px*

![Section 2](../screens/sections/startups-section-2.png)

### Section 3 — `section`

*1360×532px*

![Section 3](../screens/sections/startups-section-3.png)

### Section 10 — `[class*="hero"]`

*1360×337px*

![Section 10](../screens/sections/startups-section-10.png)

### Section 1 — `section`

*1440×496px*

![Section 1](../screens/sections/mcp-section-1.png)

### Section 2 — `section`

*1440×600px*

![Section 2](../screens/sections/mcp-section-2.png)

## Animations & Motion (ANIMATIONS.md)

# Animation Reference

> Cinematic motion design extracted from live DOM. Follow these specs exactly to recreate the experience.

## Motion Technology Stack

| Library | Type | Notes |
|---------|------|-------|
| **Web Animations API (12 active)** | animation |  |

## Scroll Journey

The page is **10,042px** tall. Each frame below shows what the user sees at that scroll depth.

> **Use these screenshots to understand WHAT animates, WHEN it animates, and HOW it moves.**

### 0% — Top / Hero
Scroll position: 0px

![Scroll 0%](../screens/scroll/scroll-000.png)

### 17% — Opening Section
Scroll position: 1,554px

![Scroll 17%](../screens/scroll/scroll-017.png)

### 33% — First Feature Section
Scroll position: 3,017px

![Scroll 33%](../screens/scroll/scroll-033.png)

### 50% — Mid-Page
Scroll position: 4,571px

![Scroll 50%](../screens/scroll/scroll-050.png)

### 67% — Lower Content
Scroll position: 6,125px

![Scroll 67%](../screens/scroll/scroll-067.png)

### 83% — Near Footer
Scroll position: 7,588px

![Scroll 83%](../screens/scroll/scroll-083.png)

### 100% — Bottom / Footer
Scroll position: 9,142px

![Scroll 100%](../screens/scroll/scroll-100.png)

## Video Elements

| # | Role | Autoplay | Loop | Muted | Size | First Frame |
|---|------|----------|------|-------|------|-------------|
| 1 | content | — | ✓ | ✓ | 593×228 | — |
| 2 | content | — | ✓ | ✓ | 421×458 | — |
| 3 | content | — | ✓ | ✓ | 335×220 | — |
| 4 | content | — | ✓ | ✓ | — | — |
| 5 | content | — | ✓ | ✓ | — | — |
| 6 | content | — | ✓ | ✓ | — | — |

- **Source:** `https://webstatic.chargebee.com/assets/web/20260804043214/images/home_v2/oct-2025/gartner-video.mp4`
- **Poster:** `https://webstatic.chargebee.com/assets/web/20260804043214/images/home_v2/oct-2025/gartner-video.webp`
- **Source:** `https://webstatic.chargebee.com/assets/web/20260804043214/images/home_v2/oct-2025/gartner-video.mp4`
- **Poster:** `https://webstatic.chargebee.com/assets/web/20260804043214/images/home_v2/oct-2025/gartner-video.webp`
- **Source:** `https://webstatic.chargebee.com/assets/web/20260804043214/images/home_v2/oct-2025/beelieve-video.mp4`
- **Poster:** `https://webstatic.chargebee.com/assets/web/20260804043214/images/home_v2/oct-2025/beelieve-video.webp`
- **Source:** `https://webstatic.chargebee.com/assets/web/20260804043214/images/home_v2/videos/video-5.mp4`
- **Poster:** `https://webstatic.chargebee.com/assets/web/20260804043214/images/home_v2/videos/video-5.webp`
- **Source:** `https://webstatic.chargebee.com/assets/web/20260804043214/images/home_v2/videos/video-7.mp4`
- **Poster:** `https://webstatic.chargebee.com/assets/web/20260804043214/images/home_v2/videos/video-7.webp`
- **Source:** `https://webstatic.chargebee.com/assets/web/20260804043214/images/home_v2/videos/video-6.mp4`
- **Poster:** `https://webstatic.chargebee.com/assets/web/20260804043214/images/home_v2/videos/video-6.webp`

## Scroll Animation Patterns

| Pattern | Library | Element Count | Duration | Delay | Easing |
|---------|---------|---------------|----------|-------|--------|
| parallax / sticky scroll | CSS | 3 | — | — | — |

### CSS Implementation

## CSS Keyframes (38 extracted)

### `@keyframes slides`

Duration: `20s` · Easing: `linear` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.rc-animate-\[20s_slides_infinite_linear\]`, `.index .rc-bg__buttons__container`

```css
@keyframes slides {
  0% {
    transform: translate(0px);
  }
  100% {
    transform: translate(-50%);
  }
}
```

> Transform/motion animation

### `@keyframes skeletonShimmer`

Duration: `1.5s` · Easing: `ease` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.rc-form__fields .rc-form__skeleton-input, .rc-form__fields .rc-form__skeleton-l`, `.rc-form__fields .rc-form__skeleton-button`

```css
@keyframes skeletonShimmer {
  0% {
    background-position-x: 200%;
    background-position-y: 0px;
  }
  100% {
    background-position-x: -200%;
    background-position-y: 0px;
  }
}
```

> Background color/gradient shift · Background position (shimmer/scroll)

### `@keyframes skeletonShimmer`

Duration: `1.5s` · Easing: `ease` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.rc-form__fields .rc-form__skeleton-input, .rc-form__fields .rc-form__skeleton-l`, `.rc-form__fields .rc-form__skeleton-button`

```css
@keyframes skeletonShimmer {
  0% {
    background-position-x: 200%;
    background-position-y: 0px;
  }
  100% {
    background-position-x: -200%;
    background-position-y: 0px;
  }
}
```

> Background color/gradient shift · Background position (shimmer/scroll)

### `@keyframes slides`

Duration: `20s` · Easing: `linear` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.rc-animate-\[20s_slides_infinite_linear\]`, `.index .rc-bg__buttons__container`

```css
@keyframes slides {
  0% {
    transform: translate(0px);
  }
  100% {
    transform: translate(-50%);
  }
}
```

> Transform/motion animation

### `@keyframes rc-bounce`

Duration: `1s` · Easing: `ease` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.rc-animate-bounce`

```css
@keyframes rc-bounce {
  0%, 100% {
    transform: translateY(-25%);
    animation-timing-function: cubic-bezier(0.8, 0, 1, 1);
  }
  50% {
    transform: none;
    animation-timing-function: cubic-bezier(0, 0, 0.2, 1);
  }
}
```

> Transform/motion animation

### `@keyframes rc-ping`

Duration: `1s` · Easing: `cubic-bezier(0, 0, 0.2, 1)` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.rc-animate-ping`

```css
@keyframes rc-ping {
  75%, 100% {
    transform: scale(2);
    opacity: 0;
  }
}
```

> Fade + motion enter animation

### `@keyframes rc-tv-toaster-shimmer`

Duration: `1.3s` · Easing: `linear` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.rc-tv-toaster__skeleton`

```css
@keyframes rc-tv-toaster-shimmer {
  0% {
    background-position-x: 150%, 0px;
    background-position-y: 0px, 0px;
  }
  100% {
    background-position-x: -150%, 0px;
    background-position-y: 0px, 0px;
  }
}
```

> Background color/gradient shift · Background position (shimmer/scroll)

### `@keyframes rc-tv-toaster-chevron`

Duration: `1.8s` · Easing: `ease-in-out` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.rc-tv-toaster__restore-logo path`

```css
@keyframes rc-tv-toaster-chevron {
  0%, 100% {
    opacity: 0.45;
    transform: translateY(1px);
  }
  50% {
    opacity: 1;
    transform: translateY(-1.5px);
  }
}
```

> Fade + motion enter animation

### `@keyframes rc-tv-toaster-spin`

Duration: `6s` · Easing: `linear` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.rc-tv-toaster__restore-mark svg`

```css
@keyframes rc-tv-toaster-spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(1turn);
  }
}
```

> Transform/motion animation

### `@keyframes ripple`

Duration: `1s` · Easing: `linear` · Delay: `0s` · Iteration: `1` · Fill: `none`

Used by: `.index .rc-hero--ripple:hover .rc-ripple`

```css
@keyframes ripple {
  0% {
    opacity: 1;
    transform: rotate(60deg) translate(200px, 300px);
  }
  100% {
    opacity: 1;
    transform: rotate(60deg) translate(200px);
  }
}
```

> Fade + motion enter animation

### `@keyframes scroll-left`

Duration: `18s` · Easing: `linear` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.index .rc-marquee__track`

```css
@keyframes scroll-left {
  0% {
    transform: translate(0px);
  }
  100% {
    transform: translate(-50%);
  }
}
```

> Transform/motion animation

### `@keyframes animatedgradient`

Duration: `3s` · Easing: `ease` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.index .rc-marquee:hover::after`

```css
@keyframes animatedgradient {
  0% {
    background-position-x: 0px;
    background-position-y: 50%;
  }
  50% {
    background-position-x: 100%;
    background-position-y: 50%;
  }
  100% {
    background-position-x: 0px;
    background-position-y: 50%;
  }
}
```

> Background color/gradient shift · Background position (shimmer/scroll)

### `@keyframes fadeInRight`

Used by: `.index .fadeInRight`

```css
@keyframes fadeInRight {
  0% {
    opacity: 0;
    transform: translate3d(10%, 0px, 0px);
  }
  100% {
    opacity: 1;
    transform: none;
  }
}
```

> Fade + motion enter animation

### `@keyframes fadeInLeft`

Used by: `.index .fadeInLeft`

```css
@keyframes fadeInLeft {
  0% {
    opacity: 0.1;
    transform: translate3d(-10%, 0px, 0px);
  }
  100% {
    opacity: 1;
    transform: none;
  }
}
```

> Fade + motion enter animation

### `@keyframes fadeInUp`

Used by: `.index .fadeInUp`

```css
@keyframes fadeInUp {
  0% {
    opacity: 0.7;
    transform: translate3d(0px, 15%, 0px);
  }
  100% {
    opacity: 1;
    transform: none;
  }
}
```

> Fade + motion enter animation

### `@keyframes za-cta-heart-blink`

Duration: `0.65s` · Easing: `ease-in-out` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.index .za-grid__col:hover .za-cta--heart`

```css
@keyframes za-cta-heart-blink {
  0%, 100% {
    opacity: 1;
    scale: 1;
  }
  50% {
    opacity: 0.2;
    scale: 0.8;
  }
}
```

> Opacity fade

### `@keyframes showLogo`

Duration: `0.4s` · Easing: `ease-in-out` · Delay: `0s` · Iteration: `1` · Fill: `forwards`

Used by: `.index .rc-slider__body .slick-slide.slick-current [class^="cb-storybook-img"]`

```css
@keyframes showLogo {
  100% {
    opacity: 1;
    transform: translate(0px);
  }
}
```

> Fade + motion enter animation

### `@keyframes showAuthorInfo`

Duration: `0.25s` · Easing: `ease-in-out` · Delay: `0.5s` · Iteration: `1` · Fill: `forwards`

Used by: `.index .rc-slider--casestudy .card.active .rc-casestudy__body`

```css
@keyframes showAuthorInfo {
  100% {
    opacity: 1;
    transform: translateY(0px);
  }
}
```

> Fade + motion enter animation

### `@keyframes anime`

Duration: `8s` · Easing: `linear` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `#rcFooter footer .rc-footer-cta`

```css
@keyframes anime {
  0% {
    background-position-x: 0px;
    background-position-y: 50%;
  }
  50% {
    background-position-x: 100%;
    background-position-y: 50%;
  }
  100% {
    background-position-x: 0px;
    background-position-y: 50%;
  }
}
```

> Background color/gradient shift · Background position (shimmer/scroll)

### `@keyframes anime`

Duration: `8s` · Easing: `linear` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `#rcFooter footer .rc-footer-cta`

```css
@keyframes anime {
  0% {
    background-position-x: 0px;
    background-position-y: 50%;
  }
  50% {
    background-position-x: 100%;
    background-position-y: 50%;
  }
  100% {
    background-position-x: 0px;
    background-position-y: 50%;
  }
}
```

> Background color/gradient shift · Background position (shimmer/scroll)

### `@keyframes splide-loading`

Duration: `1s` · Easing: `linear` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.splide__spinner`

```css
@keyframes splide-loading {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(1turn);
  }
}
```

> Transform/motion animation

### `@keyframes agent-shimmer-962d5e26`

Duration: `1.4s` · Easing: `ease` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.agent-loading__bar[data-v-962d5e26]`

```css
@keyframes agent-shimmer-962d5e26 {
  0% {
    background-position-x: 200%;
    background-position-y: 0px;
  }
  100% {
    background-position-x: -200%;
    background-position-y: 0px;
  }
}
```

> Background color/gradient shift · Background position (shimmer/scroll)

### `@keyframes rc-tv-toaster-shimmer`

Duration: `1.3s` · Easing: `linear` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.rc-tv-toaster__skeleton`

```css
@keyframes rc-tv-toaster-shimmer {
  0% {
    background-position-x: 150%, 0px;
    background-position-y: 0px, 0px;
  }
  100% {
    background-position-x: -150%, 0px;
    background-position-y: 0px, 0px;
  }
}
```

> Background color/gradient shift · Background position (shimmer/scroll)

### `@keyframes rc-tv-toaster-chevron`

Duration: `1.8s` · Easing: `ease-in-out` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.rc-tv-toaster__restore-logo path`

```css
@keyframes rc-tv-toaster-chevron {
  0%, 100% {
    opacity: 0.45;
    transform: translateY(1px);
  }
  50% {
    opacity: 1;
    transform: translateY(-1.5px);
  }
}
```

> Fade + motion enter animation

### `@keyframes rc-tv-toaster-spin`

Duration: `6s` · Easing: `linear` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.rc-tv-toaster__restore-mark svg`

```css
@keyframes rc-tv-toaster-spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(1turn);
  }
}
```

> Transform/motion animation

### `@keyframes ripple`

Duration: `1s` · Easing: `linear` · Delay: `0s` · Iteration: `1` · Fill: `none`

Used by: `.index .rc-hero--ripple:hover .rc-ripple`

```css
@keyframes ripple {
  0% {
    opacity: 1;
    transform: rotate(60deg) translate(200px, 300px);
  }
  100% {
    opacity: 1;
    transform: rotate(60deg) translate(200px);
  }
}
```

> Fade + motion enter animation

### `@keyframes scroll-left`

Duration: `18s` · Easing: `linear` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.index .rc-marquee__track`

```css
@keyframes scroll-left {
  0% {
    transform: translate(0px);
  }
  100% {
    transform: translate(-50%);
  }
}
```

> Transform/motion animation

### `@keyframes animatedgradient`

Duration: `3s` · Easing: `ease` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.index .rc-marquee:hover::after`

```css
@keyframes animatedgradient {
  0% {
    background-position-x: 0px;
    background-position-y: 50%;
  }
  50% {
    background-position-x: 100%;
    background-position-y: 50%;
  }
  100% {
    background-position-x: 0px;
    background-position-y: 50%;
  }
}
```

> Background color/gradient shift · Background position (shimmer/scroll)

### `@keyframes fadeInRight`

Used by: `.index .fadeInRight`

```css
@keyframes fadeInRight {
  0% {
    opacity: 0;
    transform: translate3d(10%, 0px, 0px);
  }
  100% {
    opacity: 1;
    transform: none;
  }
}
```

> Fade + motion enter animation

### `@keyframes fadeInLeft`

Used by: `.index .fadeInLeft`

```css
@keyframes fadeInLeft {
  0% {
    opacity: 0.1;
    transform: translate3d(-10%, 0px, 0px);
  }
  100% {
    opacity: 1;
    transform: none;
  }
}
```

> Fade + motion enter animation

### `@keyframes fadeInUp`

Used by: `.index .fadeInUp`

```css
@keyframes fadeInUp {
  0% {
    opacity: 0.7;
    transform: translate3d(0px, 15%, 0px);
  }
  100% {
    opacity: 1;
    transform: none;
  }
}
```

> Fade + motion enter animation

### `@keyframes za-cta-heart-blink`

Duration: `0.65s` · Easing: `ease-in-out` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.index .za-grid__col:hover .za-cta--heart`

```css
@keyframes za-cta-heart-blink {
  0%, 100% {
    opacity: 1;
    scale: 1;
  }
  50% {
    opacity: 0.2;
    scale: 0.8;
  }
}
```

> Opacity fade

### `@keyframes showLogo`

Duration: `0.4s` · Easing: `ease-in-out` · Delay: `0s` · Iteration: `1` · Fill: `forwards`

Used by: `.index .rc-slider__body .slick-slide.slick-current [class^="cb-storybook-img"]`

```css
@keyframes showLogo {
  100% {
    opacity: 1;
    transform: translate(0px);
  }
}
```

> Fade + motion enter animation

### `@keyframes showAuthorInfo`

Duration: `0.25s` · Easing: `ease-in-out` · Delay: `0.5s` · Iteration: `1` · Fill: `forwards`

Used by: `.index .rc-slider--casestudy .card.active .rc-casestudy__body`

```css
@keyframes showAuthorInfo {
  100% {
    opacity: 1;
    transform: translateY(0px);
  }
}
```

> Fade + motion enter animation

### `@keyframes scrollRowOne`

```css
@keyframes scrollRowOne {
  0% {
    background-position-x: 0px;
    background-position-y: 0px;
  }
  100% {
    background-position-x: -860px;
    background-position-y: 0px;
  }
}
```

> Background color/gradient shift · Background position (shimmer/scroll)

### `@keyframes scrollRowTwo`

```css
@keyframes scrollRowTwo {
  0% {
    background-position-x: 0px;
    background-position-y: 0px;
  }
  100% {
    background-position-x: 690px;
    background-position-y: 0px;
  }
}
```

> Background color/gradient shift · Background position (shimmer/scroll)

### `@keyframes scrollRowOne`

```css
@keyframes scrollRowOne {
  0% {
    background-position-x: 0px;
    background-position-y: 0px;
  }
  100% {
    background-position-x: -860px;
    background-position-y: 0px;
  }
}
```

> Background color/gradient shift · Background position (shimmer/scroll)

### `@keyframes scrollRowTwo`

```css
@keyframes scrollRowTwo {
  0% {
    background-position-x: 0px;
    background-position-y: 0px;
  }
  100% {
    background-position-x: 690px;
    background-position-y: 0px;
  }
}
```

> Background color/gradient shift · Background position (shimmer/scroll)

## Global Transition Declarations

These `transition` values were extracted from CSS rules across the site:

```css
transition: transform 0.3s;
transition: 0.3s cubic-bezier(0.4, 0, 0.2, 1);
transition: opacity 0.35s;
transition: opacity 0.4s;
transition: background 0.2s;
transition: transform 0.2s;
transition: opacity 0.28s, max-height 0.28s;
transition: opacity 0.2s, background-color 0.2s;
transition: transform 0.4s, opacity 0.4s;
transition: opacity 0.25s ease-in-out;
transition: 0.25s ease-in-out;
transition: 0.3s ease-in-out;
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
  transition: opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1),
              transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}
```

### Step 3 — Key Motion Principles

- **Duration scale:** `0.3s` · `0.35s` · `0.4s` · `0.2s` — use these values, never invent new durations
- **Always add** `@media (prefers-reduced-motion: reduce) { * { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; } }`

### Step 4 — Scroll Journey Reference

Match what happens at each scroll position:

- **0%** (`0px`) → `screens/scroll/scroll-000.png`
- **17%** (`1554px`) → `screens/scroll/scroll-017.png`
- **33%** (`3017px`) → `screens/scroll/scroll-033.png`
- **50%** (`4571px`) → `screens/scroll/scroll-050.png`
- **67%** (`6125px`) → `screens/scroll/scroll-067.png`
- **83%** (`7588px`) → `screens/scroll/scroll-083.png`
- **100%** (`9142px`) → `screens/scroll/scroll-100.png`

## Layout & Grid (LAYOUT.md)

# Layout Reference

> Auto-extracted from live DOM. Use this to understand how the site is structured spatially.

## Spacing System

**Base grid:** 4px

**Scale:** `2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30` px

| Spacing | Semantic Use |
|---------|-------------|
| 4px | Tight — within a component |
| 8px | Medium — between sibling items |
| 16px | Wide — between sections |
| 32px | Vast — major section breaks |

## Flex Layouts

| Element | Direction | Justify | Align | Gap | Children |
|---------|-----------|---------|-------|-----|----------|
| `nav#navigation-menu.hds-navigation-menu.navigation-menu` | row | — | center | 16px | 4 |
| `div.rc-bg__buttons.rc-bg__buttons--row1` | row | — | — | — | 2 |
| `div.rc-bg__buttons.rc-bg__buttons--row1` | row | — | — | — | 2 |
| `div.rc-bg__buttons.rc-bg__buttons--row3` | row | — | — | — | 2 |
| `div.rc-bg__buttons.rc-bg__buttons--row4` | row | — | — | — | 2 |
| `div.hero-cta-group` | row | center | center | 20px | 1 |
| `div.rc-bg__buttons__container` | row | — | center | — | 8 |
| `div.rc-bg__buttons__container` | row | — | center | — | 8 |
| `div.rc-bg__buttons__container` | row | — | center | — | 11 |
| `div.rc-bg__buttons__container` | row | — | center | — | 8 |
| `div.rc-bg__buttons__container` | row | — | center | — | 8 |
| `div.rc-bg__buttons__container` | row | — | center | — | 8 |
| `div.rc-bg__buttons__container` | row | — | center | — | 10 |
| `div.rc-bg__buttons__container` | row | — | center | — | 6 |

## Grid Layouts

| Element | Template Columns | Gap | Children |
|---------|-----------------|-----|----------|
| `div.rc-grid.rc-gap-5` | `1440px` | 0px | 2 |
| `div.rc-bg__buttons__wrapper` | `1440px` | — | 4 |
| `div.za-wrapper__body` | `320px 908px` | normal 60px | 2 |
| `div.rc-grid.rc-relative` | `1440px` | — | 3 |
| `div.rc-trusted__container` | `33.0781px 33.0781px 33.0781px 33.0781px 33.0781px ` | 10px | 4 |

## Structural Containers

### `<header>` (`header.cb-header`)

```
display:          block
children:         1
```

### `<footer>` (`footer.deferred-section.rc-bg-contain`)

```
display:          block
children:         2
```

### `<nav>` (`nav#navigation-menu.hds-navigation-menu.navigation-menu`)

```
display:          flex
flex-direction:   row
justify-content:  —
align-items:      center
gap:              16px
children:         4
```

## Layout Rules

- **Container max-width:** `1440px` — always center with `margin: auto`
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
| **Rc Font Bold** | unknown | 7× | `.rc-font-bold` |
| **SvgPosition** | unknown | 7× | `.svgPosition` |
| **Rc Button  Arrow** | button | 6× | `.rc-button__arrow` |
| **Main Card Image** | card | 6× | `.main-card-image` |
| **Cb Button Reset** | button | 5× | `.cb-button-reset`, `.cb-focusable`, `.hds-navigation-menu__trigger` |
| **Nav Tab** | nav-item | 5× | `.nav-tab` |
| **Rc Container** | unknown | 5× | `.rc-container` |
| **Hds Navigation Menu  Item** | card | 4× | `.hds-navigation-menu__item`, `.navigation-item` |
| **Lazy Video** | unknown | 3× | `.lazy-video`, `.rc-video-as--bg` |
| **Za Testimonial  Header** | unknown | 3× | `.za-testimonial__header` |
| **Za Testimonial  Aside** | unknown | 3× | `.za-testimonial__aside` |
| **Za Testimonial  Designation** | unknown | 3× | `.za-testimonial__designation` |
| **Za Testimonial  Logo** | unknown | 3× | `.za-testimonial__logo` |
| **Cb Storybook Img  Whereby  Primary  Right** | unknown | 3× | `.cb-storybook-img__whereby--primary--right` |
| **Logo Primary** | unknown | 3× | `.logo-primary`, `.parent` |
| **Za Testimonial  Body** | unknown | 3× | `.za-testimonial__body` |
| **Za Testimonial  Content** | unknown | 3× | `.za-testimonial__content` |
| **Za Masonry** | unknown | 3× | `.za-masonry` |
| **Za Masonry  Header** | unknown | 3× | `.za-masonry__header` |
| **Za Masonry  Body** | unknown | 3× | `.za-masonry__body` |

## Cards

### Main Card Image

**Instances found:** 6

**CSS classes:** `.main-card-image`

**HTML structure:**

```html
<img src="https://webstatic.chargebee.com/assets/web/20260804043214/images/hero-animation/new/pricing-main.svg" alt="PRICING - Chargebee recurring billing platform" class="main-card-image" loading="eager" fetchpriority="high" width="690" height="490" data-v-2b4e77b5="">
```

**Base styles (from design tokens):**

```css
.main-card-image {
  background: #e8f4f5;
  border-radius: 29px;
  padding: 8px;
}```

### Hds Navigation Menu  Item

**Instances found:** 4

**CSS classes:** `.hds-navigation-menu__item` `.navigation-item`

**HTML structure:**

```html
<li class="hds-navigation-menu__item navigation-item" data-panel="products"><button type="button" class="hds-navigation-menu__trigger cb-button-reset cb-focusable" aria-expanded="false" aria-haspopup="true" id="navigation-trigger-products" aria-controls="navigation-panel-products"> Products <svg class="nav-chevron navigation__chevron-down-icon" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><path class="navigation__chevron-down-icon__left" d="M4.67065 6L9.3 10.6" stroke="currentColor" stroke-width="1.75"></path><pa
```

**Base styles (from design tokens):**

```css
.hds-navigation-menu__item {
  background: #e8f4f5;
  border-radius: 29px;
  padding: 8px;
}```

## Navigation Items

### Nav Tab

**Instances found:** 5

**CSS classes:** `.nav-tab`

**HTML structure:**

```html
<button type="button" class="nav-tab" data-v-2b4e77b5=""><span class="tab-icon" data-v-2b4e77b5=""><svg xmlns="http://www.w3.org/2000/svg" width="8" height="8" viewBox="0 0 8 8" fill="none"> <path fill-rule="evenodd" clip-rule="evenodd" d="M3.1065 0.246094H1.96208C1.61095 0.246094 1.32629 0.530745 1.32629 0.88188V6.73111C1.32629 7.08225 1.61094 7.3669 1.96208 7.3669H6.28543C6.63656 7.3669 6.92121 7.08225 6.92121 6.73111V4.06081C6.92121 3.35854 6.35191 2.78924 5.64964 2.78924H5.01385C4.66272 2.78924 4.37807 2.50459 4.37807 2.15345V1.51767C4.37807 0.815396 3.80876 0.246094 3.1065 0.246094ZM5.347
```

**Base styles (from design tokens):**

```css
.nav-tab {
  padding: 4px 8px;
  cursor: pointer;
  /* active: color: #ff5722; */
}```

## Buttons

### Rc Button  Arrow

**Instances found:** 6

**CSS classes:** `.rc-button__arrow`

**HTML structure:**

```html
<span class="rc-button__arrow">Get a Demo</span>
```

**Base styles (from design tokens):**

```css
.rc-button__arrow {
  background: #ff5722;
  color: #012a38;
  border-radius: 29px;
  padding: 4px 8px;
  cursor: pointer;
}```

### Cb Button Reset

**Instances found:** 5

**CSS classes:** `.cb-button-reset` `.cb-focusable` `.hds-navigation-menu__trigger`

**HTML structure:**

```html
<button type="button" class="hds-navigation-menu__trigger cb-button-reset cb-focusable" aria-expanded="false" aria-haspopup="true" id="navigation-trigger-products" aria-controls="navigation-panel-products"> Products <svg class="nav-chevron navigation__chevron-down-icon" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><path class="navigation__chevron-down-icon__left" d="M4.67065 6L9.3 10.6" stroke="currentColor" stroke-width="1.75"></path><path class="navigation__chevron-down-icon__right" d="M12.6707 6L8.67065 10" st
```

**Base styles (from design tokens):**

```css
.cb-button-reset {
  background: #ff5722;
  color: #012a38;
  border-radius: 29px;
  padding: 4px 8px;
  cursor: pointer;
}```

## Other Components

### Rc Font Bold

**Instances found:** 7

**CSS classes:** `.rc-font-bold`

**HTML structure:**

```html
<span class="rc-font-bold"> Propelling subscription operations in 130+ countries </span>
```

**Base styles (from design tokens):**

```css
.rc-font-bold {
  background: #e8f4f5;
  padding: 4px;
}```

### SvgPosition

**Instances found:** 7

**CSS classes:** `.svgPosition`

**HTML structure:**

```html
<svg class="svgPosition" preserveAspectRatio="xMaxYMin" width="100%" height="100%" viewBox="0 0 140 80" fill="none"><path fill-rule="evenodd" clip-rule="evenodd" d="M47.3107 37.1693C47.2399 41.4483 45.5889 45.5499 42.6755 48.6845V25.8204C44.1628 27.3182 45.3383 29.0962 46.1339 31.0513C46.9295 33.0065 47.3295 35.1001 47.3107 37.2108M51.3431 37.0238C51.2501 33.9831 50.4909 30.9998 49.1189 28.2846C47.747 25.5694 45.7957 23.1885 43.403 21.3099C41.9402 20.1504 40.3419 19.1732 38.6431 18.3999V61.6132H42.6755V54.1719C49.1606 47.5621 51.3431 43.3426 51.3431 37.0861" fill="var(--primary-color, #8A1A31)
```

**Base styles (from design tokens):**

```css
.svgPosition {
  background: #e8f4f5;
  padding: 4px;
}```

### Rc Container

**Instances found:** 5

**CSS classes:** `.rc-container`

**HTML structure:**

```html
<div class="rc-container"><div class="rc-trusted__container"><div class="rc-trusted__gartner rc-corner--smooth"><video class="rc-video-as--bg lazy-video" aria-label="Chargebee Gartner Magic Quadrant Leader 2025" loop="" muted="" playsinline="" webkit-playsinline="" preload="none" poster="https://webstatic.chargebee.com/assets/web/20260804043214/images/home_v2/oct-2025/gartner-video.webp" data-autoplay=""><source src="https://webstatic.chargebee.com/assets/web/20260804043214/images/home_v2/oct-2025/gartner-video.mp4" type="video/mp4"> Your browser does not support the video tag. </video><div cl
```

**Base styles (from design tokens):**

```css
.rc-container {
  background: #e8f4f5;
  padding: 4px;
}```

### Lazy Video

**Instances found:** 3

**CSS classes:** `.lazy-video` `.rc-video-as--bg`

**HTML structure:**

```html
<video class="rc-video-as--bg lazy-video" aria-label="Chargebee Gartner Magic Quadrant Leader 2025" loop="" muted="" playsinline="" webkit-playsinline="" preload="none" poster="https://webstatic.chargebee.com/assets/web/20260804043214/images/home_v2/oct-2025/gartner-video.webp" data-autoplay=""><source src="https://webstatic.chargebee.com/assets/web/20260804043214/images/home_v2/oct-2025/gartner-video.mp4" type="video/mp4"> Your browser does not support the video tag. </video>
```

**Base styles (from design tokens):**

```css
.lazy-video {
  background: #e8f4f5;
  padding: 4px;
}```

### Za Testimonial  Header

**Instances found:** 3

**CSS classes:** `.za-testimonial__header`

**HTML structure:**

```html
<div class="za-testimonial__header"><div class="za-testimonial__img"><picture><!--[--><source type="image/webp" sizes="(max-width: 640px) 320px, (max-width: 768px) 640px, (max-width: 1024px) 768px, (max-width: 1280px) 1024px, (max-width: 1440px) 1280px, (max-width: 1536px) 1440px, (max-width: 1600px) 1536px, (max-width: 1920px) 1600px, 1920px" srcset="https://webstatic.chargebee.com/assets/web/20260804043214/images/home_v2/testimonial/aside/iwona-włodarczy.webp 320w, https://webstatic.chargebee.com/assets/web/20260804043214/images/home_v2/testimonial/aside/iwona-włodarczy.webp 640w, https://we
```

**Base styles (from design tokens):**

```css
.za-testimonial__header {
  background: #e8f4f5;
  padding: 4px;
}```

### Za Testimonial  Aside

**Instances found:** 3

**CSS classes:** `.za-testimonial__aside`

**HTML structure:**

```html
<div class="za-testimonial__aside"><div class="za-testimonial__designation"><strong>Iwona Włodarczyk,</strong> Head of Product </div><div class="za-testimonial__logo"><div class="cb-storybook-img__whereby--primary--right"><svg class="parent logo-primary" width="100%" height="100%" viewBox="0 0 248 80" fill="none"><svg class="svgPosition" preserveAspectRatio="xMaxYMin" width="100%" height="100%" viewBox="0 0 144 80" fill="none"><path d="M28.235 21.1992C25.7273 21.1992 23.0286 23.1337 20.8791 27.6714L18.1087 21.032H17.9415C17.4878 22.0828 16.0548 22.656 14.7174 22.656H0.125V22.9426C1.29525 23.44
```

**Base styles (from design tokens):**

```css
.za-testimonial__aside {
  background: #e8f4f5;
  padding: 4px;
}```

### Za Testimonial  Designation

**Instances found:** 3

**CSS classes:** `.za-testimonial__designation`

**HTML structure:**

```html
<div class="za-testimonial__designation"><strong>Iwona Włodarczyk,</strong> Head of Product </div>
```

**Base styles (from design tokens):**

```css
.za-testimonial__designation {
  background: #e8f4f5;
  padding: 4px;
}```

### Za Testimonial  Logo

**Instances found:** 3

**CSS classes:** `.za-testimonial__logo`

**HTML structure:**

```html
<div class="za-testimonial__logo"><div class="cb-storybook-img__whereby--primary--right"><svg class="parent logo-primary" width="100%" height="100%" viewBox="0 0 248 80" fill="none"><svg class="svgPosition" preserveAspectRatio="xMaxYMin" width="100%" height="100%" viewBox="0 0 144 80" fill="none"><path d="M28.235 21.1992C25.7273 21.1992 23.0286 23.1337 20.8791 27.6714L18.1087 21.032H17.9415C17.4878 22.0828 16.0548 22.656 14.7174 22.656H0.125V22.9426C1.29525 23.4441 2.32221 25.1398 3.27752 27.4326L12.353 49.3331H12.6396L18.5386 35.0751L24.4376 49.3331H24.7242L29.7635 36.8185C31.7219 31.8987 32.
```

**Base styles (from design tokens):**

```css
.za-testimonial__logo {
  background: #e8f4f5;
  padding: 4px;
}```

### Cb Storybook Img  Whereby  Primary  Right

**Instances found:** 3

**CSS classes:** `.cb-storybook-img__whereby--primary--right`

**HTML structure:**

```html
<div class="cb-storybook-img__whereby--primary--right"><svg class="parent logo-primary" width="100%" height="100%" viewBox="0 0 248 80" fill="none"><svg class="svgPosition" preserveAspectRatio="xMaxYMin" width="100%" height="100%" viewBox="0 0 144 80" fill="none"><path d="M28.235 21.1992C25.7273 21.1992 23.0286 23.1337 20.8791 27.6714L18.1087 21.032H17.9415C17.4878 22.0828 16.0548 22.656 14.7174 22.656H0.125V22.9426C1.29525 23.4441 2.32221 25.1398 3.27752 27.4326L12.353 49.3331H12.6396L18.5386 35.0751L24.4376 49.3331H24.7242L29.7635 36.8185C31.7219 31.8987 32.9877 29.1999 32.9877 26.74C32.9399
```

**Base styles (from design tokens):**

```css
.cb-storybook-img__whereby--primary--right {
  background: #e8f4f5;
  padding: 4px;
}```

### Logo Primary

**Instances found:** 3

**CSS classes:** `.logo-primary` `.parent`

**HTML structure:**

```html
<svg class="parent logo-primary" width="100%" height="100%" viewBox="0 0 248 80" fill="none"><svg class="svgPosition" preserveAspectRatio="xMaxYMin" width="100%" height="100%" viewBox="0 0 144 80" fill="none"><path d="M28.235 21.1992C25.7273 21.1992 23.0286 23.1337 20.8791 27.6714L18.1087 21.032H17.9415C17.4878 22.0828 16.0548 22.656 14.7174 22.656H0.125V22.9426C1.29525 23.4441 2.32221 25.1398 3.27752 27.4326L12.353 49.3331H12.6396L18.5386 35.0751L24.4376 49.3331H24.7242L29.7635 36.8185C31.7219 31.8987 32.9877 29.1999 32.9877 26.74C32.9399 23.4919 31.1248 21.1992 28.235 21.1992ZM14.6218 41.738
```

**Base styles (from design tokens):**

```css
.logo-primary {
  background: #e8f4f5;
  padding: 4px;
}```

### Za Testimonial  Body

**Instances found:** 3

**CSS classes:** `.za-testimonial__body`

**HTML structure:**

```html
<div class="za-testimonial__body"><div class="za-testimonial__content"><span class="rc-font-bold"> Propelling subscription operations in 1…</span><span> Chargebee gives us the flexibility to c…</span></div></div>
```

**Base styles (from design tokens):**

```css
.za-testimonial__body {
  background: #e8f4f5;
  padding: 4px;
}```

### Za Testimonial  Content

**Instances found:** 3

**CSS classes:** `.za-testimonial__content`

**HTML structure:**

```html
<div class="za-testimonial__content"><span class="rc-font-bold"> Propelling subscription operations in 1…</span><span> Chargebee gives us the flexibility to c…</span></div>
```

**Base styles (from design tokens):**

```css
.za-testimonial__content {
  background: #e8f4f5;
  padding: 4px;
}```

### Za Masonry

**Instances found:** 3

**CSS classes:** `.za-masonry`

**HTML structure:**

```html
<div class="za-masonry" id="za-masonry--1"><div class="za-masonry__header"><div class="za-masonry__title za-masonry__title--nosudo">Monetize your way</div></div><div class="za-masonry__body"><div class="za-masonry__bg"></div><div class="za-masonry__main"><div class="za-masonry__row"><div class="za-grid"><div class="za-grid__row za-grid__row--b"><div class="za-grid__col za-grid__col--jcfe"><div class="za-media za-media--highlighted za-media--bg za-media--col-alt2"><div class="za-media__aside"><div class="za-media__figure -rc-ml-10"></div></div></div></div></div></div></div></div></div></div>
```

**Base styles (from design tokens):**

```css
.za-masonry {
  background: #e8f4f5;
  padding: 4px;
}```

### Za Masonry  Header

**Instances found:** 3

**CSS classes:** `.za-masonry__header`

**HTML structure:**

```html
<div class="za-masonry__header"><div class="za-masonry__title za-masonry__title--nosudo">Monetize your way</div></div>
```

**Base styles (from design tokens):**

```css
.za-masonry__header {
  background: #e8f4f5;
  padding: 4px;
}```

### Za Masonry  Body

**Instances found:** 3

**CSS classes:** `.za-masonry__body`

**HTML structure:**

```html
<div class="za-masonry__body"><div class="za-masonry__bg"></div><div class="za-masonry__main"><div class="za-masonry__row"><div class="za-grid"><div class="za-grid__row za-grid__row--b"><div class="za-grid__col za-grid__col--jcfe"><div class="za-media za-media--highlighted za-media--bg za-media--col-alt2"><div class="za-media__aside"><div class="za-media__figure -rc-ml-10"><picture><!--[--><source type="image/webp" sizes="(max-width: 640px) 320px, (max-width: 768px) 640px, (max-width: 1024px) 768px, (max-width: 1280px) 1024px, (max-width: 1440px) 1280px, (max-width: 1536px) 1440px, (max-width:
```

**Base styles (from design tokens):**

```css
.za-masonry__body {
  background: #e8f4f5;
  padding: 4px;
}```

## Component Rules

- Match class names exactly from the patterns above
- Each component instance must be visually identical to others of its type
- Do not add extra wrappers or change the DOM structure
- Use `#ff5722` for all interactive/active states

## Interactions & States (INTERACTIONS.md)

# Interaction Reference

> Micro-interactions extracted from live DOM. Recreate these exactly for authentic feel.

## Coverage

| Component Type | Count | States Captured |
|----------------|-------|----------------|
| Button | 3 | default, hover, focus |
| Role Button | 3 | default, hover, focus |
| Link | 3 | default, focus, hover |

## Transition System

These transition declarations were extracted from interactive elements:

```css
transition: color 0.2s, background 0.2s;
transition: opacity 0.2s, background-color 0.2s;
transition: color 0.24s cubic-bezier(0.45, 0.05, 0.55, 0.95), background-color 0.24s cubic-bezier(0.45, 0.05, 0.55, 0.95), border-color 0.24s cubic-bezier(0.45, 0.05, 0.55, 0.95);
transition: all;
transition: opacity 0.24s cubic-bezier(0.45, 0.05, 0.55, 0.95);
```

Apply these to all interactive elements. Never invent new durations or easings.

## Button Interactions

### Button 1 — `Open view mode toggle`

**States:**

- Default: `../screens/states/button-1-default.png`
- Hover: `../screens/states/button-1-hover.png`
- Focus: `../screens/states/button-1-focus.png`

**On hover:**

```css
/* color: rgba(255, 255, 255, 0.85) → */ color: rgb(255, 255, 255);
/* border-color: rgba(255, 255, 255, 0.85) → */ border-color: rgb(255, 255, 255);
/* outline: rgba(255, 255, 255, 0.85) none 3px → */ outline: rgb(255, 255, 255) none 3px;
/* outline-color: rgba(255, 255, 255, 0.85) → */ outline-color: rgb(255, 255, 255);
```

**Transition:** `color 0.2s, background 0.2s`

### Button 2 — `Dismiss banner`

**States:**

- Default: `../screens/states/button-2-default.png`
- Hover: `../screens/states/button-2-hover.png`
- Focus: `../screens/states/button-2-focus.png`

**On hover:**

```css
/* background-color: rgba(0, 0, 0, 0) → */ background-color: rgba(1, 42, 56, 0.06);
/* opacity: 0.75 → */ opacity: 1;
```

**Transition:** `opacity 0.2s, background-color 0.2s`

### Button 3 — `Products`

**States:**

- Default: `../screens/states/button-3-default.png`
- Hover: `../screens/states/button-3-hover.png`
- Focus: `../screens/states/button-3-focus.png`

**On focus:**

```css
/* outline: rgb(1, 42, 56) none 3px → */ outline: rgb(255, 51, 0) solid 2px;
/* outline-color: rgb(1, 42, 56) → */ outline-color: rgb(255, 51, 0);
```

**Transition:** `color 0.24s cubic-bezier(0.45, 0.05, 0.55, 0.95), background-color 0.24s cubic-bezier(0.45, 0.05, 0.55, 0.95), border-color 0.24s cubic-bezier(0.45, 0.05, 0.55, 0.95)`

## Role Button Interactions

### Role Button 1 — `Go to slide 1`

**States:**

- Default: `../screens/states/role-button-1-default.png`
- Hover: `../screens/states/role-button-1-hover.png`
- Focus: `../screens/states/role-button-1-focus.png`

**On focus:**

```css
/* outline: rgb(1, 42, 56) none 3px → */ outline: rgb(0, 187, 255) solid 3px;
/* outline-color: rgb(1, 42, 56) → */ outline-color: rgb(0, 187, 255);
```

**Transition:** `all`

### Role Button 2 — `AI`

**States:**

- Default: `../screens/states/role-button-2-default.png`
- Hover: `../screens/states/role-button-2-hover.png`
- Focus: `../screens/states/role-button-2-focus.png`

**On focus:**

```css
/* outline: rgb(1, 42, 56) none 3px → */ outline: rgb(0, 187, 255) solid 3px;
/* outline-color: rgb(1, 42, 56) → */ outline-color: rgb(0, 187, 255);
```

**Transition:** `all`

### Role Button 3 — `Media`

**States:**

- Default: `../screens/states/role-button-3-default.png`
- Hover: `../screens/states/role-button-3-hover.png`
- Focus: `../screens/states/role-button-3-focus.png`

**On focus:**

```css
/* outline: rgb(1, 42, 56) none 3px → */ outline: rgb(0, 187, 255) solid 3px;
/* outline-color: rgb(1, 42, 56) → */ outline-color: rgb(0, 187, 255);
```

**Transition:** `all`

## Link Interactions

### Link 1 — `Accessibility Screen-Reader Guide, Feedb`

**States:**

- Default: `../screens/states/link-1-default.png`
- Focus: `../screens/states/link-1-focus.png`

**Transition:** `all`

_No visible style changes detected for this element._

### Link 2 — `Learn more`

**States:**

- Default: `../screens/states/link-2-default.png`
- Hover: `../screens/states/link-2-hover.png`
- Focus: `../screens/states/link-2-focus.png`

**On focus:**

```css
/* outline: rgb(255, 51, 0) none 3px → */ outline: rgb(1, 42, 56) solid 2px;
/* outline-color: rgb(255, 51, 0) → */ outline-color: rgb(1, 42, 56);
```

**Transition:** `all`

### Link 3 — `Chargebee homepage`

**States:**

- Default: `../screens/states/link-3-default.png`
- Hover: `../screens/states/link-3-hover.png`
- Focus: `../screens/states/link-3-focus.png`

**On hover:**

```css
/* opacity: 1 → */ opacity: 0.7;
```

**On focus:**

```css
/* outline: rgb(1, 42, 56) none 3px → */ outline: rgb(255, 51, 0) solid 2px;
/* outline-color: rgb(1, 42, 56) → */ outline-color: rgb(255, 51, 0);
```

**Transition:** `opacity 0.24s cubic-bezier(0.45, 0.05, 0.55, 0.95)`

## Interaction Rules

- Accent color `#ff5722` is used for focus rings, active states, and hover highlights
- Hover effects use **opacity** changes, not color shifts
- Hover effects include **color transitions** — use the extracted values, not approximations
- Focus states use **outline** (not box-shadow) — always match the extracted focus ring
- Transition durations in use: `0.2s`, `0.24s`
- Always respect `prefers-reduced-motion` — set all transitions to `0s` when enabled

## Design Tokens — JSON Files

### tokens/colors.json
```json
{
  "$schema": "https://design-tokens.github.io/community-group/format/",
  "core": {
    "text-primary": {
      "value": "#012a38",
      "role": "text-primary",
      "name": "theme-color"
    },
    "background": {
      "value": "#ffffff",
      "role": "background",
      "name": "tw-ring-offset-color"
    },
    "text-muted": {
      "value": "#8a9aa1",
      "role": "text-muted",
      "name": "cb-text-subtle"
    },
    "surface": {
      "value": "#e8f4f5",
      "role": "surface",
      "name": "tw-ring-offset-color"
    },
    "accent": {
      "value": "#ff5722",
      "role": "accent"
    }
  },
  "status": {
    "danger": {
      "value": "#ff3300",
      "role": "danger",
      "name": "tw-ring-color"
    }
  },
  "extended": {
    "color-e0e0e0": {
      "value": "#e0e0e0",
      "role": "unknown"
    },
    "color-9ca3af": {
      "value": "#9ca3af",
      "role": "unknown"
    },
    "color-bff90b": {
      "value": "#bff90b",
      "role": "unknown"
    },
    "cb-teal-muted": {
      "value": "#22748b",
      "role": "info",
      "name": "cb-teal-muted"
    },
    "iti-hover-color": {
      "value": "#000000",
      "role": "unknown",
      "name": "iti-hover-color"
    },
    "color-84e4ee": {
      "value": "#84e4ee",
      "role": "unknown"
    },
    "cb-ticker-muted": {
      "value": "#d3d9dc",
      "role": "unknown",
      "name": "cb-ticker-muted"
    },
    "color-d5f4f7": {
      "value": "#d5f4f7",
      "role": "unknown"
    },
    "color-03779e": {
      "value": "#03779e",
      "role": "unknown"
    },
    "color-90c2c7": {
      "value": "#90c2c7",
      "role": "unknown"
    },
    "color-335466": {
      "value": "#335466",
      "role": "unknown"
    },
    "color-174350": {
      "value": "#174350",
      "role": "unknown"
    }
  },
  "meta": {
    "theme": "light",
    "extracted": "2026-08-04"
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
    "max": 30
  }
}
```

### tokens/typography.json
```json
{
  "families": [
    "Sora",
    "Inter",
    "SF Mono"
  ],
  "scale": {
    "heading-1": {
      "fontFamily": "Sora",
      "fontSize": "250px",
      "fontWeight": "700",
      "lineHeight": null,
      "source": "css"
    },
    "heading-2": {
      "fontFamily": "Sora",
      "fontSize": "200px",
      "fontWeight": "700",
      "lineHeight": null,
      "source": "css"
    },
    "heading-3": {
      "fontFamily": "Sora",
      "fontSize": "190px",
      "fontWeight": "700",
      "lineHeight": null,
      "source": "css"
    },
    "body": {
      "fontFamily": "Inter",
      "fontSize": "14px",
      "fontWeight": "400",
      "lineHeight": null,
      "source": "css"
    },
    "caption": {
      "fontFamily": "Inter",
      "fontSize": "16px",
      "fontWeight": "400",
      "lineHeight": null,
      "source": "css"
    },
    "code": {
      "fontFamily": "SF Mono",
      "fontSize": "14px",
      "fontWeight": "400",
      "lineHeight": null,
      "source": "css"
    }
  },
  "fontFaces": [
    {
      "family": "Inter",
      "src": "https://www.chargebee.com/_nuxt4/Inter-cyrillic-ext.Cpd2YT5r.woff2",
      "format": "woff2",
      "weight": "400"
    },
    {
      "family": "Inter",
      "src": "https://www.chargebee.com/_nuxt4/Inter-cyrillic.C5ekK6td.woff2",
      "format": "woff2",
      "weight": "400"
    },
    {
      "family": "Inter",
      "src": "https://www.chargebee.com/_nuxt4/Inter-greek-ext.Ai74Rjx-.woff2",
      "format": "woff2",
      "weight": "400"
    },
    {
      "family": "Inter",
      "src": "https://www.chargebee.com/_nuxt4/Inter-greek.BQL42Lnq.woff2",
      "format": "woff2",
      "weight": "400"
    },
    {
      "family": "Inter",
      "src": "https://www.chargebee.com/_nuxt4/Inter-vietnamese.YEzCLjIM.woff2",
      "format": "woff2",
      "weight": "400"
    },
    {
      "family": "Inter",
      "src": "https://www.chargebee.com/_nuxt4/Inter-latin-ext.B_-bZUTo.woff2",
      "format": "woff2",
      "weight": "400"
    },
    {
      "family": "Inter",
      "src": "https://www.chargebee.com/_nuxt4/Inter-latin.8kRkwJBP.woff2",
      "format": "woff2",
      "weight": "400"
    },
    {
      "family": "Sora",
      "src": "https://www.chargebee.com/_nuxt4/Sora-latin-ext.C4beA2JP.woff2",
      "format": "woff2",
      "weight": "400"
    },
    {
      "family": "Sora",
      "src": "https://www.chargebee.com/_nuxt4/Sora-latin.5v9NviDD.woff2",
      "format": "woff2",
      "weight": "400"
    }
  ],
  "rules": {
    "maxSizesPerScreen": 4,
    "headingWeightRange": "600-700",
    "bodyWeight": 400,
    "lineHeightBody": 1.5,
    "lineHeightHeading": 1.2
  }
}
```

## Bundled Fonts (fonts/)

The following font files are bundled in the `fonts/` directory:

- `fonts/Inter-Black.ttf`
- `fonts/Inter-Bold.ttf`
- `fonts/Inter-ExtraBold.ttf`
- `fonts/Inter-ExtraLight.ttf`
- `fonts/Inter-Light.ttf`
- `fonts/Inter-Medium.ttf`
- `fonts/Inter-Regular.ttf`
- `fonts/Inter-SemiBold.ttf`
- `fonts/Inter-Thin.ttf`
- `fonts/Sora-Bold.ttf`
- `fonts/Sora-ExtraBold.ttf`
- `fonts/Sora-ExtraLight.ttf`
- `fonts/Sora-Light.ttf`
- `fonts/Sora-Medium.ttf`
- `fonts/Sora-Regular.ttf`
- `fonts/Sora-SemiBold.ttf`
- `fonts/Sora-Thin.ttf`

Use these local font files in `@font-face` declarations instead of fetching from Google Fonts.

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

![mcp.png](screens/pages/mcp.png)

![pricing.png](screens/pages/pricing.png)

![schedule-a-demo.png](screens/pages/schedule-a-demo.png)

![startups.png](screens/pages/startups.png)

![trial-signup.png](screens/pages/trial-signup.png)

### Section Clips (screens/sections/)

*Clipped individual sections and components*

![home-section-8.png](screens/sections/home-section-8.png)

![home-section-9.png](screens/sections/home-section-9.png)

![mcp-section-1.png](screens/sections/mcp-section-1.png)

![mcp-section-2.png](screens/sections/mcp-section-2.png)

![pricing-section-4.png](screens/sections/pricing-section-4.png)

![pricing-section-5.png](screens/sections/pricing-section-5.png)

![startups-section-1.png](screens/sections/startups-section-1.png)

![startups-section-10.png](screens/sections/startups-section-10.png)

![startups-section-2.png](screens/sections/startups-section-2.png)

![startups-section-3.png](screens/sections/startups-section-3.png)

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

![link-1-default.png](screens/states/link-1-default.png)

![link-1-focus.png](screens/states/link-1-focus.png)

![link-2-default.png](screens/states/link-2-default.png)

![link-2-focus.png](screens/states/link-2-focus.png)

![link-2-hover.png](screens/states/link-2-hover.png)

![link-3-default.png](screens/states/link-3-default.png)

![link-3-focus.png](screens/states/link-3-focus.png)

![link-3-hover.png](screens/states/link-3-hover.png)

![role-button-1-default.png](screens/states/role-button-1-default.png)

![role-button-1-focus.png](screens/states/role-button-1-focus.png)

![role-button-1-hover.png](screens/states/role-button-1-hover.png)

![role-button-2-default.png](screens/states/role-button-2-default.png)

![role-button-2-focus.png](screens/states/role-button-2-focus.png)

![role-button-2-hover.png](screens/states/role-button-2-hover.png)

![role-button-3-default.png](screens/states/role-button-3-default.png)

![role-button-3-focus.png](screens/states/role-button-3-focus.png)

![role-button-3-hover.png](screens/states/role-button-3-hover.png)

### Screenshot Index (screens/INDEX.md)

# Screenshot Index

## Scroll Journey

> Shows the cinematic state at each point of the page

| Scroll | Y Position | File |
|--------|-----------|------|
| 0% | 0px | `screens/scroll/scroll-000.png` |
| 17% | 1554px | `screens/scroll/scroll-017.png` |
| 33% | 3017px | `screens/scroll/scroll-033.png` |
| 50% | 4571px | `screens/scroll/scroll-050.png` |
| 67% | 6125px | `screens/scroll/scroll-067.png` |
| 83% | 7588px | `screens/scroll/scroll-083.png` |
| 100% | 9142px | `screens/scroll/scroll-100.png` |

## Pages

| Page | URL | File |
|------|-----|------|
| Chargebee: Billing & Monetization for SaaS and AI Companies | `https://www.chargebee.com` | `screens/pages/home.png` |
| Plans and Pricing - Chargebee | `https://www.chargebee.com/pricing/` | `screens/pages/pricing.png` |
| Chargebee for Startups | Get Started for Free | `https://www.chargebee.com/startups/` | `screens/pages/startups.png` |
| Sign Up - Get Your Free Sandbox - Chargebee | `https://www.chargebee.com/trial-signup/` | `screens/pages/trial-signup.png` |
| Get a demo of Chargebee's Recurring Billing Platform Today | `https://www.chargebee.com/schedule-a-demo/` | `screens/pages/schedule-a-demo.png` |
| AI Billing Infrastructure with MCP Server | Chargebee | `https://www.chargebee.com/mcp/` | `screens/pages/mcp.png` |

## Sections

| Page | Section | File |
|------|---------|------|
| home | #8 ([class*="hero"]) | `screens/sections/home-section-8.png` |
| home | #9 ([class*="hero"]) | `screens/sections/home-section-9.png` |
| pricing | #4 ([class*="pricing"]) | `screens/sections/pricing-section-4.png` |
| pricing | #5 ([class*="pricing"]) | `screens/sections/pricing-section-5.png` |
| startups | #1 (section) | `screens/sections/startups-section-1.png` |
| startups | #2 (section) | `screens/sections/startups-section-2.png` |
| startups | #3 (section) | `screens/sections/startups-section-3.png` |
| startups | #10 ([class*="hero"]) | `screens/sections/startups-section-10.png` |
| mcp | #1 (section) | `screens/sections/mcp-section-1.png` |
| mcp | #2 (section) | `screens/sections/mcp-section-2.png` |

## Homepage Screenshots (screenshots/)

![homepage.png](screenshots/homepage.png)

