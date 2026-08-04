---
name: stripe-sdk
description: Use when implementing payments in code — Stripe Checkout, Subscriptions, Customer Portal, Webhooks, usage-based / metered billing, one-time charges, or evaluating Paddle / Polar / LemonSqueezy as alternatives. This is the code-level companion to the payment-plumber agent (which plans) and pricing-strategy skill (which decides). Triggers — "add Stripe", "Stripe Checkout", "subscription billing", "webhook handler", "Customer Portal", "metered billing", "Paddle vs Stripe", "Polar.sh", "LemonSqueezy", "wire up payments", "subscribe button", "billing implementation".
---

# Stripe SDK — code-level payment integration

This skill is the **code level**. For "should we charge $/month?" use `pricing-strategy`. For "plan the billing system" use the `payment-plumber` agent. For "write the Stripe code" — here.

## Provider choice — pick before you code

| Provider | Best for | VAT | Fees | API quality |
|---|---|---|---|---|
| **Stripe** | Global, devs, complex billing | DIY (Stripe Tax: extra) | 2.9% + 30¢ | Gold standard |
| **Paddle** | SaaS selling globally | **Merchant of Record — VAT handled** | 5% + 50¢ | Good |
| **Polar** | Indie devs, creators, OSS | Merchant of Record | 4% + 40¢ | Newer, clean |
| **LemonSqueezy** | Digital goods, no-code-ish | Merchant of Record | 5% + 50¢ | Acquired by Stripe 2024, still active |

**Decision in 30 seconds:**

- Selling to **EU/UK customers**? → Paddle or Polar (they handle VAT registration in 70+ countries for you). Stripe Tax exists but you remit yourself
- Selling to **US-only or you're already incorporated globally**? → Stripe
- **Solo dev, < $10K MRR**, want zero tax/compliance overhead? → Polar
- **Existing Stripe usage** in another product? → Stick with Stripe for consistency

For Karim's UGC business (clients in MENA + global) and `karim-social-autopilot-saas`: **Paddle or Polar** unless tax/VAT is already handled elsewhere.

## Install (Stripe)

```bash
npm install stripe                    # server SDK
npm install @stripe/stripe-js         # client SDK (browser)
```

```ts
// lib/stripe.ts
import Stripe from 'stripe';

export const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!, {
  apiVersion: '2025-04-30.basil',     // pin to a known version — don't auto-upgrade
  typescript: true,
});
```

**Env vars (always — never inline keys):**
```
STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLISHABLE_KEY=pk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_test_...
```

## Pattern 1 — Checkout (one-time + subscriptions)

The simplest, most reliable Stripe integration. Redirect to Stripe's hosted page, get paid, redirect back.

```ts
// app/api/checkout/route.ts
import { stripe } from '@/lib/stripe';
import { auth } from '@/auth';

export async function POST(req: Request) {
  const session = await auth();
  if (!session) return new Response('Unauthorized', { status: 401 });

  const { priceId } = await req.json();

  const checkout = await stripe.checkout.sessions.create({
    mode: 'subscription',                          // or 'payment' for one-time
    payment_method_types: ['card'],
    line_items: [{ price: priceId, quantity: 1 }],
    customer_email: session.user.email,
    client_reference_id: session.user.id,          // link back to your user
    success_url: `${process.env.NEXT_PUBLIC_SITE_URL}/dashboard?upgraded=1`,
    cancel_url: `${process.env.NEXT_PUBLIC_SITE_URL}/pricing`,
    allow_promotion_codes: true,
    billing_address_collection: 'auto',
  });

  return Response.json({ url: checkout.url });
}
```

```jsx
// Pricing page button
'use client';
async function subscribe(priceId: string) {
  const { url } = await fetch('/api/checkout', {
    method: 'POST', body: JSON.stringify({ priceId }),
  }).then(r => r.json());
  window.location.href = url;
}

<button onClick={() => subscribe('price_xxx')}>Subscribe — $29/mo</button>
```

Prices live in the Stripe Dashboard. Copy `price_xxx` IDs into your code or env vars.

## Pattern 2 — Webhook handler (the critical piece)

**Stripe is async.** Checkout success doesn't mean payment captured. Webhooks are how you really know.

