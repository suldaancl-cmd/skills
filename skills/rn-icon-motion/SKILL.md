---
name: rn-icon-motion
description: Animated icons across iOS, Android and React Native — SF Symbols effects via expo-symbols, Lottie and Rive icon pipelines, SVG path animation with react-native-svg, tab-bar icon morphing, and Android AnimatedVectorDrawable. Use whenever an icon should react to state rather than sit static. Triggers: "animated icon", "icon animation", "SF Symbol", "symbolEffect", "tab bar icon", "icon morph", "lottie icon", "rive icon", "animated svg", "loading spinner", "like button animation", "checkmark animation".
version: 1.0.0
author: Karim
tags: [react-native, expo, icons, motion, lottie, rive, svg, mobile]
---

# Icon Motion

Icons are the highest-frequency motion surface in an app — a tab bar animates on every navigation. They are also the most commonly left static, which is why an animated one reads as expensive.

Authority: [[reference_mobile_motion_guide]]. Related: `rn-component-motion` (tab bars), `icon-system` and `app-icon` (static icon design), `lottie-runtime`, `rive-runtime`.

## Pick the route

| Need | Route | Version |
|---|---|---|
| Native iOS system icons with built-in effects | `expo-symbols` (SF Symbols) | 57.0.1 |
| Designer-authored icon animation, plays once or loops | Lottie (`lottie-react-native`) | 7.3.x |
| Icon that reacts to state / user input | Rive (`rive-react-native`) | 9.8.x |
| Custom vector you control frame by frame | `react-native-svg` + Reanimated | 15.15.5 |
| Simple scale / rotate / colour on an existing icon | Reanimated or Moti directly | — |
| Android-native vector morph | `AnimatedVectorDrawable` | platform |

Escalate only when the tier below can't do it. A like-button bounce is Moti, not Rive.

Install with `npx expo install <pkg>` — it picks the SDK-compatible version, which often trails npm latest.

## SF Symbols (iOS)

```tsx
import { SymbolView } from 'expo-symbols';

<SymbolView
  name="bell.fill"
  type="hierarchical"
  animationSpec={{ effect: { type: 'bounce' }, repeating: false }}
  size={28}
/>
```

Effects: `bounce`, `pulse`, `scale`, `appear`, `disappear`, `replace`. `replace` is the good one — it morphs between two symbols (`play.fill` → `pause.fill`) natively, which is expensive to fake.

**iOS only.** Always ship an Android fallback in the same component — a missing symbol renders as empty space, not an error:

```tsx
Platform.OS === 'ios' ? <SymbolView … /> : <MaterialIcon … />
```

## Lottie icons

For icons a designer authored in After Effects. Prefer **dotLottie** (`.lottie`) — roughly 80% smaller than raw JSON.

```tsx
import LottieView from 'lottie-react-native';

const ref = useRef<LottieView>(null);
<LottieView ref={ref} source={require('./like.lottie')} loop={false} autoPlay={false} />
// fire on interaction
ref.current?.play();
```

- Drive **segments** for state: `play(0, 30)` to like, `play(30, 60)` to unlike. One file, both directions.
- Never `autoPlay` a looping icon in a list — 40 looping Lotties is a frame-rate disaster.
- Lottie cannot be recoloured at runtime without `colorFilters`; if the icon must follow a theme, use SVG or Rive instead.

## Rive icons

When the icon must respond to input rather than play a fixed clip — a toggle that follows the drag, a loader with multiple states.

```tsx
import Rive, { RiveRef } from 'rive-react-native';

const ref = useRef<RiveRef>(null);
<Rive ref={ref} resourceName="icons" stateMachineName="ToggleSM" />
ref.current?.setInputState('ToggleSM', 'isOn', true);
```

State machines take boolean / number / trigger inputs. This is the only route where the icon can be *interactive* rather than played.

## SVG path animation

Full control, no asset pipeline. `react-native-svg` 15.15.5 + Reanimated:

```tsx
import Svg, { Path } from 'react-native-svg';
import Animated, { useAnimatedProps, useSharedValue, withTiming } from 'react-native-reanimated';

const AnimatedPath = Animated.createAnimatedComponent(Path);
const progress = useSharedValue(0);

const animatedProps = useAnimatedProps(() => ({
  strokeDashoffset: LENGTH * (1 - progress.value),
}));

<Svg viewBox="0 0 24 24">
  <AnimatedPath d={CHECK_PATH} stroke="#FFDA21" strokeWidth={2} fill="none"
    strokeDasharray={LENGTH} animatedProps={animatedProps} strokeLinecap="round" />
</Svg>
```

The `strokeDasharray` + `strokeDashoffset` pair is the draw-on trick — set both to the path length and animate the offset to 0. Get `LENGTH` from the path once (`getTotalLength()` at design time, hardcode it) rather than measuring per render.

**`createAnimatedComponent` + `animatedProps` is required.** Animating an SVG `Path`'s `d` or stroke via style will not work.

## Tab-bar icon morphing

The highest-value icon motion you can ship:

1. Two variants — outline (inactive) and filled (active).
2. Cross-fade them with opacity while scaling the active one `1 → 1.12 → 1`.
3. Spring the indicator separately (`damping: 20`, 200–260ms).
4. `Haptics.selectionAsync()` on change.

On iOS, `SymbolView` with `effect: { type: 'replace' }` does 1–2 natively for system icons.

## Guardrails

- **Icons are content.** Every animated icon still needs `accessibilityLabel`; motion is not a label.
- Honour `useReducedMotion()` — swap the variant instantly instead of morphing. Never remove the state change itself.
- Icon animations are **80–200ms**. Anything slower reads as lag, because the user already knows what they tapped.
- Don't animate more than one icon at a time in a row or list — competing motion reads as noise.
- Keep looping icons off-screen-aware; pause when not visible.

## Failure table

| Symptom | Cause |
|---|---|
| Blank space where an icon should be on Android | `expo-symbols` with no platform fallback |
| SVG path won't animate | animated via style instead of `animatedProps` + `createAnimatedComponent` |
| Frame rate collapses in a list | multiple `autoPlay` looping Lotties |
| Lottie icon ignores dark mode | Lottie can't recolour at runtime — use SVG or Rive |
| Draw-on starts fully drawn | `strokeDashoffset` not initialised to the full path length |
| Icon animation feels laggy | duration over ~200ms |
