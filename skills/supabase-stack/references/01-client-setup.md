# 01 — Client setup

One file, two placeholders, one export. Nothing else.

## Install

```bash
npm install @supabase/supabase-js
```

## Paste-ready prompt (Karim's docx, verbatim)

```text
Create a simple Supabase connection file for this project.

1) Create a new file called:
   src/supabaseClient.js

2) Inside it, write a clean Supabase setup with two variables that I can replace later:
   const SUPABASE_URL = "{{SUPABASE_URL}}";
   const SUPABASE_PUBLIC_KEY = "{{SUPABASE_KEY}}";

3) Import createClient from "@supabase/supabase-js" and export one Supabase client:
   export const supabase = createClient(SUPABASE_URL, SUPABASE_PUBLIC_KEY);

Make the file very simple and show clearly where I should paste my URL and my public key.
```

## Expected output

```js
// src/supabaseClient.js
import { createClient } from "@supabase/supabase-js";

// Paste your Supabase project URL here:
const SUPABASE_URL = "{{SUPABASE_URL}}";

// Paste your Supabase public (anon / publishable) key here:
const SUPABASE_PUBLIC_KEY = "{{SUPABASE_KEY}}";

export const supabase = createClient(SUPABASE_URL, SUPABASE_PUBLIC_KEY);
```

## Manual steps (Supabase dashboard)

1. Go to https://supabase.com → **Start your project**.
2. Create organization → personal / free plan (50K MAU free is plenty to start).
3. Create project → save the database password somewhere safe.
4. Wait ~1 min for provisioning.
5. **Project Settings → API**:
   - Copy **Project URL** → paste over `{{SUPABASE_URL}}`.
   - Copy **`anon` / `publishable` key** → paste over `{{SUPABASE_KEY}}`. **Never** use the `service_role` key in browser code.

## Env-var variant (for deploy)

If the project will go live, swap the hardcoded literals for env vars in the same file:

```js
const SUPABASE_URL = import.meta.env.VITE_SUPABASE_URL;
const SUPABASE_PUBLIC_KEY = import.meta.env.VITE_SUPABASE_ANON_KEY;
```

And create `.env.local` (gitignored):

```dotenv
VITE_SUPABASE_URL=https://your-project.supabase.co
VITE_SUPABASE_ANON_KEY=eyJhbGciOi...
```

`.gitignore` must include `.env` and `.env.local`. The deploy step handles that — see [`06-deploy-hostinger.md`](06-deploy-hostinger.md).

## Why `VITE_` prefix

Vite only exposes env vars starting with `VITE_` to client-side code. Without the prefix, `import.meta.env.SUPABASE_URL` is `undefined` in the browser. Next.js uses `NEXT_PUBLIC_` for the same reason; CRA uses `REACT_APP_`.