```ts
// app/api/webhooks/stripe/route.ts
import { stripe } from '@/lib/stripe';
import { headers } from 'next/headers';
import { db } from '@/lib/db';

export async function POST(req: Request) {
  const body = await req.text();                              // raw body for signature
  const sig = (await headers()).get('stripe-signature')!;

  let event;
  try {
    event = stripe.webhooks.constructEvent(
      body, sig, process.env.STRIPE_WEBHOOK_SECRET!,
    );
  } catch (err) {
    return new Response(`Webhook signature failed: ${err}`, { status: 400 });
  }

  switch (event.type) {
    case 'checkout.session.completed': {
      const s = event.data.object;
      await db.user.update({
        where: { id: s.client_reference_id! },
        data: {
          stripeCustomerId: s.customer as string,
          stripeSubscriptionId: s.subscription as string,
          plan: 'pro',
        },
      });
      break;
    }
    case 'customer.subscription.updated':
    case 'customer.subscription.deleted': {
      const sub = event.data.object;
      await db.user.update({
        where: { stripeSubscriptionId: sub.id },
        data: {
          plan: sub.status === 'active' ? 'pro' : 'free',
          subscriptionStatus: sub.status,
        },
      });
      break;
    }
    case 'invoice.payment_failed':
      // notify user, schedule retry
      break;
  }

  return new Response('ok', { status: 200 });
}
```

**Body parsing:**
- **App Router** (above): `await req.text()` returns raw body — works out of the box, nothing to configure
- **Pages Router** (legacy): need `export const config = { api: { bodyParser: false } }` + read raw body via `buffer(req)` from `micro` or similar

Use App Router for new projects.

**Idempotency** is mandatory. Stripe retries webhooks. Use `event.id` as a dedup key:

```ts
const existing = await db.webhookEvent.findUnique({ where: { id: event.id } });
if (existing) return new Response('already processed', { status: 200 });
await db.webhookEvent.create({ data: { id: event.id, type: event.type } });
// ... then process
```

**App Router Next.js gotcha:** `await req.text()` is required (not `req.json()`) for signature verification — the body must be raw.

## Pattern 3 — Customer Portal (cancel, update card, view invoices)

Stripe hosts a full account-management UI. Zero code beyond a single endpoint.

```ts
// app/api/portal/route.ts
export async function POST(req: Request) {
  const session = await auth();
  const user = await db.user.findUnique({ where: { id: session.user.id } });
  if (!user?.stripeCustomerId) return new Response('No subscription', { status: 400 });

  const portal = await stripe.billingPortal.sessions.create({
    customer: user.stripeCustomerId,
    return_url: `${process.env.NEXT_PUBLIC_SITE_URL}/account`,
  });

  return Response.json({ url: portal.url });
}
```

```jsx
<button onClick={async () => {
  const { url } = await fetch('/api/portal', { method: 'POST' }).then(r => r.json());
  window.location.href = url;
}}>Manage Subscription</button>
```

Configure the portal once in Stripe Dashboard → Settings → Billing → Customer Portal. Toggle: allow cancel, allow plan change, show invoice history.

## Pattern 4 — Local testing with Stripe CLI

```bash
# Install once
brew install stripe/stripe-cli/stripe  # mac
scoop install stripe                    # windows
stripe login
```

Forward webhooks to localhost:
```bash
stripe listen --forward-to localhost:3000/api/webhooks/stripe
```

Outputs `whsec_...` — use this as `STRIPE_WEBHOOK_SECRET` in dev.

Trigger events for testing:
```bash
stripe trigger checkout.session.completed
stripe trigger customer.subscription.deleted
```

Test cards (always work in test mode):
- `4242 4242 4242 4242` — generic success
- `4000 0000 0000 9995` — declined (insufficient funds)
- `4000 0027 6000 3184` — requires 3D Secure / SCA

## Pattern 5 — Usage-based / metered billing

For "$0.001 per API call" or "$X per GB uploaded" pricing:

```ts
// 1. Create a metered price in Stripe Dashboard
// 2. Subscribe customer to it as usual
// 3. Report usage as it happens:

await stripe.subscriptionItems.createUsageRecord(
  subscriptionItemId,
  {
    quantity: 100,
    timestamp: Math.floor(Date.now() / 1000),
    action: 'increment',
  },
);
```

Stripe sums all usage at invoice time. No need to track in your DB.

## Pattern 6 — Multi-tier subscriptions

Have multiple prices for different tiers. The clean pattern:

```ts
// Map your internal plan names to Stripe price IDs
const PLANS = {
  pro_monthly: 'price_1ABC...',
  pro_yearly: 'price_1DEF...',
  team_monthly: 'price_1GHI...',
} as const;
```

**Plan changes** (upgrade/downgrade mid-cycle):
```ts
const sub = await stripe.subscriptions.retrieve(user.stripeSubscriptionId);
await stripe.subscriptions.update(sub.id, {
  items: [{ id: sub.items.data[0].id, price: PLANS.team_monthly }],
  proration_behavior: 'create_prorations',   // 'none' to skip pro-rata
});
```

## Pattern 7 — Free trials

