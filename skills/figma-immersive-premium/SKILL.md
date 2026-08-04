---
name: figma-immersive-premium
description: >
  Daily-driver playbook for building immersive, premium ("$20K–$50K agency" bar) work
  natively in Figma using the full 2026 MCP feature set — the shader engine (generative
  fills + post-effect shaders), motion/animation, variables-as-tokens, design-system
  libraries, Slides, FigJam, and cinematic gradients. Load this FIRST whenever the goal
  is to PRODUCE high-end visual work in Figma (hero sections, landing pages, product UI,
  brand systems, decks) — not just inspect or hand off. It is the router: it maps every
  Figma MCP tool to its job, enforces premium-design-laws (type, color, gradient, symbol
  hygiene), and dispatches to the right Figma skill at each step. Triggers: "make
  something premium/immersive in Figma", "best Figma work", "cinematic Figma hero",
  "Figma shader / gradient", "premium brand system in Figma", "design system in Figma".
disable-model-invocation: false
---

# Figma Immersive Premium

The standard is **cinematic, not flat cards.** Karim has explicitly rejected tidy
card-on-dark-panel layouts as "so bad." Everything below assumes the bar is an
award-tier agency build: earned depth, motion, real assets, disciplined type and color.

This skill is the **conductor**. It does not replace the mechanic skills — it tells you
which one to load when, and holds the premium rules they don't.

## Load order (every premium Figma job)

1. **`premium-design-laws`** — the standing law (type / color / gradient / symbol hygiene). Load first, always.
2. **This skill** — the immersive routing + Figma-native premium primitives.
3. **`figma-use`** — MANDATORY before any `use_figma` write. Never call `use_figma` without it.
4. The **job skill** for the step (see routing table).

Deck-first rule still applies: present 3–4 color/font directions and let Karim pick **before** building. Lock the chosen direction as Figma **variables** (see Tokens), then build.

## The complete Figma MCP toolbelt (2026)

Every tool, grouped by job. These are the real tool names — do not invent others.

### Read / inspect
- `get_design_context` — structure of a node: layout, sizing, assets, styling, Code Connect hints, screenshot context, motion placement markers. The structure of record.
- `get_screenshot` — pixel render of a node. Use to verify what you built actually looks right.
- `get_metadata` — lightweight node tree / ids without full context. Cheap orientation.
- `get_variable_defs` — the file's variables (tokens): colors, numbers, strings, modes.
- `get_motion_context` — authoritative animation data: keyframes, easing, timing, code snippets, timeline cohorts.
- `get_libraries` / `search_design_system` — discover team library components, variables, styles before you build anything new.
- `get_figjam` — read a FigJam board.
- `get_code_connect_map` / `get_code_connect_suggestions` / `get_context_for_code_connect` — design↔code mapping.
- `whoami` — confirm the authenticated account / plan when permissions act up.

### Write / create
- `use_figma` — the canvas write engine (runs Plugin API JS). Create/edit nodes, bind variables, build components, auto-layout, fills. **Requires `figma-use` loaded first.**
- `create_new_file` — new blank Design / FigJam / Slides file. Requires `figma-create-new-file`.
- `generate_diagram` — Mermaid → FigJam diagram. Requires `figma-generate-diagram`.
- `export_video` — export an animated node/flow to video. Pairs with motion.
- `upload_assets` / `download_assets` — move raster/vector assets in and out.
- `add_code_connect_map` / `send_code_connect_mappings` — write Code Connect.

### Shaders — the immersive engine (the headline 2026 feature)
- `list_shader_fills` → `get_shader_fill` — **generative** shaders. They synthesize pixels with **no input raster**: aurora fields, mesh gradients, noise, plasma, caustics, gradient flows. This is your premium-background / hero / texture source.
- `list_shader_effects` → `get_shader_effect` — **post-effect** shaders. They **sample an existing raster** and transform it: chromatic aberration, grain, displacement, glow, distortion, halftone. This is your cinematic finishing layer.

The pattern for both: `list_*` returns `{id, name, description, nextCursor}`; call `get_*` with the `id` to read the shader source, then apply/adapt it via `use_figma`.

## The shader playbook (what makes it look expensive)

Shaders are the single biggest lever for "immersive premium" in native Figma. Use them deliberately, not decoratively.

