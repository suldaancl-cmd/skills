# Reanimated patterns — the immersive 20% beyond the basics

## Worklet rules (read once)

- Functions that run on the UI thread are **worklets**. `useAnimatedStyle`, `useAnimatedScrollHandler`, and gesture callbacks are worklets automatically.
- To call JS (setState, navigation, analytics) from inside a worklet, wrap it: `runOnJS(fn)(args)`.
- To kick a worklet from JS, use `runOnUI(fn)()`. You rarely need this directly.
- Shared values are read/written as `.value`. Reading `.value` during render is fine; **mutating** it during render is not.

## Scroll-driven header / parallax

The signature "premium" scroll effect — header shrinks, hero image parallaxes, title fades:

```tsx
const scrollY = useSharedValue(0);
const onScroll = useAnimatedScrollHandler(e => { scrollY.value = e.contentOffset.y; });

const heroStyle = useAnimatedStyle(() => ({
  transform: [
    { translateY: interpolate(scrollY.value, [-120, 0, 200], [-60, 0, 100]) }, // parallax
    { scale: interpolate(scrollY.value, [-120, 0], [1.3, 1], 'clamp') },        // stretch on pull
  ],
  opacity: interpolate(scrollY.value, [0, 180], [1, 0], 'clamp'),
}));

<Animated.ScrollView onScroll={onScroll} scrollEventThrottle={16}>…</Animated.ScrollView>
```

`interpolate(value, inputRange, outputRange, 'clamp')` is the workhorse — clamp so it doesn't overshoot past the range. `interpolateColor(v, inputRange, [colorA, colorB])` does the same for colors (header background on scroll).

## Gesture + Reanimated (drag-to-dismiss sheet)

```tsx
const ty = useSharedValue(0);
const pan = Gesture.Pan()
  .onChange(e => { ty.value = Math.max(0, ty.value + e.changeY); })
  .onEnd(e => {
    if (ty.value > 120 || e.velocityY > 800) {
      ty.value = withTiming(600, {}, () => runOnJS(onDismiss)());
    } else {
      ty.value = withSpring(0, { damping: 18 });
    }
  });

const style = useAnimatedStyle(() => ({ transform: [{ translateY: ty.value }] }));
<GestureDetector gesture={pan}><Animated.View style={style}>…</Animated.View></GestureDetector>
```

Note the `Gesture.Pan()` builder API (Gesture Handler v2) — not the old `useAnimatedGestureHandler`. Velocity-based fling-to-dismiss feels far better than a pure position threshold.

## Shared-element transition (list card → detail)

The move that makes navigation feel native. Reanimated shared transitions:

```tsx
// On BOTH the list thumbnail and the detail hero, same tag:
<Animated.Image sharedTransitionTag={`cover-${id}`} source={…} />
```

Render both screens under a native-stack navigator. The tag matches the two elements and Reanimated morphs position/size between them. Keep the tag unique per item (`cover-${id}`) or every card animates to the same target.

## Layout animations (free entrance/exit motion)

```tsx
import Animated, { FadeInDown, FadeOut, LinearTransition } from 'react-native-reanimated';

<Animated.View entering={FadeInDown.springify().delay(i * 40)} exiting={FadeOut} layout={LinearTransition}>
```

- `entering` / `exiting` animate mount/unmount with no shared-value wiring.
- `layout={LinearTransition}` animates a view smoothly when its size/position changes (list reorder, expand/collapse).
- Stagger a list by `.delay(index * 40)`.

## Reduced motion

```tsx
import { useReducedMotion } from 'react-native-reanimated';
const reduce = useReducedMotion();
// then: duration = reduce ? 0 : 320, or skip entering animations entirely.
```
