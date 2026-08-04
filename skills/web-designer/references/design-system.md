# Design system — tokens before components

Before building any component, declare tokens. This is what separates "looks designed" from "thrown together". Even a one-page artifact deserves a token layer.

## Token hierarchy

1. **Primitives** — raw values (colors, font families, sizes). Don't use these directly in components.
2. **Semantic tokens** — intent-bound aliases (`color-text-primary`, `color-surface`, `space-md`). Components consume these.
3. **Component tokens** — per-component overrides when needed (`button-bg`, `card-border-radius`).

Use CSS variables in plain web, CSS + TS types in React/Next, or a tokens.json → Style Dictionary pipeline for multi-platform.

## Color

### Scale structure

Per color, generate a 50-950 lightness scale (11 stops). Tailwind does this by default; you can also:
- Start with brand color at 500.
- Generate via HSL by adjusting lightness in even steps.
- Check each stop for WCAG contrast against white and black.

### Semantic layer

```css
:root {
  /* Surfaces */
  --color-bg: #ffffff;
  --color-surface: #fafafa;
  --color-surface-raised: #ffffff;

  /* Text */
  --color-text: #111111;
  --color-text-muted: #6b7280;
  --color-text-subtle: #9ca3af;
  --color-text-inverse: #ffffff;

  /* Borders */
  --color-border: rgba(0, 0, 0, 0.08);
  --color-border-strong: rgba(0, 0, 0, 0.15);

  /* Interactive */
  --color-accent: #D4A853;
  --color-accent-hover: #C79A43;
  --color-accent-muted: rgba(212, 168, 83, 0.12);

  /* Semantic */
  --color-success: #10B981;
  --color-warning: #F59E0B;
  --color-danger:  #EF4444;
  --color-info:    #3B82F6;
}

[data-theme="dark"] {
  --color-bg: #050508;
  --color-surface: #0A0A0F;
  --color-surface-raised: #111118;
  --color-text: #E8E4DD;
  --color-text-muted: #8A8578;
  --color-border: rgba(255, 255, 255, 0.08);
  --color-border-strong: rgba(255, 255, 255, 0.15);
}
```

### Contrast rules (non-negotiable)

- Body text vs background: **≥ 4.5:1** (WCAG AA normal text).
- Large headings (≥24px bold or ≥18.66px bold): **≥ 3:1**.
- Interactive element borders/icons: **≥ 3:1**.
- Test with a contrast checker or `window.getComputedStyle` + formula. Never eyeball.

Never use pure black (`#000`) on pure white (`#FFF`) for body — it's sterile. Use `#111` on `#FAFAFA` or `#F9F5F0`.

## Typography

### Scale (modular)

Pick a ratio (`1.2` for UI/dense, `1.25` major third, `1.333` perfect fourth for editorial, `1.414` for dramatic display, `1.618` golden for luxury). Build from a base of 16px (1rem):

```css
:root {
  --text-xs:   0.75rem;   /* 12px */
  --text-sm:   0.875rem;  /* 14px */
  --text-base: 1rem;      /* 16px */
  --text-lg:   1.125rem;  /* 18px */
  --text-xl:   1.25rem;   /* 20px */
  --text-2xl:  1.5rem;    /* 24px */
  --text-3xl:  2rem;      /* 32px */
  --text-4xl:  2.5rem;    /* 40px */
  --text-5xl:  3.5rem;    /* 56px */
  --text-6xl:  clamp(4rem, 8vw, 8rem);
  --text-7xl:  clamp(5rem, 12vw, 14rem);  /* hero display */
}
```

For display type use fluid (`clamp`) so it scales with viewport. For body, fix at 16–18px — fluid body hurts readability.

### Font pairing

Always pair a **display** font with a **body** font. Optionally a **mono** for technical surfaces.

| Style | Display | Body | Mono |
|---|---|---|---|
| Editorial luxury | Fraunces, PP Editorial New, Instrument Serif | Switzer, Geist | Geist Mono |
| Premium minimal | Lyon, Newsreader | Geist Sans, SF Pro | JetBrains Mono |
| Dark tech | Clash Display, Geist, Monument Extended | Geist, Inter Display | Geist Mono |
| Brutalist Swiss | Archivo Black, Neue Haas Grotesk | Same, lower weight | IBM Plex Mono |
| Playful | Space Grotesk, Cabinet Grotesk | Inter | Space Mono |

### Line-height

- Display/headings: `0.95–1.1`
- Body: `1.5–1.7` (longer line lengths want higher line-height)
- UI labels: `1.2–1.4`

### Tracking (letter-spacing)

- Display large (>40px): `-0.02em` to `-0.04em` (negative tracking tightens large type)
- Body: `0` or `-0.005em`
- All-caps labels: `0.05em` to `0.15em`
- Monospace technical: `0.025em`