**Fills (generative) — earn the gradient.** premium-design-laws bans cheap rainbow 3-stop gradients on headings. A shader **fill** is how you get a *rich* gradient/field that reads expensive instead of cheap:
- Hero backgrounds: a slow aurora / mesh-gradient fill in same-family accent stops (not rainbow).
- Section atmospheres: subtle plasma or noise at 4–8% opacity over the surface token, to kill flatness.
- Brand texture: a signature generative field reused across hero + key sections for cohesion.

Workflow: `list_shader_fills` → pick by `name`/`description` → `get_shader_fill` to read source → apply via `use_figma`, then **retune the color uniforms to your locked accent variables** so the shader speaks your palette, not its defaults.

**Effects (post) — the finishing pass.** Apply *after* the composition reads well, never to rescue a weak layout:
- Grain / noise over the whole frame → instantly less "AI-flat", more editorial.
- Chromatic aberration on a hero word or image edge → motion-poster energy.
- Displacement / glow on a focal element → depth and light.

Discipline: one signature fill + at most one or two effects per surface. Stacking shaders muddies fast (premium-design-laws: no muddy color, no accent bloat). If you can't name *why* a shader is there, remove it.

## Variables as the token system (do this before you build)

Figma **variables** are your design tokens. Lock the deck choice here so everything inherits it:
- Color: `bg / surface / border / text / accent / cta / state` semantic variables, in **light + dark modes**.
- Type scale + spacing as number variables. Radius, elevation as variables.
- Bind shader uniforms and component props to these variables — change the brand in one place.

Mechanic: `figma-generate-library` teaches WHAT to build and in what order (foundations → tokens → components); `figma-use` teaches HOW to call the API. Load **both together** for token/component work. Read `figma-use/references/variable-patterns.md` for the binding patterns.

## Motion — cinematic, not decorative

Animation is where premium separates from template. Three directions — `figma-motion-pipeline` is the router that picks between them:
- **Author motion inside Figma**: load `figma-use-motion` alongside `figma-use` — keyframes, easing, animation styles, timeline duration on nodes. Then `export_video` for a deliverable. (This is the path for "I want to make animation/motion in Figma".)
- **Implement Figma motion as web/SwiftUI code**: load `figma-implement-motion` — `get_motion_context` is the source of truth (keyframes, easing, motion.dev/CSS snippets, timeline cohorts). Honor `prefers-reduced-motion`.
- **Implement Figma motion as an Expo / React Native app**: load `react-native-motion` — Figma Motion and `figma-implement-motion` only emit web + SwiftUI, never React Native, so this skill owns the bridge to Reanimated/Moti. Use `useReducedMotion()`.

