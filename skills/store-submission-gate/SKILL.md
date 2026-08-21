---
name: store-submission-gate
description: Use BEFORE submitting an iOS or Android app to review — a pre-flight audit that catches the rejection causes while they are still cheap to fix. Covers the guidelines most first submissions trip over, including Apple minimum functionality for wrapped web apps, spam and duplicate-app rules, login-services parity, mandatory in-app account deletion, privacy manifests and required-reason APIs, permission purpose strings, and the Play policy equivalents. Run it as a gate on the build and metadata, not after a rejection arrives. For recovering from a rejection that already happened, use app-rejection-recovery instead.
---

# Store Submission Gate

A rejection costs days of calendar time and resets review priority. Almost all of them are predictable. This skill is the pre-flight audit — run it on the build and the metadata **before** hitting Submit.

**Scope boundary.** This is prevention. If a rejection has already arrived, `app-rejection-recovery` has the taxonomy, the Resolution Center template, and the appeal-vs-fix decision. Play operational gates → `play-console-mastery`.

## How to run this

Go through every section. Each item is either **PASS**, **FAIL**, or **N/A** — no "probably fine". Anything that is FAIL blocks submission. Record the result; that record is the evidence that the gate ran.

---

## 1. Completeness — the single largest rejection category

Apple rejects more submissions under **Guideline 2.1 App Completeness** than any other rule, and Play has an equivalent broken-functionality policy.

- [ ] App launches without crashing on a **clean install** on a real device — not a warm simulator with cached state
- [ ] No placeholder text, lorem ipsum, "TODO", or stock images left in any screen
- [ ] No dead buttons or links to unbuilt screens. If a feature is not ready, **remove the entry point**, do not ship a stub
- [ ] All external links resolve; no localhost, no staging URLs, no expired domains
- [ ] Support URL and marketing URL are live and load
- [ ] Every screen behind a login is reachable by the reviewer — see section 2
- [ ] Tested on the **oldest** OS version the app claims to support, not only the newest
- [ ] Tested on a real **mid-range Android** device, not only a Pixel emulator

The most common single cause: the reviewer hits a screen the developer never tested from a cold start.

## 2. Reviewer access — the avoidable one

- [ ] **Working demo credentials** supplied in App Review Information / Play app access instructions
- [ ] Credentials tested **the day of submission**, from a logged-out device
- [ ] The demo account has representative data — an empty account looks like a broken app
- [ ] If the app needs hardware, a specific region, or a physical device to function, that is explained with a **demo video** link
- [ ] If sign-in uses OTP or SMS, provide either a bypass code or a static test account. A reviewer cannot receive your SMS
- [ ] Any geo-restricted content is either accessible from the review region or explained

Login-gated apps with untested credentials are rejected almost automatically.

## 3. Minimum functionality — the vibe-coded-app killer

**Apple Guideline 4.2** rejects apps that are little more than a website in a wrapper, a repackaged template, or too thin to justify existing as an app.

- [ ] The app does something a mobile browser cannot — offline use, push notifications, camera, location, biometrics, home-screen widgets, background sync, native gestures
- [ ] It is **not** a `WebView` pointing at an existing site with a navigation bar
- [ ] It has native navigation and native UI, not a rendered web page
- [ ] It would still be useful with no network for at least one flow

If the honest answer is "it is our website in an app", the fix is to build a native capability, not to rewrite the review notes. This is the rejection that most surprises teams shipping fast.

## 4. Spam and duplicates

**Apple Guideline 4.3** targets apps that are near-copies of others, including your own, and template farms.

- [ ] Not a re-skin of another app on the same or a related developer account
- [ ] Not built from a marketplace template with only colours and copy changed
- [ ] Category is genuinely correct, not chosen for ranking
- [ ] Keyword spam absent from name, subtitle, and description
- [ ] If several similar apps are planned, they are consolidated into one app with configuration rather than shipped as separate binaries

This is where template-driven app businesses die. Differentiation must be functional, not cosmetic.

## 5. Payments

