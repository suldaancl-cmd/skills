# Motion Technology Matrix

## Reanimated

Use for:

- React Native component and screen animation.
- Gesture-linked transforms.
- Shared values, derived values, spring/timing curves.
- Sensor-driven or continuous UI updates when supported by the project stack.

Do not use it as an excuse to recreate a complex interactive vector illustration from hundreds of manual paths when Rive is a better artifact.

## Gesture Handler

Use with Reanimated for native touch gestures such as pan, pinch, tap, long press, rotation, and composed gestures. Define gesture priority, cancellation, hit slop, accessibility alternative, and conflict with navigation.

## Rive

Use for:

- Interactive vector animation with a state machine.
- A reusable branded object responding to input/state.
- Complex authored interpolation that should stay in one `.riv` asset.

Avoid embedding dynamic localized copy or the entire application screen.

## Lottie

Use for:

- Short, deterministic, decorative vector sequences.
- Logo reveal, success mark, loader, sparkle, or small ornament.
- Cross-platform playback of an exported animation.

Avoid:

- Full-screen UI.
- Forms, buttons, navigation, live values, or localized text.
- Sensor- or gesture-driven state systems that require complex runtime control.
- Unsupported effects that rasterize badly or render inconsistently.

## Canvas, SVG, and Skia-style runtimes

Use for custom waveforms, charts, particle fields, masks, shaders, and high-frequency drawing. Choose the engine already used in the repository. Test GPU/CPU cost, memory, overdraw, and fallbacks.

## CSS, Motion, and GSAP

- Prefer CSS for simple transitions and keyframes.
- Use the project's existing component motion library for state/layout choreography.
- Use GSAP for timeline-heavy web sequences or scroll orchestration when already justified.
- Do not mix several motion engines on one screen without a clear ownership boundary.

## Three.js / React Three Fiber

Use for true interactive 3D on web when camera, light, material, or object manipulation is product-essential. Otherwise prefer pre-rendered optimized layers.

## Remotion

Use for deterministic frame-based video composition: promos, tutorials, store videos, launch trailers, and data-driven exports. Do not use it as the in-app interaction engine.

## Figma motion

Use for design intent, prototyping, approval, and extractable keyframe context. Production code still owns runtime behavior, performance, accessibility, and real data.

