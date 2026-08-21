---
name: expo-iap
description: In-app purchases and subscriptions in Expo / React Native — RevenueCat, StoreKit 2, Google Play Billing, restore-purchases, sandbox testing, and the App Store Guideline 3.1.1 rejection traps. Use whenever a mobile app needs to charge money for digital content. Triggers "in-app purchase", "IAP", "subscription in my app", "RevenueCat", "StoreKit", "Play Billing", "paywall wiring", "premium unlock", "restore purchases", "app subscription rejected", "can I use Stripe in my app".
version: 1.0.0
author: Karim
tags: [expo, react-native, iap, subscriptions, revenuecat, storekit, monetization, mobile]
---

# In-app purchases in Expo

**Stripe cannot sell digital content inside an iOS or Android app.** Apple's Guideline 3.1.1 and Google Play's Payments policy both require the platform's own billing for anything unlocked inside the app — subscriptions, premium features, credits, ad removal. Shipping a Stripe subscription screen is a guaranteed rejection, not a risk.

This is the most common reason a finished app fails review, because the paywall *design* work never surfaces it.

Related: `paywall-strategy-planner` (pick the model before wiring), `paywall-compliance-guardrails` (what Apple prohibits in the UI), `stripe-sdk` (web checkout — the correct tool on the other side of the line), `app-rejection-recovery`.

## Where the line actually falls

| Selling | Must use |
|---|---|
| Subscriptions, premium features, credits, ad-removal, digital content | **IAP** — no exceptions |
| Physical goods, real-world services (rides, food, tickets) | Stripe / any processor — IAP is *forbidden* here |
| Person-to-person services bought outside the app | Outside billing |
| Same subscription sold on your website | Stripe on web, IAP in app, same account |

The web/app split is legitimate and common: sell on your site with Stripe, entitle the same user in-app. What you cannot do is *link out* from inside the app to that web checkout for a digital good — that is the 3.1.1(a) "external purchase link" trap. Rules on link-outs have shifted repeatedly under litigation; check the current guideline text before relying on one.

## Pick the layer

| | Verified 2026-08-09 | Use when |
|---|---|---|
| **`react-native-purchases`** (RevenueCat) | **10.7.0**, peer `react-native >= 0.73.0`, published 3 days ago | **Default.** Cross-platform entitlements, receipt validation, restore, and subscription analytics you would otherwise build |
| `react-native-purchases-ui` | **10.7.0**, peer-pins `react-native-purchases` **exactly** `10.7.0` | RevenueCat's hosted paywall UI. The exact pin means these two upgrade together or not at all |
| `react-native-iap` | **16.2.0**, now requires `react-native-nitro-modules ^0.36.5` | Direct StoreKit / Play Billing, no third party. You own receipt validation |
| `expo-in-app-purchases` | 14.5.0 (`next`: 14.6.0) | **Avoid on SDK 57.** See below |

**`expo-in-app-purchases` is not in the SDK.** Verified against Expo 57's `bundledNativeModules.json` — 123 modules are pinned, and this is not one of them (`expo-store-review` is, at `~57.0.1`). So `npx expo install expo-in-app-purchases` does **not** pin an SDK-compatible version — it falls through to npm latest, which is the exact failure mode `npx expo install` exists to prevent.

## Install

```bash
npx expo install expo-build-properties
npm i react-native-purchases react-native-purchases-ui
npx expo prebuild
```

**Requires a dev client.** RevenueCat ships native code — it does not run in Expo Go. If purchases silently no-op, this is why.

## Minimal wiring

```tsx
import Purchases from 'react-native-purchases';

// once, at app start — before any paywall renders
await Purchases.configure({
  apiKey: Platform.OS === 'ios' ? IOS_KEY : ANDROID_KEY,
  appUserID: user?.id ?? null,        // null = anonymous, RevenueCat generates one
});

// read entitlement — this is the ONLY source of truth for "is the user premium"
const info = await Purchases.getCustomerInfo();
const isPro = info.entitlements.active['pro'] !== undefined;

// buy
const offerings = await Purchases.getOfferings();
const pkg = offerings.current?.availablePackages[0];
if (pkg) await Purchases.purchasePackage(pkg);
```

Never cache `isPro` in your own database as the authority. Subscriptions lapse, refund, and renew outside your app entirely — read the entitlement on launch and on foreground.

## Restore purchases is mandatory

Apple rejects apps that sell a non-consumable or subscription without a visible restore control.

```tsx
const info = await Purchases.restorePurchases();
```

Put it on the paywall itself, as a visible tappable control — not buried in settings, not a footnote in 10pt grey.

## Sandbox testing

- **iOS:** create a Sandbox Apple ID in App Store Connect → Users and Access. Sign in under *Settings → Developer → Sandbox Account*, **not** the main Apple ID. Sandbox subscription periods are compressed — a 1-month sub renews every 5 minutes and auto-cancels after 6 renewals.
- **Android:** upload a build to a closed testing track and add licence testers in Play Console. Local debug builds cannot purchase.
- Products must be **created and in "Ready to Submit"** before they appear. A missing product returns an empty offerings list, not an error — check `offerings.current` for null before blaming the SDK.

## Rejection traps

| Trap | Guideline |
|---|---|
| Stripe / web checkout for digital content | 3.1.1 |
| Link out to a web purchase page for a digital good | 3.1.1(a) |
| No restore-purchases control | 3.1.1 |
| Price, period, and renewal terms not shown *before* purchase | 3.1.2 |
| Subscription with no functional free tier and no clear value statement | 3.1.2(a) |
| Countdown timers / fake scarcity on the paywall | 4.3 + dark-pattern review |
| Blocking the app entirely until purchase, with no close control | 3.1.2(a) |

Run `paywall-compliance-guardrails` before submitting — it covers the UI half of this table.

## Failure table

| Symptom | Cause |
|---|---|
| Purchase does nothing, no error | running in Expo Go — needs a dev client |
| `offerings.current` is null | products not "Ready to Submit", or not attached to an Offering in RevenueCat |
| Works on iOS, silent on Android | testing a local debug build instead of a Play testing track |
| Entitlement flips off after reinstall | reading a cached local flag instead of `getCustomerInfo()` |
| Subscription renews every 5 minutes | expected — sandbox time compression |
| `react-native-purchases-ui` version conflict | it peer-pins `react-native-purchases` to an exact version; bump both together |
| Rejected on resubmit for the same reason | the paywall was fixed but the restore control is still not visible on the paywall screen |
