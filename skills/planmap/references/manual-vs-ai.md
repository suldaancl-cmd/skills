# What no AI agent can do for you

The checklist behind `MANUAL-SETUP.md`. Walk it against the project's integrations table and
keep every row that applies. Two reasons a task lands here: the vendor requires a legal person
(identity, card, signature), or the agent is forbidden from doing it by policy even when it
technically could.

## Hard blocks — identity, money, legal

| Task | Why the agent cannot | Typical time |
|---|---|---|
| Create any account (email + phone verification, CAPTCHA) | Account creation and CAPTCHA solving are prohibited actions | 5 min each |
| Enter a payment card, subscribe to a paid plan | Entering financial credentials is prohibited | 5 min |
| Stripe / Paddle / Polar KYC — legal entity, bank account, tax ID | Identity verification of a real person | 20 min + 1-3 days review |
| Apple Developer Program enrollment | `$99`/yr, Apple ID with 2FA, DUNS number for an organization | 30 min + 3-14 days |
| DUNS number request | Dun & Bradstreet verifies a real business | 15 min + 5-30 days |
| Google Play Developer account | `$25` one-time, identity + address verification | 30 min + 1-3 days |
| Sign any contract, DPA, or vendor agreement | Signature binds a person | varies |
| Buy a domain | Payment method + registrant identity | 10 min |

## Credentials the agent must never touch

| Task | Why | Time |
|---|---|---|
| Generate an API key in a vendor console | The agent has no session in your dashboards, and must not enter your password to get one | 2 min each |
| Rotate or paste a production secret | Secrets go in a secret store, never through a chat | 2 min each |
| Set up 2FA / authenticator / recovery codes | Physical device | 5 min each |
| Anything requiring an SMS code | Your phone | 2 min |
| OAuth client secrets (Google, Meta, Apple Sign-In) | Created inside a console you are logged into | 10 min each |

## Reviews and consoles the agent cannot pass

| Task | Why | Time |
|---|---|---|
| Google OAuth consent screen verification | Google reviews a real business, its domain and privacy policy | 30 min + 2-6 weeks if scopes are sensitive |
| Meta / WhatsApp Business API review | Business verification with documents | 1 hr + 1-4 weeks |
| App Store / Play Store submission and review replies | Submission is an act by the account holder | 1 hr + 1-7 days per round |
| Payment provider going live (out of test mode) | Follows KYC approval | waiting |
| Domain and DNS changes at the registrar | Registrar login; the agent can write the records for you to paste | 15 min + propagation |

## Judgment calls that are yours by right

Not blocked by policy, but wrong for an agent to decide alone.

- Picking the colors-and-fonts deck option. Karim's standing rule: no code until he picks.
- Approving a design against the reference. Taste is the thing being bought.
- Pricing, and what goes in the free tier.
- What customer data is collected, retained and where it lives.
- Anything irreversible in production: destructive migrations, deleting buckets, DNS cutover.

## The honest framing for the report

Say the count, not the vibe. "Fourteen human-only steps, six of them blocking the first deploy,
about ninety minutes of your time plus two to three weeks waiting on Apple" is useful. "You'll
need to set up a few accounts" is not, and it is how a plan quietly hides two weeks of
paperwork.

If a row's time estimate is a guess, mark it `unverified`. Vendor review times change, and a
confident wrong number is worse than a range.
