# 02 — Email/password auth

Two methods, one rule: never auto-login after signup.

## Method signatures (Supabase JS v2)

```js
// Sign up — new account
const { data, error } = await supabase.auth.signUp({ email, password });
// On success, Supabase sends a verification email automatically.
// `data.user` exists but is not "confirmed" yet.

// Sign in — existing account
const { data, error } = await supabase.auth.signInWithPassword({ email, password });
// Fails until the user clicks the link in their email.

// Sign out
await supabase.auth.signOut();

// Listen for auth state changes (mount this once near the app root)
const { data: { subscription } } = supabase.auth.onAuthStateChange((event, session) => {
  // event: SIGNED_IN | SIGNED_OUT | TOKEN_REFRESHED | USER_UPDATED | PASSWORD_RECOVERY
});
```

## Paste-ready prompt — basic wiring (Karim's docx, verbatim)

```text
Connect the Sign In and Sign Up pages in this project to Supabase Auth.

Use the Supabase client from: src/supabaseClient.js

1) For Sign Up:
   - Use supabase.auth.signUp({ email, password })

2) For Sign In:
   - Use supabase.auth.signInWithPassword({ email, password })

3) After successful login or signup:
   - Redirect the user to the Home page ("/")

4) Add simple error handling:
   - If Supabase returns an error, show a small error message under the form

Do not change the UI design — only add the logic to make these forms work.

Show me only the updated Sign In and Sign Up files.
```

## Paste-ready prompt — production signup UX (Karim's docx, verbatim)

This is the upgrade the Profit Studio video shows. Use it as a follow-up to the basic wiring.

```text
Improve the UX of my Supabase email/password signup flow.

Current behavior:
- When the user completes Sign Up, the app goes back to the Sign In page,
  but there is no success message and the email field is empty.

I want the following behavior:

1) After a successful Supabase signUp({ email, password }):
   - Do NOT auto-login.
   - Redirect the user to the Sign In page.
   - Keep / pre-fill the email they just used for signup in the Sign In form.

2) On the Sign In page:
   - If the user comes from a successful signup:
     - Show a clear success message above the form, for example:
       "Your account has been created. Please check your email and verify your address before logging in."
   - The email input should already contain the email used during signup.

3) You can pass the email from Sign Up to Sign In using:
   - router state, OR
   - a query parameter, OR
   - any simple, clean method that works well with this project.

4) Keep the existing design and layout exactly the same.
   Just add:
   - the logic for passing the email
   - the success message on the Sign In screen
   - and basic error handling if signup fails.

Show me only the updated Sign Up and Sign In components.
```

## Manual steps (Supabase dashboard)

1. **Authentication → Sign In / Providers → Email**: confirm "Confirm email" is **ON** (default). This is what forces verification.
2. **Authentication → URL Configuration**:
   - **Site URL** = your production URL (or `http://localhost:5173` for local dev).
   - **Redirect URLs** = add any URLs Supabase is allowed to send users back to (e.g. `https://example.com/**`).
3. (Optional) **Authentication → Email Templates**: rebrand the verification email if shipping to real users.

## Checking the signed-in user

```js
const { data: { user } } = await supabase.auth.getUser();
if (!user) {
  // Show login screen / redirect to /sign-in
}
```

For pages that require login, gate on this either at route-level (React Router loader, Next.js middleware) or with a simple effect that redirects if `user` is null.

## Common pitfalls

- **"Email not confirmed" on first login** — that's correct. The user hasn't clicked the link yet.
- **Verification email lands in spam** — set a custom SMTP in Supabase Auth settings before shipping, or your domain reputation will sink.
- **Forms work locally but break after deploy** — Site URL or Redirect URL is misconfigured. Add the production URL to both.
- **Storing user data immediately after `signUp`** — works, but the row should reference `data.user.id` (a UUID) which is the same `auth.uid()` the RLS policies will check.
