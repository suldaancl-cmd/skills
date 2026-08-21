---
name: rn-component-motion
description: Motion for the React Native components users actually touch — bottom sheets, swipeable rows, pull-to-refresh, animated lists, carousels, toasts, tab bars, accordions, FABs, and modals. Covers @gorhom/bottom-sheet, gesture-handler Swipeable, FlashList, reanimated-carousel, and toast patterns. Use when a component should respond to touch rather than just re-render. Triggers: "bottom sheet", "swipe to delete", "swipeable row", "pull to refresh", "animated list", "list item animation", "carousel", "toast", "snackbar", "tab bar animation", "accordion", "expand collapse", "FAB", "component feels static".
version: 1.0.0
author: Karim
tags: [react-native, expo, motion, components, gesture, mobile]
---

# React Native Component Motion

The components users touch every session. This is where "vibe coded" is *felt* — a screen can look perfect and still feel cheap because the sheet snaps instead of settles and the row deletes without acknowledging the swipe.

Authority: [[reference_mobile_motion_guide]]. Engine skills: `reanimated`, `moti`, `gesture-patterns`. Screen-level motion is `rn-screen-transitions`.

## Version note

Versions below are **latest on npm as of 2026-08-06**. Always install with `npx expo install <pkg>` — it resolves the SDK-compatible version, which is often *behind* latest (e.g. Expo SDK 57 pins `react-native-gesture-handler` 2.32.x while npm latest is 3.1.0). Installing latest by hand is a common way to break a build.

## The component motion table

| Component | Library | npm latest | SDK 57 resolves to | The rule |
|---|---|---|---|---|
| Bottom sheet | `@gorhom/bottom-sheet` | 5.2.14 | 5.2.14 | Snap points, not a modal with a slide |
| Swipeable row | `react-native-gesture-handler` (`ReanimatedSwipeable`) | 3.1.0 | **2.32.x** | Resistance at the end, never free travel |
| Long list | `@shopify/flash-list` | 2.3.2 | **2.0.2** | Replaces FlatList; animate items, not the list |
| Carousel | `react-native-reanimated-carousel` | 5.1.0 | 5.1.0 | Parallax/stack modes built in |
| Toast / snackbar | `react-native-toast-message` | 2.4.0 | 2.4.0 | Enter from the safe area, not the screen edge |
| Pull-to-refresh | `RefreshControl` or a Reanimated custom header | built-in | — | Custom only when the brand demands it |

The bolded columns are the point: **`npx expo install` deliberately installs behind npm latest.** Verified on SDK 57.0.10 — FlashList resolved to 2.0.2 (latest 2.3.2) and gesture-handler to 2.32.x (latest 3.1.0). Plain `npm i` would pull latest and break the build. Only `three`, `@react-three/fiber` and `@react-three/drei` are safe via plain `npm i` — they are not native modules.

## Bottom sheets

```tsx
import BottomSheet, { BottomSheetView } from '@gorhom/bottom-sheet';

const snapPoints = useMemo(() => ['35%', '85%'], []);

<BottomSheet ref={ref} snapPoints={snapPoints} enablePanDownToClose index={-1}>
  <BottomSheetView style={{ flex: 1 }}>{/* content */}</BottomSheetView>
</BottomSheet>
```

- **Use `BottomSheetScrollView` / `BottomSheetFlatList`**, never a plain `ScrollView`. A plain one fights the sheet's pan and the sheet stops dragging.
- Two snap points beat three. Each extra stop is a decision you force on the user.
- `enablePanDownToClose` without a backdrop leaves users stuck on Android — add `backdropComponent`.
- The sheet must live **inside** `GestureHandlerRootView`, above your navigator, or gestures silently die.

## Swipeable rows

```tsx
import ReanimatedSwipeable from 'react-native-gesture-handler/ReanimatedSwipeable';

<ReanimatedSwipeable
  friction={2}
  rightThreshold={40}
  renderRightActions={(progress, translation) => <DeleteAction progress={progress} />}
>
  <Row />
</ReanimatedSwipeable>
```

- `friction={2}` is the single most important value — friction 1 feels frictionless in the bad way, like the row is falling.
- Animate the action itself off `progress`. A static red block sliding out is level 1; an icon that scales in as the threshold nears is level 3.
- **Destructive actions need a confirm or an undo toast.** A swipe that deletes instantly will be triggered by accident in a pocket.
- Only one row open at a time — close the previous on `onSwipeableWillOpen`.

## Animated lists

Use `FlashList`, then animate **items**, never the container:

```tsx
import { FlashList } from '@shopify/flash-list';
import Animated, { FadeInDown, LinearTransition } from 'react-native-reanimated';

<FlashList
  data={items}
  keyExtractor={(i) => i.id}
  renderItem={({ item, index }) => (
    <Animated.View entering={FadeInDown.delay(Math.min(index, 8) * 40)} layout={LinearTransition}>
      <Row item={item} />
    </Animated.View>
  )}
/>
```

- **Cap the stagger index** (`Math.min(index, 8)`). Uncapped, item 200 waits 8 seconds to appear.
- `layout={LinearTransition}` gives free reflow when an item is removed — this is what makes deletion feel real.
- Do not put `entering` on recycled rows without a cap; FlashList recycles views and every scroll re-fires the animation.

## Toasts

Enter from inside the safe area, never the raw screen edge — a toast that slides from `y: 0` clips under the notch.

```tsx
<MotiView
  from={{ opacity: 0, translateY: -12 }}
  animate={{ opacity: 1, translateY: 0 }}
  exit={{ opacity: 0, translateY: -12 }}
  transition={{ type: 'spring', damping: 18 }}
/>
```

Auto-dismiss at **4s** for info, never for errors the user must act on. Always wrap in `AnimatePresence` or `exit` never runs.

## Tab bars

The most-seen component motion in any app. Animate the **icon and the indicator**, not the bar:

- Indicator slides with a spring (`damping: 20`), 200–260ms.
- Active icon scales `1 → 1.12` and back, or swaps to a filled variant — see `rn-icon-motion`.
- Haptic on change: `Haptics.selectionAsync()`. This is the cheapest premium signal in the whole app.
- Never animate tab bar *height* — it reflows every screen underneath.

## Accordions and FABs

Accordion: animate `height` via `useAnimatedStyle` with a measured value, or use `LinearTransition` on the parent and let layout animation do it. Never animate `height: 'auto'` — it is not interpolatable.

FAB expansion: stagger children **60ms apart** and rotate the FAB icon 45° into a close state. Collapse in reverse order, not simultaneously.

## Guardrails

- Every gesture component needs `GestureHandlerRootView` at the app root.
- Honour `useReducedMotion()` — collapse stagger to 0 and skip scale; keep opacity so state changes stay perceivable.
- Never `setState` inside a gesture handler — use shared values and `runOnJS` only on settle.
- Test swipe and sheet gestures on a **real mid-range Android**; the simulator's mouse-drag hides the friction problems entirely.

## Failure table

| Symptom | Cause |
|---|---|
| Sheet won't drag when content scrolls | plain `ScrollView` instead of `BottomSheetScrollView` |
| Gestures do nothing | missing `GestureHandlerRootView` |
| List items re-animate on every scroll | `entering` on recycled FlashList rows |
| Last items appear seconds late | uncapped stagger index |
| Toast clipped by the notch | animating from the screen edge, not the safe area |
| Row swipe feels like falling | `friction` left at 1 |
| Accordion jumps open | animating `height: 'auto'` |
