---
name: android-motion-system
description: Use when animation in a React Native, Expo, or Compose app looks right on iOS but janks, stutters, or feels wrong on Android — or when building motion that must feel native on both. Covers why the two platforms diverge (frame pacing, variable refresh rate, OEM animator scales, overscroll and edge-effect differences, back-gesture prediction), the Material motion vocabulary Android users expect, Reanimated worklet rules that only bite on Android, and how to profile jank with the tools that actually attribute a dropped frame. Reach for this before shipping motion to Play, since dropped frames become ANR and vitals problems, not just polish problems.
---

# Android Motion System

Motion built and reviewed only on iOS ships broken to the larger half of the market. Android diverges in frame pacing, refresh rate, system gesture behaviour, and OEM settings — and on Android, bad motion is not merely ugly. Sustained main-thread blocking becomes ANRs, and ANRs feed Android vitals, which quietly suppresses store discoverability.

**Companion skills.** Reanimated API detail → `reanimated`, `react-native-motion`. Compose fundamentals → `android-jetpack-compose`. Play vitals consequences → `play-console-mastery`. Cross-platform motion specs → `motion-spec-bridge`.

## Why iOS-tuned motion breaks on Android

| Cause | What you see | Fix |
|---|---|---|
| **Variable refresh rate** | Animation runs at the wrong speed or stutters on 90/120 Hz panels | Never assume 60 fps. Drive by time, not by frame count |
| **OEM animator duration scale** | Animations run 0.5×, 2×, or instantly on some users' devices | Respect it — it is an accessibility setting. Do not fight it |
| **Frame pacing** | Micro-stutter that no single slow frame explains | Profile pacing, not just average fps |
| **JS-thread animation** | Smooth on a fast phone, janky on mid-range | Move to the UI thread — worklets or native driver |
| **Overscroll behaviour** | iOS rubber-band expected, Android stretch/glow appears | Do not emulate iOS bounce on Android; use platform behaviour |
| **Predictive back gesture** | Back animation fights the system preview | Adopt the predictive back API rather than overriding back |
| **Cold-start jank** | First animation after launch drops frames | Warm shaders and defer non-critical work off the first frames |

The mid-range Android device is the target, not the flagship. A OnePlus or Pixel flagship hides every one of these problems.

## The rule that prevents most Android jank

**Animation must never depend on the JavaScript thread per frame.**

On iOS the JS thread often keeps up well enough to hide the mistake. On mid-range Android it does not, and the same code visibly stutters.

Concretely, in React Native and Expo:

- Drive animation with **Reanimated worklets** running on the UI thread
- If using the legacy `Animated` API, `useNativeDriver: true` is mandatory — and it only supports transform and opacity, not layout properties
- **Never** animate by calling `setState` per frame
- **Never** animate `width`, `height`, `top`, or `left`. Animate `transform` and `opacity`, which the compositor can handle without a layout pass
- `LayoutAnimation` is legacy and behaves inconsistently on Android — prefer Reanimated layout animations

## Reanimated rules that only bite on Android

- **The Babel plugin must be LAST** in `babel.config.js`. Anything after it breaks worklet compilation, sometimes silently. After changing it, run `npx expo start --clear` — a stale Metro cache will keep serving the broken build and you will debug a phantom.
- Values read inside a worklet must be shared values. Capturing a plain JS variable copies it once and it never updates.
- Crossing the JS/UI boundary per frame with `runOnJS` reintroduces exactly the jank worklets were meant to remove. Call it on gesture end, not on gesture move.
- Heavy work inside a worklet blocks the UI thread directly — that is worse than blocking JS, because it drops frames with no queue to absorb it.

## Material motion vocabulary

Android users have platform expectations. Ignoring them makes an app feel foreign even when it is technically smooth.

| Pattern | When to use | Character |
|---|---|---|
| **Container transform** | An element expands into a full screen — card to detail | The element persists and grows; nothing cross-fades |
| **Shared axis** | Steps in a sequence, tabs, onboarding | Both outgoing and incoming move along the same axis |
| **Fade through** | Switching between unrelated destinations | Outgoing fades and shrinks slightly, incoming fades in |
| **Fade** | Elements entering or leaving within a screen | Simple opacity, short |

Emphasis and duration guidance:

- **Short, functional transitions** — roughly 100–200 ms. Feedback, small state changes.
- **Standard transitions** — roughly 200–350 ms. Most screen and container transitions.
- **Large or complex movement** — up to roughly 500 ms. Beyond that the app feels slow, not premium.
- **Easing** — enter with a decelerating curve, exit with an accelerating curve. Linear reads as mechanical; symmetric ease-in-out reads as sluggish for UI.

Springs generally feel better than fixed-duration curves for anything the user is directly manipulating; durations are appropriate for anything the system initiates.

## System settings you must respect

- **Reduce motion / animator duration scale.** Users set these deliberately, often for vestibular reasons. Honour them — replace movement with a fade, do not simply run the animation anyway. Ignoring this is both an accessibility failure and a review risk.
- **Dark theme.** Motion that relies on shadow or glow needs its dark-theme equivalent checked; elevation reads differently.
- **Font scale.** Large accessibility font sizes break animations that assume fixed element heights.
- **Predictive back.** Android surfaces a preview of the destination as the user drags back. Overriding the back gesture with a custom animation fights the system and looks broken.

## Edge and scroll behaviour

- Android uses a **stretch overscroll effect**, not the iOS rubber-band. Do not emulate iOS bounce; use the platform default.
- Nested scrolling behaves differently. A horizontal carousel inside a vertical scroll needs explicit gesture handling on Android more often than on iOS.
- Long lists need recycling. A large non-virtualised list drops frames on scroll and is a leading source of Android jank in RN apps.

## Profiling jank properly

Average fps hides the problem. One dropped frame in a 300 ms transition is what the user actually perceives.

1. **Enable the on-device developer overlay** for GPU rendering profiling to see per-frame cost live.
2. **Use a system trace** to attribute a dropped frame to a specific cause — layout, GPU, or a blocked main thread. This is the only tool that tells you *why*.
3. **Test with animator duration scale at 0.5× and 2×** to catch time-assumption bugs.
4. **Test on a real mid-range device**, in release mode. Debug builds are not representative — the JS bundle is unminified and the bridge is slower.
5. **Watch the pre-launch report** in Play Console; it runs on real hardware you do not own.
6. **Check Android vitals after release** — ANR rate is the metric that turns a motion problem into a distribution problem.

## Pre-ship motion checklist

1. Every animation runs on the UI thread — worklets or native driver, verified not assumed.
2. No animation of layout properties; transform and opacity only.
3. Reanimated Babel plugin last; Metro cache cleared after the change.
4. Reduce-motion and animator duration scale respected.
5. Tested at 60 Hz and at a high-refresh-rate panel.
6. Tested on a real mid-range Android device in release mode.
7. Long lists virtualised.
8. Predictive back adopted rather than overridden.
9. Platform overscroll used, not an iOS imitation.
10. System trace shows no sustained main-thread blocking.

## Verification

Before reporting Android motion work as done, point to:

- a system trace or frame-timing capture from a **real mid-range device in release mode**
- a screen recording at the device's actual refresh rate
- the Play pre-launch report showing no new ANRs

"It looks smooth on my phone" is not evidence. If profiling was not run, say so plainly and label the work unverified.
