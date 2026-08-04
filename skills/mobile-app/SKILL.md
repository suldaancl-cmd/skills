---
name: mobile-app
description: The entry point for building or extending an iOS + Android app with Expo / React Native — one TypeScript codebase that ships to both stores. Orchestrates the whole flow (requirements → phased plan → one-phase-at-a-time build → ship) and routes to the right specialist skills for navigation, auth, design, Arabic/RTL, and store release. Use this whenever the user wants to build a mobile app, add a feature to a React Native / Expo app, says "make an iOS and Android app", "build a mobile app", "add a screen", "ship to the App Store / Play Store", or starts any cross-platform mobile work. Start here and it will pull in everything else.
---

# Mobile App (Expo / React Native)

The orchestrator for cross-platform mobile work. One Expo/React Native codebase ships to **both iOS and Android**, reuses the React knowledge you already have, and supports Arabic/RTL cleanly — which is why it's the default path here rather than two native codebases.

This skill doesn't do everything itself; it runs the process and routes each concern to the specialist skill that owns it. Think of it as the general contractor.

## The flow

For anything bigger than a one-line fix, run this sequence — it's the same discipline that lets a solo dev ship fast without shipping bugs:

1. **Nail requirements** → invoke **`grill-me`**. Let it interrogate the feature until the ambiguity is gone. Don't skip this because the idea "seems obvious" — the gaps are where rework hides.
2. **Plan in phases** → invoke **`phased-plan`**. Break the feature into small, individually testable slices, written to `plans/<feature>.md`.
3. **Build one phase at a time** → invoke **`phased-implementation`**. Build a phase, prove it on a simulator/device, stop for review, then continue. One phase per PR.
4. **Run & debug the app** → use **`argent-react-native-app-workflow`** for starting Metro, iOS simulator, Android emulator, and diagnosing build/runtime errors.
5. **Ship to the stores** → invoke **`expo-eas-ship`** for EAS build, TestFlight, App Store, and Play Store submission plus OTA updates.

For a trivial fix, skip straight to the change — the process is for features, not typos.

## Who owns what

Reach for these as each concern comes up rather than reinventing them:

| Concern | Skill |
|---|---|
| App architecture, navigation, state, offline-first | `react-native-architecture` |
| Implementation, native modules, list perf, platform-specific code | `react-native-expert` |
| Run / build / debug (Metro, simulator, emulator, logcat) | `argent-react-native-app-workflow` |
| Auth (Clerk) | `clerk-expo` |
| Auth / DB (Supabase) | `supabase-stack`, `supabase-postgres-best-practices` |
| Design system + UI (lock this FIRST) | `ui-ux-pro-max`, then `frontend-design`, `design-md-expo` |
| iOS platform conventions | `apple-hig` |
| Arabic / RTL layout | `rtl-arabic-i18n` |
| Store build & release | `expo-eas-ship` |

Mobile in-app purchases: Expo apps typically use **RevenueCat** (wraps App Store + Play billing) rather than Stripe, which is web-only for card checkout. Flag this when monetization comes up.

Mobile E2E testing has no dedicated skill in this library yet — **Maestro** is the lightest option for RN flow tests. Call this gap out if the user wants automated UI tests, rather than pretending coverage exists.

## Guardrails

These are Karim's standing rules — honor them without being reminded:

- **Design before code.** For any user-facing UI, lock the colors + fonts deck first (`ui-ux-pro-max`) and get a pick before building. No default fonts, no ad-hoc palettes. Screens built before the system is locked get rebuilt.
- **Arabic-first for user-facing copy.** UI strings, onboarding, notifications → Arabic (with proper RTL via `rtl-arabic-i18n`). Code, identifiers, comments, and infra stay English. Never mix directions mid-block.
- **One phase per PR.** Never combine phases (see `phased-implementation`). Keeps reviews real.
- **Never write to production data.** Read-only against prod, through the proper read-only MCP. Any prod mutation waits for explicit human go.
- **Defer architectural & schema decisions to the human owner.** Database migrations, new tables/columns, auth model, and anything hard to reverse are not yours to decide silently — write them into the plan's *Open questions for review* and let Karim answer via `grill-me`.
- **Editing an existing app: merge, don't replace.** Add to what's there; don't rewrite working code or wipe existing screens because a fresh version felt cleaner.

## Prove it

Before calling any feature done, point to what proves it: a screenshot from the simulator, a passing test, the recorded flow, or the EAS build URL. "It should work" is not evidence. If something isn't verified, say so plainly.
