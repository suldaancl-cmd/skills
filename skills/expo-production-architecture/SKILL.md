---
name: expo-production-architecture
description: Design, implement, or review a production Expo and React Native application architecture, including Expo Router, development builds, native capabilities, data flow, and EAS environments. Use for substantial Expo features or architecture; not for backend-only work.
---

# Expo production architecture

Build a real mobile product that remains testable on iOS and Android and can be submitted to stores.

## Establish the real environment

- Inspect `package.json`, Expo config, lockfile, native directories, EAS profiles, routing tree, and applicable repository instructions.
- Pin decisions to the installed Expo SDK and React Native versions. Verify version-sensitive APIs in official Expo or library documentation.
- Determine whether the project uses managed prebuild, checked-in native projects, Expo Go, or a development build. Do not assume Expo Go supports every native dependency.
- Preserve an existing navigation, styling, state, auth, or backend choice unless change is required by the task.

## Assign responsibilities

- **Expo client:** presentation, device capabilities, local interaction state, authenticated requests, cached server state, and user-visible progress.
- **Trusted API/backend:** secrets, authorization, provider calls, billing, moderation, webhooks, and durable job creation.
- **Background worker:** long-running, retryable, resource-heavy, or provider-asynchronous work.
- **System of record:** durable users, projects, entitlements, jobs, results, and audit state.

Expo API Routes or server functions can handle short request/response and streaming work. Do not use them as the sole runtime for long video, website generation, or agent workflows that must survive client closure or function timeout.

## Structure navigation and state

- Use route groups to separate authentication, onboarding, and signed-in flows without leaking internal grouping into URLs.
- Protect sensitive screens in both navigation and backend authorization; a hidden route is not an access-control boundary.
- Keep URL/route parameters serializable and stable. Store large or sensitive state outside navigation params.
- Distinguish local UI state, cached server state, and durable backend state. Avoid one global store for everything.
- Load `$tanstack-query-mobile` when TanStack Query owns cached server state, mutations, offline behavior, or Realtime cache reconciliation.
- Design deep links, back behavior, interrupted onboarding, push-notification entry, and restored sessions deliberately.

## Native and platform behavior

- Use a development build when native modules, config plugins, entitlements, app extensions, or platform testing require it.
- Verify permissions and denial/recovery flows on device.
- Keep iOS and Android behavior intentionally equivalent, not visually forced into false sameness.
- Plan safe areas, keyboard, status/navigation bars, dynamic type, RTL, accessibility, offline use, and lifecycle transitions.

## Environment and release boundaries

- Only public identifiers and publishable client keys may be embedded in the app.
- Treat any value consumed by client code as extractable, regardless of EAS visibility labels.
- Separate development, preview, and production projects, URLs, signing, bundle identifiers, and telemetry where practical.
- Make build-time configuration explicit and validate the effective config before building.

Read [references/expo-architecture-record.md](references/expo-architecture-record.md) for a substantial implementation or review. Verify with the repository's existing checks plus at least one real-device path when possible.
