---
name: app-store-release-operations
description: Prepare, audit, build, beta-test, and submit an Expo mobile app to Apple App Store and Google Play, including metadata, privacy, AI-content controls, payments, review access, and EAS release configuration. Use for release readiness or submission; not for feature implementation unrelated to review.
---

# App-store release operations

Move a verified release candidate through beta and store review without hiding product behavior from reviewers.

## Establish current requirements

- Inspect the installed Expo/EAS versions, app config, identifiers, signing setup, build profiles, native permissions, privacy manifests, entitlements, update strategy, and existing store records.
- Verify current Apple, Google, and Expo requirements from official sources before making policy or command claims. Record the access date for review-sensitive guidance.
- Preserve bundle/package identifiers and signing history. Never create a second store listing or rotate signing material merely to bypass a configuration problem.

## Preflight the product

- Production backend, worker, provider integrations, legal pages, support contact, and deletion flow must be available to reviewers.
- Provide a working review account and exact steps for gated or AI functionality; never put passwords or secrets in public metadata.
- Ensure login options satisfy current platform requirements.
- If accounts can be created, implement the platform-required in-app deletion path and explain retained data.
- Request only permissions needed by visible features, with accurate purpose strings and denial recovery.
- Confirm age rating, content rights, export/compliance declarations, privacy/data-safety answers, tracking choices, and SDK disclosures match actual behavior.

## AI-specific review

- Explain what AI generates, which providers/processors receive data, and what controls are available.
- Add reporting/flagging and moderation appropriate to generated or shared content.
- Prevent disallowed, deceptive, or harmful output and provide a support/escalation route.
- Do not download executable code that changes native app functionality in a way forbidden by store policy.
- Keep long-running agents on the backend; the app submits work and retrieves progress/results.

## Payments and entitlement

- Determine whether the product sells digital functionality/content, physical goods/services, or an external business service under current store rules.
- Use the required in-app billing system where applicable. Validate purchase on the server and make entitlement idempotent and restorable.
- Test subscription state, grace/hold/revocation, family/account changes where relevant, refund, and cross-device restore.
- Keep web and mobile pricing/entitlements consistent with the approved product strategy.

## Build and beta

- Use the repository's supported EAS CLI and documented commands; discover flags rather than guessing.
- Separate development, preview/internal, and production profiles.
- Validate effective Expo config, version/build numbers, icons/splash, associated domains/deep links, notification credentials, and environment selection.
- Distribute through TestFlight and Google internal/closed testing before production.
- Test the exact store build against production-like services on real devices and collect the evidence defined by the quality skill.

## Submission package

Use [references/store-submission-record.md](references/store-submission-record.md). Prepare:

- Localized name, subtitle/short description, full description, keywords where supported, category, support/privacy URLs, and release notes.
- Screenshots that show the real app and match current device requirements.
- Review notes, demo account, special hardware/location instructions, and explanation of AI/payment behavior.
- Rollout, monitoring, feature-disable, and support plan.

Submitting, releasing, changing public metadata, or altering store credentials is an external side effect. Prepare everything first and obtain the user's confirmation immediately before the final action unless they already authorized that exact action in the active workflow.
