# Reconstruction Playbook

## Visual decomposition questions

For every region ask:

1. Does the user need to read, select, focus, edit, announce, localize, or update it?
   - If yes, it is semantic UI or live data.
2. Does it respond continuously to touch, audio, sensor, scroll, network, or time?
   - If yes, it is a runtime graphic or control.
3. Is it purely atmospheric and visually complex?
   - If yes, it may remain raster or rendered art.
4. Does it need clean scaling, recoloring, or state changes?
   - If yes, prefer vector or native layers.
5. Would reproducing it with dozens of layers improve the product, or only satisfy a false notion of editability?
   - Keep the simplest artifact that preserves fidelity and required behavior.

## Art versus UI boundary

### Usually artwork

- Architecture, natural foliage, paper texture, clouds, grain, shadows cast by off-screen plants.
- Complex 3D portals, sculpted stairs, sand dunes, ornamental environments.
- Noninteractive atmospheric light and material detail.

### Always semantic or runtime-driven

- Button and tab labels.
- Form fields and authentication controls.
- Navigation.
- Quranic text and translations.
- Timers, percentages, scores, location, distance, accuracy, and status.
- Compass rotation and sensor indicator.
- Recording waveform and audio-reactive effects.
- Error, loading, permission, offline, and empty states.

## Glass reconstruction

Represent glass as a system rather than one screenshot effect:

- Tinted translucent fill.
- Background blur where supported.
- Subtle highlight gradient.
- Inner or outer stroke.
- Elevation shadow.
- Optional noise texture used sparingly.
- Platform fallback when true backdrop blur is unavailable or expensive.

Do not stack many expensive blur surfaces without testing target hardware.

## Typography reconstruction

- Identify role before font: display, title, heading, body, label, caption, numeric/data.
- Verify font licensing and Arabic glyph quality.
- Re-enter copy from trusted sources.
- Test long English, long Arabic, dynamic type, and mixed numerals.
- Preserve intentional optical alignment without hardcoding one language.

## Fidelity strategy

Aim for high perceptual fidelity, not meaningless layer count. Match in this order:

1. Composition and silhouette.
2. Major color and luminance distribution.
3. Typography scale and hierarchy.
4. Spacing and control geometry.
5. Material, shadow, blur, and border detail.
6. Micro-decoration.

