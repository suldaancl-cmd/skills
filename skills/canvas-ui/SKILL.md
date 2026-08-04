---
name: canvas-ui
description: 33 open-source html-in-canvas + WebGL page effects (liquid, shatter, glass, VHS, blaze, hex-float, ascii, dither, particle reveal…) installable via the shadcn registry @canvas-ui, in React/Vue/Svelte/Solid/Preact/vanilla. Use when a site or landing page needs a cinematic full-page effect, a shader hero, an interactive cursor lens, or a scroll reveal.
license: MIT
metadata:
  source: https://github.com/DavidHDev/canvas-ui
  docs: https://canvasui.dev
  author: David Haz (DavidHDev)
  installed: 2026-08-02
---

# Canvas UI

Open-source library of html-in-canvas and WebGL effects that render **the live page itself** through a shader. Framework agnostic. The HTML stays interactive underneath — these are not background videos or decorative overlays.

Endorsed by shadcn. Used in production on `getrubric.app`.

## Install a component

Registry is namespaced `@canvas-ui`. Works with or without the shadcn MCP.

```bash
npx shadcn@latest add @canvas-ui/liquid-react
```

Framework suffixes: `-react`, `-vue`, `-svelte`, `-solid`, `-preact`, `-vanilla`.

First use in a project — add the registry to `components.json`:

```json
{
  "registries": {
    "@canvas-ui": "https://canvasui.dev/r/{name}.json"
  }
}
```

Optional MCP so the agent can browse and read docs directly:

```bash
npx shadcn@latest mcp init --client claude
```

## Catalog

`three` in the deps column means the component pulls `three` + `@types/three`. Everything else is dependency-free.

| Component | Deps | What it does |
|---|---|---|
| `ascii-object` | three | Renders any GLB/glTF model, SVG, or image in a floating studio scene as ASCII characters chosen by shape, so glyphs trace the object's edges. |
| `asciify` | — | Redraws the page as live ascii characters in a soft radius around the cursor, with glyph, shade-block, and binary ramps. Chromium + Firefox. |
| `bend` | — | Folds the top and bottom of the page over virtual edges as you scroll, like scrolling on the face of a cube. |
| `blaze` | — | Fire sparks, smoke, and heat distortion rising from the bottom of the page. |
| `bubble` | — | A glassy droplet trailing the cursor as blending metaballs, refracting the live page with dispersion, frost, and iridescent sheen. |
| `canvas` | — | Paints the page onto woven artist canvas: fiber texture, paper tint, grain, dotted halftone screen, soft intro crossfade. Text stays crisp. |
| `cloth` | — | Hangs the live HTML on fabric rippling in the wind with softly lit folds. Cursor strokes send waves across the cloth. |
| `clouds` | — | Procedural fog drifting over the page, blurring what it covers. Cursor movement parts the clouds. |
| `decrypt-reveal` | — | Renders the page as real ASCII cipher text that decodes back into crisp UI around the cursor behind a flickering wavefront. |
| `displacement` | — | Warps the live HTML on a displacement grid rippling away from the cursor, with chromatic fringing and film grain. |
| `dithered-object` | three | Renders any GLB/glTF model, SVG, or image through a 1-bit Bayer, halftone, or Floyd–Steinberg dither. |
| `droplets` | — | Rain droplets running down the screen, refracting the page behind them. |
| `flame-wrap` | — | Wraps any element in an aligned border of fire: flames from the top edge, molten outline, sparks, heat shimmer. |
| `force-field` | — | Energy shield lattice over the live HTML. Cursor charges cells; clicks detonate shockwave ripples with bloom, grain, burning reveal. |
| `frost` | — | A frozen pane of ice with refraction and frost grain. Hovering melts a hole that freezes back over. |
| `glass` | — | Cursor-following glass lens refracting the page like real glass, with crystal-ball zoom over target elements. |
| `glass-object` | three | Turns any GLB/glTF model, SVG, or image into a floating liquid-glass object: real refraction, chromatic dispersion, frost, tinted absorption, studio lighting. |
| `glitch` | — | Broadcast glitch bursts tearing the page into shifted slices with RGB splits, corrupted blocks, analog noise, then settling clean. |
| `glyph-rain` | — | Glowing glyph streams over the live HTML; every drop head casts a real pool of light onto the page with embossed relief shading. |
| `grid` | — | Splits the page into a grid of 3D tiles rippling in waves around the cursor. |
| `hex-float` | — | Renders the page onto a floor of shiny beveled hex tiles leaning back in perspective, bobbing, rising toward the cursor. |
| `laser` | — | Hides everything below a glowing laser beam near the bottom of the viewport. Scrolling prints new content in from behind it. |
| `liquid` | — | Pointer-driven WebGL fluid simulation over the page. |
| `liquid-object` | three | Drags a GLB/glTF model, SVG, or image through an invisible GPU fluid that swirls under the cursor and splits light into chromatic fringes. |
| `magnify` | — | Sci-fi scanner lens following the cursor, magnifying the page inside a configurable HUD reticle with chromatic haze and click ripples. |
| `particle-object` | three | Rebuilds a GLB/glTF model, SVG, or image as a particle cloud the cursor pushes, swirls, and springs back into shape. |
| `particle-reveal` | — | Renders the page as fine grayscale dust merging back into crisp UI around the cursor. |
| `particle-scroll` | — | Dissolves everything below a chosen line into drifting sand that reassembles as you scroll. |
| `peel` | — | Peels the page back from a chosen edge as the cursor approaches, revealing a second layer underneath. |
| `retro-dither` | — | Retro dither lens pixelating and quantizing the page around the cursor. |
| `ripple` | — | Water ripples spreading from every click, refracting the page like a pond surface with dispersion and crest glints. |
| `shatter` | — | Shatters the page into 3D glass shards that lift, tilt, and float around the cursor, refracting content beneath, with perspective and soft shadows. |
| `vhs` | — | Plays the page back like a worn VHS tape: tape wave, head-switch noise, chroma bleed, grain. |

## Picking one

- **AI / tech / agency hero** → `hex-float`, `force-field`, `glyph-rain`, `decrypt-reveal`
- **Luxury / product** → `glass`, `glass-object`, `liquid`, `shatter`
- **Editorial / print feel** → `canvas`, `retro-dither`, `asciify`
- **Scroll storytelling** → `particle-scroll`, `bend`, `laser`, `peel`
- **3D product prop** → `*-object` variants (need a GLB/SVG/image; pair with [[img2threejs]] to generate the model from a photo)

## Rules

- Every effect renders the real DOM — check text contrast **through** the shader, not before it. Run the contrast pass from [[premium-design-laws]] on the composited result.
- One page-wide effect per page. Two shaders fighting for the same viewport reads as a demo, not a product.
- Each component exposes tunables (grain, iridescence, float on/off, speed). Tune on `canvasui.dev` first, then copy the generated code — do not hand-guess uniform values.
- `three`-dependent components ship a WebGL context; budget for it on mobile and gate behind `prefers-reduced-motion`.

## Related

[[frontend-design]] · [[premium-design-laws]] · [[ui-ux-pro-max]] · [[antalik-ui]] · [[webgl-effect-recipes]] · [[shader-dev]]
