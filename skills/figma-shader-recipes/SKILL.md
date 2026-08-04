---
name: figma-shader-recipes
description: >
  Cookbook for Figma's 2026 shader engine — generative shader FILLS (aurora, mesh
  gradient, plasma/fluid, value-noise, caustics, gradient-flow) and post-effect shader
  EFFECTS (film grain, chromatic aberration, glow/bloom, displacement, halftone,
  scanlines, vignette). Use this WHENEVER the goal is rich, expensive-looking texture,
  atmosphere, or cinematic finishing in a Figma file — hero backgrounds, section
  atmospheres, brand texture, focal glow. Triggers: "Figma shader", "shader fill/effect",
  "generative background in Figma", "make this Figma hero look premium/cinematic",
  "add grain/aberration/glow/noise in Figma", "mesh gradient in Figma". Load alongside
  `figma-use` (shaders are applied via `use_figma`) and after `premium-design-laws`.
disable-model-invocation: false
---

# Figma Shader Recipes

Shaders are the single biggest lever for "this looks like a $50K build" in native Figma. They are also the fastest way to make something look cheap if stacked carelessly. Use them deliberately — every shader earns its place or comes off.

## The two kinds (don't confuse them)

- **Shader FILLS** — *generative*. They synthesize pixels from nothing (no input image). This is your background / atmosphere / texture source. Tools: `list_shader_fills` → `get_shader_fill`.
- **Shader EFFECTS** — *post-process*. They sample the raster underneath and transform it. This is your finishing pass on an already-good composition. Tools: `list_shader_effects` → `get_shader_effect`.

## The workflow (always the same)

1. `list_shader_fills` (or `list_shader_effects`) — returns `{id, name, description, nextCursor}`. Read the names/descriptions to find the closest match to the recipe you want.
2. `get_shader_fill` / `get_shader_effect` with the `id` — returns the shader **source**. This is your template; do not invent shader source from scratch when a close one exists in the library.
3. Apply / adapt via `use_figma` (load `figma-use` first), then **retune the color uniforms to the project's locked accent variables** so the shader speaks the brand palette, not its built-in defaults.
4. `get_screenshot` the node and check it reads as intended before moving on.

If the library has nothing close, read the nearest source to learn the uniform conventions, then adapt — don't fabricate a shader blind.

## Generative FILL recipes (backgrounds & texture)

Pick by intent. Keep colors in the same family as the accent system; opacity low where it sits behind content.

- **Aurora field** — slow, soft bands of light. The default premium hero background. Tune to 2 same-family accent stops + a near-black base; keep motion slow if animated.
- **Mesh gradient** — multi-point soft gradient blobs. Richer than a linear gradient, reads expensive. Use 3–4 control colors from one family; avoid complementary clashes (that's the rainbow trap).
- **Plasma / fluid** — organic flowing color. Strong brand signature; use ONE per project and reuse across hero + key sections for cohesion.
- **Value noise / fbm** — subtle organic grain field. At 4–8% opacity over a surface token it kills flatness instantly (the "not-AI-flat" trick).
- **Caustics / light** — rippling light pools. Luxury / product / editorial energy. Keep subtle; it dominates fast.
- **Gradient flow / conic** — directional sweep. Good behind a wordmark or as a section divider glow.

Discipline: one signature fill per surface. If you can't name *why* it's there, delete it (premium-design-laws: gradients are earned, no accent bloat).

## Post-EFFECT recipes (the finishing pass)

Apply only after layout + type + color already read well. Effects rescue nothing; they elevate.

- **Film grain** — uniform fine noise over the whole frame. The highest ROI effect. Editorial, cinematic, anti-flat. Keep it fine and low.
- **Chromatic aberration** — RGB channel split at edges. On a hero word, image edge, or focal element → motion-poster energy. Tiny amounts only; large = broken-screen.
- **Glow / bloom** — light bleed from bright areas. Depth and atmosphere around a focal element or light source. Pair with a dark foundation.
- **Displacement / ripple** — warp via a noise map. Liquid, glassy, dreamlike. Strong; one focal use per screen.
- **Halftone / dither** — dot/line screen. Print-editorial, retro-premium. Works on monochrome imagery.
- **Scanlines / vignette** — frame and focus. Use vignette to pull the eye to center; scanlines for a CRT/tech mood. Subtle.

Stacking rule: at most one or two effects per surface. Grain + one accent effect is usually the whole budget. More than that muddies (premium-design-laws: no muddy color).

## Tuning to the brand

The win is in the uniforms, not the shader choice:
- Replace the shader's default colors with the project's accent **variables** so a brand change propagates everywhere.
- Match the foundation: dark project → dark base color in the fill; light project → light base.
- Opacity: behind content 4–12%; as a standalone hero 40–100% depending on contrast headroom for the text on top.
- Verify text contrast on top of any fill stays WCAG-aware (premium-design-laws).

## Anti-patterns (read "cheap" — kill on sight)

- Rainbow / complementary mesh gradients (the #1 cheap tell).
- Three or more effects stacked until the image is mud.
- A shader added "to fill space" with no reason.
- Heavy chromatic aberration / displacement that looks like a rendering bug.
- Shader colors left at library defaults, ignoring the brand palette.
- Using a shader to rescue a weak layout instead of fixing the layout.

## Pairs with

`figma-immersive-premium` (router) · `figma-gradient-systems` (when the fill is gradient-specific) · `figma-depth-and-light` (glow/shadow interplay) · `webgl-effect-recipes` + `premium-motion-cookbook` (when porting the look to web).
