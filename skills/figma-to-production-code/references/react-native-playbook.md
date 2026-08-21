# Expo and React Native Playbook

## Repository-first decisions

- Read the existing Expo SDK and React Native versions before selecting APIs.
- Reuse the existing router/navigation, styling, component, data, and localization stack.
- Prefer packages already installed and working.
- Verify compatibility against official documentation when versions matter.

## Layout

- Respect safe areas and system UI.
- Build flex/auto-sizing layouts rather than scaling a 390x844 canvas.
- Keep atmospheric art in an anchored `ImageBackground`-style layer only when appropriate.
- Keep buttons, text, inputs, lists, navigation, and status content semantic.
- Test small screens, the reference device, and a larger phone/tablet policy.

## Assets

- Use optimized raster formats supported by the project for complex art.
- Use SVG or native icon components for scalable icons when supported.
- Provide explicit dimensions/aspect ratios to avoid layout shift.
- Preload critical hero assets and avoid decoding oversized images.
- Keep static fallbacks for Rive/Lottie/3D assets.

## Motion

- Use Reanimated for component, route, gesture-linked, and sensor-linked motion when it is the established stack.
- Use Gesture Handler for native gesture recognition.
- Keep continuous animation values outside React render state.
- Cancel animations and subscriptions on unmount/background.
- Respect OS reduced-motion preferences.

## Sensors and audio

- Define permission request, denial, unavailable hardware, stale data, and calibration states.
- Smooth noisy sensor values and use shortest-path angle interpolation.
- Do not imply precision beyond the sensor/data source.
- For audio, separate permission, capture, visualization, upload/processing, and result states.

## Accessibility

- Provide roles, labels, hints only when useful, state announcements, and logical focus order.
- Keep touch targets appropriate for the platform.
- Support dynamic text where the product permits it.
- Never communicate state by color or motion alone.

## Verification

- Run on a real device or representative simulator/emulator when available.
- Verify Expo Go versus development-build compatibility before promising a runtime path.
- Capture screenshots at known dimensions and record device/OS/build metadata.

