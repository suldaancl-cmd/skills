---
name: play-console-mastery
description: Use when shipping an Android app to Google Play — creating the developer account, passing the 12-tester closed-testing gate, choosing release tracks, filling the Data Safety form, meeting the annual target-API and Play Billing deadlines, running staged rollouts, or fixing a Play policy rejection. Covers the operational surface that Apple-centric release skills miss entirely — Play Console account types and D-U-N-S, internal/closed/open/production tracks, pre-launch reports, Play App Signing and AAB, Play Integrity, Android vitals ANR and crash thresholds, permissions declaration forms, and the halt-rollout procedure. Reach for this before writing any Play listing or clicking Publish.
---

# Play Console Mastery

Google Play is not "the App Store with different colours". It has its own gates, its own annual deadlines, and its own ways to silently stop showing your app to users. This skill is the operational map.

**Companion skills.** Rejections and appeals for BOTH stores → `store-rejection-defense`. Play-side marketing levers (listing experiments, custom listings, pre-registration, LiveOps) → `play-store-growth`. Expo/EAS submission mechanics → `eas-app-stores`, `expo-eas-ship`.

## Hard rule — the two gates that stop new apps

Most first-time Play launches die on one of these. Check both before writing a line of listing copy.

### Gate 1 — the closed-testing requirement (personal accounts)

Personal developer accounts created from **13 Nov 2023 onward** must run a closed test with **at least 12 testers who stay opted in continuously for 14 days** before they can apply for production access.

What trips people up:

- It is **12 continuously opted-in testers**, not 12 installs and not 12 people who tried it once. A tester who opts out resets the count.
- The 14 days are **continuous**. Drop below 12 and the clock restarts.
- The test must be on a **closed** track. Internal testing does not satisfy it.
- After the 14 days you still have to **apply** for production access and answer questions about what you learned. A human reviews it and can refuse.
- **Organization accounts are exempt.** Registering as an organization avoids this gate entirely — but that needs a D-U-N-S number, which itself takes time to obtain.

Plan for this as a **multi-week** lead time, not a launch-day step.

### Gate 2 — the annual target API level deadline

Google raises the minimum `targetSdkVersion` every year, with the deadline on or around **31 August**.

- New apps and updates must target an API level released within roughly the last year.
- Existing apps that fall behind stop being discoverable to new users on newer Android versions. The app is not removed — it quietly stops appearing. Installs die and nothing tells you why.
- An extension request form exists, but it buys months, not years.

**Verify the current required level in Play Console before every release cycle.** This number changes annually, so any value hardcoded in a document is stale by definition.

## Account setup

| Item | Detail |
|---|---|
| Registration fee | One-time, per developer account |
| Personal account | Identity verification required; subject to the 12-tester gate |
| Organization account | Requires a **D-U-N-S number**; exempt from the 12-tester gate |
| Payments profile | Separate from the developer account; required before selling anything |
| Merchant account | Needed for paid apps and in-app products |

Choosing personal to "move faster" is usually the slower path — it buys the closed-testing gate. If a company exists or can exist, register as an organization and start the D-U-N-S request immediately, since that is the long pole.

## Release tracks

Four tracks, ordered by exposure:

| Track | Testers | Review speed | Use it for |
|---|---|---|---|
| **Internal testing** | Up to 100, by email | Fastest — usually minutes | Smoke-testing a build, sharing with the team |
| **Closed testing** | Email lists or Google Groups | Normal review | The 12-tester gate; real beta feedback |
| **Open testing** | Anyone with the link | Normal review | Public beta, scale testing, early reviews |
| **Production** | Everyone | Slowest, most scrutiny | Launch |

Notes that matter:

- Internal testing skips most review. Do **not** read a fast internal approval as evidence that production will pass.
- A build promoted between tracks keeps its version code. Version codes must strictly increase and are never reusable, even for a deleted release.
- Tracks can run in parallel with different builds.

## The build artifact

- **Android App Bundle (`.aab`) is mandatory for new apps.** Bare APKs are not accepted.
- **Play App Signing** holds the app signing key; you keep an upload key. Losing the upload key is recoverable through support. Losing the app signing key when you opted out of Play App Signing is not — the app can never be updated again.
- Back up the upload keystore and its passwords somewhere that survives a laptop dying. This is the single most common irrecoverable Android mistake.
- The **pre-launch report** runs the build on real devices in a test lab and surfaces crashes, ANRs, accessibility issues, and security findings before users see them. Read it on every release. It is free signal that most developers ignore.

