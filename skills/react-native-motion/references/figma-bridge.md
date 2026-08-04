# Figma → React Native — worked example + mapping tables

`get_motion_context` emits motion.dev and CSS `@keyframes`. Here's how each maps to RN. Keep the **values verbatim** (durations, easing coefficients, offsets) — only the API changes.

## Easing mapping

| Figma / CSS emits | React Native |
|---|---|
| `cubic-bezier(x1,y1,x2,y2)` | `Easing.bezier(x1, y1, x2, y2)` |
| `ease-out` | `Easing.out(Easing.cubic)` |
| `ease-in-out` | `Easing.inOut(Easing.ease)` |
| `linear` | `Easing.linear` |
| `EASE_IN_AND_OUT_BACK` / overshoot | `Easing.inOut(Easing.back(1.4))` — tune the back factor to match |
| spring (CUSTOM_SPRING) | `withSpring(to, { damping, stiffness, mass })` — see spring note below |

**Spring note:** Figma/motion.dev springs are physics-based; Reanimated's are too, but the parameter names differ. Start from the snippet's stiffness/damping if present; otherwise approximate visually and verify on device. A snippet's spring is not a bezier — don't flatten it to `withTiming`, you'll lose the overshoot the designer wanted.

## motion.dev snippet → Moti (the easy path)

```
// get_motion_context snippet (web):
initial={{ opacity: 0, y: 16 }}
animate={{ opacity: 1, y: 0 }}
transition={{ duration: 0.32, ease: [0.16, 1, 0.3, 1] }}
```

becomes:

```tsx
<MotiView
  from={{ opacity: 0, translateY: 16 }}
  animate={{ opacity: 1, translateY: 0 }}
  transition={{ type: 'timing', duration: 320, easing: Easing.bezier(0.16, 1, 0.3, 1) }}
/>
```

Notes: motion.dev `y` → RN `translateY`; seconds → milliseconds; the `ease` array → `Easing.bezier(...)`. Moti's `from/animate/transition` is a near 1:1 of motion.dev's `initial/animate/transition`, which is why Moti is the default target for the bridge.

## CSS `@keyframes` → Reanimated sequence

```
/* multi-stop keyframe from get_motion_context */
@keyframes pop {
  0%   { transform: scale(0.8); opacity: 0; }
  60%  { transform: scale(1.05); opacity: 1; }
  100% { transform: scale(1); }
}  /* 400ms, ease-out */
```

becomes a `withSequence` (durations split across the stops proportionally):

```tsx
const s = useSharedValue(0.8), o = useSharedValue(0);
useEffect(() => {
  o.value = withTiming(1, { duration: 240 });
  s.value = withSequence(
    withTiming(1.05, { duration: 240, easing: Easing.out(Easing.cubic) }), // 0→60%
    withTiming(1,    { duration: 160, easing: Easing.out(Easing.cubic) }), // 60→100%
  );
}, []);
const style = useAnimatedStyle(() => ({ opacity: o.value, transform: [{ scale: s.value }] }));
```

For many stops, Reanimated's `Keyframe` API is cleaner than nested `withSequence` — use it when a track has 4+ stops.

## Worked example — Figma staggered list-in → Moti

`get_motion_context` returns 5 nodes sharing a `timelineCohort`, each `fade + slide-up`, staggered 40ms. **Don't** paste the transition 5×. Implement once, drive from the array (mirrors `figma-implement-motion` Rule 7 — factor repeated motion):

```tsx
const ITEM = {
  from: { opacity: 0, translateY: 16 },
  animate: { opacity: 1, translateY: 0 },
};
items.map((item, i) => (
  <MotiView key={item.id} from={ITEM.from} animate={ITEM.animate}
    transition={{ type: 'timing', duration: 320, delay: i * 40, easing: Easing.out(Easing.cubic) }}>
    <Row {...item} />
  </MotiView>
));
```

The cohort's shared duration + the 40ms stagger keep it coordinated — exactly what `timelineCohorts` encodes. If you gave each item an independent timer they'd drift.

## transform-origin

RN has no `transform-origin`. When a snippet scales/rotates off-center:
- Compose the transform array so a `translate` moves the pivot, then `scale`/`rotate`, then translate back; or
- Anchor via layout (put the element in a wrapper sized to the pivot).
Call it out in your summary when a design relied on a corner/edge origin — it's the most common source of "looks slightly off vs Figma."
