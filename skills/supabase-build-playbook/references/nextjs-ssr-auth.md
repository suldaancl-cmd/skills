# Supabase Auth in Next.js (App Router) — the @supabase/ssr pattern

This is the modern, correct way to wire Supabase Auth into a Next.js App Router
app. It's what current tutorials build and what the old `supabase-stack` skill
(Vite/`src/supabaseClient.js`, single client) does **not** cover.

The key idea that trips people up: **two packages, and a different client for
each runtime.** Server Components, Route Handlers, and middleware run on the
server and read the session from **cookies**; Client Components run in the
browser. A single client can't serve both — the session won't survive the
server/client boundary.

```bash
npm install @supabase/supabase-js @supabase/ssr
```

- `@supabase/supabase-js` — the core client (queries, auth calls).
- `@supabase/ssr` — cookie-based session handling so the server can read who's
  logged in. (It replaced the deprecated `@supabase/auth-helpers-nextjs` — don't
  use that.)

## Environment variables

```bash
# .env.local  — publishable key only; NEVER the secret key here
NEXT_PUBLIC_SUPABASE_URL=https://<project>.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=<sb_publishable_... or legacy anon>
```

`NEXT_PUBLIC_*` is shipped to the browser — that's fine for the publishable key
(RLS protects you) and forbidden for the secret key.

## Browser client — for Client Components

```ts
// lib/supabase/client.ts
import { createBrowserClient } from '@supabase/ssr'

export function createClient() {
  return createBrowserClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
  )
}
```

## Server client — for Server Components / Route Handlers / Server Actions

```ts
// lib/supabase/server.ts
import { createServerClient } from '@supabase/ssr'
import { cookies } from 'next/headers'

export async function createClient() {
  const cookieStore = await cookies()
  return createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    {
      cookies: {
        getAll() {
          return cookieStore.getAll()
        },
        setAll(cookiesToSet) {
          try {
            cookiesToSet.forEach(({ name, value, options }) =>
              cookieStore.set(name, value, options)
            )
          } catch {
            // called from a Server Component — middleware refreshes instead
          }
        },
      },
    }
  )
}
```

## Middleware — refresh the session on every request

Without this, server-side sessions go stale and users get logged out
unexpectedly. The middleware reads and rewrites the auth cookies on each request.

```ts
// middleware.ts
import { createServerClient } from '@supabase/ssr'
import { NextResponse, type NextRequest } from 'next/server'

export async function middleware(request: NextRequest) {
  let response = NextResponse.next({ request })

  const supabase = createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    {
      cookies: {
        getAll() {
          return request.cookies.getAll()
        },
        setAll(cookiesToSet) {
          cookiesToSet.forEach(({ name, value, options }) =>
            response.cookies.set(name, value, options)
          )
        },
      },
    }
  )

  // IMPORTANT: refreshes the token. Do not put logic between client + getUser.
  await supabase.auth.getUser()
  return response
}

export const config = {
  matcher: ['/((?!_next/static|_next/image|favicon.ico).*)'],
}
```

## Email / password flows

```ts
// sign up — keep email verification ON; do NOT auto-login
const supabase = createClient()
const { error } = await supabase.auth.signUp({ email, password })
// on success: redirect to /sign-in, prefill the email,
// show "check your inbox to verify". An unverified auto-login = locked-out users.

// sign in
const { error } = await supabase.auth.signInWithPassword({ email, password })

// sign out
await supabase.auth.signOut()
```

## Google OAuth

```ts
const { error } = await supabase.auth.signInWithOAuth({
  provider: 'google',
  options: { redirectTo: `${location.origin}/auth/callback` },
})
```

OAuth only works on the **deployed** URL with config in three places:
1. Supabase → Authentication → URL Configuration: set Site URL + Redirect URLs.
2. Google Cloud Console: create an OAuth client.
3. Paste Supabase's callback URL into Google's "Authorized redirect URIs".

You also need a `/auth/callback` route handler that exchanges the code for a
session via `supabase.auth.exchangeCodeForSession(...)`.

## Reading the user on the server (the common case)

```tsx
// any Server Component / page
import { createClient } from '@/lib/supabase/server'

export default async function Page() {
  const supabase = await createClient()
  const { data: { user } } = await supabase.auth.getUser()
  if (!user) redirect('/sign-in')
  // queries here run as this user → RLS applies automatically
  const { data: clients } = await supabase.from('clients').select('*')
  return <ClientList clients={clients} />
}
```

Use `getUser()` (verifies the token with Supabase), not `getSession()`, for auth
decisions on the server — `getSession()` trusts the cookie without revalidating.

## Auth hardening checklist (all off by default)

- Email confirmation: ON.
- Leaked-password protection (HaveIBeenPwned): enable in Auth settings.
- MFA: offer TOTP once the basics work.
- Set a sensible JWT expiry and rely on the middleware to refresh.
