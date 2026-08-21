# Design-to-code handoff schema

## Source manifest

| Source | Role | Must preserve | May infer |
|---|---|---|---|

## Screen contract

- Screen name and route:
- Supported sizes/orientations:
- Safe-area behavior:
- Scroll and keyboard behavior:
- Entry and exit transitions:
- Loading/empty/error/offline states:
- LTR/RTL differences:

## Tokens

- Color and semantic roles.
- Typography and localization fallback.
- Spacing, radius, border, elevation, blur.
- Motion duration, easing/spring, and reduced-motion substitutions.

## Components

For each component specify purpose, anatomy, properties, variants, interaction states, accessibility role/label, content limits, and responsive behavior.

## Motion record

| Element | Trigger | From | To | Timing/physics | Interruptible | Reduced motion | Runtime |
|---|---|---|---|---|---|---|---|

Runtime examples: native transition, Reanimated, Skia, Lottie, Rive, video, or no animation. Select by behavior and maintainability, not novelty.

## Verification record

- Reference viewport:
- Implementation viewport:
- Structural mismatches:
- Typography mismatches:
- Asset approximations:
- Platform differences:
- Accessibility and reduced-motion result:
