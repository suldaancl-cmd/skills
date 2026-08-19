# Figma Structure and Naming

## Page structure

Use the project's existing convention when healthy. Otherwise:

- `00_REFERENCE`: originals, crops, annotations, source hierarchy.
- `01_FOUNDATIONS`: variables, typography, effects, grids.
- `02_COMPONENTS`: component sets and documentation.
- `03_SCREENS`: approved editable screens by flow and locale.
- `04_MOTION`: prototypes, timelines, motion boards.
- `05_HANDOFF`: redlines, implementation map, export nodes.
- `90_ARCHIVE`: superseded work retained for recovery.

## Layer names

Prefer semantic paths:

- `Screen/Qibla/Active/AR`
- `Navigation/Bottom/PrayerSelected`
- `Card/Location/Default`
- `Control/Microphone/Recording`
- `Data/Compass/Dial`
- `Art/Environment/Back`

Avoid names based only on appearance or creation order.

## Variable collections

- `Primitives/Color`
- `Semantic/Color`
- `Layout/Spacing`
- `Layout/Radius`
- `Typography/Role`
- `Effect/Elevation`
- `Effect/Blur`
- `Motion/Duration`
- `Motion/Easing`

Create component-scoped variables only when semantic/global tokens cannot express the requirement.

## Component properties

Use the smallest meaningful property set:

- `state`: default, pressed, focused, disabled, loading, error, success.
- `size`: compact, regular, large.
- `tone`: primary, secondary, destructive, neutral.
- `selected`: true/false.
- `icon`: instance swap or boolean where supported.
- `locale`: avoid using a variant when text and auto layout can adapt; use explicit RTL structure only when layout genuinely differs.

## Figma MCP read/write discipline

- Read page metadata before deep context for large files.
- Read variables and libraries before adding tokens or components.
- Write one coherent batch at a time: foundations, then component, then screen.
- After each batch, inspect node tree and render a screenshot.
- On failure, inspect partial output before retrying.
- Use exact file and node IDs; never guess them.
- Preserve the old design in archive or a duplicate unless deletion is explicitly authorized.

