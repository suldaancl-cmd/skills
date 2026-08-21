---
name: visual-fidelity-qa
description: Verify that a reconstructed Figma design and production app or website faithfully match the approved reference while remaining semantic, interactive, responsive, localized, accessible, and performant. Use for screenshot diffs, overlay review, motion review, RTL/LTR checks, state coverage, and final acceptance. Do not equate a successful build or matching screenshot alone with production readiness.
compatibility: Static automated comparison uses Python 3 and Pillow when available. Runtime verification requires the project's normal run environment.
metadata:
  version: 1.0.0
  owner: ASSALA AISTUDIO LTD
---

# Visual Fidelity QA

Produce evidence that the result matches the approved visual direction and behaves like a real product. Separate perceptual fidelity from semantic, functional, accessibility, and performance quality.

## When to use

- A Figma reconstruction must be approved against a reference image.
- A coded screen must be compared with Figma or an AI-generated source image.
- Motion must be checked against a Figma timeline, prototype, or motion specification.
- The user asks whether the work is truly production-ready.

## Boundaries

- A low pixel difference does not prove semantic UI, accessibility, or correct behavior.
- A passing build does not prove visual fidelity.
- Do not force reference and capture to the same dimensions without recording the resize.
- Do not hide deliberate platform differences; label and justify them.
- Do not call the result “pixel perfect” without a dimension-matched visual comparison.

## Required reading

Read `references/qa-playbook.md`. Use `assets/qa-report.md` for the final report.

## Procedure

### 1. Establish the comparison set

Collect:

- Original reference.
- Clean cropped reference.
- Figma render at target dimensions.
- Runtime screenshot from the target device/browser.
- Motion specification.
- Runtime recording when motion is in scope.
- Device, viewport, OS/browser, locale, theme, font scale, and build identifier.

Ensure the captures show the same product state and data.

### 2. Validate provenance and dimensions

- Confirm which file is authoritative.
- Record any compression, crop, scaling, or color-profile conversion.
- Match viewport and pixel dimensions when possible.
- If dimensions differ, compare layout semantics separately and create an explicitly labeled normalized comparison.

### 3. Run static visual comparison

Use three views:

1. Side-by-side.
2. 50% overlay or blink comparison.
3. Difference heatmap and numeric summary.

When Python and Pillow are available:

```bash
python scripts/visual_diff.py reference.png actual.png --out-dir qa-output
```

The script reports mean absolute error, RMSE, percentage of pixels beyond a configurable threshold, an overlay, and a difference heatmap. These metrics are evidence, not an automatic design grade.

### 4. Inspect by category

Review in this order:

- Composition and large geometry.
- Background crop and z-order.
- Typography hierarchy, font, wrapping, and baselines.
- Spacing, alignment, radius, and control size.
- Color, gradients, opacity, blur, borders, and shadows.
- Icons, illustration, and fine decoration.

Record expected platform rendering differences separately.

### 5. Audit semantic structure

Confirm:

- No screenshot is acting as the full UI.
- Text and live values are semantic.
- Interactive controls expose correct roles and states.
- Repeated UI maps to components.
- Background art contains no required interaction.
- Data graphics respond to data rather than a baked image.

### 6. Audit states and interaction

Test applicable states:

- Default, pressed, focused, selected, disabled.
- Loading, empty, offline, error, success.
- Permission not requested, denied, granted, unavailable.
- Navigation entry, exit, interruption, back.
- Repeated rapid input.
- Keyboard and focus behavior.
- Sensor/audio/data unavailable and stale states.

### 7. Audit motion

Compare:

- Initial state.
- Trigger.
- Key poses.
- Duration and delay.
- Easing or spring character.
- Stagger and coordination.
- End state.
- Interruption/reversal.
- Loop and stop conditions.
- Reduced-motion fallback.

For continuous motion, inspect input mapping, smoothing, clamp, latency, and stale/unavailable behavior.

### 8. Audit locale and accessibility

- Arabic RTL and English LTR.
- Long copy, mixed numerals, and text scaling.
- Correct mirroring policy.
- Verified sensitive/scriptural/legal content.
- Screen reader roles, labels, state, and announcements.
- Touch targets, focus order, contrast, and noncolor state cues.
- Reduced motion and high-contrast behavior where applicable.

### 9. Audit responsiveness and performance

- Test one smaller and one larger target than the reference.
- Test safe areas, keyboard, rotation policy, and crop anchors.
- Measure or observe frame stability on target-class hardware.
- Inspect large image decode, blur/overdraw, memory, and expensive continuous effects.
- Record exact tooling and conditions; do not invent performance numbers.

### 10. Classify findings

- `BLOCKER`: fake/flattened UI, wrong critical content, broken primary interaction, inaccessible critical path, or unusable performance.
- `MAJOR`: obvious mismatch or missing state that materially changes experience.
- `MINOR`: localized visual difference without product impact.
- `INFO`: intentional, documented platform or responsive difference.

### 11. Re-test and sign off

Fix blockers and majors, regenerate evidence, and update the report. Approval is scoped to the tested screen, state, locale, viewport, and build.

## Completion contract

Deliver:

1. Test matrix and environment.
2. Side-by-side, overlay, and heatmap where possible.
3. Numeric metrics with limitations.
4. Findings grouped by severity and category.
5. State, locale, accessibility, and performance evidence.
6. Approved differences.
7. Pass/fail status for every stage gate.
8. Exact remaining work.

## Example

**Finding:** “The runtime screenshot is visually close but the primary card and all buttons are one background image with invisible touch overlays.”

**Result:** `BLOCKER`, regardless of pixel similarity. Rebuild those elements as semantic components, then repeat visual and interaction QA.

