---
name: expo-eas-ship
description: Build, sign, and submit an Expo / React Native app to the Apple App Store and Google Play using EAS (Expo Application Services), plus over-the-air updates. Covers eas.json build profiles, credentials and signing, `eas build`, `eas submit`, TestFlight and Play internal testing, `eas update` for OTA, and app.json/app.config store metadata. Use this whenever the user wants to ship, release, distribute, or submit a mobile app, get it on TestFlight or the stores, set up app signing, push an OTA update, or says "get this on the App Store / Play Store", "make a build", "eas build", or "release the app".
---

# Expo EAS Ship

Get an Expo/React Native app from source to the App Store and Google Play, and push updates after. This is the "last mile" that turns a working simulator app into something real users install. It's fiddly the first time (certificates, provisioning, store metadata), so work through it in order and verify each gate before moving on.

## Prerequisites — check first

- `eas-cli` available (`npx eas-cli --version`); logged in (`eas whoami`, else `eas login`).
- An **Apple Developer account** ($99/yr) for iOS, and a **Google Play Developer account** ($25 once) for Android. You cannot ship to the stores without these — surface it early if the user doesn't have them.
- `app.json` / `app.config.ts` has a stable **iOS bundle identifier** and **Android package name** (reverse-DNS, e.g. `ai.yorby.app`). These are permanent once published — get them right before the first submit.

## Step 1 — Configure build profiles (`eas.json`)

Run `eas build:configure` to scaffold, then set three profiles. The reason for three: you want fast internal builds, shareable test builds, and store builds to be distinct.

```json
{
  "build": {
    "development": { "developmentClient": true, "distribution": "internal" },
    "preview":     { "distribution": "internal" },
    "production":  { "autoIncrement": true }
  },
  "submit": { "production": {} }
}
```

- **development** — dev client for daily work on device.
- **preview** — internal distribution (ad-hoc / internal track) so testers install without the stores.
- **production** — store-ready; `autoIncrement` bumps build numbers so submissions don't collide.

## Step 2 — Credentials & signing

Let EAS manage credentials unless the user needs otherwise — it generates and stores the iOS distribution cert + provisioning profile and the Android keystore for you. **The Android keystore is unrecoverable if lost and locks you out of updating your own app** — after the first build, back it up (`eas credentials` → export) somewhere safe. Say this out loud; it's the single most expensive mistake to make here.

## Step 3 — Build

```bash
eas build --platform ios --profile production
eas build --platform android --profile production
# or both: --platform all
```

Builds run on EAS servers and return a build-details URL. **That URL is your proof the build succeeded** — capture it; don't claim a build worked without it. iOS builds need the Apple account linked (EAS walks you through it on first run).

## Step 4 — Submit to the stores

```bash
eas submit --platform ios --profile production --latest
eas submit --platform android --profile production --latest
```

- **iOS** → lands in **App Store Connect → TestFlight** first. Internal testers can install within minutes; external testing and App Store review take longer. First-ever submit also needs the app record created in App Store Connect (name, bundle id, privacy details).
- **Android** → lands on the **Play Console internal testing** track by default. Promote internal → closed → production in the Play Console. First submit needs the app created in Play Console + the store listing filled in.

Store review is a human gate on both platforms — plan for a review turnaround, and know that first submissions get scrutinized harder (privacy labels, permission justifications, login demo credentials).

## Step 5 — OTA updates (`eas update`)

For JS-only changes (no native module changes), skip a full store round-trip:

```bash
eas update --branch production --message "fix: <what changed>"
```

This ships the new JS bundle to installed apps over the air. **Native changes** (new native module, SDK upgrade, permission change, icon/splash) still require a fresh `eas build` + submit — OTA can't change native code. Getting this boundary wrong ships a broken update, so check whether the change touched native before reaching for `eas update`.

## Store metadata

Bundle id / package name, version, app icon, splash, and permission usage strings live in `app.json` / `app.config.ts`. iOS requires a plain-language reason for each sensitive permission (`NSCameraUsageDescription`, etc.) or review rejects the build. `eas metadata` can manage store listing text as code if the user wants it version-controlled.

## Verify

A ship is done when you can point to: the **EAS build URL** (green), the **submission** landing in TestFlight / Play internal testing, and — for an update — the `eas update` group id. If any step isn't confirmed, report exactly which gate is still pending rather than implying the app is live.
