# QA Playbook

## Test matrix

Record one row per test combination:

- Build/commit.
- Screen and state.
- Locale and direction.
- Theme.
- Viewport/device.
- OS/browser.
- Font scale/zoom.
- Reduced motion.
- Network/permission/data condition.

## Static metrics

Useful metrics include:

- Mean absolute RGB error.
- Root mean square RGB error.
- Percentage of pixels above a threshold.
- Exact dimension match.

Metrics are sensitive to font rasterization, compression, antialiasing, color profile, and capture differences. Use them to locate and track change, not as a universal quality score.

## Perceptual review

Check large features before microdetails:

1. Silhouette and composition.
2. Main surface sizes and anchors.
3. Text hierarchy.
4. Color/luminance distribution.
5. Spacing and control geometry.
6. Material effects.
7. Decoration.

## Semantic review

Use an inspector, accessibility tree, DOM/native hierarchy, or Figma node tree as appropriate. Confirm that visible semantics are not baked into images.

## Motion review

Compare recordings at normal speed, then inspect key frames. A frame-accurate match is appropriate for rendered video; interactive app motion should prioritize state, timing, interruption, input response, and accessibility.

## Acceptance strategy

Set thresholds per project. A practical contract can combine:

- Zero blockers.
- Zero unapproved major issues.
- Numeric difference within an agreed range for a controlled capture.
- All critical states and locales tested.
- Stable runtime on target-class hardware.

Never use a numeric screenshot threshold as the only acceptance condition.

