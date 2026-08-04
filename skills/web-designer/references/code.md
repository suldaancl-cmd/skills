# Frontend implementation — React, Next.js, Vue, Svelte, Tailwind, HTML/CSS

Clean, performant, accessible code that matches the design. This file is about the implementation layer after the design is decided.

## Stack selection

| Situation | Stack |
|---|---|
| Single-page artifact (portfolio, landing, tool) | HTML + CSS + vanilla JS, or Astro |
| React app, needs SSR/routing | Next.js (App Router) |
| React app, SPA only | Vite + React |
| Vue app | Nuxt (SSR) or Vite + Vue |
| Content-heavy (blog, docs, marketing) | Astro, or Next.js if heavy interactivity |
| Interactive dashboard | React/Vue + TanStack Query + state library |
| Real-time / game-like | Svelte (smaller runtime) or React + R3F |

## Styling — pick one, don't mix

### Tailwind CSS (recommended default)
Fast iteration, no CSS file bloat, readable at the callsite, great design-token integration.

- Configure design tokens in `tailwind.config.ts` (colors, fonts, spacing, radius extend the defaults).
- Use `@apply` sparingly — almost never. Compose classes inline; extract to components when repeated.
- Use `cva` (class-variance-authority) for components with variants.
- Use `twMerge` to resolve conflicts in compound className logic.
- Use `clsx` / `cn()` for conditionals.

### CSS Modules
Good for teams averse to utility classes. Locality of styles, scoped class names.

### Styled-components / Emotion
Mostly legacy at this point. New projects: prefer Tailwind or CSS Modules + PostCSS.

### Vanilla CSS
Underrated. Modern CSS (cascade layers, `@scope`, `:has`, container queries, nesting) is extremely capable. For static sites and artifacts, plain CSS is often faster to write and ship than a CSS framework.

### Never
- Inline `style={}` for anything non-dynamic.
- Global CSS that leaks into components.
- Mixing two systems (Tailwind + styled-components in the same component).

## React patterns

### Server Components first (Next.js App Router)
Default to Server Components. Add `"use client"` only when you need:
- Event handlers
- Browser APIs (`window`, `document`, `localStorage`)
- State (`useState`, `useReducer`)
- Effects (`useEffect`)
- Refs to DOM
- Third-party libs that use these internally (Motion, GSAP, most UI libs)

### Component composition
```tsx
// Good — composable
<Card>
  <Card.Header>
    <Card.Title>Plan</Card.Title>
    <Card.Description>Monthly</Card.Description>
  </Card.Header>
  <Card.Content>{children}</Card.Content>
  <Card.Footer>
    <Button>Subscribe</Button>
  </Card.Footer>
</Card>

// Bad — over-prop-ified
<Card
  title="Plan"
  description="Monthly"
  content={<Pricing />}
  footerButton={{ label: "Subscribe", onClick: ... }}
/>
```

### Data fetching
- Server: fetch inline in Server Components.
- Client: TanStack Query (React Query). Don't roll your own cache.
- Mutations: Server Actions (Next.js) or TanStack Query mutations.
- Never: `useEffect` for data fetching. This is a 2020 pattern.

### Forms
- React Hook Form for complex forms.
- Server Actions with `useFormState` / `useActionState` for Next.js forms.
- Zod for schema validation (shared client/server).
- Accessibility: see `accessibility.md` — every input has a label.

### State management
- Local state: `useState`, `useReducer`.
- Shared state within a tree: `Context` (sparingly — causes re-renders).
- Global state: Zustand (simple), Jotai (atomic), Redux Toolkit (large apps).
- Server state: TanStack Query (not global state).
- URL state: `searchParams` (Next.js) or `useSearchParams`. Filters, pagination, tabs.

### Lists
- Every item needs a stable `key` — ID, not index.
- Virtualize lists over ~100 items (`@tanstack/react-virtual`).

### Images
- Next.js: `<Image>` component with explicit `width`/`height` or `fill` + sized parent.
- Raw HTML: `loading="lazy"`, `decoding="async"`, `<img>` with `srcset` for responsive.
- Always specify dimensions to prevent CLS (Cumulative Layout Shift).

### Fonts
- Next.js: `next/font/google` or `next/font/local` — self-hosted, zero layout shift.
- Raw HTML: `<link rel="preload">` + `font-display: swap` in `@font-face`.
- Variable fonts reduce weight requests and enable fluid typography.

## Performance — non-negotiables

### Core Web Vitals targets
- **LCP** (Largest Contentful Paint): ≤ 2.5s
- **INP** (Interaction to Next Paint): ≤ 200ms
- **CLS** (Cumulative Layout Shift): ≤ 0.1