### Measure (line length)

Cap body text at **60–75 characters per line** (`max-width: 65ch`). Longer is fatiguing.

## Spacing

Use a single scale, not ad-hoc values. 4px or 8px base.

```css
:root {
  --space-0: 0;
  --space-1: 0.25rem;  /* 4px  */
  --space-2: 0.5rem;   /* 8px  */
  --space-3: 0.75rem;  /* 12px */
  --space-4: 1rem;     /* 16px */
  --space-6: 1.5rem;   /* 24px */
  --space-8: 2rem;     /* 32px */
  --space-12: 3rem;    /* 48px */
  --space-16: 4rem;    /* 64px */
  --space-24: 6rem;    /* 96px */
  --space-32: 8rem;    /* 128px */
  --space-48: 12rem;   /* 192px — section padding */
}
```

**Section padding rule:** double what feels right. `py-24` minimum on desktop for any major section. Premium designs use `py-32` to `py-48`.

## Radius

```css
:root {
  --radius-xs: 2px;
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 20px;
  --radius-2xl: 32px;
  --radius-full: 9999px;
}
```

**Concentric radius trick:** When nesting cards, the inner radius = outer radius − padding. `outer: 2rem, padding: 0.375rem → inner: calc(2rem - 0.375rem)`. This is what makes premium UI feel "machined".

## Shadows

Layered shadows > single shadow. Use at least 2 stops for realistic depth:

```css
:root {
  --shadow-xs: 0 1px 2px rgba(0, 0, 0, 0.04);
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.06), 0 1px 2px rgba(0, 0, 0, 0.04);
  --shadow-md: 0 4px 12px -2px rgba(0, 0, 0, 0.08), 0 2px 4px rgba(0, 0, 0, 0.04);
  --shadow-lg: 0 20px 40px -10px rgba(0, 0, 0, 0.12), 0 8px 16px rgba(0, 0, 0, 0.06);
  --shadow-xl: 0 40px 80px -20px rgba(0, 0, 0, 0.15), 0 16px 32px rgba(0, 0, 0, 0.08);
  --shadow-inner: inset 0 1px 0 rgba(255, 255, 255, 0.1);
}
```

Most "premium" UI uses `shadow-xl` or larger with low opacity — soft and diffused, not dark.

## Motion tokens

```css
:root {
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);           /* expo.out - punchy UI */
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);       /* smooth two-sided */
  --ease-apple: cubic-bezier(0.32, 0.72, 0, 1);        /* Apple-style deceleration */
  --ease-bounce: cubic-bezier(0.68, -0.55, 0.265, 1.55);

  --duration-fast: 150ms;
  --duration-base: 250ms;
  --duration-slow: 400ms;
  --duration-slower: 700ms;
  --duration-cinematic: 1200ms;
}
```

## Breakpoints

```css
/* mobile-first */
--breakpoint-sm:  640px;
--breakpoint-md:  768px;
--breakpoint-lg:  1024px;
--breakpoint-xl:  1280px;
--breakpoint-2xl: 1536px;
```

Design mobile first, always. Desktop is the bonus, not the base.

## Component architecture

### Hierarchy
1. **Primitives** — Button, Input, Icon, Text, Stack, Grid. Unopinionated, token-consuming.
2. **Patterns** — Card, Dialog, DropdownMenu, Tabs. Composed from primitives.
3. **Features** — Hero, PricingTable, FeatureGrid. Composed from patterns, domain-specific.

Use Radix UI / Ark UI / React Aria for accessibility-correct primitives; style with tokens.

### Variants

Define explicit variants, not boolean props. Use `cva` (class-variance-authority) or similar:

```ts
const button = cva("inline-flex items-center justify-center font-medium transition", {
  variants: {
    variant: {
      primary: "bg-accent text-white hover:bg-accent-hover",
      secondary: "bg-surface text-text border border-border hover:bg-surface-raised",
      ghost: "text-text hover:bg-surface-raised",
    },
    size: {
      sm: "h-8 px-3 text-sm rounded-md",
      md: "h-10 px-4 text-base rounded-lg",
      lg: "h-12 px-6 text-lg rounded-xl",
    },
  },
  defaultVariants: { variant: "primary", size: "md" },
});
```

## Developer handoff

When handing off:
- Ship `tokens.json` or `tokens.css` as the source of truth.
- Document components with props tables + usage examples (Storybook or MDX).
- Note responsive behavior per breakpoint.
- Include a11y notes: keyboard nav, ARIA, focus rings.
- Include motion specs: duration, ease, trigger.

## The test

Walk away for 10 minutes. Come back and scan the design. If you can tell it's yours without a logo — you have a point of view. That's the goal.
