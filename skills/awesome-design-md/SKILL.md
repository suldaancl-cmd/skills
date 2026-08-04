---
name: awesome-design-md
description: "Curated library of 71 production-grade DESIGN.md files for famous brands — Apple, Stripe, Notion, Linear, Cursor, Vercel, Figma, Tesla, Ferrari, Nike, BMW, Claude, Coinbase, Spotify, Airbnb, and 56 more. Each file is a complete Google-Stitch-format design system: hero brand voice + full color palette (hex tokens) + typography scale + components + layout rules. Use when the user says 'design like X', 'make it feel like Notion / Stripe / Linear', 'use Apple's design language', 'I want a Cursor-style hero', 'pull the design system from Brand Y', or wants a ground-floor design system for a new project sourced from a real production website. Pairs with ui-ux-pro-max (lock the system) and frontend-design (write the code). Source: github.com/VoltAgent/awesome-design-md (50K+ stars)."
---

# awesome-design-md

**71 production DESIGN.md files** ready to feed into `ui-ux-pro-max` or `frontend-design` as the locked design system.

## When to use

The user wants their new website / app / landing page to **feel like a specific famous brand**. Instead of vibing a design from scratch, hand Claude a DESIGN.md from this library — full color tokens, typography scale, components, and brand voice already spec'd.

## How to invoke

```bash
# 1. Find the brand
ls ~/.claude/skills/awesome-design-md/design-md/

# 2. Read its DESIGN.md (use the Read tool)
~/.claude/skills/awesome-design-md/design-md/<brand>/DESIGN.md

# 3. Feed it into the design pipeline:
#    Option A — use directly with frontend-design as the spec
#    Option B — load into ui-ux-pro-max as inspiration, then --persist into MASTER.md
```

## The 71 brands

**SaaS / dev-tool:**
`airtable`, `cal`, `clickhouse`, `cohere`, `composio`, `cursor`, `expo`, `figma`, `framer`, `hashicorp`, `intercom`, `linear.app`, `lovable`, `mintlify`, `miro`, `mongodb`, `notion`, `posthog`, `raycast`, `replicate`, `resend`, `sanity`, `sentry`, `shopify`, `slack`, `stripe`, `supabase`, `superhuman`, `vercel`, `warp`, `webflow`, `zapier`

**AI labs / model providers:**
`claude`, `cohere`, `elevenlabs`, `lovable`, `meta`, `minimax`, `mistral.ai`, `nvidia`, `ollama`, `opencode.ai`, `runwayml`, `together.ai`, `voltagent`, `x.ai`

**Big-brand / consumer:**
`airbnb`, `apple`, `coinbase`, `kraken`, `mastercard`, `meta`, `nike`, `pinterest`, `playstation`, `revolut`, `spacex`, `spotify`, `starbucks`, `tesla`, `uber`, `vodafone`, `wired`, `wise`

**Automotive (rich brand pages):**
`bmw`, `bmw-m`, `bugatti`, `ferrari`, `lamborghini`, `renault`

**Crypto / fintech:**
`binance`, `coinbase`, `kraken`, `mastercard`, `revolut`, `wise`

**Other:**
`clay`, `ibm`, `theverge`

## File format (Google Stitch convention)

Each `DESIGN.md` follows this structure:

```yaml
---
version: alpha
name: <BrandName>
description: <Hero brand voice — one paragraph describing the visual identity>

colors:
  primary: "#..."
  primary-pressed: "#..."
  on-primary: "#..."
  brand-<role>: "#..."
  surface: "#..."
  ink: "#..."
  semantic-success: "#..."
  ... (typically 30-60 color tokens)

typography:
  hero-display:
    fontFamily: <Font>
    fontSize: 80px
    fontWeight: 600
    lineHeight: 1.05
  ... (full type scale)

components: ...
layout: ...
```

## Workflow — design like Notion in 3 commands

```bash
# 1. Read Notion's DESIGN.md
cat ~/.claude/skills/awesome-design-md/design-md/notion/DESIGN.md

# 2. Hand it to ui-ux-pro-max as inspiration + persist
python3 ~/.claude/skills/ui-ux-pro-max/scripts/search.py \
  "productivity workspace tool notion-inspired" \
  --design-system --persist -p "MyApp"

# 3. Invoke frontend-design with the locked design-system/MASTER.md
#    → Claude writes production React/Next code using Notion's tokens
```

## Pairing

| Goal | Pair with |
|---|---|
| Reference a famous brand directly | `awesome-design-md` (this) → `frontend-design` |
| Generate a new design system inspired by Brand X | `awesome-design-md` → `ui-ux-pro-max --persist` → `frontend-design` |
| Reverse-engineer a brand NOT in the 71 list | `skillui <url>` (CLI) instead — generates DESIGN.md from any live site |
| Final quality pass | `impeccable polish` |

## Source

`github.com/VoltAgent/awesome-design-md` — 50K+ stars. The format originated with Google Stitch (`stitch.withgoogle.com`).
