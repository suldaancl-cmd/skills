---
name: auth-implementation
description: Use when adding user authentication to a web app — signup/login, OAuth providers (Google, GitHub, Apple), email magic links, session management, JWT vs database sessions, middleware-protected routes, password reset, or picking between Auth.js / Clerk / Supabase Auth / Better Auth. Triggers — "add auth", "login flow", "OAuth", "NextAuth", "Auth.js", "Clerk", "Supabase Auth", "Better Auth", "session management", "JWT", "protected route", "user authentication", "signup", "magic link", "auth middleware".
---

# Auth Implementation — pick a stack and ship

Authentication is the #1 thing solo devs over-engineer. There are 4 production-ready options in 2026 — pick by your constraints, not by what's trendy. The actual implementation is ~50-200 lines per option.

## The 4 real choices

| Tool | Self-host | DB-backed | Hosted UI | Best for |
|---|---|---|---|---|
| **Auth.js (NextAuth v5)** | ✅ | ✅ optional | ❌ (you build) | Next.js apps, full control, free |
| **Clerk** | ❌ hosted | ✅ (theirs) | ✅ (prebuilt) | Fastest to launch, has user management UI |
| **Supabase Auth** | ✅ (or hosted) | ✅ (Supabase Postgres) | Partial | Already using Supabase |
| **Better Auth** | ✅ | ✅ optional | ❌ (you build) | Framework-agnostic, newer, type-safe |

**Decision in 30 seconds:**

```
Already using Supabase?       → Supabase Auth
Need users-table managed for you, fast? → Clerk ($25/mo Pro after free tier)
Next.js + free + DIY UI?      → Auth.js v5
Non-Next + type-safe + self-host? → Better Auth
```

For Karim's `karim-social-autopilot-saas`: if using Supabase → Supabase Auth. Otherwise Clerk (fastest to ship, $25/mo when revenue justifies). Auth.js v5 if budget-conscious or full control needed.

## When NOT to roll your own

**Never** implement password hashing, session management, OAuth callbacks, CSRF, or PKCE manually. The libraries below have battle-tested all of it. The "I'll just write a quick JWT thing" trap costs weeks of subtle vulnerabilities.

## Option 1 — Auth.js v5 (NextAuth) — the free workhorse

Next.js App Router, free, fully customizable. The default for Next.js apps with budget constraint.

```bash
npm install next-auth@beta
```

```ts
// auth.ts
import NextAuth from 'next-auth';
import Google from 'next-auth/providers/google';
import GitHub from 'next-auth/providers/github';

export const { handlers, auth, signIn, signOut } = NextAuth({
  providers: [
    Google,
    GitHub,
    // EmailProvider for magic links, CredentialsProvider for password, etc.
  ],
  session: { strategy: 'jwt' },          // 'jwt' (this example) or 'database' (see adapter section below)
  pages: { signIn: '/login' },
  callbacks: {
    async session({ session, token }) {
      session.user.id = token.sub;
      return session;
    },
  },
});
```

```ts
// app/api/auth/[...nextauth]/route.ts
export { GET, POST } from '@/auth';
```

```ts
// middleware.ts — protect routes
export { auth as middleware } from '@/auth';
export const config = { matcher: ['/dashboard/:path*', '/account/:path*'] };
```

```jsx
// app/dashboard/page.tsx — Server Component
import { auth } from '@/auth';
import { redirect } from 'next/navigation';

export default async function Dashboard() {
  const session = await auth();
  if (!session) redirect('/login');
  return <h1>Hi {session.user.name}</h1>;
}
```

```jsx
// app/login/page.tsx
import { signIn } from '@/auth';

export default function Login() {
  return (
    <form action={async () => { 'use server'; await signIn('google', { redirectTo: '/dashboard' }); }}>
      <button>Continue with Google</button>
    </form>
  );
}
```

**Env vars:**
```
AUTH_SECRET=<openssl rand -base64 32>
AUTH_GOOGLE_ID=...
AUTH_GOOGLE_SECRET=...
AUTH_GITHUB_ID=...
AUTH_GITHUB_SECRET=...
```

**Database adapter** (for `session: 'database'`):
```bash
npm install @auth/prisma-adapter   # or @auth/drizzle-adapter
```

```ts
import { PrismaAdapter } from '@auth/prisma-adapter';
import { prisma } from '@/lib/prisma';

export const { handlers, auth } = NextAuth({
  adapter: PrismaAdapter(prisma),
  session: { strategy: 'database' },
  // ...
});
```

## Option 2 — Clerk — the fastest path

Drop-in auth with hosted user management UI (admin sees users, can ban, impersonate). $0 free tier up to 10K MAU. $25/mo Pro tier.

```bash
npm install @clerk/nextjs
```

```jsx
// app/layout.tsx
import { ClerkProvider } from '@clerk/nextjs';

export default function RootLayout({ children }) {
  return (
    <ClerkProvider>
      <html><body>{children}</body></html>
    </ClerkProvider>
  );
}
```

