---
name: rn-screen-transitions
description: Screen and navigation transition choreography for React Native and Expo — expo-router / react-navigation animation options, shared-element transitions, modal and sheet presentation, gesture-driven back, and the native-stack requirements that make them work. Use whenever a screen change should feel designed rather than default. Triggers: "screen transition", "navigation animation", "page transition", "shared element", "sharedTransitionTag", "hero transition", "modal presentation", "sheet", "swipe back", "screen feels janky", "animate between screens".
version: 1.0.0
author: Karim
tags: [react-native, expo, navigation, motion, transition, mobile]
---

# React Native Screen Transitions

Screen transitions are the **most-seen motion in any app** — every tap fires one — and the most commonly left at default. Getting them right is the cheapest large win in perceived quality.

Authority: [[reference_mobile_motion_guide]]. Companion skills: `reanimated`, `expo-router`, `gesture-patterns`, `micro-interaction-spec`.

## The one rule that breaks everything

**Shared-element transitions require a native-stack navigator.** On a JS stack they fail silently — no error, no animation, just an instant cut. If `sharedTransitionTag` "does nothing", check the navigator before you touch the animation.

Expo Router's `Stack` is native-stack by default. `@react-navigation/stack` (the JS one) is not.

## Level ladder — same navigation, four qualities

Borrowed from the craft ladder in [[reference_raroque_premium_app_feel]]; screen transitions have exactly the same levels:

| Level | What the user sees |
|---|---|
| 1 | Platform default — an iOS push or Android fade |
| 2 | A deliberate choice of default (`slide_from_bottom` for a create flow, `fade` for a tab swap) |
| 3 | Custom timing and easing tuned to the content |
| 4 | Shared element — the thing they tapped *becomes* the next screen |

Most apps sit at 1. Level 2 costs one line. Level 4 is what makes an app feel expensive.

## Expo Router — per-screen options

```tsx
// app/_layout.tsx
import { Stack } from 'expo-router';

<Stack
  screenOptions={{
    animation: 'slide_from_right',   // default for the stack
    animationDuration: 260,
    gestureEnabled: true,            // iOS swipe-back
  }}
>
  <Stack.Screen name="index" />
  <Stack.Screen name="compose" options={{ animation: 'slide_from_bottom', presentation: 'modal' }} />
  <Stack.Screen name="detail"  options={{ animation: 'fade_from_bottom' }} />
</Stack>
```

`animation` accepts `default | fade | fade_from_bottom | flip | simple_push | slide_from_bottom | slide_from_right | slide_from_left | none`. `presentation` accepts `card | modal | transparentModal | containedModal | formSheet | fullScreenModal`.

**Pick by intent, not by taste:**

| Intent | Presentation |
|---|---|
| Going deeper into a hierarchy | `slide_from_right` (push) |
| Creating something new | `slide_from_bottom` + `modal` |
| A quick decision, context stays visible | `transparentModal` or `formSheet` |
| Switching peers (tabs) | `fade` or `none` — never a push |
| Destructive confirm | `transparentModal`, no slide |

Sliding a tab switch is the most common wrong choice: it implies hierarchy where there is none.

## Shared-element transitions

```tsx
import Animated from 'react-native-reanimated';

// list screen
<Animated.Image sharedTransitionTag={`cover-${item.id}`} source={item.cover} />

// detail screen — SAME tag
<Animated.Image sharedTransitionTag={`cover-${item.id}`} source={item.cover} />
```

Rules that actually bite:

- The tag must be **unique per element and identical across both screens**. Interpolating the id is not optional — a static tag on a list breaks the moment there are two items.
- Native stack only (see above).
- Keep the shared node simple. Animating a whole card with text and buttons produces visible reflow; share the image, cross-fade the rest.
- Both screens must mount the element at a **measurable size**. A shared node inside a not-yet-laid-out parent jumps.

## Gesture-driven back

`gestureEnabled: true` gives the iOS interactive pop for free. Two things to know:

- On Android it is off by default and stays off — do not fake it with a pan handler; use the hardware/gesture back.
- If a screen has a horizontal `ScrollView` or a `Pan` gesture at the edge, they fight. Set `gestureResponseDistance` to shrink the back-gesture hit zone rather than disabling the scroll.

## Reduced motion

```tsx
import { useReducedMotion } from 'react-native-reanimated';

const reduced = useReducedMotion();
<Stack screenOptions={{ animation: reduced ? 'fade' : 'slide_from_right', animationDuration: reduced ? 0 : 260 }} />
```

Never ship `animation: 'none'` as the reduced-motion path — users still need to perceive that the screen changed. Cross-fade instead of removing feedback.

## Timing

- Push / pop: **250–350ms**. Below 200 reads as a cut; above 400 feels sluggish.
- Modal up: **300–400ms** — larger travel earns more time.
- Tab fade: **120–180ms**.
- Match the back animation to the forward one. Asymmetric durations are the most common "feels off but I can't say why".

## Failure table

| Symptom | Cause |
|---|---|
| `sharedTransitionTag` does nothing | JS stack instead of native-stack |
| Shared element jumps at the start | element not laid out / no measurable size on one side |
| Two list items animate to the same target | static tag — interpolate the id |
| Back gesture fights a carousel | shrink `gestureResponseDistance` |
| Transition janks only on Android | work on the JS thread during the transition — defer it with `InteractionManager` |
| Modal slides in from the side | `presentation` left as `card` |

## Verify it

`get_screenshot`-style stills cannot show a transition. Screen-record on a **real mid-range Android**, then step frames — the iOS simulator hides the jank that matters. One recording per transition, watched at quarter speed, catches more than any amount of reading the code.