Premium motion rules: ease everything (no linear), stagger reveals via timeline cohorts, motivate every move (entrance, focus, feedback — never motion for motion's sake). For web hand-off, pair with the local `gsap` + `lenis-smooth-scroll` + `premium-motion-cookbook` skills.

## Routing table — load the right skill for the step

| You want to… | Load (with `figma-use` where it writes) | Tools |
|---|---|---|
| New blank Design/FigJam/Slides file | `figma-create-new-file` | `create_new_file` |
| Build a full page/screen/section in Figma | `figma-generate-design` | `use_figma`, `search_design_system` |
| Build/extend a design system + tokens + components | `figma-generate-library` + `figma-use` | `use_figma`, `get_variable_defs` |
| Generative gradient/field/texture (shaders) | `figma-shader-recipes` + `figma-use` | `list/get_shader_fill` |
| Cinematic post-effect (grain, aberration, glow) | `figma-shader-recipes` + `figma-use` | `list/get_shader_effect` |
| Premium / earned gradient (linear/radial/mesh) | `figma-gradient-systems` + `figma-use` | gradient paints, `list/get_shader_fill` |
| Color palette + tokens + dark mode | `figma-color-systems` + `figma-use` | `get_variable_defs`, `use_figma` |
| Type scale + text styles + pairing | `figma-typography-systems` + `figma-use` | `use_figma` |
| Production components + variants + props | `figma-component-craft` + `figma-generate-library` + `figma-use` | `use_figma` |
| Depth / shadows / glassmorphism / light | `figma-depth-and-light` + `figma-use` | `use_figma` (effects) |
| Animate nodes in Figma | `figma-use-motion` + `figma-use` | `use_figma`, `export_video` |
| Turn Figma motion into code (which target?) | `figma-motion-pipeline` (router) | `get_motion_context`, `get_design_context` |
| …into web / SwiftUI code | `figma-implement-motion` | `get_motion_context`, `get_design_context` |
| …into an Expo / React Native app | `react-native-motion` | `get_motion_context`, `get_design_context` |
| Build a deck in Figma Slides | `figma-use-slides` + `figma-use` | `use_figma` |
| Whiteboard / FigJam work | `figma-use-figjam` + `figma-use` | `use_figma`, `get_figjam` |
| Architecture / flow / ERD / sequence diagram | `figma-generate-diagram` | `generate_diagram` |
| Implement a Figma design as web code | `figma-implement-design` (custom) / `figma-generate-design` | `get_design_context`, `get_screenshot` |
| Implement a Figma design as SwiftUI | `figma-swiftui` | `get_design_context` |
| Map Figma components to code | `figma-code-connect` / `figma-code-connect-components` | `add_code_connect_map` |
| Project-specific design-system rules file | `figma-create-design-system-rules` | `create_design_system_rules` |

## The Figma-native technique pack (deep dives)

Six craft skills sit under this router — load the relevant one when you reach that step:

- `figma-shader-recipes` — the shader engine cookbook (generative fills + post effects). The immersive headliner.
- `figma-gradient-systems` — earned linear/radial/mesh gradients, grain-over-gradient, gradient tokens.
- `figma-color-systems` — primitive ramps → semantic aliases → light/dark modes, WCAG.
- `figma-typography-systems` — modular scale, role-separated text styles, pairing, Arabic/RTL.
- `figma-component-craft` — variants without explosion, component properties, variable-bound, states.
- `figma-depth-and-light` — layered elevation, glassmorphism, lit edges, dark-mode depth (the flat-card cure).

## Pair with the local design stack

These non-Figma skills raise the ceiling — reach for them in the same job:
- **Lock the system**: `ui-ux-pro-max` (palettes, font pairings, UX rules with citations).
- **Color / type depth**: `color-expert`, `color-system`, `typography-scale`, `design-token`.
- **Build the code**: `frontend-design`; web motion via `gsap`, `lenis-smooth-scroll`, `premium-motion-cookbook`, `webgl-effect-recipes`.
- **Polish / audit**: `impeccable`, `design-review`, `critique-typography`, `critique-visual-hierarchy`.
- **Real assets**: cut out subjects (rembg), use real imagery — never flat placeholder cards (Karim's bar).

## Force Figma's own agents to obey these laws

Figma's Config-2026 canvas agent takes **Skills** (packaged conventions it follows), and Dev Mode has `create_design_system_rules`. To make Figma's *own* agents follow Karim's bar — not just Claude — install [references/figma-agent-rules.md](references/figma-agent-rules.md) as a Figma agent Skill (one-time paste), and merge it into the `create_design_system_rules` output. That file mirrors `premium-design-laws`, so both sides share one source of truth. Re-paste when the laws change.

## Premium laws, applied to Figma (non-negotiable)

- **Symbol hygiene** in any text you put on the canvas: no `//`-style section labels, no `-----`/`=====` ASCII rules, no box-drawing or decorative slash/pipe/dot separators. Use whitespace rhythm, a 1px hairline border variable, or an uppercase eyebrow micro-label (tracking ~0.18em).
- **Type**: honor the default-fonts ban (no lazy Cormorant / Outfit / JetBrains Mono / Noto Kufi). Real modular scale, explicit line-height + letter-spacing, display tracking negative, strict display/body/meta separation. For Arabic-first work use Arabic-safe pairings and `rtl-arabic-i18n`.
- **Color / gradient**: one disciplined accent system; gradients earned (same-family stops or a real reference), never rainbow on headings; WCAG-aware CTA contrast.
- **Verify**: after building, `get_screenshot` the node and check it against the intent before declaring done.

## Anti-patterns (these read "cheap" — kill on sight)

- Flat card grid on a dark panel with no depth, no motion, no real imagery.
- Rainbow / 3-stop gradients on headings; shaders stacked until muddy.
- Default font fallbacks; uniform weight; no type scale.
- Decorative motion with no purpose; linear easing; motion that ignores reduced-motion.
- Hardcoded hex/spacing instead of variables — the brand can't move in one place.
- Shaders or effects added "to fill space" rather than for a named reason.
