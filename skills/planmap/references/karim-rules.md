# Karim's rules — binding on any agent that plans or builds a project

Stated by Karim 2026-08-11. These are not style preferences. An agent that skips one of them
has not finished the job, no matter how good the plan looks.

Read this file **before** phase 1 and check it again **before** handing anything over.

---

## Rule 1 — Plan every angle. Silence is a bug.

Every route, every screen, every integration, every failure path gets its own row. If
something is undecided, the row says **`TBD — needs decision: <the exact question>`**. It never
just goes missing.

Before writing `PLANMAP.md`, walk this list and confirm each has at least one row, or an
explicit "not needed for V1, because…":

- what happens on **first launch**, and on **second launch**
- what happens when the user is **offline**
- what happens when a **payment fails**, and when a **refund** is requested
- what happens when the **AI call fails, times out, or returns garbage**
- what happens when the user wants to **delete their account and data**
- **who can see what** — the permission model, per table
- what the app does on the **free tier vs paid**, and what happens the moment a subscription lapses
- **where every secret lives** in local, and in production
- what breaks if a **third-party service disappears** or doubles its price

A plan that covers the happy path only is not a plan. It is a demo script.

---

## Rule 2 — Create `.env.local` and hand it to Karim to fill.

Do not tell him "you'll need some API keys". **Create the file.** Two files, actually:

| File | Committed? | Holds |
|---|---|---|
| `.env.example` | yes | every variable name, empty value, one comment line each |
| `.env.local` | **no — must be in `.gitignore`** | the real values Karim pastes |

Write the first cut the moment the stack is decided — phase 2, mid-interview, so he fills it
while you keep working. Finalise it in phase 5 against the integrations table.

Every line gets a comment saying **where to get that value**:

```bash
# Supabase → Project Settings → API → Project URL
EXPO_PUBLIC_SUPABASE_URL=

# Supabase → Project Settings → API → anon public key
# Safe to ship in the app. The service_role key is NOT — never put it here.
EXPO_PUBLIC_SUPABASE_ANON_KEY=

# Stripe → Developers → API keys → Secret key
# Server only. If this ever appears in client code, rotate it immediately.
STRIPE_SECRET_KEY=
```

Then tell him, in one message: the **full path** of the file, **how many** values it needs, and
**which ones block the first deploy**.

Three things that are never negotiable:
- `.env.local` in `.gitignore` **before** the first commit, not after.
- Never ask him to paste a secret into the chat. The file is the channel.
- Any variable exposed to the client (`EXPO_PUBLIC_`, `NEXT_PUBLIC_`, `VITE_`) is **public**.
  Say so on the line. A secret behind a public prefix is a leak, not a config.

---

## Rule 3 — Every step you need from him, counted and up front.

Already the job of `MANUAL-SETUP.md`. The rule adds one thing: **the counts come first**, before
any table. "Fourteen human-only steps, six blocking the first deploy, about ninety minutes of
your time plus two to three weeks waiting on Apple" — not "you'll need to set up a few accounts."

---

## Rule 4 — Tell him the risks before he starts, not after he is committed.

`PLANMAP.md` and `MANUAL-SETUP.md` both open with a **risks** section. Four questions, answered
plainly:

1. **What can go wrong?** The realistic failure modes, ranked by likelihood, not by drama.
2. **What will this cost?** Monthly at zero users, and monthly at the point it starts working.
   Every figure carries its assumption. Unknown means write `unverified`.
3. **What is he locking himself into?** Bundle IDs, chosen vendors, database shape, anything
   that is expensive to reverse later. Name the exit cost.
4. **What is irreversible?** Destructive migrations, DNS cutover, publishing a bundle ID,
   deleting a bucket. These get a confirmation gate in the build loop.

**Advise, do not present a menu.** He asked to be guided. Give the recommendation first, the
reasoning in one line, then the alternatives. "I'd use X because Y — but Z is also fine if you
care more about W" beats a neutral table every time.

If he picks something you think will hurt him, say so in one line and build what he picked.
His call, your stated risk, on the record.

---

## Rule 5 — Choices in Arabic.

Every question and every option in the interview appears in **Arabic as well as English**. The
`(recommended)` marker carries across. He is choosing between real tradeoffs; he should be able
to read them in the language he thinks fastest in.

Layout laws from `feedback_arabic_english_format` still bind: one direction per block, English
block LTR then Arabic block RTL, technical tokens stay in `inline code`, numerals stay Latin,
tables stay single-language.

---

## Rule 6 — Plain language. Explain it like he is smart but not a developer.

He has said this directly: deep technical English is hard, and he wants to actually understand,
not nod along.

- The **first time** any technical term appears, define it in one plain sentence.
  Not *"we'll use RLS"* — *"we'll use RLS (row-level security: the database itself checks who is
  allowed to read each row, so a bug in the app code can't leak another user's data)."*
- Short sentences. One idea each.
- Use a concrete analogy when the concept is abstract. Skip the analogy when it is not.
- Never hide a decision behind jargon. If he cannot restate the tradeoff back to you in his own
  words, the explanation failed — not him.

---

## Rule 7 — Give him something to watch, and never invent the link.

For anything he has to do with his own hands — creating a Stripe account, generating a key,
enrolling in the Apple Developer Program — offer a short tutorial he can watch first.

**The Verification Lock applies to links with full force.** A fabricated tutorial URL is worse
than no link: he clicks it, it 404s, and he loses trust in the whole document.

So:

- Link only what you have **actually verified** in this session — a URL you fetched, or one
  already recorded in the vault.
- Prefer the **vendor's own docs or quickstart** over a random video. They stay current.
- If you have no verified link, write the **exact search phrase** instead:
  `search: "Stripe test mode to live mode 2026"` — and label it `unverified`.
- Check the vault first. `index_video_lessons.md` and the `playbook_*` notes may already hold
  the right walkthrough, and a note he already owns beats a stranger's video.

---

## Rule 8 — Read the playbook before you plan.

The second brain outranks general knowledge. Before phase 1:

1. Read the project workspace's `BRAIN.md` and `SKILLS.md`.
2. Read the `playbook_*` / `reference_*` note that matches the domain — `app-building-kit/README.md`
   for apps, `playbook_design_killer_combo.md` for design, and so on.
3. When the vault and your general knowledge disagree, **say so out loud** and write it into
   `NOTES.md`. Do not quietly pick one.

---

## The handover check

Before saying a plan is done, all eight must be true. Name any that are not.

- [ ] Every angle in Rule 1 has a row or an explicit "not needed for V1"
- [ ] `.env.example` and `.env.local` exist; `.env.local` is gitignored; every line has a
      where-to-get-it comment
- [ ] `MANUAL-SETUP.md` opens with real counts that match the table row counts
- [ ] Risks section answers all four questions, with a recommendation not a menu
- [ ] Every interview question and option was given in Arabic too
- [ ] Every technical term was defined in plain language on first use
- [ ] Every tutorial link is verified, or labelled `unverified` with a search phrase
- [ ] The matching vault playbook was read, and any disagreement is logged in `NOTES.md`
