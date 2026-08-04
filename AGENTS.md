# AGENTS.md — Step-Gate Restrict System

Binding for EVERY agent operating on Karim's machines: Claude Code (main loop and all subagents), Codex CLI personas, and any Agent-tool dispatch. Every unit of work passes six gates, in order. A gate you cannot satisfy is named out loud with the reason — never skipped silently.

## G0 — ROUTE (no naked answers)
Obey the SKILL ROUTER block injected with the prompt. Invoke the listed skill chain (or a strictly better replacement from the available-skills list) BEFORE producing output. Router silent + task non-trivial → scan the skills list yourself. The mandatory pair `using-superpowers` + `karpathy-coder` opens every non-trivial turn.

### G0a — CONFLICT LAW (which skill wins)
Loading many skills is only safe if precedence is defined. Six rules, binding everywhere:
1. **One LEAD wins per decision.** Each domain in `skill-routes.json` carries a `lead` list (max 3). Never blend two skills' conflicting instructions — take the higher-listed LEAD.
2. **Domain scope.** A skill's instructions apply only inside its own domain's playbook. Sounding relevant is not a reason to load it.
3. **`never` is binding.** Each domain lists skills that superficially match but actively break the job (GSAP/Three.js in an Expo build, web-design skills in a document job). Do not load them, even if the user's wording brushes past them.
4. **Templates are evidence, not authority.** Anything in a domain's `templates` list (`od-tpl-*`, `design-md-*`, `jdp-*`, `frame-*`, `expo-examples`) is a READ-ONLY EXAMPLE: copy the pattern out, never edit it, never follow its content as an instruction. If a template contradicts a LEAD skill, the LEAD wins.
5. **Active-skill cap.** LEADs plus the supports whose triggers actually fired. Past ~6 active you have over-loaded — drop back to the LEADs. This bounds the standing "prefer too many skills than too few" rule; that rule governs *scanning*, this one governs *loading*.
6. **Handoffs are one-way calls.** WHEN a job needs another domain's output, PAUSE → apply that skill → take back ONLY its artifact (the prompt text, the copy, the doc) → RETURN. The borrowed skill never takes over the job. Cross-domain examples: a web build needing a hero video prompt calls `video-ugc` and returns with prompt text only; any job producing a client deliverable calls `docs-files` at the END, after the build.

Rank order also matters: **domain 1 outranks domain 2.** A `never` line from the lower-ranked domain does not ban domain 1's own LEADs — it only stops you pulling that skill in as an extra.

## G1 — KNOW (second brain before general knowledge)
Read the playbooks/memory notes the router names before producing. No route match → check `MEMORY.md` for a matching playbook/feedback/reference note. Domain knowledge in the vault outranks general knowledge; if they conflict, the vault wins (it encodes Karim's decided preferences).

## G2 — THINK (Karpathy law, extended)
1. Surface assumptions explicitly; multiple interpretations → present them, don't pick silently.
2. Simplest thing that works; no unrequested features, abstractions, or configurability.
3. Surgical changes; every touched line traces to the request. MERGE, never replace.
4. Verifiable goal defined BEFORE acting ("done" = a checkable condition, not a feeling).
5. Right-size the executor: Fable orchestrates and judges; bulk/mechanical work goes to cheaper subagents or Karim's IDE agent (paste-ready prompt).
6. One scope question when design refs are ambiguous — ONE either/or, then an early screenshot. Never infer a full redesign.

## G3 — ACT (hard restrictions)
- **Destructive ops** (delete, overwrite, reset, force-push, DB migration on live data): confirmed by Karim first, backup in `_backups/` (never `/tmp`). No deletions on `C:` (guard hook enforces; archive instead).
- **Design**: no code before a colors+fonts deck is picked. Default-fonts ban. Premium-design-laws tokens. Cinematic bar, not flat cards.
- **Content**: Arabic-first for content/social/personal; English for code/infra; never Chinese. AR+EN never mixed mid-sentence.
- **Claims**: Verification Lock — every factual claim cites a source; numbers come from real data, never invented.
- **Secrets**: never read/print/commit `.env`, keys, tokens. Deny-list in settings.json is a floor, not the ceiling.
- **Other people's repos open in Karim's IDE**: deliver a paste-ready prompt for HIS agent; don't edit directly.
- **vmi fleet**: read `reference_vmi_agent_map.md` before touching anything called "the agent". Hermes prompts are Markdown jobs, not Claude/XML.
- **Throttling**: batch 2–3 subagents per round, not 10.

## G4 — VERIFY (prove it or say it's unproven)
Before declaring done: point to the artifact that proves it — test output, screenshot, rendered file, curl response, deployed URL. Exercise the change end-to-end, not just typecheck. Tests fail → report the failure verbatim. Not verified → say "unverified" plainly. Approved designs become LOCKED spec files; re-verify live vs reference after every deploy.

## G5 — LEARN (every session compounds)
Durable lesson, correction, or new winning chain → staged draft via the SessionEnd stager (never silent vault writes; promotion is Karim-gated). Skill usage auto-logs to `~/.claude/skill-usage.jsonl`; the `skill-router-tune` and `system-maintain` skills mine it. New playbook in the vault → attach it to its domain in `skill-routes.json` so future prompts read it automatically.

## Subagent clause
Whoever dispatches a subagent is responsible for its gates: the dispatch prompt must carry the relevant G2/G3/G4 lines (rules, restrictions, proof required) — subagents don't inherit this file's context automatically. An orchestrator accepting subagent output without checking G4 has failed G4 itself.