- [ ] Digital goods, subscriptions, and unlockable content use **in-app purchase**, not an external payment sheet
- [ ] Physical goods and real-world services use an external processor — using IAP for these is *also* a rejection
- [ ] Subscription screens state, before purchase: **title, duration, price per period, and what auto-renews**
- [ ] Links to Terms of Use and Privacy Policy are on the paywall itself
- [ ] A **Restore Purchases** control exists and works
- [ ] No language steering users to a cheaper website checkout, unless operating under a specific entitlement that permits it
- [ ] Free trial terms stated plainly, including what happens when it ends
- [ ] Play side — Play Billing Library at or above the currently required version

Paywall copy that hides the renewal terms is one of the most reliable rejections in both stores.

## 6. Privacy

- [ ] Privacy policy URL is live, reachable without a login, and describes actual behaviour
- [ ] **In-app account deletion** exists if accounts can be created — Apple requires deletion initiated *in the app*, and Play requires a web-accessible route as well
- [ ] Every permission has a purpose string that says **why**, specifically. "This app needs camera access" fails; "Take a photo of your receipt to log an expense" passes
- [ ] Permissions are requested **in context**, at the moment of use, not all at launch
- [ ] Apple privacy nutrition labels match what the code and its SDKs actually collect
- [ ] Play Data Safety form matches the same reality
- [ ] **Privacy manifest** present for the app and its third-party SDKs where required, with required-reason API declarations
- [ ] App Tracking Transparency prompt shown before any tracking identifier is used
- [ ] No data collected before consent where consent is required
- [ ] No permission requested that the app does not actually use — leftover permissions from a removed feature are a common failure

## 7. Login services parity

**Apple Guideline 4.8.** If the app offers third-party or social login, it must also offer a login option that limits data collection to name and email, allows hiding the email, and does not track for advertising without consent.

- [ ] Either no third-party login at all, or a qualifying privacy-preserving option is offered alongside it
- [ ] Email-and-password alone also satisfies this, if no social login is present
- [ ] Account creation is not forced for features that do not need an account

## 8. Metadata and assets

- [ ] Screenshots show the **actual current app**, not mockups, marketing renders, or an older version
- [ ] No device frames from the other platform, and no other platform named in the description
- [ ] Screenshot dimensions match current requirements for every required size class
- [ ] App name and subtitle are not keyword strings
- [ ] Description does not promise features that do not exist
- [ ] Age rating questionnaire answered honestly, including user-generated content and unrestricted web access
- [ ] Icon has no transparency, no alpha channel issues, no store badges baked in

## 9. User-generated content

If users can post anything visible to other users, both stores require moderation infrastructure. Missing it is an automatic rejection.

- [ ] A method to filter objectionable content
- [ ] A mechanism for users to **report** content, reachable in the UI
- [ ] The ability to **block** abusive users
- [ ] Published contact information for reports
- [ ] A stated commitment to act on reports within 24 hours

## 10. Special categories

Only relevant if they apply — but if they apply and are missed, rejection is certain.

| Category | Extra requirement |
|---|---|
| Health / medical | Evidence for claims; regulatory disclaimers; no diagnosis without basis |
| Finance / crypto | Entity licensing and disclosures; strict rules on trading and wallets |
| Kids | Stricter privacy; no third-party analytics or ads in some tiers; Families policy on Play |
| Gambling / contests | Licensing, geo-restriction, age gating |
| VPN / privacy tools | Narrow eligibility; must disclose data handling |
| AI-generated content | Content safety controls; disclosure of AI generation |

## 11. Build hygiene

- [ ] Version and build number incremented; Android version code strictly increasing
- [ ] Release build tested, not a debug build
- [ ] Debug menus, test flags, and developer toggles removed from the release
- [ ] No console logging of sensitive data
- [ ] No API keys or secrets in the client bundle — assume the bundle is readable
- [ ] Crash reporting wired and verified to actually report
- [ ] Android — `.aab` built, signing key backed up
- [ ] iOS — bitcode, entitlements, and capabilities match what the app uses

## Submission record

Produce this before submitting:

```
GATE RUN — <app name> <version> — <date>
Sections passed  : n/11
FAIL items       : <list, or "none">
Demo credentials : tested <date>, from logged-out device
Devices tested   : <oldest OS>, <mid-range Android>
Blocking issues  : <list, or "none — cleared for submission">
```

## Verification

Do not report this gate as run without the record above. A gate that was "mentally checked" is not a gate. Anything left unverified is written down as **unverified**, not silently passed.
