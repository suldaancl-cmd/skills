---
name: headless-cms-stack
description: Use when choosing or integrating a headless CMS for a premium / content-managed website — Sanity, Storyblok, Prismic, Contentful, DatoCMS, Craft, Payload, Strapi — with Next.js / Nuxt / Astro. Covers the CMS picker (which wins when), award-tier integration patterns (App Router server-component fetch + on-demand revalidation), draft/preview + live visual editing, content modeling, CMS image CDNs + next/image, i18n/RTL Arabic, and the security pitfalls (read vs write tokens, draft leaks, CORS, lock-in).
---

# Headless CMS Stack (premium / award-tier content sites)

Devs build the front-end; clients edit content. This skill picks the CMS and wires it correctly.
Code targets 2026: Next.js 16 App Router, `next-sanity` with `defineLive`.

## 1. Headless CMS vs alternatives — decide first

| Approach | Who edits | When it wins |
|---|---|---|
| **Hard-coded** (content in repo/MDX) | nobody (devs only) | One-off marketing/landing pages, portfolios, docs in-repo. No client, no recurring content. Fastest, zero CMS cost, no token surface. |
| **No-code builder** (Webflow / Framer) | client edits *design + content* in a GUI | Client wants to move boxes themselves; small-to-mid marketing sites; tight timeline. *(Covered by the Webflow/Framer skills — not here.)* |
| **Headless CMS** | client edits *content only*; devs own the front-end | Premium/award-tier custom front-end (GSAP/WebGL/bespoke layout) **+** a client who needs to edit copy/posts/case-studies without touching design. The default for agency builds where you keep full code control but hand off content. |

Rule of thumb: bespoke front-end you'd be proud to put on Awwwards **and** a non-technical content owner → headless CMS. Either alone → pick hard-coded or Webflow/Framer.

## 2. CMS picker — what it is / when to choose

Most-seen on Awwwards-tier sites: **Sanity** and **Storyblok** (agency favorites), with **Prismic** and **DatoCMS** close behind.

