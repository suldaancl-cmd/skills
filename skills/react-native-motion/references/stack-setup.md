# Stack setup — versions, install, and the one gotcha that wastes an hour

Install everything through Expo so versions stay SDK-compatible:

```bash
# Core — ships in the Expo SDK, but pin via expo install:
npx expo install react-native-reanimated react-native-gesture-handler

# Declarative layer + graphics + designer motion (optional, per need):
npx expo install moti @shopify/react-native-skia
npx expo install lottie-react-native
npm i rive-react-native            # Rive isn't in the Expo install list
npx expo install expo-haptics expo-blur expo-linear-gradient
```

## The Reanimated Babel plugin gotcha

`react-native-reanimated/plugin` **must be the last entry** in `babel.config.js` plugins. If it isn't last (or is missing), worklets silently fail — animations either don't run or throw "Reanimated 2 failed to create a worklet." This is the single most common lost hour in RN motion.

```js
// babel.config.js
module.exports = function (api) {
  api.cache(true);
  return {
    presets: ['babel-preset-expo'],
    plugins: [
      // ...all your other plugins...
      'react-native-reanimated/plugin', // <-- ALWAYS LAST
    ],
  };
};
```

After changing Babel config, restart Metro with `npx expo start --clear` — the transform cache holds the old config otherwise.

## Provider wiring

- **Gesture Handler** needs the root wrapped once: `import { GestureHandlerRootView }` and wrap the app root (`<GestureHandlerRootView style={{ flex: 1 }}>`). Expo Router does this in the root layout.
- **Reanimated** needs no provider, but shared-element transitions need the screens rendered under a Reanimated-aware navigator (native-stack).

## Version notes (Expo SDK 52+/2026)

- **Reanimated 3.x** is the stable baseline; **4.x** (new architecture / CSS-like animations) is landing — check the installed major before using 4-only APIs (`css`-style transitions). Prefer the shared-value API in this skill; it works on both.
- **Moti** tracks Reanimated majors — if you bump Reanimated, bump Moti together.
- New Architecture (Fabric) is default on recent Expo SDKs; Reanimated 3.6+/4 and Skia support it. If you see native crashes on animation, confirm all four (Reanimated, Gesture Handler, Skia, Moti) are on New-Arch-compatible versions.
