---
name: expo-splash-launch
description: Animated splash screen and launch-to-first-screen continuity for Expo and React Native — expo-splash-screen control, hiding at the right moment, animating the handoff, and killing the white flash. Use when building app launch experience, an animated splash, or fixing a jarring/flashing/slow start. Triggers: "splash screen", "launch screen", "app opening animation", "white flash on launch", "startup experience", "animated logo on open", "cold start feels slow".
version: 1.0.0
author: Karim
tags: [expo, react-native, splash, launch, motion, mobile]
---

# Expo Splash & Launch Continuity

The launch is the **first impression**, it plays on every single open, and it lands in App Store preview videos. It is also the most-skipped polish in the stack — most apps ship the static image and a white flash.

Authority: [[reference_mobile_motion_guide]]. Companion skills: `reanimated`, `moti`, `rn-screen-transitions`, `app-icon`.

## The model

There are **two** splash screens and confusing them causes most bugs:

1. **The native splash** — a static image the OS draws before JavaScript exists. Cannot be animated. Configured in `app.json`.
2. **Your JS splash** — a React component that mounts after the bundle loads and can animate anything.

Premium launch = native splash holds → JS mounts underneath it → you hide the native one → your component animates out into the first screen. The user perceives **one continuous motion**, not three stages.

## Setup

```bash
npx expo install expo-splash-screen
```

```json
// app.json — the native half
{
  "expo": {
    "plugins": [["expo-splash-screen", {
      "image": "./assets/splash-icon.png",
      "imageWidth": 200,
      "resizeMode": "contain",
      "backgroundColor": "#141218",
      "dark": { "backgroundColor": "#141218" }
    }]]
  }
}
```

**The `backgroundColor` must match your first screen's background.** This one line removes the white flash that makes apps feel cheap. Set the `dark` variant too or dark-mode users get a white blink.

## Hold, then hand off

```tsx
import { useEffect, useState, useCallback } from 'react';
import * as SplashScreen from 'expo-splash-screen';

// Module scope — before any component renders.
SplashScreen.preventAutoHideAsync();
SplashScreen.setOptions({ duration: 400, fade: true }); // native fade-out

export default function App() {
  const [ready, setReady] = useState(false);

  useEffect(() => {
    (async () => {
      try {
        await Promise.all([loadFonts(), restoreSession(), warmCache()]);
      } finally {
        setReady(true); // ALWAYS flip, even on failure
      }
    })();
  }, []);

  // Hide only once the first frame is actually painted.
  const onLayout = useCallback(async () => {
    if (ready) await SplashScreen.hideAsync();
  }, [ready]);

  if (!ready) return null;
  return <View style={{ flex: 1 }} onLayout={onLayout}>{/* first screen */}</View>;
}
```

Two non-obvious parts:

- **`preventAutoHideAsync()` must run at module scope**, not in an effect. In an effect it races the first frame and the splash flickers away early.
- **Hide in `onLayout`, not in the effect.** Hiding when state flips reveals an unpainted screen for a frame or two. `onLayout` fires after layout, so the handoff is seamless.

## Animating the handoff

Keep the native splash artwork and your JS component **visually identical**, then animate the JS one:

```tsx
import { MotiView } from 'moti';

<MotiView
  from={{ opacity: 1, scale: 1 }}
  animate={{ opacity: 0, scale: 1.08 }}
  transition={{ type: 'timing', duration: 420, delay: 80 }}
  pointerEvents="none"
  style={StyleSheet.absoluteFill}
>
  <LogoMark />
</MotiView>
```

The scale-up-and-fade reads as the logo "opening into" the app. A straight fade reads as a loading screen disappearing — technically the same, emotionally different.

Better still: make the logo **become** an element of the first screen (the header mark, the avatar). That is a shared-element transition — see `rn-screen-transitions`.

## Rules

- **Never block launch on the network.** Fonts and cached session, yes. A profile fetch, no — render the shell and fill it in. A splash that waits on a slow connection is how apps get uninstalled.
- **Always flip the ready flag in `finally`.** A rejected promise that skips `setReady(true)` leaves the user staring at the splash forever. This is the single most common way apps ship a hard hang.
- **Cap the hold.** If work exceeds ~2s, hide anyway and show a skeleton — `loading-states` covers the shell.
- **Honour reduced motion.** `useReducedMotion()` → cross-fade at duration 0 rather than scale.
- Test **cold start**, not Fast Refresh. Kill the app fully; a warm start hides every problem here.

## Failure table

| Symptom | Cause |
|---|---|
| White flash between splash and app | `backgroundColor` in `app.json` ≠ first screen bg; set the `dark` variant too |
| Splash disappears then reappears | `preventAutoHideAsync()` called inside an effect instead of module scope |
| Blank/unpainted frame after splash | hiding on state change instead of in `onLayout` |
| Stuck on splash forever | a rejected promise skipped `setReady(true)` — use `finally` |
| Logo jumps size at handoff | native `imageWidth` doesn't match the JS component's rendered size |
| Fine in dev, bad on device | tested warm start; always verify a true cold start |

## Verify it

Screen-record a **cold start on a real mid-range Android** and step through frames. You are looking for exactly two things: no colour flash at any boundary, and no size/position jump of the logo between the native and JS splash.
