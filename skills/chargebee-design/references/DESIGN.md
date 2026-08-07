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
