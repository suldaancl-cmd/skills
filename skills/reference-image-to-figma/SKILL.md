---
name: reference-image-to-figma
description: Rebuild AI-generated UI images, PNGs, JPEGs, screenshots, or concept renders as native editable Figma frames with live text, auto layout, variables, components, variants, assets, and RTL/LTR behavior. Use when the reference image is visually approved but the current Figma is missing, flattened, or stylistically wrong. Do not use to import the whole screenshot as the final design.
compatibility: Requires image inspection and a supported Figma MCP connection with write access for direct canvas edits.
metadata:
  version: 1.0.0
  owner: ASSALA AISTUDIO LTD
  mcp-server: figma
---

# Reference Image to Editable Figma

Reconstruct a raster visual reference as semantic design. The objective is not to recover nonexistent source layers; it is to create the closest maintainable Figma system that preserves the approved composition and art direction.

## When to use

- A generated image is the visual source of truth.
- Existing Figma screens are structurally editable but visually unacceptable.
- A Figma file contains full-screen raster tiles instead of components.
- The user wants subsequent motion or code handoff.

## Boundaries

This skill creates or specifies native Figma design structure. It does not:

- Claim lossless reverse engineering.
- Replace verified content with OCR guesses.
- Convert photographs or complex 3D scenes into fake editable vectors.
- Delete legacy pages unless the user explicitly authorizes exact targets.
- Implement production application behavior; use `figma-to-production-code` after the Figma gate.

## Required reading

- Read `references/reconstruction-playbook.md` for decomposition and art/UI boundaries.
- Read `references/figma-structure.md` before writing to Figma.

## Figma MCP tool strategy

Tool names vary by client. Resolve tools by capability:

1. **Screenshot/render:** inspect the exact reference frame and final result.
2. **Metadata:** get a sparse page/node outline before requesting deep context.
3. **Design context:** retrieve layout, styling, assets, and components for bounded nodes.
4. **Variables/libraries:** inspect tokens and reusable systems before creating new ones.
5. **Write-to-canvas:** create and update native Figma nodes in bounded batches.
6. **Motion context:** use only after static structure when motion already exists.
7. **Code Connect:** map stable Figma components to stable code components later.

When the host provides Figma prerequisite skills, load them before write calls. When a write tool supports skill attribution, pass this skill name. Never loop blind retries after a failed write; inspect partial state, remove or isolate partial output, correct the root cause, and retry once.

## Procedure

### 1. Inspect without mutation

1. Open every reference at full resolution.
2. Identify accidental chrome: viewer buttons, editor toolbars, download controls, device frames, black bars, or captions outside the product UI.
3. Inspect the target Figma file at page level, then inspect only relevant pages and frames.
4. Inventory existing variables, styles, components, libraries, page conventions, and assets.
5. Capture the current design before any authorized edits.

### 2. Establish the reference contract

Document:

- Authoritative reference.
- Target frame size and safe area.
- Platform and locale.
- Exact-match regions.
- Regions allowed to adapt for usability or platform constraints.
- Verified copy sources.
- Required component states.
- Golden screen and approval gate.

If references conflict, assign ownership separately for composition, visual style, content, and behavior.

### 3. Decompose the image

Use `assets/layer-plan.csv` and classify every visible region:

- `ART_RASTER`
- `ART_VECTOR`
- `UI_SEMANTIC`
- `DATA_GRAPHIC`
- `MOTION_ONLY`
- `UNKNOWN`

For each region record bounding box, z-index, expected asset, responsive behavior, locale behavior, state owner, and uncertainty.

### 4. Prepare assets

1. Preserve the original reference.
2. Create a clean crop without editor chrome.
3. Retain complex art as an optimized asset when vector reconstruction would reduce fidelity or waste effort.
4. Split art into depth layers only when parallax, occlusion, or responsive cropping needs it.
5. Recreate simple icons and geometry as vectors; visually verify any auto-trace.
6. Obtain official brand marks and licensed fonts.
7. Keep text, values, buttons, inputs, navigation, scripture, and data out of raster assets.
8. Record every asset in `assets/asset-manifest.csv` with rights and export requirements.

