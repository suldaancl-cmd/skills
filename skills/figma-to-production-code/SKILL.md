---
name: figma-to-production-code
description: Implement semantic Figma designs or approved visual references as production Expo/React Native or React/Next.js code with real components, design tokens, localization, RTL/LTR, accessibility, responsive behavior, assets, data states, and motion hooks. Use after or alongside editable Figma reconstruction. Do not generate a screenshot-shaped page made from absolute-positioned pixels or a full-screen raster.
compatibility: Requires a code workspace. Figma-backed tasks benefit from Figma MCP design context, variables, assets, motion context, and Code Connect.
metadata:
  version: 1.0.0
  owner: ASSALA AISTUDIO LTD
---

# Figma to Production Code

Translate design intent into maintainable runtime behavior. Match the approved visual direction while respecting the existing architecture, platform behavior, real data, localization, accessibility, and performance.

## When to use

- An editable Figma screen must become Expo/React Native or web code.
- A generated UI image is approved and the user authorizes direct code-first reconstruction.
- Existing implementation is structurally or visually inconsistent with Figma.
- Figma components need mapping to production components.

## Boundaries

- Do not implement a full-screen screenshot as the interface.
- Do not use absolute coordinates for ordinary responsive layout.
- Do not invent backend behavior, credentials, legal copy, or data contracts.
- Do not add libraries before inspecting the current stack and versions.
- Do not rewrite unrelated architecture or delete existing work without authorization.
- Do not claim completion until the application has been run and visually verified.

## Required reading

- Read `references/react-native-playbook.md` for Expo/React Native.
- Read `references/web-playbook.md` for React/Next.js.
- Read `references/design-code-contract.md` for tokens, assets, Code Connect, and cross-platform boundaries.

## Procedure

### 1. Inspect the repository

Before editing, identify:

- Package manager and workspace/monorepo boundaries.
- Framework and exact versions.
- Navigation/routing.
- Styling and token system.
- Component library.
- State/data layer.
- Localization and RTL handling.
- Asset pipeline.
- Animation libraries.
- Test, lint, typecheck, build, and run commands.
- Existing dirty changes that must be preserved.

Use the project's established conventions unless they block the visual or product contract.

### 2. Read bounded Figma context

For large files:

1. Read page metadata.
2. Read the exact golden-screen node.
3. Read variables, component instances, and assets.
4. Read motion context when present.
5. Read Code Connect mappings when available.

Do not request the entire heavy file as one context blob. Do not infer node IDs.

### 3. Create an implementation map

Fill `assets/implementation-map.csv`:

- Figma component/node.
- Runtime component/path.
- Props and variants.
- Token mapping.
- Asset mapping.
- State and data owner.
- Motion owner.
- Accessibility semantics.
- Locale and responsive behavior.

Resolve shared primitives before composing many screens.

### 4. Establish tokens

Map Figma values to project tokens:

- Primitive and semantic colors.
- Typography roles.
- Spacing, size, and radius.
- Elevation, blur, opacity.
- Motion duration/easing.
- Breakpoints or device size policy.

Avoid copying arbitrary one-off numbers when a semantic token exists. Preserve intentional exceptions with comments or documentation.

### 5. Route assets correctly

- Live UI and text: code.
- Simple icons/logos: verified SVG/vector or platform asset.
- Complex background art: optimized responsive raster.
- Interactive data graphics: runtime SVG/canvas/native layers.
- Decorative finite animation: Lottie if justified.
- Interactive vector: Rive if justified.
- 3D: runtime engine only if actual interaction is required.
- Marketing video: Remotion composition outside the app interaction layer.

Never let a background asset contain controls that must receive input or expose accessibility semantics.

### 6. Implement the golden screen

1. Build shared primitives and tokens.
2. Build the screen structure with semantic components.
3. Wire all visible states, including permission, loading, empty, error, offline, and success where applicable.
4. Add real localization and RTL/LTR behavior.
5. Add accessibility roles, labels, focus order, hit targets, and reduced motion.
6. Add motion using the owner chosen in the motion specification.
7. Integrate data through explicit interfaces; use clearly labeled fixtures only when real services are unavailable.
8. Run the target application and capture the exact screen.

### 7. Responsive behavior

Do not globally scale a fixed screenshot coordinate system. Define:

- Fixed and flexible regions.
- Min/max widths.
- Safe areas and system bars.
- Art cropping/anchor behavior.
- Text wrap and truncation policy.
- Keyboard behavior.
- Orientation policy.
- Web breakpoints or mobile size classes.

Test at least one smaller and one larger target than the reference.

### 8. Localization and RTL

- Keep all user-facing strings outside visual assets.
- Use the project's localization system.
- Apply RTL at layout and text levels, not by reversing the entire screen blindly.
- Mirror directional arrows and progress only when meaning requires it.
- Do not mirror logos, media controls, clocks, Kaaba imagery, or other nondirectional assets automatically.
- Verify Arabic shaping, line height, numerals, mixed text, and long strings.
- Treat Quranic text as verified content with appropriate typography and source controls.

### 9. State and interaction verification

Test:

- Default, pressed, focused, selected, disabled, loading, success, and error states.
- Navigation and back behavior.
- Permission denial and recovery.
- Offline and stale data.
- Rapid repeated input and interrupted animation.
- Screen reader semantics and keyboard/focus behavior where applicable.
- Reduced motion.

### 10. Validate and hand off

Run the safest relevant commands in the project:

- Formatting.
- Targeted tests.
- Typecheck.
- Lint.
- Build.
- Runtime launch and visual verification.

Report what was actually run. Use `visual-fidelity-qa` to compare the runtime screenshot with Figma and the original reference.

## Code Connect

Use Code Connect only when both sides are stable enough to map:

- Map component to component, not arbitrary screen fragments.
- Match the framework label exactly.
- Map props/variants intentionally.
- Keep mappings in sync when source paths or APIs change.
- Treat mappings as context for the agent, not automatic proof that code matches design.

## Completion contract

Deliver:

1. Implementation map.
2. Token and asset mapping.
3. Production components and screen.
4. State/data boundaries and fixtures, if used.
5. Motion integration and reduced-motion behavior.
6. Localization and accessibility evidence.
7. Commands and runtime checks performed.
8. Visual QA evidence and remaining deviations.

## Example

**Input:** An editable Figma Qibla screen with a layered compass and Arabic/English variants.

**Expected implementation:** A responsive Expo screen using semantic navigation and buttons, live localized labels, sensor-derived heading with permission and calibration fallbacks, independently rendered compass layers, optimized background artwork, Reanimated motion, and screenshot comparison on the target phone dimensions.

