# PLANMAP — {{PROJECT}}

Slug `{{SLUG}}` · drafted {{DATE}} · status **DRAFT, scope not locked**

Fill every section. A section you cannot answer yet says `TBD — needs decision` on its own
line. Never leave a silent gap; a gap reads as "handled" and it is not.

## 1. Identity

| | |
|---|---|
| One line | |
| Who pays | |
| Platforms | web / iOS / Android / admin |
| Tenancy | single-tenant / B2B multi-tenant |
| Primary language | Arabic / English / both, and which is default |
| Locked with Karim on | |

**Assumptions I made** (each one is a thing he can overrule):

- 

### V1 is done when

Karim's own words from the interview, not a paraphrase:

> 

### Explicitly OUT of V1

Copied verbatim from the interview. Anything on this list that gets built anyway is scope
creep, no matter how small it looked.

- 

## 2. Sitemap — frontend

Every route. Mark access as `public`, `auth`, or `admin`. Group by area.

| Route | Screen | Access | Purpose | Key components |
|---|---|---|---|---|
| `/` | | public | | |

Mobile screens, if any, in their own table with the same columns.

## 3. Backend map

### Tables

| Table | Key columns | RLS policy | Notes |
|---|---|---|---|

### Functions and jobs

| Name | Type | Trigger | Runtime budget |
|---|---|---|---|
| | edge function / cron / queue worker | | |

Long-running work does not belong in an edge function. Anything over the platform's wall-clock
limit goes to the job runner named in section 4.

### Storage

| Bucket | Contents | Public? | Lifecycle |
|---|---|---|---|

## 4. AI layer

| | |
|---|---|
| Gateway | |
| Default model | |
| Escalation model | |
| Fallback | |
| Router rule | when the default fails, or the customer is on a premium tier |

### Model per role

| Agent role | Model | Tools it gets | Why this model |
|---|---|---|---|

### Cost

Assumption for one model call: `___ input tokens + ___ output tokens`. State it — a cost figure
without its token assumption is meaningless.

| Users | Calls/month | Model cost | Fixed infra | Total |
|---|---|---|---|---|
| 10 | | | | |
| 100 | | | | |
| 1,000 | | | | |

Billing unit for customers: not "model call". Weight input tokens, output tokens, tool
executions, build minutes, storage and deploy operations, then add margin.

## 5. Integrations

Every third party. This table is the input to `MANUAL-SETUP.md` — a service missing here is a
service Karim will discover missing at 2am on launch day.

| Service | Purpose | Plan / price | Env var | Set up by |
|---|---|---|---|---|
| | | | `` | AI / **Karim** |

Count: `___` services, `___` of them needing a key Karim must generate himself.

## 6. Design references

| Screen | Mobbin URL | What to take from it |
|---|---|---|

Design system source: which deck option Karim picked, or `PENDING — no code until he picks`.

## 7. Diagrams

- Sitemap (FigJam): 
- System map (FigJam): 
- Mermaid source (fallback): `figma/sitemap.mmd`

## 8. Build phases

Each phase ends in something runnable and a named check that fails if it broke.

| Phase | Ships | Verify checkpoint | Depends on |
|---|---|---|---|
| 1 | | | |

## 9. Risks and open questions for Karim

| # | Question | Blocks | My recommendation |
|---|---|---|---|

## 10. Interview record

Batches run: `___` · both mandatory questions answered: yes / no

| Decision | What he chose | Did I disagree? |
|---|---|---|

## 11. Task list

The build loop ticks these. One line per feature, in build order. A box is ticked only after
it is tested on the real thing, reviewed and committed — see `references/build-loop.md`.

- [ ] 

## 12. Verification log

| Claim | Evidence | Verified? |
|---|---|---|
| prices in section 4 and 5 | source | unverified until checked against vendor pages |
