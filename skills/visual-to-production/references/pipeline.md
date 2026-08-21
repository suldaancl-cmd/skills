# Full Pipeline Playbook

## Phase 0 — Authorization and preservation

- Determine whether the request is review-only or authorizes writes.
- Resolve exact Figma file, page, node, repository, branch, and output target.
- Work in a duplicate page, branch, or recoverable section when the original matters.
- Keep originals unchanged and record the reference file hashes when practical.

## Phase 1 — Reference normalization

- Inspect the original image, not a compressed preview.
- Crop editor chrome and device mockup artifacts from the working reference.
- Preserve an uncropped copy for provenance.
- Record width, height, aspect ratio, pixel density if known, language, and likely device.
- Flag generated typography, impossible geometry, inconsistent shadows, and duplicated icons.

## Phase 2 — Visual reverse specification

Create a written specification before drawing:

- Composition grid and safe-area behavior.
- Major surfaces and z-order.
- Spacing and alignment anchors.
- Typography hierarchy and verified content.
- Palette, gradients, opacity, glass, blur, shadow, and texture.
- Reusable components and states.
- Asset classification and ownership.
- Responsive and locale behavior.
- Proposed interaction and motion.

This is reverse specification, not recovery of original design intent.

## Phase 3 — Golden screen

Choose the screen with the greatest combined risk:

- Complex art and semantic UI overlap.
- Important RTL/LTR behavior.
- Critical interaction or sensor/data graphic.
- Representative shared navigation and components.

Finish the golden screen end-to-end before building the complete flow.

## Phase 4 — System extraction

After the screen is visually accepted:

- Extract primitives and semantic tokens.
- Promote repeated structures to components.
- Define variants and state ownership.
- Separate product data from visual defaults.
- Create implementation mappings.

Avoid designing a large abstract system before the golden screen proves the visual language.

## Phase 5 — Motion architecture

Classify motion by ownership:

- Navigation/state transition.
- Gesture-driven interaction.
- Sensor/audio/data-driven visualization.
- Decorative finite sequence.
- Interactive vector state machine.
- 3D scene animation.
- Rendered marketing video.

Assign one primary runtime owner for each motion. Do not duplicate the same state machine in Figma, Lottie, Rive, and code.

## Phase 6 — Production implementation

- Inspect before adding dependencies.
- Build tokens and primitives before composing the screen.
- Use real localization, accessibility, navigation, and data contracts.
- Run the product on the actual target class of device or browser.
- Capture evidence at exact reference dimensions when possible.

## Phase 7 — QA and sign-off

Track issues by severity:

- `BLOCKER`: flattened semantic UI, broken interaction, wrong content, missing locale, inaccessible critical action, or unusable performance.
- `MAJOR`: clearly wrong layout, typography, color, motion, state, or responsive behavior.
- `MINOR`: small optical, spacing, or rendering difference that does not change meaning.
- `INFO`: deliberate documented platform difference.

No stage is complete merely because an artifact exists.

