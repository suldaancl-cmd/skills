---
name: supabase-stack
description: Wire Supabase into an existing Vite/React (or similar) project the Profit Studio way — `src/supabaseClient.js`, email/password + Google auth with email verification, AI-generated RLS-protected Postgres tables, private storage buckets with signed URLs, and a safe GitHub → Hostinger/Vercel deploy. Use this skill whenever the user asks to add Supabase, hook up sign-in / sign-up, build a Postgres-backed app with per-user data, store private user files, set RLS policies, configure environment variables for deploy, or paste a "supabase prompt" into their IDE agent (Claude Code / Cursor / Windsurf / Google AI Studio). Trigger even when they only say "auth", "login page", "user accounts", "save data per user", "row level security", "private uploads", "signed URL", or "deploy my app".
license: MIT
metadata:
  author: karim
  version: "1.0.0"
  date: 2026-05-28
  sources:
    - https://www.youtube.com/watch?v=1NgO4Tzv27I  # Profit Studio — full-stack Supabase (auth, DB, RLS, storage)
    - https://www.youtube.com/watch?v=s_2taeO8KRI  # Profit Studio — safe deploy (Claude Code → GitHub → Hostinger)
    - C:/Users/user/OneDrive/Desktop/New Microsoft Word Document.docx  # Karim's paste-ready prompts
---

# Supabase Stack — auth, DB, storage, deploy

Hands a working Supabase backend to a frontend project in 4 steps:

1. Connect (client + env vars)
2. Auth (email/password + Google)
3. Database (per-user tables protected by RLS)
4. Storage (private bucket, signed URLs, per-user folders)

Plus a safe deploy path (GitHub → Hostinger or any Vite-aware host).

## When this skill is the right answer

Karim usually has the project already open in his own IDE (VS Code, Cursor, Windsurf, Claude Code in VS Code, Google AI Studio). The deliverable is almost always a **paste-ready prompt** for his IDE agent — not files this Claude writes directly. Don't spawn a shipper agent against his repo. Give him the prompt block and let his agent execute it.

If the user is in a fresh project this Claude does own (e.g. an artifact, sandbox), this skill's prompts can be executed directly. Use judgement.

## Profit Studio conventions (do not invent your own)

These are non-negotiable defaults. They match the videos + Karim's docx prompts. Override only on explicit request.

| Decision | Convention |
|---|---|
| Client file path | `src/supabaseClient.js` |
| Env var names | `VITE_SUPABASE_URL` + `VITE_SUPABASE_ANON_KEY` (Vite prefix is required for browser access) |
| Placeholder syntax in initial scaffold | `{{SUPABASE_URL}}` / `{{SUPABASE_KEY}}` (Karim pastes real values after) |
| Auth — email signup | `supabase.auth.signUp({ email, password })`, **email verification stays ON** |
| Post-signup UX | No auto-login. Redirect to Sign In. Pre-fill the email. Show "check your email to verify" message. |
| Auth — email login | `supabase.auth.signInWithPassword({ email, password })` |
| Auth — Google | Only works on the **deployed** site. Configure Site URL + Redirect URLs in Supabase first; then OAuth client in Google Cloud; paste Supabase callback URL into Google Cloud's Authorized redirect URIs. |
| Per-user table column | `user_id uuid references auth.users(id) on delete cascade` |
| RLS policies | Always enable RLS. Filter every operation by `auth.uid() = user_id`. |
| Storage bucket | Private (Public bucket OFF). Default name: `app-files`. |
| Storage path layout | `{auth.uid()}/{filename}` — each user gets their own folder. |
| Serving private files | `createSignedUrl(path, expiresInSeconds)` — never expose raw URLs. |
| Delete flow | Remove from storage **and** from DB row in one operation. |
| UI changes during wiring | None. Only logic. Karim is explicit: "Do not change the UI design — only add the logic." |

If the AI-generated SQL uses a different bucket name than `app-files`, ALL four RLS policies must reference the same name or they won't apply.

## Step decision tree

Ask the user (or infer from their message) which steps they need. Then deliver only those.

```
Does the project have a Supabase client yet?
├─ No  → references/01-client-setup.md
└─ Yes → skip
Do they need auth?
├─ Email/password           → references/02-auth-email-password.md
├─ + Google                 → references/03-auth-google.md  (deploy first!)
└─ Already wired            → skip
Per-user data?
└─ references/04-database-rls.md
Private file uploads?
└─ references/05-storage-signed-urls.md
Going live?
└─ references/06-deploy-hostinger.md  (also works for Vercel/Netlify with minor swaps)
Want Karim's exact paste-ready prompts (verbatim from the docx)?
└─ references/07-paste-prompts.md
```

## How to deliver

For each step the user needs:

1. State the convention being applied (1 line).
2. Show the paste-ready prompt block in a fenced code block. Prompts are written for an IDE agent that has read/write access to the project.
3. After the prompt, list the **manual steps** Karim must do in the Supabase dashboard or Google Cloud (the things no agent can do for him).
4. Stop. Do not run the prompt yourself unless the user explicitly says "execute it here".

## Why these conventions

- **`src/supabaseClient.js` (not `lib/`)** — matches Vite/React scaffolds out of the box and what Profit Studio's video uses; everyone watching the video will already have this path.
- **`{{SUPABASE_URL}}` placeholders** — Karim pastes real values exactly once, in one file. Stops keys from leaking into chat history or screen-shares.
- **Email verification stays on** — prevents fake signups and bot accounts. The video makes this explicit.
- **No auto-login after signup** — the user must verify their email first. Auto-login before verification = locked-out users who can't recover.
- **`auth.uid() = user_id` policies** — the single line that turns a shared Postgres table into a multi-tenant SaaS backend. Without it, every user sees every row.
- **Private bucket + signed URLs** — keeps file URLs unguessable and time-limited. Public buckets = anyone with the URL has it forever.
- **`{user_id}/{filename}` folder layout** — pairs with the storage RLS policy so the database enforces per-user isolation at the filesystem level too.
- **Don't push `.env`** — Hostinger/Vercel pulls from GitHub. If `.env` is in the repo, the keys are public. The deploy prompt handles `.gitignore` correctly.

## What this skill is NOT

- Not Postgres performance tuning — that's [`supabase-postgres-best-practices`](../supabase-postgres-best-practices/SKILL.md).
- Not a brand reference card — that's [`design-md-supabase`](../design-md-supabase/).
- Not subscription/Stripe wiring — Profit Studio promised a dedicated video; revisit when that lands.

## References

Detailed prompts and SQL in:

- [`references/01-client-setup.md`](references/01-client-setup.md)
- [`references/02-auth-email-password.md`](references/02-auth-email-password.md)
- [`references/03-auth-google.md`](references/03-auth-google.md)
- [`references/04-database-rls.md`](references/04-database-rls.md)
- [`references/05-storage-signed-urls.md`](references/05-storage-signed-urls.md)
- [`references/06-deploy-hostinger.md`](references/06-deploy-hostinger.md)
- [`references/07-paste-prompts.md`](references/07-paste-prompts.md) — Karim's docx prompts verbatim