```ts
const checkout = await stripe.checkout.sessions.create({
  mode: 'subscription',
  line_items: [{ price: priceId, quantity: 1 }],
  subscription_data: {
    trial_period_days: 14,
  },
  // ...
});
```

Or skip the card collection for trial:
```ts
subscription_data: {
  trial_period_days: 14,
  trial_settings: { end_behavior: { missing_payment_method: 'cancel' } },
},
payment_method_collection: 'if_required',
```

## Paddle alternative — when VAT matters

```bash
npm install @paddle/paddle-node-sdk
```

Conceptually identical: hosted checkout, webhooks, customer portal. Differences:
- Paddle is **Merchant of Record** — they pay VAT/sales tax in 70+ countries on your behalf
- Webhook event names differ (`subscription.activated` vs `customer.subscription.created`)
- 5% + 50¢ vs Stripe's 2.9% + 30¢ — pay the premium for tax simplicity

Use Paddle when your customers are in EU/UK/global and you don't want to register for VAT yourself.

## Polar.sh — indie creator alternative

```bash
npm install @polar-sh/sdk
```

- Built on Stripe, but as Merchant of Record (handles VAT)
- 4% + 40¢
- Excellent dev DX, OSS-friendly (sponsorship features built-in)
- Newer (2023+), smaller ecosystem

For Karim selling globally as solo: **Polar > Stripe** if MRR < $10K (VAT compliance otherwise eats hours).

## Security checklist

- ✅ Never put `STRIPE_SECRET_KEY` in client code (only `pk_*` is public)
- ✅ Always verify webhook signatures
- ✅ Always check `event.livemode` matches your environment
- ✅ Store `stripeCustomerId` + `stripeSubscriptionId` in your DB; don't refetch on every request
- ✅ Idempotency keys on `customers.create` / `subscriptions.create` calls (Stripe SDK supports `{ idempotencyKey }` option)
- ✅ Use Restricted Keys (Stripe Dashboard → API keys) for cron jobs that don't need full access
- ✅ Set `Stripe-Account` header when operating on Connect accounts
- ✅ HTTPS only for webhook URLs in production

## Gotchas

1. **Webhook timing** — Checkout success page can load BEFORE the webhook fires. Don't grant access based on URL params; wait for the webhook. Show "Setting up your account..." for 2-5 seconds
2. **Body parser** — Webhook routes must receive raw body. Next.js App Router: `await req.text()`. Pages Router: `export const config = { api: { bodyParser: false } }`
3. **Test mode vs live mode** — separate keys, separate customers, separate webhooks. Never mix in one environment
4. **API version pinning** — set `apiVersion` in the SDK init. Stripe deprecates old versions but supports them indefinitely. Set it explicitly; don't depend on the default
5. **Customer creation race** — calling `customers.create` for the same email twice creates two customers. Use `customers.list({ email })` first, or store the ID in your DB at signup
6. **Decimal handling** — Stripe uses **cents** (USD), or smallest currency unit. `$29.99` = `2999`. Never multiply prices by 100 manually — let Stripe quote them
7. **Refunds aren't free** — Stripe doesn't refund the original processing fee. Factor into your CAC math
8. **Tax** — Stripe Tax is opt-in and adds ~0.5%. Enable per region. Or skip Stripe and use Paddle/Polar for tax-included pricing
9. **Subscription proration** — by default, plan changes prorate. For "next-cycle changes only", set `proration_behavior: 'none'` and `billing_cycle_anchor`

## Quick decision guide

| Need | Reach for |
|---|---|
| Solo SaaS, want zero tax overhead | Polar.sh or Paddle |
| Already Stripe somewhere else | Stick with Stripe |
| One-time digital product | Stripe Checkout `mode: 'payment'` or LemonSqueezy |
| Subscriptions with self-serve cancel | Stripe + Customer Portal |
| Metered API pricing | Stripe metered subscriptions + `createUsageRecord` |
| Free trial, no CC up front | Stripe `payment_method_collection: 'if_required'` |
| Plan upgrades/downgrades | `subscriptions.update` with `proration_behavior` |
| Test webhooks locally | `stripe listen --forward-to ...` |
| VAT in EU/UK | Paddle or Polar (not Stripe) |
| Marketplace / Connect (split payments) | Stripe Connect (deep topic — separate engagement) |

## Related

`payment-plumber` (agent — plans the billing system at strategy level), `pricing-strategy` (decides tiers/prices), `auth-implementation` (gate paid features behind auth), `cfo-advisor` (CAC/LTV math), `senior-backend` (API patterns around webhooks), `env-secrets-manager` (storing keys), `senior-security` (PCI/key handling).