```ts
// middleware.ts
import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server';

const isProtected = createRouteMatcher(['/dashboard(.*)', '/account(.*)']);

export default clerkMiddleware((auth, req) => {
  if (isProtected(req)) auth.protect();
});
```

```jsx
// app/dashboard/page.tsx
import { auth, currentUser } from '@clerk/nextjs/server';

export default async function Dashboard() {
  const user = await currentUser();
  return <h1>Hi {user.firstName}</h1>;
}
```

```jsx
// app/login/[[...sign-in]]/page.tsx
import { SignIn } from '@clerk/nextjs';
export default () => <SignIn />;
```

**Env vars:**
```
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=...
CLERK_SECRET_KEY=...
```

That's it. Signup, login, password reset, OAuth, MFA, organizations — all included. Customize with `<SignIn appearance={...}>` for brand styling. **The fastest possible path for Karim's SaaS.**

## Option 3 — Supabase Auth — when your DB is Supabase

Auth living in the same Postgres as your data. RLS (Row Level Security) policies become your authz layer.

```bash
npm install @supabase/supabase-js @supabase/ssr
```

```ts
// lib/supabase/server.ts
import { createServerClient } from '@supabase/ssr';
import { cookies } from 'next/headers';

export async function createClient() {
  const cookieStore = await cookies();
  return createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    {
      cookies: {
        getAll() { return cookieStore.getAll(); },
        setAll(items) { items.forEach(({ name, value, options }) => cookieStore.set(name, value, options)); },
      },
    },
  );
}
```

```jsx
// app/dashboard/page.tsx
import { createClient } from '@/lib/supabase/server';
import { redirect } from 'next/navigation';

export default async function Dashboard() {
  const supabase = await createClient();
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) redirect('/login');
  return <h1>Hi {user.email}</h1>;
}
```

```jsx
// app/login/actions.ts
'use server';
import { createClient } from '@/lib/supabase/server';
import { redirect } from 'next/navigation';

export async function login(formData: FormData) {
  const supabase = await createClient();
  const { error } = await supabase.auth.signInWithPassword({
    email: formData.get('email') as string,
    password: formData.get('password') as string,
  });
  if (error) return { error: error.message };
  redirect('/dashboard');
}

export async function loginWithGoogle() {
  const supabase = await createClient();
  const { data } = await supabase.auth.signInWithOAuth({
    provider: 'google',
    options: { redirectTo: `${process.env.NEXT_PUBLIC_SITE_URL}/auth/callback` },
  });
  if (data.url) redirect(data.url);
}
```

**RLS for authorization (the killer feature):**
```sql
-- in Supabase SQL editor
alter table posts enable row level security;
create policy "users see only their posts" on posts
  for select using (auth.uid() = user_id);
```

Now any frontend query auto-filters to the user's rows. No server-side `where userId = ...` needed.

See `supabase-postgres-best-practices` (already installed) for deeper Supabase patterns.

## Option 4 — Better Auth — newer, framework-agnostic

Type-safe, framework-agnostic, self-hostable. Newer than Auth.js but gaining adoption fast in 2026. Use when you want Auth.js-style control + better TypeScript ergonomics + no Next.js dependency.

```bash
npm install better-auth
```

```ts
// lib/auth.ts
import { betterAuth } from 'better-auth';
import { Pool } from 'pg';

export const auth = betterAuth({
  database: new Pool({ connectionString: process.env.DATABASE_URL }),
  emailAndPassword: { enabled: true },
  socialProviders: {
    google: {
      clientId: process.env.GOOGLE_CLIENT_ID!,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET!,
    },
  },
});
```

```ts
// app/api/auth/[...all]/route.ts
import { auth } from '@/lib/auth';
import { toNextJsHandler } from 'better-auth/next-js';
export const { POST, GET } = toNextJsHandler(auth.handler);
```

```ts
// Client
import { createAuthClient } from 'better-auth/react';
export const authClient = createAuthClient();

const { data } = await authClient.signIn.email({ email, password });
```

Framework adapters for Hono, SvelteKit, Astro, Solid, Vue. Strong TS inference end-to-end.

## Session strategy — JWT vs Database

| | JWT | Database |
|---|---|---|
| **Lookup cost** | None — verify signature | One DB query per request |
| **Revocation** | Hard (token valid until expiry) | Easy (delete row) |
| **Size** | Bigger cookies | Tiny cookies (session ID only) |
| **Best for** | Stateless APIs, microservices | Web apps where you need "force logout" |

**Recommendation for solo SaaS:** start with `'jwt'` (zero DB setup, the example above ships as-is). Migrate to `'database'` once you need force-logout, session inspection, or rich session payloads. Migration is a 3-line config change + adapter import.

## Common patterns

