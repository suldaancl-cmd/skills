# 03 — Google sign-in

**Hard requirement: deploy the app first.** Google sign-in does not work on `localhost` for new OAuth clients in most cases (and is awkward when it does). Profit Studio is explicit about this — test on the deployed URL only.

## JS call

```js
const { data, error } = await supabase.auth.signInWithOAuth({
  provider: "google",
  options: {
    redirectTo: `${window.location.origin}/`,  // where to land after OAuth dance
  },
});
```

That's the entire client-side code. The rest is dashboard configuration in Supabase + Google Cloud.

## Paste-ready prompt

```text
Add a "Continue with Google" button to the Sign In and Sign Up pages.

1) Use the Supabase client from: src/supabaseClient.js

2) On button click, call:
   supabase.auth.signInWithOAuth({
     provider: "google",
     options: { redirectTo: `${window.location.origin}/` }
   })

3) Place the button below the existing email/password form, with a small
   "or" divider between them.

4) Keep the existing design and layout exactly the same.
   - Match the button styling to the existing app design (do not invent a new style).
   - Do not change the email/password flow at all.

5) Note: Google sign-in only works on the deployed site, not on localhost,
   so I will test this after deploy.

Show me only the updated Sign In and Sign Up components.
```

## Manual steps (in order)

### Part A — Supabase

1. **Authentication → URL Configuration**:
   - **Site URL** = `https://your-deployed-domain.com` (the real one — not localhost).
   - **Redirect URLs** = add `https://your-deployed-domain.com/**` so Supabase will accept post-OAuth redirects back to your site.
2. **Authentication → Sign In / Providers → Google**:
   - Open the Google provider panel.
   - **Copy the Callback URL** Supabase shows. It will look like:
     `https://abcdefg.supabase.co/auth/v1/callback`
   - Leave this tab open — you'll come back to paste the Google client ID & secret.

### Part B — Google Cloud Console

3. Go to https://console.cloud.google.com → create or pick a project.
4. **APIs & Services → OAuth consent screen**:
   - User type: External.
   - App name, support email, developer email.
   - Add yourself as a test user if the app is in "Testing" mode.
   - Agree to the Google API Services User Data Policy.
5. **APIs & Services → Credentials → Create Credentials → OAuth client ID**:
   - Application type: **Web application**.
   - **Authorized JavaScript origins**: `https://your-deployed-domain.com`
   - **Authorized redirect URIs**: paste the Supabase callback URL from step 2.
   - Create → copy the **Client ID** and **Client Secret**.

### Part C — back in Supabase

6. Paste **Client ID** and **Client Secret** into Supabase's Google provider panel.
7. Toggle "Enable Sign in with Google" **on**.
8. Save.

### Part D — test

9. Visit your deployed site (not localhost).
10. Click "Continue with Google" → pick an account → you should land back on the homepage signed in.
11. In Supabase **Authentication → Users**, the new user appears with provider = `google`.

## Common pitfalls

- **`redirect_uri_mismatch`** — the URL Supabase is asking Google to bounce to isn't in the OAuth client's Authorized redirect URIs. Copy/paste again, no trailing slash difference.
- **Loops back to sign-in** — Site URL in Supabase doesn't match your deployed domain. Or the user closed the popup. Or the OAuth client is in "Testing" mode and the user isn't a test user.
- **Works locally but not on production** — vice versa. Each environment needs its own Site URL/Redirect URL/Authorized origins entries. Don't replace; add both.
