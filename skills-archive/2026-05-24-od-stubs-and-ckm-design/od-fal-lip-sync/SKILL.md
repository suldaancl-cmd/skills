---
name: od-fal-lip-sync
description: |
  Create talking head videos and lip sync audio to video via fal.ai. Useful for explainer avatars, multilingual dubbing previews, and social cuts.
triggers:
  - "lip sync"
  - "talking head"
  - "audio to video"
  - "avatar video"
  - "fal lipsync"
od:
  mode: video
  category: video-generation
  upstream: "https://github.com/fal-ai-community/skills"
---

> Codex import: this local copy is namespaced as `od-fal-lip-sync` to avoid collisions with existing skills. Upstream source: `nexu-io/open-design/skills/fal-lip-sync`.

# fal-lip-sync

> Curated from the fal.ai community team.

## What it does

Create talking head videos and lip sync audio to video via fal.ai. Useful for explainer avatars, multilingual dubbing previews, and social cuts.

## Source

- Upstream: https://github.com/fal-ai-community/skills
- Category: `video-generation`

## How to use

This catalogue entry advertises the skill in Open Design so the agent
discovers it during planning. To run the full upstream workflow with
its original assets, scripts, and references, install the upstream
bundle into your active agent's skills directory:

```bash
# Inspect the upstream README for exact paths
open https://github.com/fal-ai-community/skills
```

Then ask the agent to invoke this skill by name (`fal-lip-sync`) or with
one of the trigger phrases listed in this skill's frontmatter.