### Protected Server Component
```jsx
import { auth } from '@/auth';
import { redirect } from 'next/navigation';

export default async function Settings() {
  const session = await auth();
  if (!session) redirect('/login?next=/settings');
  return <SettingsClient userId={session.user.id} />;
}
```

### Protected API route
```ts
import { auth } from '@/auth';

export async function POST(req: Request) {
  const session = await auth();
  if (!session) return new Response('Unauthorized', { status: 401 });
  // proceed
}
```

### Get current user in a Client Component
```jsx
'use client';
import { useSession } from 'next-auth/react';   // Auth.js
import { useUser } from '@clerk/nextjs';          // Clerk

function UserBadge() {
  const { data: session } = useSession();        // Auth.js
  // OR: const { user } = useUser();             // Clerk
  if (!session) return null;
  return <span>{session.user.email}</span>;
}
```

### Role-based access
```ts
// In session callback (Auth.js)
async session({ session, token }) {
  session.user.role = await getUserRole(token.sub);   // 'admin' | 'user'
  return session;
}

// In a Server Component
const session = await auth();
if (session?.user.role !== 'admin') redirect('/');
```

## Magic links (passwordless email login)

```ts
// Auth.js v5 — note: provider renamed from 'next-auth/providers/email' (v4) to 'next-auth/providers/nodemailer' (v5)
import Nodemailer from 'next-auth/providers/nodemailer';

providers: [
  Nodemailer({
    server: process.env.EMAIL_SERVER,    // smtp://user:pass@smtp.resend.com:587
    from: 'auth@yoursite.com',
  }),
],
```

Clerk and Supabase Auth ship magic links by default — just toggle in dashboard.

## OAuth setup — the gotchas

For each provider, you'll need:
1. **OAuth app** registered with the provider (Google Cloud Console, GitHub Developer Settings, etc.)
2. **Redirect URI**: `https://yoursite.com/api/auth/callback/<provider>` (Auth.js) or whatever your tool documents
3. **Client ID + Secret** → into env vars
4. **Authorized domains** added in the provider dashboard

Common mistakes:
- Forgetting to add `http://localhost:3000` as dev origin
- Mismatched redirect URI (must be exact, including trailing slash)
- Using Client Secret in browser code (never — server-only)

## Security checklist before shipping

- ✅ `AUTH_SECRET` is 32+ random bytes, not a placeholder
- ✅ HTTPS-only in production (`secure` cookie flag)
- ✅ `SameSite=Lax` on session cookies
- ✅ Password requirement: 8+ chars, no max length (long passphrases > complex shorts)
- ✅ Rate-limit login/signup endpoints (Upstash Ratelimit + middleware)
- ✅ Email verification before access to sensitive ops
- ✅ Password reset tokens single-use, 1-hour expiry
- ✅ MFA for admin accounts at minimum (Clerk gives free; Auth.js needs plugin)
- ✅ Sessions invalidate on password change

Auth.js, Clerk, Supabase Auth, Better Auth all enforce these by default. Don't fight them.

## Quick decision guide

| Need | Reach for |
|---|---|
| "Just give me login fast, I'll pay later" | Clerk |
| Next.js + free + own users table | Auth.js v5 with Prisma adapter |
| Postgres + RLS-based authz | Supabase Auth |
| Non-Next.js (Hono / SvelteKit / etc.) | Better Auth |
| Need org/team/multi-tenant out of the box | Clerk Organizations |
| Need impersonation/admin UI for support | Clerk |
| Embed inside an existing Postgres | Supabase Auth or Better Auth |
| Avoid vendor lock-in | Auth.js or Better Auth |

## Gotchas

1. **Auth.js v4 vs v5** — they're different. v5 (beta but stable in 2026) is App-Router-native and the right choice for new projects. v4 is Pages-Router only
2. **Clerk's free tier is generous but watch MAU** — 10K MAU free. If your SaaS hits 10K active users you're earning > $25/mo anyway
3. **Supabase Auth + custom claims** — adding role to JWT requires `customAccessToken` setting; non-obvious
4. **Cookie sizes** — JWT strategies with many claims hit 4KB cookie limits. Use database sessions if you need rich session data
5. **OAuth in dev with localhost** — most providers want `127.0.0.1` not `localhost`, or require HTTPS. Use `next dev --experimental-https` or ngrok
6. **Edge runtime + database adapter** — Auth.js with Prisma fails on Edge runtime. Use `auth.js`-with-Node-runtime or switch to Drizzle adapter
7. **`useSession` triggers re-render** — wrap consumers in suspense/memo. Don't put it at app root

## Related

`senior-backend` (broader API security), `senior-frontend` (Next.js patterns), `supabase-postgres-best-practices` (RLS policies), `stripe-sdk` (paired — auth gates the paywall), `env-secrets-manager` (storing AUTH_SECRET / OAuth creds), `senior-security` (threat model for the auth surface).
