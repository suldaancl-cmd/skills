# The interview question bank

Phase 1 runs on this. Batches of 3 to 6, one topic per batch, every question multiple choice
with one option marked `(recommended)` and a half-line reason. He can always answer free text.

The point is not the questions — it is that the AI stops guessing. Adapt them to the project;
the batch order and the two mandatory questions do not change.

## Batch 1 — idea and money

- What is the product in one sentence, and who is the paying customer?
- Is this a new product, a clone of something that works, or an internal tool?
- Free, paid, or free-with-a-paywall in V1?
- What already exists — designs, code, brand, an audience?

## Batch 2 — users and their first minute

- Who signs up, and what happens in their first sixty seconds?
- One user type, or several with different permissions?
- Personal accounts, or organisations with members? *(this one decides the whole data model —
  never infer it)*
- Arabic, English, or both, and which is the default?

## Batch 3 — screens and their order

- Which screens exist? Name them all.
- **Onboarding before auth, or auth before onboarding?** Where does the "building your plan"
  step sit?
- What does the home screen show the moment it opens?
- Is there an admin surface, and who sees it?

## Batch 4 — data

- What are the main entities and what does each one own?
- Who computes derived values — a database default, the app, or the AI?
- What is per-user private versus shared?
- Time zones and dates: device time, or stored per user?

## Batch 5 — the AI behaviour, and its failures

- What exactly does the AI do, on what input, producing what output?
- How long is that allowed to take? *(anything over a few seconds leaves the request cycle and
  goes to a job runner)*
- **When the AI is wrong, what can the user do?** Edit the result, retry, or nothing?
- **When the AI fails outright, what happens?** Auto-retry, ask for new input, or fail loudly?
- Does the user see progress in real time, or just a spinner?

Answer this batch and phase 2 starts: hand him the first cut of `MANUAL-SETUP.md` now.

## Batch 6 — stack

Default to `references/stack-defaults.md` and ask only where the project genuinely differs.

- Auth, database, model gateway, job runner, storage, email, error tracking — confirm or swap.
- One codebase for web and mobile, or separate?
- Where does the backend live — API routes inside the app, or a separate service?
- Which model is the cheap default and which is the escalation?

## Batch 7 — the V1 boundary (mandatory)

- **What does "V1 is done" mean for you?** Working MVP with good UI, or store-ready with
  payments and legal pages?
- **What is explicitly OUT of V1?** Payments, paywall, push notifications, analytics,
  referrals, teams, offline. Name each one in or out — write the OUT list into `PLANMAP.md`
  verbatim so nobody quietly builds it.
- Tests in V1, or manual testing only?
- Real launch date, or no date?

## Batch 8 — the seams

The questions that only get asked after something breaks.

- When auth creates a user, how does that become a row in your own database — webhook,
  on-first-request, or a scheduled sync? *(webhook is the production answer)*
- Which uploads go direct from the client, and which go through your server?
- What has to keep working offline or on a bad connection?
- What happens on account deletion — hard delete, soft delete, or export first? *(the stores
  require the option to exist at all)*

## Stop condition

Stop when a batch produces no new decision — not when the picture feels clear. Feeling clear
after three batches is the exact failure this loop exists to prevent. Six to ten batches is
normal for a real product.

Then write the plan, and say how many batches it took.
