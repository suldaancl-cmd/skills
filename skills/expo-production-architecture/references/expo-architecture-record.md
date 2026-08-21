# Expo architecture record

## Runtime facts

- Expo SDK / React Native:
- Managed prebuild or checked-in native projects:
- Expo Go or development build:
- Router and navigation pattern:
- Styling system:
- State and query libraries:
- Auth/session provider:
- API/backend:
- EAS profiles:

## Responsibility map

| Concern | Client | Trusted API | Worker | System of record |
|---|---|---|---|---|
| Authentication | | | | |
| AI request | | | | |
| Long-running job | | | | |
| Billing/entitlement | | | | |
| Files | | | | |
| Notifications | | | | |

## Route map

For each flow identify entry points, protection, back behavior, deep links, restore behavior, and failure fallback.

## Native capability record

For every native dependency record supported platforms, config plugin/native edits, permission copy, Expo Go compatibility, development-build requirement, and store entitlement.

## Verification matrix

- Cold start signed out/signed in.
- Interrupted onboarding.
- Offline and slow network.
- Small/large iOS device.
- Representative Android device.
- RTL and dynamic text.
- Permission allowed/denied/revoked.
- Background/foreground restoration.
