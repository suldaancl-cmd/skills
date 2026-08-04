# 07 — Karim's paste-ready prompts (verbatim from the docx)

These are the prompts Karim already uses with his IDE agent. They are reproduced here exactly as written. Use them as-is when delivering to him; tweak only on explicit request.

Source: `New Microsoft Word Document.docx` on Karim's Desktop.

---

## Prompt 1 — Supabase client

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

---

## Prompt 2 — Wire Sign In / Sign Up to Supabase Auth

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

---

## Prompt 3 — Polished signup UX (email verification flow)

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

---

## How to use these

1. Copy the prompt block.
2. Paste into your IDE agent (Claude Code in VS Code, Cursor, Windsurf, Google AI Studio's edit pane).
3. Run the prompt against the project that already has `src/supabaseClient.js` (or run prompt 1 first).
4. Review the diff before accepting.

For Google sign-in, RLS-protected tables, and storage prompts, see the matching reference files in this skill.