### Critical checklist
- **Images sized**: `width`/`height` set, `aspect-ratio` CSS fallback.
- **Fonts preloaded**: self-hosted, `font-display: swap`, variable where possible.
- **JS deferred**: `<script defer>` or `<script type="module">`; never blocking.
- **CSS critical path**: inline critical CSS for above-the-fold; defer the rest.
- **Third-party scripts audited**: every `<script src="https://...">` costs TTI. Load async/defer, use Partytown for heavy analytics.
- **Bundle size**: Monitor. React app shouldn't ship 500KB of JS for a marketing page — use Astro or RSC.
- **Code split**: route-based + component-based for heavy widgets (charts, editors, 3D).
- **Prefetch**: `<Link prefetch>` on internal nav; `<link rel="prefetch">` for likely-next pages.
- **Cache headers**: static assets long `immutable`; HTML short or no-cache.

### Animations
- Transform & opacity only in hot paths. See `motion.md`.
- `will-change: transform` on actively animating elements; remove after.
- `contain: layout paint` on isolated components.
- `content-visibility: auto` on below-the-fold sections to skip rendering until scrolled near.

## Responsive — mobile-first

```css
/* Tailwind */
<div class="px-4 md:px-8 lg:px-16">...</div>

/* Raw CSS */
.container { padding-inline: 1rem; }
@media (min-width: 768px) { .container { padding-inline: 2rem; } }
```

- Start at 375px (iPhone SE) and scale up.
- `min-h-[100dvh]` not `h-screen` for full-height on iOS.
- Container queries (`@container`) for component-level responsiveness — especially for reusable components in layouts of varying width.
- Test at: 375, 768, 1024, 1440, 1920. Devtools > Responsive Mode.

## TypeScript

Always. On new projects, `"strict": true` from day one.

- Type props explicitly. Don't `FC<Props>` — just `function Card({ ... }: CardProps)`.
- `as const` for literal unions.
- Use Zod for runtime validation at boundaries (API responses, forms). Derive TS types with `z.infer`.
- Generic components: yes, but readable. A 4-param generic is a code smell.

## SEO (marketing surfaces)

- `<title>` and `<meta name="description">` per page — unique, specific.
- Open Graph tags for social sharing: `og:title`, `og:description`, `og:image` (1200×630).
- Canonical URLs (`<link rel="canonical">`).
- Semantic HTML structure (see `accessibility.md`) — search engines read it like users.
- `sitemap.xml` and `robots.txt`.
- Structured data (JSON-LD) for products, articles, events — improves rich results.
- Performance matters for SEO (Core Web Vitals are ranking signals).

## Dev workflow

- **Format**: Prettier (or Biome, now mature). No debate; automate it on save.
- **Lint**: ESLint or Biome with React + a11y rules (eslint-plugin-jsx-a11y).
- **Type check**: `tsc --noEmit` in CI.
- **Pre-commit**: Husky + lint-staged to catch issues before push.
- **CI**: lint, typecheck, test, build. Deploy previews on PR.

## File structure — keep it shallow

```
src/
  app/                  # Next.js App Router or similar
    (marketing)/        # route group
      page.tsx
      pricing/page.tsx
  components/
    ui/                 # Button, Card, Dialog, Input — primitives
    features/           # PricingTable, FeatureGrid — domain
    layout/             # Header, Footer, PageLayout
  lib/
    utils.ts            # cn(), formatters, helpers
    api.ts              # API client
  hooks/
  styles/
    globals.css
    tokens.css
```

Don't create 5 levels of nesting for "organization". Flat is usually better. Co-locate files (`Button.tsx`, `Button.test.tsx`, `Button.module.css`).

## Common code mistakes

- **`useEffect` for derived state.** Compute in render.
- **Creating a new object/array as prop every render.** Memoize or lift.
- **`<div>` soup.** Use semantic HTML (`<section>`, `<article>`, `<nav>`, `<button>`).
- **Hardcoded values instead of tokens.** `color: #111` → `color: var(--color-text)`.
- **Props drilling 5 levels.** Use composition or Context.
- **Early `useCallback` / `useMemo`.** Profile first; most don't help.
- **Custom hook for one-time logic.** Inline it; extract only when reused 2+ times.
- **Async IIFE in useEffect.** Use the cleanup function correctly; cancel in-flight on unmount.
- **Fighting the framework.** Server Components exist; use them.

## When to break the rules

- Landing page, one-off, no team ownership: ship a single HTML file with inline CSS if it's cleaner.
- Prototype: skip the TS/tests/lints, move fast. Convert later if it graduates.
- Constraint-driven (5KB budget, works in IE11): use the constraint as a creative input.

Match the tool to the task. The goal is shipping a great design, not architecture purity.
