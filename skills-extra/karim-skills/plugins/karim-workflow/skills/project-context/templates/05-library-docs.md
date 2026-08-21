# 05 — Library Docs

> Not generic documentation. **How this project uses each library**, and where to get the
> current truth before writing a line.

## The rule that comes first

Before using any library: **check whether an MCP server is configured for it. If yes, query the
MCP for the live schema, API, or component before writing code.** A remembered API is a guess.
No MCP → check the version pinned in `02-architecture.md`, then the official docs. Never both
half-remembered.

MCP servers available on this machine that matter here: <list the ones this project touches —
e.g. `supabase`, `figma-dev-mode`, `playwright`, `vercel`, `shadcn`.>

---

## <Library name> — <what it does here>

**Version:** `<pinned>` · **MCP:** `<name or none>` · **Docs:** <url>

**We use it for:** <the narrow slice this project actually uses>

**How we call it:**
```ts
// the canonical pattern — copy this shape, do not invent a second one
```

**Rules:**
- <e.g. all queries go through `lib/db/`, never called from a component>
- <e.g. always pass the user id; RLS is on and a missing id returns empty, not an error>

**Gotchas:**
- <the thing that silently breaks — version quirks, SSR issues, Windows path behaviour>

---

## <Library name>

**Version:** · **MCP:** · **Docs:**

**We use it for:**

**How we call it:**
```ts
```

**Rules:**

**Gotchas:**

---

> Add a section the first time a library is used, not before. An unused entry is noise the
> agent still pays tokens to read.
