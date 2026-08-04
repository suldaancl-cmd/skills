# 06 — Safe deploy: VS Code → GitHub → Hostinger (or Vercel/Netlify)

The deployment workflow Profit Studio teaches. The key idea: **`.env` never goes to GitHub** — the host gets its own copy of the env vars.

## What goes where

| Where | What |
|---|---|
| Local `.env.local` | Real secrets. Gitignored. Loaded by Vite as `import.meta.env.VITE_*`. |
| GitHub repo | Code only. No secrets, no `node_modules`, no build output. |
| Hostinger / Vercel / Netlify | Pulls from GitHub, runs `npm run build`, serves `dist/`. Has its own copy of the env vars set via the host's UI. |

## Paste-ready prompt — safe first push to GitHub

Use this prompt as a Claude Code / IDE-agent prompt **on the project itself**. It does only Git/GitHub setup. It does not touch the UI, DB logic, or design.

```text
Prepare this project for its first push to GitHub. Do ONLY Git and GitHub setup.
Do not modify the UI, the database logic, the design, or any application code.

The target repository is: <PASTE-YOUR-GITHUB-HTTPS-URL>.git

Required:

1) Ensure `.gitignore` exists and contains at least:
   node_modules
   dist
   build
   .env
   .env.local
   .env.*.local
   .DS_Store
   *.log

2) If any `.env` / `.env.local` / `.env.*.local` files are currently TRACKED
   by git, untrack them with `git rm --cached <file>` (do NOT delete the file
   from disk). Print the list of files you untracked.

3) Initialize git if not already a repo (`git init`).
4) Set `main` as the default branch.
5) Add the remote `origin` to <PASTE-YOUR-GITHUB-HTTPS-URL>.git if not set.
6) Stage everything except gitignored files (`git add .`).
7) Create a single initial commit:
   "chore: initial commit, pre-deploy hygiene".

8) Stop here. Tell me clearly:
   - the branch name to push,
   - the remote URL,
   - and that I should use VS Code's "Publish Branch" button (or
     `git push -u origin main`) to send the commit to GitHub myself.

DO NOT run `git push` yourself. DO NOT change UI code, DB code, or design.
```

## Paste-ready prompt — figure out the env-var list before going to the host

```text
What environment variables does this project need to run in production?

Look at every place the code reads `import.meta.env.*` (Vite),
`process.env.*` (Next.js / Node), or any other env mechanism.

List each variable with:
- the exact name (e.g. `VITE_SUPABASE_URL`),
- what it is (one sentence),
- where I find its value (e.g. "Supabase → Project Settings → API → Project URL"),
- whether it is safe to expose to the browser (Vite `VITE_*` and Next `NEXT_PUBLIC_*` are public).

Answer briefly. Do not change any code.
```

## Manual steps — Hostinger (Profit Studio's path)

1. Hostinger dashboard → **Deploy a Node.js web app** for your domain.
2. Choose **Import Git repository** (not "upload files").
3. Connect GitHub → pick the repo you just pushed.
4. **Framework preset**: Hostinger usually auto-detects. For Vite/React it's `Vite`. If unsure, ask the IDE agent: "What is the framework preset for this project? Answer briefly."
5. **Branch**: `main`. **Root directory**: leave blank unless the app lives in a subfolder.
6. **Environment variables**: add every var from the list above. Paste real values here (this is the only safe place outside `.env.local`).
7. Click **Deploy**.
8. After it finishes, status should read `Running`, with **Auto deployment** = enabled. Future `git push`es to `main` redeploy automatically.

## Manual steps — Vercel (recommended if not committed to Hostinger)

1. https://vercel.com → **Add New → Project** → import the GitHub repo.
2. Framework Preset: auto-detected.
3. Build Command: `npm run build` (default for Vite).
4. Output Directory: `dist` (Vite default).
5. **Environment Variables** section: add every `VITE_*` var.
6. Deploy.

## Manual steps — Netlify

1. https://app.netlify.com → **Add new site → Import an existing project** → GitHub → pick repo.
2. Build command: `npm run build`. Publish directory: `dist`.
3. **Site settings → Environment variables** → add each `VITE_*` var.
4. Trigger deploy.

## Update workflow (after first deploy)

```
1. Edit code locally in your IDE.
2. `npm run dev` → test it works.
3. If it works, commit: VS Code Source Control → stage → commit message → commit.
4. Push: "Sync Changes" (or `git push`).
5. Host auto-rebuilds. Refresh the live site after ~30-60s.

If a change broke something locally:
- VS Code → Source Control → click the file → "Discard Changes" BEFORE you commit.
- Or `git restore <file>`.
```

## Hard rules

- Never commit `.env` or `.env.local`. If you accidentally did, **rotate the keys immediately** (Supabase: Project Settings → API → reset the anon key; Stripe: roll the key; etc.) — git history is permanent.
- Never paste secrets into Claude/agent prompts unless you've already accepted those will be in your chat history. Use placeholder names like `{{VITE_SUPABASE_URL}}` when authoring prompts.
- Never use the Supabase `service_role` key in client-side code. It bypasses RLS.
- Production Google sign-in needs the deployed domain in Supabase's Site URL and Google Cloud's Authorized origins. See [`03-auth-google.md`](03-auth-google.md).