### 5. Create a safe Figma workspace

Use this default page architecture unless the project already has a stronger convention:

- `00_REFERENCE`
- `01_FOUNDATIONS`
- `02_COMPONENTS`
- `03_SCREENS`
- `04_MOTION`
- `05_HANDOFF`
- `90_ARCHIVE`

Place the source reference and clean crop in `00_REFERENCE`, name them clearly, and lock them. Do not edit the original image.

### 6. Establish foundations

Create or reuse:

- Primitive color variables.
- Semantic color variables.
- Spacing and sizing variables.
- Radius variables.
- Typography roles.
- Elevation, blur, and opacity tokens.
- Motion duration and easing tokens when needed.
- Light/dark or brand modes only when the product requires them.

Bind actual nodes to tokens. Merely creating variables does not make a design systematic.

### 7. Reconstruct the golden screen

1. Set the clean reference as a locked overlay at the exact target size.
2. Build from the largest structural regions to the smallest details.
3. Use auto layout for vertical/horizontal stacks, lists, controls, navigation, and cards.
4. Use constraints or min/max behavior for art composition and responsive regions.
5. Rebuild glass surfaces with Figma fills, gradients, strokes, effects, and transparency when feasible.
6. Keep complex environmental art below semantic UI.
7. Use live verified text with defined typography roles.
8. Promote repeated UI into components before duplicating screens.
9. Add variants for meaningful states: default, pressed, focused, selected, disabled, loading, error, and success as applicable.
10. Create Arabic RTL and English LTR variants without mirroring nondirectional icons or religious imagery incorrectly.
11. Name layers by role, not appearance: `Header/Brand`, `Card/Recitation`, `Action/Primary`, not `Rectangle 492`.

### 8. Validate structure

Reject the screen if any condition is true:

- A full-screen screenshot is still the visible product UI.
- Button text, navigation labels, inputs, or live values are rasterized.
- Repeated elements are detached copies without a justified reason.
- Layout depends on dozens of arbitrary absolute coordinates.
- Variables exist but are not bound.
- Component states are represented only by comments.
- Arabic is visually reversed, incorrectly aligned, clipped, or unverified.
- Background art captures controls that must be interactive.

### 9. Validate fidelity

1. Render the reconstructed frame at reference dimensions.
2. Compare with side-by-side, 50% overlay, and difference view.
3. Record deviations in geometry, typography, color, effect, asset crop, and content.
4. Fix blockers and majors before creating the remaining screens.
5. Obtain golden-screen approval.

### 10. Prepare handoff

Deliver:

- Figma URL and exact node IDs.
- Page and component inventory.
- Variable and style inventory.
- Asset manifest with export formats.
- Component/state matrix.
- Responsive and locale notes.
- Motion candidates and uncertainties.
- Fidelity report and approved differences.

## Generated-image-specific rules

- Generated images often contain impossible perspective, inconsistent padding, repeated icons, false text, and light that cannot be reproduced by one CSS/Figma blur. Resolve these deliberately; do not hide them.
- For a cinematic background plus glass UI, keep the environment as artwork and rebuild the entire interaction layer.
- For a compass, separate dial, ticks, needle/indicator, center art, labels, accuracy state, and location card.
- For a recording screen, separate microphone control, timer, waveform, state label, metrics, word chips, and actions. The waveform belongs to runtime data, not a static screenshot.
- For authentication, use official sign-in assets and accessible controls; generated brand buttons are reference only.

## Example

**Input:** One generated Qibla screen with a detailed cream environment, a glass compass, location card, and bottom navigation.

**Expected result:** The environment remains an optimized background asset; the compass is decomposed into independently rotatable runtime-ready layers; all labels and values are live; buttons and navigation are components with states; Arabic and English variants exist; the original image remains locked in the reference page; a rendered overlay documents fidelity.

