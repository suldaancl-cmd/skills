---
name: antalik-ui
description: Three zero-dependency React micro-libraries by Jakub Antalik — thinking-orbs (six animated agent loading states), border-beam (traveling/breathing border glow), metal-fx (WebGL liquid-metal ring on buttons). Use for AI/agent loading states, thinking indicators, highlighted CTA buttons, premium chip and pill treatments.
license: MIT
metadata:
  source: https://github.com/Jakubantalik
  demos: https://orbs.jakubantalik.com · https://metal.jakubantalik.com
  author: Jakub Antalik
  installed: 2026-08-02
---

# Antalik UI

Three small React packages. All MIT, all zero-dependency, all theme-aware and SSR-safe. Install per project with npm — there is no registry or CLI.

Reach for these when a build needs **one** premium detail (a loading state, a highlighted CTA) rather than a page-wide effect. For page-wide shaders use [[canvas-ui]].

---

## 1. thinking-orbs — agent loading states

```bash
npm install thinking-orbs
```

```tsx
import { ThinkingOrb } from 'thinking-orbs';

<ThinkingOrb state="searching" size={64} />
```

Six states, each a distinct animation — pick the verb that matches what the agent is actually doing:

| State | Animation |
|---|---|
| `working` | particles on tilted orbits |
| `searching` | scan meridian sweeps a dotted globe |
| `solving` | bands scramble, then click back solved |
| `listening` | waveform rolls through the rings |
| `composing` | undulating multi-band sash |
| `shaping` | dotted outline: circle → triangle → square |

Two sizes, **separate designs not a scale factor** — `64` for chat-avatar scale, `20` for inline text. Each carries its own dot count, dot size, and speed tuning.

Other props: `theme` (`auto` default / `dark` / `light`), `speed` (multiplier on the baked speed), `paused`, `aria-label`. All `<canvas>` props pass through.

`theme="auto"` resolves in three layers, live: ancestor `data-theme` / `dark` class (Tailwind + shadcn convention, watched via `MutationObserver`) → `prefers-color-scheme` → client-only paint after resolve.

Built-in: `role="img"` with per-state `aria-label`; `prefers-reduced-motion` renders a static frame; instances pause offscreen (`IntersectionObserver`) and on hidden tabs, resuming in phase off one shared clock. Plain 2D canvas arcs — no `ctx.filter`, no SVG filters, no WebGL. DPR capped at 2.

---

## 2. border-beam — animated border glow

```bash
npm install border-beam
```

```tsx
import { BorderBeam } from 'border-beam';

<BorderBeam size="md"><Card /></BorderBeam>
```

Wraps content, overlays the beam, auto-detects the first child's `border-radius`.

**Rotate family** (traveling beam): `md` full border glow (default) · `sm` compact, for small elements · `line` bottom-only, for search bars.

**Pulse family** (breathing, no rotation): `pulse-inner` contained · `pulse-outside` outward halo.

Colors: `colorful` (rainbow, default) · `mono` (grayscale) · `ocean` · `sunset`. All but `mono` cycle a hue shift.
Also: `theme` (`dark` default / `light` / `auto`), `strength` 0–1, `duration` (pulse breathe speed, default `2.3`).

Two gotchas on `pulse-outside`:
- The core and halo render **behind** the child at `z-index: -1`, so the child must be opaque or the inner glow shows through. Wrapper is `overflow: visible` — give the surrounding layout room.
- It rides on the child's **own 1px border** as the idle hairline and paints none of its own. If the child has no border, add one (or `box-shadow: inset 0 0 0 1px`) so the edge survives when the beam fades.

---

## 3. metal-fx — WebGL liquid-metal ring

```bash
npm install metal-fx
```

```tsx
import { MetalFx } from 'metal-fx';

<MetalFx variant="button"><button>Upgrade to Pro</button></MetalFx>
```

Wraps a single child, measures it, paints an animated metal ring on top. Child stays interactive — overlays are `pointer-events: none`.

Variants: `button` (pill silhouette, 1px ring, scale 1.6) · `circle` (2px ring, scale 1.3).
Presets: `chromatic` iridescent (default) · `silver` · `gold` — each with tuned dark and light blocks.
Also: `theme` (`auto` default, live via `matchMedia`; SSR falls back to `dark` then rehydrates), `strength` 0–1, `paused`.

**Proximity reflection** — pass refs to neighbours and they get a mirrored reflection of the ring. Dark mode only; skipped entirely in light mode with no DOM scanning.

```tsx
<MetalFx variant="circle" reflectionTargets={[chipRef]}>
  <button ref={sendRef} aria-label="Send">↑</button>
</MetalFx>
```

Performance: one shared WebGL context across every mount, shader compiled once, one `rAF` loop for all instances, `IntersectionObserver` pauses offscreen copies and skips the GL render when all are offscreen.

---

## Rules

- These are **accent** components. One `metal-fx` button per screen — a page of metal pills reads as a template, not a product.
- Match `thinking-orbs` state to the real agent action. A `searching` orb over a write operation is a lie the user notices.
- All three are theme-aware already. Do not wrap them in your own theme conditionals; drive `theme` from app state only when the app's toggle ignores the OS.
- Font and color choices around them still bind to [[premium-design-laws]] and the Colors & Fonts deck rule — these components do not pick type or palette for you.

## Related

[[canvas-ui]] · [[frontend-design]] · [[premium-design-laws]] · [[premium-app-craft]] · [[loading-states]] · [[micro-interaction-spec]]
