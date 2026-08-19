# Routing Matrix

## Visual asset route

| Visual region | Preferred artifact | Notes |
|---|---|---|
| Photo or complex generated environment | AVIF/WebP/PNG/JPEG | Optimize by platform; keep text and controls out. |
| Simple icon or logo | SVG/vector | Verify trademark and geometry; do not blindly auto-trace. |
| Complex decorative illustration | SVG, layered raster, or Rive | Choose based on interaction and performance. |
| Glass card or control surface | Native Figma/code effects | Rasterize only if it is purely decorative and immutable. |
| Live text, labels, scripture, prices | Live text/data | Never bake into an image or animation. |
| Chart, waveform, progress, compass | Runtime graphic | Bind to real data; use canvas/SVG/native layers as appropriate. |
| True 3D product scene | WebGL/Three.js/R3F or platform-specific runtime | Use pre-rendered layers when true 3D is not product-essential. |

## Motion route

| Need | Primary route | Avoid |
|---|---|---|
| React Native screen and component motion | Reanimated | Full-screen video or Lottie replacement for UI |
| Touch gestures | Gesture Handler + Reanimated | JS-thread-only continuous gestures |
| Interactive vector state machine | Rive | Many manually synchronized Lottie files |
| Short decorative vector sequence | Lottie | Localized text or live data inside animation |
| Custom waveform, shader, or canvas effect | Runtime canvas/Skia/SVG | Large bitmap frame sequences |
| Web UI motion | CSS/Motion/GSAP based on existing stack | Adding a second motion stack without need |
| 3D web interaction | Three.js/R3F or existing engine | Pre-rendered fake interaction when user input matters |
| Product video, promo, tutorial | Remotion | Shipping Remotion as the app interaction runtime |
| Figma prototype | Smart Animate/timeline | Treating prototype playback as production code |

## Platform route

- Use Expo/React Native for cross-platform mobile unless the project already commits to native Swift/Kotlin.
- Use React/Next.js for web when that is the existing stack; preserve its routing, styling, and component conventions.
- Use Code Connect or a documented component map after Figma and code components are stable.
- Prefer existing dependencies and patterns over introducing new libraries solely because they are named in this skill.

