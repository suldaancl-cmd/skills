# Design-to-Code Contract

## Token mapping

Each Figma semantic token maps to one runtime token. Record exceptions.

| Figma role | Runtime role |
|---|---|
| Semantic color | Theme color token |
| Typography role | Text style/component variant |
| Spacing/radius | Layout token |
| Elevation/blur | Effect token or documented platform fallback |
| Motion duration/easing | Runtime motion token |

## Component mapping

Map components only when ownership is clear:

- Stable Figma component.
- Stable runtime component.
- Known prop/variant relationship.
- Defined content slot behavior.
- Accessibility and locale behavior documented.

## Intentional platform differences

Document differences such as:

- Native versus web focus behavior.
- Backdrop blur support and performance.
- Safe areas and system navigation.
- Font rendering and line metrics.
- Sensor availability.
- Hover versus touch states.

The goal is equivalent product intent and high visual fidelity, not identical internal implementation.

## Forbidden shortcuts

- Full-screen screenshot as UI.
- Rasterized localized content.
- Invisible overlay buttons on top of a screenshot.
- One component per Figma layer without product meaning.
- Hardcoded device-only coordinates for ordinary layout.
- Fake live data embedded in artwork.
- Claims of completion without running the target.

