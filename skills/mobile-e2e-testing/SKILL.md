---
name: mobile-e2e-testing
description: Use when a React Native or Expo app needs an automated test loop before shipping — choosing between Maestro and Detox, writing flows that survive a UI refactor, wiring tests into EAS builds and CI, building a device matrix that catches Android-only failures, and testing the paths that reviewers actually break (cold start, login, purchase, permissions, offline). Reach for this when the ask is regression safety, flaky-test triage, or proving a build works before submission, rather than unit-testing business logic.
---

# Mobile E2E Testing

Unit tests prove functions work. They do not prove the app launches, the login screen accepts a password, or the paywall restores a purchase — which are exactly the paths that get a submission rejected. This skill is the end-to-end loop.

**Companion skills.** Pre-submission audit → `store-submission-gate`. Android-specific frame and ANR profiling → `android-motion-system`. Build and submit mechanics → `eas-app-stores`, `expo-eas-ship`.

## Choosing the runner

| | **Maestro** | **Detox** |
|---|---|---|
| Test format | Declarative YAML flows | JavaScript with an assertion API |
| Setup cost | Low — runs against an installed build | Higher — needs native build config |
| Selector style | Text and accessibility labels, tolerant | Test IDs, strict |
| Synchronisation | Built-in waiting and retry | Deterministic — waits for the app to be idle |
| Flakiness | More forgiving, occasionally too forgiving | Less flaky when configured, harder to configure |
| Best for | Most apps, fast coverage, non-specialist authors | Large suites, complex async, teams with native expertise |

**Default recommendation: start with Maestro.** It gets a working suite in an afternoon, runs against the same binary you submit, and does not require touching native build configuration. Move to Detox only when the suite is large enough that flakiness costs more than setup would have.

Do not run both. Two suites means two sets of flakes and neither gets maintained.

## What to test — in priority order

Coverage effort should follow rejection and revenue risk, not code structure.

1. **Cold start.** Fresh install, first launch, no cached state. The single most common real-world failure and the one reviewers hit first.
2. **Login and signup**, including a wrong password and a network failure.
3. **The purchase path**, including restore. Money paths break silently and cost revenue directly.
4. **Permission flows** — granted, denied, and denied-then-changed-in-settings. Denial is the untested branch that crashes.
5. **The primary value flow.** Whatever the app is actually for, end to end.
6. **Offline and flaky network.** Airplane mode mid-request.
7. **Deep links** and notification taps opening the right screen from a cold start.
8. **Logout and account deletion**, since deletion is store-mandated and rarely tested.

Everything beyond this is a bonus. Eight reliable flows beat forty flaky ones.

## Writing flows that survive a refactor

The reason E2E suites get abandoned is that every UI change breaks them. Avoid that by construction:

- **Select by accessibility label or test ID, never by position.** An index-based selector breaks the moment a element is inserted.
- **Add test IDs deliberately** to the elements tests depend on, and treat them as an API — renaming one is a breaking change.
- **Never assert on exact copy** unless the copy is the thing under test. Marketing text changes weekly.
- **Never assert on styling.** That is a visual-regression concern, not a flow concern.
- **One flow, one intent.** A flow that tests login and checkout gives an ambiguous failure.
- **Reset state between flows.** Tests that depend on each other fail in a confusing order and cannot run in parallel.
- **No fixed sleeps.** A hardcoded wait is a flake waiting for a slower CI machine. Wait for a condition instead.

## Test data

- Use a **dedicated test account** per environment, never a real user account.
- Seed deterministic data. A test asserting "3 items" against a shared mutable account will fail eventually.
- For purchases, use the platform sandbox — StoreKit test configuration on iOS, Play license testing on Android. Never test against live billing.
- Store credentials in CI secrets, not in the flow files. Flow files are committed.

## The device matrix

The whole point of E2E is catching what one developer's phone hides.

| Slot | Why |
|---|---|
| **Oldest supported iOS** | Deprecated APIs and layout differences |
| **Newest iOS** | New system behaviours and permission prompts |
| **Small screen** | Layout overflow, cut-off buttons, unreachable CTAs |
| **Mid-range Android** | Performance, ANR, and jank — the most valuable single slot |
| **Newest Android** | Permission model and predictive-back changes |
| **Tablet / large screen** | Only if the app claims tablet support |

If only one extra device can be afforded, make it a **real mid-range Android**. It catches more than any simulator.

Simulators and emulators are fine for logic-level flows. They are not evidence for performance, camera, biometrics, push notifications, or in-app purchase.

## CI wiring

The loop that actually holds:

1. **On every pull request** — run the smoke subset: cold start plus the primary value flow. Must finish in a few minutes or people will bypass it.
2. **On merge to main** — run the full suite.
3. **Before every submission** — run the full suite against the **exact binary being submitted**, not a fresh build from the same commit. Build config differences are real.
4. **Nightly** — run the full matrix, including the slow devices.

Rules that keep it useful:

- A failing E2E run **blocks the merge**. A non-blocking suite is decoration and will rot within a month.
- Record video and capture screenshots on failure. A failure log with no visual is nearly useless for UI tests.
- Keep the smoke subset genuinely fast. Slow required checks get disabled.

## Flake triage

A flaky test is worse than no test — it teaches the team to ignore red.

When one flakes, classify it before touching it:

| Symptom | Usual cause | Fix |
|---|---|---|
| Passes locally, fails in CI | Timing; CI is slower | Replace sleeps with condition waits |
| Fails only on the first run | Cold-start or permission dialog not handled | Handle the dialog explicitly |
| Fails intermittently at the same step | Race between navigation and assertion | Wait for the destination, not a duration |
| Fails only on Android | Real platform difference | Do not paper over it — this is a genuine bug |
| Fails after unrelated changes | Selector was positional or copy-based | Move to a test ID |

**A test that fails only on Android is usually reporting a real Android bug.** Quarantining it hides the exact class of defect the suite exists to catch.

Quarantine policy: a flaky test may be quarantined for one sprint with an owner and a deadline. After that it is fixed or deleted. Permanently skipped tests are lies in the repository.

## Pre-submission run

Before submitting a build:

1. Full suite green against the exact submission binary.
2. Cold start verified on a real mid-range Android in release mode.
3. Purchase and restore verified in sandbox on both platforms.
4. Permission-denied branch verified, not only the granted path.
5. Demo credentials used by the tests confirmed to be the ones given to reviewers.
6. Failure artefacts from the last red run reviewed and closed out.

## Verification

Before reporting the test loop as done, point to:

- the CI run URL with a green full suite and its timestamp
- the device list the run actually covered
- a recorded video of the primary value flow passing on a real Android device

A suite that has never failed has usually never been checked for false passes. Break one assertion deliberately once and confirm the suite goes red — an E2E suite that cannot fail is not testing anything.