## The Data Safety form

A separate declaration from the privacy policy, and Play checks the two against each other and against the actual code.

Declare, per data type — collected, shared, whether collection is optional, whether it is encrypted in transit, and whether users can request deletion.

Where people get rejected:

- **An SDK collects data you forgot about.** Analytics, ad, crash, and attribution SDKs all collect. The declaration must cover what the *dependencies* do, not only first-party code.
- **The form contradicts the privacy policy.** Both are read. A mismatch is a policy rejection.
- **Claiming no collection while requesting an advertising ID.** The ad-ID declaration is separate and cross-checked.
- **Account deletion.** If users can create an account, you must offer a way to request deletion — including a **web-accessible** route, not only in-app.

Re-audit this form every time a dependency is added.

## Permissions and declaration forms

Sensitive permissions require an in-console declaration explaining why, and most require the permission to be *core* to the app:

| Permission / feature | Why it is gated |
|---|---|
| `QUERY_ALL_PACKAGES` | Reveals every installed app; needs a strong justification |
| `MANAGE_EXTERNAL_STORAGE` | Broad filesystem access; use scoped storage or the photo picker |
| SMS / Call Log | Very narrow list of eligible app types |
| `AccessibilityService` | Must genuinely serve users with disabilities |
| Foreground service types | Android 14+ requires a declared type and a Play declaration |
| Background location | Must justify why foreground location is insufficient |

Default answer: **remove the permission**. Almost every declaration rejection is fixed faster by deleting the permission than by arguing for it. The photo picker replaces broad storage access in most apps.

## Android vitals — the silent ranking penalty

Play tracks per-app quality metrics and applies **bad-behaviour thresholds**. Cross them and the app loses discoverability in Play search and recommendations. No email, no rejection — just fewer installs.

The two that matter most:

- **User-perceived ANR rate** — an ANR while the user is actively engaged
- **User-perceived crash rate**

Both are measured against daily active users, and the thresholds are low single-digit fractions of a percent. **Read the current thresholds in the Android vitals dashboard** rather than trusting a written-down number, since Google revises them.

Practical consequences for a React Native or Expo app:

- Long synchronous work on the main thread causes ANRs, not just jank. Move it off.
- A crash on one specific OEM Android skin still counts. Test on a real mid-range device, not only a Pixel emulator.
- Vitals are computed on **production** traffic. A clean internal test proves nothing here.

## Play Integrity

`SafetyNet Attestation` is retired. **Play Integrity API** is the current mechanism for verifying that the app binary, the device, and the Play install are genuine.

Reach for it when there is something to lose — in-app purchases, a rewards economy, exam or medical content, anything where a modified client costs money. Verdicts must be verified **on the server**. A client-side integrity check is decoration.

## Staged rollout

Production releases can go to a percentage of users. This is the safety net, so use it.

- Typical ladder — start small (1–5%), watch vitals for 24 hours, then step up.
- The percentage can be **increased** or the rollout **halted**. It cannot be decreased.
- **Halting stops new users from getting the bad build but does not roll back users who already have it.** The only real fix is shipping a higher version code with the fix and rolling that out.
- Because of that, the version shipped at 1% must already be one you are willing to have permanently on some devices.

## Release checklist

Run this before every production submission:

1. Version code strictly greater than every previous release, including deleted ones.
2. Targeting the currently required API level — checked in console today, not from memory.
3. Play Billing Library at or above the current required version if anything is sold.
4. Data Safety form re-audited against the current dependency list.
5. Privacy policy URL live, reachable, and matching the form.
6. Account deletion route available in-app **and** on the web, if accounts exist.
7. Content rating questionnaire completed; ads declaration accurate.
8. App access instructions with **working demo credentials** if any screen is behind a login.
9. Pre-launch report read; crashes and ANRs triaged.
10. Screenshots and feature graphic meet current size requirements.
11. Staged rollout percentage set, not 100%.
12. Upload keystore backed up off-machine.

## Verification

Before reporting a Play release as done, point to:

- the Play Console release dashboard showing the track and rollout percentage
- the pre-launch report with no unresolved crashes
- the Data Safety form status as complete

If a numeric requirement in this skill differs from what Play Console shows, **the console is right and this document is stale** — Google revises these annually.
