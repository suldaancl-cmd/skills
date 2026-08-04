---
name: figma-component-craft
description: >
  Build production-grade Figma COMPONENTS and libraries — variant sets that don't
  explode, component properties (boolean / instance-swap / text), variable-bound values,
  base-component pattern, slots, states (default/hover/focus/disabled), and clean naming.
  Use whenever creating or refactoring Figma components, a component library, or a design
  system's interactive parts. Triggers: "build a component in Figma", "component library",
  "variants", "component properties", "make this a reusable component", "design system
  components", "fix this messy component set". Load TOGETHER with `figma-use` (the API)
  and `figma-generate-library` (what to build and in what order); this skill is the
  craft layer on top. After `premium-design-laws`.
disable-model-invocation: false
---

# Figma Component Craft

`figma-generate-library` tells you WHAT to build and in what order (foundations → tokens → components). `figma-use` tells you HOW to call the API. This skill is the **craft**: how to make components that are production-quality instead of brittle.

The rule under everything: a component binds to **variables/styles**, never to hardcoded values. If the brand changes and your component doesn't, it isn't done.

## Structure before variants

1. **Foundations first.** Components are worthless without the color, type, spacing, and radius variables behind them. If those don't exist, build them first (`figma-color-systems`, `figma-typography-systems`).
2. **Auto-layout everything.** Padding, gap, and resizing (hug/fill) as variables. A component without auto-layout can't flex and will break on every reuse.
3. **Base-component pattern.** For families that share structure (buttons, inputs, chips), build one base component, then build the variants as instances of the base with overrides. Fixing the base fixes the family.

## Variants without the explosion

Variant sets explode combinatorially (size × state × type × icon = dozens). Keep them sane:
- Use **variant properties** only for things that change the *visual structure* (size, emphasis).
- Use **component properties** for everything else:
  - **Boolean** — show/hide an element (leading icon, trailing icon, badge).
  - **Instance swap** — swap a nested instance (which icon, which avatar) → this is your **slot** mechanism.
  - **Text** — editable text without detaching.
- Result: a button might be `Size {S,M,L} × Emphasis {Primary,Secondary,Ghost}` as variants, with `hasIcon`, `iconType`, `label` as properties — not a 40-cell matrix.

## States

Every interactive component needs: `default`, `hover`, `focus`, `disabled` (and `active`/`loading` where relevant). Build them as variants. Keep state changes token-driven (hover = `accent-hover` variable, not a new hardcoded color). Focus states matter for accessibility — don't skip them.

## Naming (so it's findable + code-mappable)

- Components: `Category/Name` → `Button/Primary`, `Input/Text`, `Card/Product`.
- Properties: human-readable (`Show icon`, `Size`) — these become the API in code.
- Consistent casing and order; this naming flows into Code Connect (`figma-code-connect`) so design changes reach the codebase.

## Quality bar (premium)

- No detached instances in real designs — if you're detaching, the component is missing a property.
- No hardcoded color/size/spacing on any layer — all bound to variables/styles.
- Resizes correctly (hug/fill set deliberately, tested at min and max width).
- Documented: a short usage note + do/don't on the component page (`figma-generate-library` covers documentation).
- Verify with `get_screenshot` across variants/states before publishing.

## Mechanics (via use_figma)

- Create main components / component sets; add `componentPropertyDefinitions` (VARIANT, BOOLEAN, INSTANCE_SWAP, TEXT).
- Bind layer fills/strokes/sizes/text to variables and styles.
- Use auto-layout (`layoutMode`, `itemSpacing`, `padding*`, `primaryAxisSizingMode`, `counterAxisSizingMode`).
- Read `figma-generate-library/references/component-creation.md` and `naming-conventions.md`; `figma-use/references/plugin-api-patterns.md` for the API shapes.

## Anti-patterns

- Variant explosion (everything a variant) instead of component properties.
- Hardcoded values; detached instances as a workaround for missing properties.
- No states / no focus state; states with ad-hoc colors.
- Inconsistent naming; no documentation.
- Components built before the token foundations exist.

## Pairs with

`figma-generate-library` (the order/what) · `figma-use` (the API) · `figma-color-systems` + `figma-typography-systems` (the tokens it binds to) · `figma-code-connect` (map to code) · local `design-system`, `component-spec`, `ui-design-system`.
