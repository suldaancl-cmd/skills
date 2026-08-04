---
name: session-intake
description: Classify what Karim just dropped into the chat (a link, a thing to build, a topic to study/download) and open the right workspace for it before doing any work. Use at the start of any chat that introduces new work — a shared URL, "build me X", "study this project", a downloaded repo/site, or a research topic. Creates ~/.claude/_projects/<slug>/ with CLAUDE.md, AGENTS.md, SKILLS.md (every matching skill on disk, ranked), NOTES.md and sources/.
---

# Session intake

Karim's chats start one of three ways. Pick the lane, then work.

## Lane 1 — he shared a link

Any URL. Social/video (TikTok, IG, YouTube, X, Reddit, direct media) → `read-link` first, full
4-phase deep dive; the analysis is the deliverable. Then the shared-link protocol in CLAUDE.md:
Arabic explanation if it carries knowledge, vault note if the brain benefits, playbook or skill
if it's a tool. Open a workspace too when the link kicks off real work (a study, a build, a teardown):

```bash
python ~/.claude/scripts/topic_workspace.py --topic "<what the link is about>" --kind link --prompt "<his message>"
```

Put the transcript, screenshots, and downloads in `sources/`.

## Lane 2 — he wants something built

App, site, deck, video, campaign, agent. Open the workspace first, then follow the domain's rules
(deck-first for design, validation-before-code for apps):

```bash
python ~/.claude/scripts/topic_workspace.py --topic "<the build>" --kind build --prompt "<his message>"
```

`--kind build` also drops ADVISE.md + DESIGN.md from the project template.

## Lane 3 — study / download / research a topic

A repo he cloned, a site he mirrored, a market to research, a system to understand:

```bash
python ~/.claude/scripts/topic_workspace.py --topic "<the topic>" --kind study --prompt "<his message>"
```

## Then, every lane

1. Read the generated `BRAIN.md` — every second-brain file matching the topic across all ~3400
   vault files: Brain topic hubs first, then curated notes, kit, past chats, intel runs, reports,
   Notion, Hermes knowledge, fleet output. The brain outranks general knowledge; if they disagree,
   say so out loud. Nothing gets answered from memory alone when the vault has a file on it.
2. Read the generated `SKILLS.md` — it ranks every skill on disk against the topic (often 100–400
   of ~1600) and pins the routing-table chain at the top. Invoke the ranked chain; reach into the
   long tail as the work goes deeper.
3. Read the playbooks the generated `CLAUDE.md` lists (they come from `skill-routes.json`).
4. Work inside the folder. Findings and decisions go in `NOTES.md`, artifacts in the folder, never
   in a scratch dir.
5. If the topic is new to the routing table, add it to `skill-routes.json` (the `skill-router-tune`
   skill does this) so the next matching prompt routes itself.

Continuing work he already has a folder for? Skip creation — read that folder's `CLAUDE.md` and
`SKILLS.md` instead, and regenerate `SKILLS.md` if new skills were installed since.

Skip intake entirely for one-liners, quick lookups, and chat about work already in flight.