- **Sanity** — fully customizable React Studio; GROQ query language; real-time; **Presentation** tool gives click-to-edit live visual editing. *Choose when:* you want maximum schema flexibility, custom editing UX, and an agency-grade structured-content model. The default for premium custom front-ends. [sanity.io/docs](https://www.sanity.io/docs)
- **Storyblok** — block-based **Visual Editor**: editors build/preview real pages live without a dev in the loop. *Choose when:* marketing team needs content velocity and self-serve page assembly; multi-site. Strong official Astro/Next/Nuxt SDKs. [storyblok.com](https://www.storyblok.com/)
- **Prismic** — page-builder around **Slices** (reusable sections) authored via **Slice Machine** (slices defined in-repo, type-safe). *Choose when:* you want a polished editorial page-builder with typed components and quick setup. [prismic.io/docs](https://prismic.io/docs)
- **Contentful** — mature enterprise SaaS; field-level localization, roles, large orgs. *Choose when:* enterprise governance/compliance and an existing content ops team matter more than bespoke editing UX. [contentful.com/developers/docs](https://www.contentful.com/developers/docs/)
- **DatoCMS** — SaaS with a built-in **imgix-backed image CDN** + GraphQL Content Delivery API; `responsiveImage` returns srcset + LQIP in one query. *Choose when:* image-heavy editorial/portfolio sites where best-in-class media handling out of the box is the priority. [datocms.com/docs](https://www.datocms.com/docs/)
- **Craft CMS** — PHP/MySQL, self-host or Craft Cloud; designer-loved; **Matrix** fields for flexible content blocks; GraphQL API for headless. *Choose when:* the team lives in the PHP/Craft world or wants Craft's authoring UX with a decoupled front-end. [craftcms.com/docs/5.x](https://craftcms.com/docs/5.x/)
- **Payload** — TypeScript-native, open-source, self-host; **Payload 3.0 runs *inside* a Next.js app** (admin at `/admin`, call the **Local API** directly in server components — no HTTP hop). Code-first config in `payload.config.ts`. *Choose when:* you want CMS + app in one TS/Next codebase, own your data, and prefer code over a GUI schema builder. [payloadcms.com/docs](https://payloadcms.com/docs)
- **Strapi** — open-source, self-host; GUI Content-Type Builder; REST + GraphQL. *Choose when:* you need self-hosting with a visual schema builder friendlier to non-developers, and value maturity/plugins over Payload's TS-native architecture. [docs.strapi.io](https://docs.strapi.io/)
- **Hygraph** — GraphQL-native SaaS with **Content Federation** (unify multiple sources into one GraphQL schema). *Choose when:* GraphQL-first teams or you must federate content from several backends. [hygraph.com/docs](https://hygraph.com/docs)
- **WordPress headless** — WordPress back-end exposed via **WPGraphQL** (or WP REST); often on WP Engine's **Faust.js**. *Choose when:* a client already on WordPress wants to keep their editor/plugins but needs a modern decoupled front-end. [faustjs.org](https://faustjs.org/) · [WPGraphQL](https://www.wpgraphql.com/)

Self-host vs SaaS: Payload / Strapi / Craft / WP = you host (data ownership, no per-seat fees, you patch it). Sanity / Storyblok / Prismic / Contentful / DatoCMS / Hygraph = managed (faster, scales itself, watch seat/API pricing + lock-in).

## 3. Integration with award frameworks

**Next.js App Router** — fetch in async **Server Components**; tag the fetch; invalidate on-demand from a **CMS webhook** → Route Handler calling `revalidateTag`. This is the premium-site pattern: static-fast, instantly updatable, no rebuilds. ([nextjs.org revalidateTag](https://nextjs.org/docs/app/api-reference/functions/revalidateTag))

**Nuxt** — `@nuxtjs/sanity`, `@storyblok/nuxt`, or `@nuxtjs/prismic`; fetch in `useAsyncData`; ISR/on-demand revalidation via Nitro route rules + a webhook endpoint.

**Astro** — content fetched in frontmatter (SSG default; SSR/on-demand for preview). Storyblok ships an **official Astro integration** with visual editing; Sanity/Prismic/DatoCMS have first-class Astro SDKs. ([storyblok.com/astro-cms](https://www.storyblok.com/astro-cms))

### Minimal correct Sanity + Next.js App Router

```ts
// sanity/lib/client.ts
import { createClient } from 'next-sanity'

export const client = createClient({
  projectId: process.env.NEXT_PUBLIC_SANITY_PROJECT_ID!,
  dataset: process.env.NEXT_PUBLIC_SANITY_DATASET!,
  apiVersion: '2026-02-01', // pin a date; bump deliberately
  useCdn: true,             // CDN for published prod reads; auto-bypassed for drafts
})
```

```ts
// sanity/lib/live.ts — Live Content API (next-sanity)
import { defineLive } from 'next-sanity/live'
import { client } from './client'

export const { sanityFetch, SanityLive } = defineLive({
  client: client.withConfig({ apiVersion: '2026-02-01' }),
  serverToken: process.env.SANITY_API_READ_TOKEN, // READ-only token, server env only
  browserToken: process.env.SANITY_API_READ_TOKEN,
})
```

```ts
// app/(site)/[slug]/page.tsx — Server Component fetch, tagged + typed via GROQ
import { defineQuery } from 'next-sanity'
import { sanityFetch } from '@/sanity/lib/live'

const PAGE_QUERY = defineQuery(
  `*[_type == "page" && slug.current == $slug][0]{title, body, "img": mainImage}`
)

export default async function Page({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params
  const { data: page } = await sanityFetch({
    query: PAGE_QUERY,
    params: { slug },
    tags: [`page:${slug}`, 'page'], // tags drive on-demand revalidation
  })
  if (!page) return null
  return <article>{page.title}</article>
}
```

```ts
// app/api/revalidate/route.ts — Sanity webhook → on-demand revalidation
// Configure a GROQ-powered webhook in Sanity manage; secret = SANITY_REVALIDATE_SECRET.
import { revalidateTag } from 'next/cache'
import { type NextRequest, NextResponse } from 'next/server'
import { parseBody } from 'next-sanity/webhook'

type WebhookPayload = { _type: string }

export async function POST(req: NextRequest) {
  try {
    const { isValidSignature, body } = await parseBody<WebhookPayload>(
      req,
      process.env.SANITY_REVALIDATE_SECRET, // validates the webhook signature
    )
    if (!isValidSignature) {
      return new Response('Invalid signature', { status: 401 })
    }
    if (!body?._type) return new Response('Bad Request', { status: 400 })

    // Next.js 16.2+: two-arg form. 'max' = stale-while-revalidate (recommended).
    // For an immediate hard expire from a webhook use: revalidateTag(body._type, { expire: 0 })
    revalidateTag(body._type, 'max')
    return NextResponse.json({ revalidated: true, type: body._type })
  } catch (err) {
    const message = err instanceof Error ? err.message : 'Unknown error'
    return new Response(message, { status: 500 })
  }
}
```

> Next.js 16.2 deprecated the single-arg `revalidateTag(tag)`; use `revalidateTag(tag, 'max')`, or `updateTag` in a Server Action for immediate in-session updates. ([nextjs.org/docs](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)) Tag the same data you want to bust; webhook fires `_type`, so tag at least by `_type` plus a per-doc tag for surgical busts.

`SanityLive` belongs once in the root layout (see §4) to stream live updates.

## 4. Draft / preview + live visual editing

Goal: editors see unpublished drafts on the real front-end, ideally click-to-edit in place.

- **Next.js `draftMode()`** — a Route Handler calls `(await draftMode()).enable()` to set a signed HttpOnly cookie; your fetch layer serves drafts when it's on, published otherwise. ([nextjs.org draft-mode](https://nextjs.org/docs/app/api-reference/functions/draft-mode))
- **Sanity Presentation** — renders the live site inside the Studio with click-to-edit overlays via stega-encoded content; mount `<VisualEditing />` only when draft mode is on.
- **Storyblok Visual Editor** — the bridge renders your real components live in the editor; editors assemble blocks with instant preview.
- **Preview tokens** — preview requests use a **read token** server-side to fetch drafts. Never ship that token to the client (Sanity routes it through draft-mode + Presentation). Gate the enable-route with the CMS-provided secret so randoms can't flip on draft mode.

```tsx
// app/layout.tsx — wire live + overlays
import { draftMode } from 'next/headers'
import { VisualEditing } from 'next-sanity/visual-editing'
import { SanityLive } from '@/sanity/lib/live'

export default async function RootLayout({ children }: { children: React.ReactNode }) {
  const { isEnabled } = await draftMode()
  return (
    <html><body>
      {children}
      <SanityLive />
      {isEnabled && <VisualEditing />}
    </body></html>
  )
}
```

Add `stega: { studioUrl }` to the client (or per-fetch) so Presentation overlays resolve; keep `stega: false` for metadata/`generateStaticParams` and any non-rendered strings.

## 5. Content modeling best practices

- **Structured rich text, never an HTML blob.** Use Sanity **Portable Text** / Storyblok richtext / Prismic structured fields — portable across web/native, sanitized, styleable. Render with the official serializer (`@portabletext/react`), mapping marks/blocks to *your* components.
- **Components / slices / blocks** = the editable unit. Model them to mirror your design-system sections (hero, feature-grid, quote, gallery). Editors compose pages from your components — they can't break the layout.
- **References vs embedding.** Reference shared/reused entities (author, product, category) so one edit propagates. Embed (inline objects) for content that only lives in one place. Don't duplicate canonical data.
- **Singletons** for one-of-a-kind docs (site settings, home, nav, footer): enforce a single document so editors can't create a second "Settings."
- **Don't over-nest.** Deeply nested objects are painful to edit and query (GROQ/GraphQL). Keep hierarchies shallow; flatten when you can.
- **Design the schema around the design system first.** Field names and block types should map 1:1 to components/tokens. Lock the design system, then model content to fit it — not the reverse.

## 6. Images — use the CMS image CDN + `next/image`

Never hand-resize. CMS image pipelines emit responsive, modern-format, placeholdered images on the fly, cached at the edge — directly feeding Core Web Vitals (LCP/CLS).

- **Sanity** — build URLs with `@sanity/image-url`; pull `asset->metadata.lqip` (base64) for the blur placeholder and `metadata.dimensions` for width/height (prevents CLS).
- **DatoCMS / Storyblok** — `responsiveImage` (Dato) / image service transforms return srcset + sizes + LQIP in one query; render via `react-datocms` `<Image>` or pipe into `next/image`.
- Serve **AVIF/WebP**, supply `sizes`, set explicit `width`/`height` or `aspectRatio`, and a **LQIP/blur** placeholder.

```ts
// sanity/lib/image.ts
import createImageUrlBuilder from '@sanity/image-url'
import { client } from './client'
export const urlFor = (src: any) => createImageUrlBuilder(client).image(src)
```

```tsx
import Image from 'next/image'
import { urlFor } from '@/sanity/lib/image'

// img includes asset->metadata.lqip + metadata.dimensions from the GROQ projection
<Image
  src={urlFor(img).width(1600).auto('format').url()}
  width={img.metadata.dimensions.width}
  height={img.metadata.dimensions.height}
  placeholder="blur"
  blurDataURL={img.metadata.lqip}
  sizes="(max-width: 768px) 100vw, 800px"
  alt={img.alt ?? ''}
/>
```

## 7. i18n / localization (incl. RTL / Arabic)

- **Field-level locales** — one document holds all languages per field (Contentful's default; Sanity via plugin). Best when translations stay structurally in sync and editors work side-by-side. ([Contentful locales](https://www.contentful.com/developers/docs/concepts/locales/))
- **Document-level locales** — a separate document per language, linked by a shared key. Best when locales diverge in structure/sections or have independent publishing workflows.
- **RTL / Arabic bilingual builds (explicit):**
  - Store a locale/`dir` per document or derive it; render `<html lang dir="rtl">` (or a wrapper) per locale.
  - Rich-text editors in Contentful/Sanity support bidirectional editing; preserve any per-block `dir` through to the rendered output.
  - Keep translations as locale variants of the **same** structured content — never a duplicated "Arabic site" with drifting schema.
  - Pair with the `rtl-arabic-i18n` skill for logical-property CSS, font fallbacks, and numeral/date handling; the CMS only owns the content + direction signal.

## 8. Pitfalls

- **Read vs write token security.** Client/preview = **read-only** token, server env only. **Never** expose a write/editor token to the browser or commit it. Mutations happen server-side (Route Handlers / Server Actions) only.
- **Draft content leaking to prod.** Default fetches must use the **published** perspective; only serve drafts behind `draftMode()` + a secret-gated enable route. Disable stega outside draft mode (clean metadata, no encoded markers shipped publicly).
- **CORS.** Lock CMS CORS origins to your exact domains (prod + preview). Wildcards + a leaked read token = open data tap.
- **Rate limits / CDN caching.** Use the CMS CDN endpoint for published reads (`useCdn: true`) and **on-demand revalidation**, not `revalidate: 0`/no-store everywhere — uncached fetch-per-request burns API quota and kills TTFB.
- **Over-modeling.** Too many micro-fields/deep nesting = unusable editor + slow queries. Model the sections editors actually assemble; add fields when a real need appears.
- **Vendor lock-in.** GROQ (Sanity), proprietary slice/block schemas, and managed-only hosting are migration friction. Mitigate: keep content structured + exportable, isolate the CMS behind a typed data layer (one `lib/` module the app imports), and prefer self-host (Payload/Strapi/Craft) when data ownership or exit cost is a hard requirement.
