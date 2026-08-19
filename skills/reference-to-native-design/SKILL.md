---
name: reference-to-native-design
description: Reconstruct screenshots, generated PNGs, or Figma references as editable design systems, component/state specifications, motion behavior, and production React Native interfaces. Use for image-to-Figma, Figma-to-code, visual matching, RTL adaptation, or motion handoff; not for unrelated image generation.
---

# Reference to native design

Convert visual intent into an editable, state-complete product interface. A screenshot is evidence of one rendered state, not a complete design system.

## Establish source roles

For every supplied image, frame, or link, record what it controls:

- Visual identity and brand.
- Layout and composition.
- Content and language.
- Component behavior.
- Motion reference.
- Asset reference.

Do not blend contradictory sources silently. If exactness is requested, preserve the designated source and disclose anything that must be inferred.

## Decompose the rendered state

Inspect at appropriate resolution and derive:

- Canvas and safe-area geometry.
- Grid, spacing rhythm, alignment, and responsive constraints.
- Typography roles, line height, truncation, and localization behavior.
- Color, gradient, blur, opacity, elevation, border, and material tokens.
- Components, variants, states, slots, and repeated patterns.
- Icons, illustrations, photos, masks, and asset-cropping rules.
- Navigation, gestures, keyboard behavior, scroll behavior, and transitions.
- Loading, empty, partial, error, offline, permission, and success states.

Never implement the screenshot as a single background image when the request is for a real interface.

## Build an editable design specification

- Use semantic tokens instead of per-screen magic values.
- Define reusable components before duplicating frames.
- Express layout with constraints/auto layout rather than absolute coordinates except where composition genuinely requires them.
- Create LTR and RTL behavior; do not merely right-align Arabic text.
- Define component properties and interactive states so the design can survive content changes.
- Identify missing fonts or assets; do not counterfeit them without disclosure.

When working in Figma, make actual editable layers and components when the connected tool supports them. A newly generated raster image is not an implemented Figma design.

## Specify motion before coding it

For each transition, define trigger, start state, end state, duration or physical model, interruption behavior, reduced-motion fallback, and ownership. Route simple state changes, hero choreography, and exportable vector animation to appropriate implementations rather than forcing everything into Lottie.

Read [references/design-handoff-schema.md](references/design-handoff-schema.md) for the expected handoff.

## Implement and verify

- Map components and tokens to the existing app architecture.
- Prefer platform-native behavior where it materially improves accessibility or interaction.
- Use real text and realistic edge-case content during verification.
- Compare implementation and reference at matching viewport and scale.
- Fix structural differences before decorative differences.
- Verify iOS, Android, RTL, dynamic text, keyboard, reduced motion, and at least one small and one large device class when in scope.

Do not claim pixel parity without a rendered comparison. Report known approximations and asset gaps.
