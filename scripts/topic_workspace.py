"""Create a topic workspace under ~/.claude/_projects/<slug>/ with an auto-built
SKILLS.md manifest of every skill in the library that matches the topic.

Usage:
  python topic_workspace.py --topic "arabic wedding app onboarding" [--slug zefaf-onboarding]
                            [--kind build|study|link] [--prompt "<original user message>"]
                            [--detail 25]

Writes: README.md, SKILLS.md, CLAUDE.md, AGENTS.md, NOTES.md, sources/
kind=build also copies ADVISE/DESIGN templates from _projects/_TEMPLATE.
Prints the created path. Never overwrites an existing file.
"""
import argparse
import json
import math
import os
import re
import shutil
from datetime import date

HOME = os.path.expanduser("~")
CLAUDE = os.path.join(HOME, ".claude")
PROJECTS = os.path.join(CLAUDE, "_projects")
TEMPLATE = os.path.join(PROJECTS, "_TEMPLATE")
ROUTES = os.path.join(CLAUDE, "skill-routes.json")
# (root, label) in priority order — first hit for a skill name wins.
SKILL_ROOTS = [
    (os.path.join(CLAUDE, "skills"), ""),
    (os.path.join(HOME, ".agents", "skills"), "agents"),
    (os.path.join(HOME, ".adal", "skills"), "adal"),
    (os.path.join(CLAUDE, "skills-archive"), "archived"),
]
VAULT = "~/.claude/projects/C--Users-user--claude-skills/memory"

STOP = set("""a an the and or of for to in on with my me i we our your this that it its is are be
make making create new build built help please need want using use how what when all some
thing things stuff about from into""".split())


def words(text):
    return [w for w in re.findall(r"[a-z0-9]{3,}", text.lower()) if w not in STOP]


def load_skills():
    """{skill_name: (description, label)} for every SKILL.md under every root, at any depth."""
    out = {}
    for root, label in SKILL_ROOTS:
        if not os.path.isdir(root):
            continue
        for dirpath, _dirs, files in os.walk(root):
            if "SKILL.md" not in files:
                continue
            name = os.path.basename(dirpath)
            if name in out:
                continue
            try:
                with open(os.path.join(dirpath, "SKILL.md"), encoding="utf-8", errors="ignore") as fh:
                    head = fh.read(2000)
            except OSError:
                continue
            out[name] = (parse_description(head), label)
    return out


def parse_description(head):
    """Frontmatter description, including YAML block scalars (`description: |`).

    ~400 skills use the block form; a plain one-line regex captures just "|" and
    silently scores them at zero against every query.
    """
    m = re.search(r"^description:\s*(.*)$", head, re.M)
    if not m:
        return ""
    first = m.group(1).strip()
    if first not in ("|", ">", "|-", ">-", "|+", ">+"):
        return first.strip("\"'")
    body = []
    for line in head[m.end():].splitlines()[1:]:
        if line.strip() and not line[:1].isspace():
            break  # next top-level key ends the block
        body.append(line.strip())
    return " ".join(b for b in body if b).strip()


VAULT_DIR = os.path.join(CLAUDE, "projects", "C--Users-user--claude-skills", "memory")
# (subpath, section title, cap) — "" is the vault root (the curated notes).
VAULT_SECTIONS = [
    ("Brain/Topics", "Brain topic hubs — open these FIRST", 6),
    ("", "Curated notes (feedback / reference / playbook / project)", 30),
    ("app-building-kit", "App-Building Kit", 10),
    ("Sessions", "Past chats", 15),
    ("Intel-Runs", "Intel runs", 10),
    ("Reports", "Reports", 15),
    ("Notion", "Notion", 10),
    ("Hermes-Knowledge", "Hermes knowledge", 10),
    ("Fleet-Output", "Fleet output", 10),
    ("Brain/Links", "Link indexes", 5),
]


def scan_vault(topic_words):
    """[(title, [(score, relpath)], total_matched)] across the second brain."""
    out = []
    for sub, title, cap in VAULT_SECTIONS:
        root = os.path.join(VAULT_DIR, sub) if sub else VAULT_DIR
        if not os.path.isdir(root):
            continue
        hits = []
        walker = (
            [(root, [], sorted(f for f in os.listdir(root) if f.endswith(".md")))]
            if sub == "" else os.walk(root)
        )
        for dirpath, _dirs, files in walker:
            for fname in files:
                if not fname.endswith(".md"):
                    continue
                s = sum(2 for w in topic_words if w in fname[:-3].lower())
                if s:
                    rel = os.path.relpath(os.path.join(dirpath, fname), VAULT_DIR).replace("\\", "/")
                    hits.append((s, rel))
        if hits:
            hits.sort(key=lambda x: (-x[0], x[1]))
            out.append((title, hits[:cap], len(hits)))
    return out


def load_agents():
    """{agent_name: description} from ~/.claude/agents/*.md (skips .backup files)."""
    out = {}
    root = os.path.join(CLAUDE, "agents")
    if not os.path.isdir(root):
        return out
    for fname in sorted(os.listdir(root)):
        if not fname.endswith(".md") or ".backup" in fname:
            continue
        try:
            with open(os.path.join(root, fname), encoding="utf-8", errors="ignore") as fh:
                head = fh.read(1500)
        except OSError:
            continue
        desc = re.search(r"^description:\s*(.+)$", head, re.M)
        out[fname[:-3]] = desc.group(1).strip().strip('"\'') if desc else ""
    return out


def load_tools():
    """(mcp_servers, plugins) configured on this machine."""
    mcp, plugins = [], []
    try:
        with open(os.path.join(CLAUDE, ".mcp.json"), encoding="utf-8") as fh:
            mcp = sorted(json.load(fh).get("mcpServers", {}))
    except (OSError, ValueError):
        pass
    try:
        with open(os.path.join(CLAUDE, "settings.json"), encoding="utf-8") as fh:
            ep = json.load(fh).get("enabledPlugins", {})
        plugins = sorted(k for k, v in ep.items() if v) if isinstance(ep, dict) else sorted(ep)
    except (OSError, ValueError):
        pass
    return mcp, plugins


def match_domains(topic_words):
    try:
        with open(ROUTES, encoding="utf-8") as fh:
            table = json.load(fh)
    except OSError:
        return []
    scored = []
    for d in table.get("domains", []):
        hits = sum(1 for kw in d.get("keywords", []) if any(w in kw.lower() for w in topic_words))
        if hits:
            scored.append((hits, d))
    return [d for _h, d in sorted(scored, key=lambda x: -x[0])[:2]]


def rank_skills(topic_words, skills, pinned):
    """pinned is the ORDERED routing chain — earlier in the chain must rank higher,
    so the bonus decays with position instead of being flat (flat ties broke alphabetically
    and silently discarded the table's deliberate order).

    Topic words are IDF-weighted: "design" occurs in 652 of 1610 skills and carries almost
    no signal, "immersive" occurs in ~12 and carries nearly all of it. Weighting them equally
    swamped the ranking with hundreds of false matches (every `design-md-*` scored on the
    word "design"; "check" pulled in `antd-component-checkbox`)."""
    bonus = {name: 50 - i for i, name in enumerate(pinned)}
    n = len(skills) or 1
    idf = {}
    for w in set(topic_words):
        df = sum(1 for nm, (d, _l) in skills.items() if w in nm.lower() or w in d.lower())
        idf[w] = math.log(n / df) if df else math.log(n)
    ranked = []
    for name, (desc, label) in skills.items():
        nl, dl = name.lower(), desc.lower()
        s = (sum(3 * idf[w] for w in topic_words if w in nl)
             + sum(1 * idf[w] for w in topic_words if w in dl))
        s += bonus.get(name, 0)
        if s:
            ranked.append((round(s, 1), name, desc, label))
    return sorted(ranked, key=lambda x: (-x[0], x[1]))


def write(path, text):
    if os.path.exists(path):
        return False
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--topic", required=True)
    ap.add_argument("--slug")
    ap.add_argument("--kind", default="study", choices=["build", "study", "link"])
    ap.add_argument("--prompt", default="")
    ap.add_argument("--detail", type=int, default=25)
    ap.add_argument("--root", help="where _projects/ lives; default: the repo you are in, "
                                   "falling back to ~/.claude")
    a = ap.parse_args()

    # In an IDE session the workspace belongs INSIDE the open repo, not in ~/.claude —
    # otherwise the folder is invisible in the editor tree and unversioned with the code.
    base = a.root or (CLAUDE if os.getcwd().lower().startswith(CLAUDE.lower()) else os.getcwd())
    projects = PROJECTS if base == CLAUDE else os.path.join(base, "_projects")

    slug = a.slug or re.sub(r"[^a-z0-9]+", "-", a.topic.lower()).strip("-")[:48]
    root = os.path.join(projects, slug)
    os.makedirs(os.path.join(root, "sources"), exist_ok=True)

    tw = words(a.topic)
    domains = match_domains(tw)
    pinned = [s for d in domains for s in d.get("skills", [])]
    library = load_skills()
    ranked = rank_skills(tw, library, pinned)  # ordered list, not a set — order carries the rank
    today = date.today().isoformat()

    chain = " -> ".join(pinned) if pinned else "(no routing-table domain matched)"
    rules = [d.get("rule", "") for d in domains if d.get("rule")]
    playbooks = [f"{VAULT}/{p}" for d in domains for p in d.get("playbooks", [])]

    detail = ranked[: a.detail]
    tail = ranked[a.detail :]
    arch = sum(1 for _s, _n, _d, lb in ranked if lb == "archived")
    lines = [f"# Skills for: {a.topic}", "",
             f"Auto-ranked {today}: **{len(ranked)} matched** out of **{len(library)} skills** scanned "
             f"across {len([r for r, _l in SKILL_ROOTS if os.path.isdir(r)])} roots "
             f"({arch} of the matches are in `skills-archive/` — restore before use). "
             "Regenerate with `topic_workspace.py` after installing skills.", "",
             f"## Ranked chain (routing table: {', '.join(d['name'] for d in domains) or 'none'})",
             "", chain, ""]
    drift = [p for p in pinned if p not in library]
    if drift:
        lines += [f"> DRIFT — in `skill-routes.json` but not on disk: {', '.join('`' + x + '`' for x in drift)}. "
                  "Plugin-namespaced or uninstalled; fix with `skill-router-tune`.", ""]
    lines += ["## Best matches — invoke these", ""]
    for s, n, d, lb in detail:
        tag = f" `[{lb}]`" if lb else ""
        lines.append(f"- **{n}** ({s}){tag} — {d[:170]}")
    if tail:
        lines += ["", f"## Long tail ({len(tail)} more, names only — invoke if the work reaches them)", "",
                  ", ".join(f"`{n}`" + (f"[{lb}]" if lb else "") for _s, n, _d, lb in tail)]
    write(os.path.join(root, "SKILLS.md"), "\n".join(lines) + "\n")

    brain = scan_vault(tw)
    btotal = sum(t for _title, _hits, t in brain)
    blines = [f"# Second brain for: {a.topic}", "",
              f"{btotal} vault files matched on {today}. Read the hubs first, then anything below "
              "that touches the task — the brain outranks general knowledge.", "",
              f"Vault root: `{VAULT}` — wikilinks below open in Obsidian, "
              "paths resolve for Read.", "",
              "- Entry point: [[Brain/HOME]] · Index: [[MEMORY]]", ""]
    for title, hits, total in brain:
        shown = f" (top {len(hits)} of {total})" if total > len(hits) else ""
        blines += [f"## {title}{shown}", ""]
        blines += [f"- [[{rel[:-3]}]] — `{VAULT}/{rel}`" for _s, rel in hits]
        blines.append("")
    write(os.path.join(root, "BRAIN.md"), "\n".join(blines) + "\n")

    write(os.path.join(root, "README.md"), f"""# {slug}

- **Kind:** {a.kind}
- **Topic:** {a.topic}
- **Opened:** {today}

## Original ask

> {a.prompt or a.topic}

## Files

- `BRAIN.md` — every matching second-brain file. Read before general knowledge.
- `SKILLS.md` — every matching skill, ranked. Read before working.
- `CLAUDE.md` — purpose + hard rules for this workspace.
- `AGENTS.md` — agent roster + gates for dispatches.
- `NOTES.md` — findings / decisions log, newest last.
- `sources/` — downloads, screenshots, transcripts, references.
""")

    write(os.path.join(root, "CLAUDE.md"), f"""# {slug} — working context

**Purpose:** {a.topic}
**Kind:** {a.kind} · **Opened:** {today}

Reading order — no output before all three: (1) `BRAIN.md` — every matching vault file
({btotal} matched), Brain hubs first · (2) `SKILLS.md` — invoke the ranked chain · (3) the
playbooks below. The second brain outranks general knowledge; if the two disagree, say so.
{chr(10).join('- ' + p for p in playbooks) or '- (none matched — check MEMORY.md)'}

## Hard rules in force
{chr(10).join('- ' + r for r in rules) or '- Inherit the global rules in ~/.claude/CLAUDE.md.'}
- Bilingual EN + AR on substantive answers. MERGE, never replace. Verify or say "unverified".

## State
- [ ] Scope locked with Karim
- [ ] Sources in `sources/`
- [ ] Deliverable defined
""")

    agents = load_agents()
    aranked = sorted(
        ((sum(3 for w in tw if w in n.lower()) + sum(1 for w in tw if w in d.lower()), n, d)
         for n, d in agents.items()),
        key=lambda x: (-x[0], x[1]))
    apick = [a for a in aranked if a[0]][:5] or [(0, n, agents.get(n, "")) for n in
                                                ("researcher", "shipper", "reviewer") if n in agents]
    mcp, plugins = load_tools()
    top_skills = [n for _s, n, _d, _l in detail[:6]]

    dispatch = f"""Gates G0-G5 bind you (they are NOT inherited automatically — that is why they are here):
G0 ROUTE — invoke these skills first: {', '.join(top_skills) or 'see SKILLS.md'}.
G1 KNOW  — read `_projects/{slug}/BRAIN.md` and open every vault file it lists that touches
           your task. The second brain outranks your general knowledge; if they disagree, say so.
G2 THINK — Karpathy: state assumptions, simplest thing that works, surgical changes only.
G3 ACT   — work inside `_projects/{slug}/`. Confirm before destructive ops. MERGE, never replace.
G4 VERIFY— point to the artifact/output that proves each claim. Unproven = say "unverified".
G5 LEARN — append findings to `_projects/{slug}/NOTES.md`.
Tools available to you: local MCP {', '.join(mcp) or 'none'}; for connector MCPs run
ToolSearch with keywords "{' '.join(tw[:5])}" before saying a capability is unavailable.
Full skill list: `_projects/{slug}/SKILLS.md`. Tool + agent map: `_projects/{slug}/TOOLS.md`."""

    write(os.path.join(root, "AGENTS.md"), f"""# {slug} — agent roster

Matched from `~/.claude/agents/` against this topic. Batch 2-3 per round (throttling rule).
Backups go to `_backups/`, never /tmp.

| Agent | Why it matched |
|---|---|
""" + "\n".join(f"| `{n}` | {d[:120]} |" for _s, n, d in apick) + f"""

## Paste this into EVERY dispatch

```
{dispatch}
```
""")

    write(os.path.join(root, "TOOLS.md"), f"""# Tools for: {a.topic}

## MCP — configured locally ({len(mcp)})
{chr(10).join('- `' + m + '`' for m in mcp) or '- none in .mcp.json'}

## MCP — connectors (Gamma, Figma, Notion, Vercel, Supabase, Adobe, Higgsfield, Apify, ...)
Not listed on disk; they load on demand. Before declaring any capability unavailable, run
`ToolSearch` with: `{' '.join(tw[:6])}`

## Plugins enabled ({len(plugins)})
{chr(10).join('- `' + p + '`' for p in plugins) or '- none'}

## Agents matched ({len(apick)})
{chr(10).join('- `' + n + '` — ' + d[:110] for _s, n, d in apick)}

Dispatch briefing to paste: see `AGENTS.md`.
""")

    write(os.path.join(root, "NOTES.md"), f"# Notes — {slug}\n\n## {today}\n\n- Workspace created.\n")

    if a.kind == "build" and os.path.isdir(TEMPLATE):
        for f in ("ADVISE.template.md", "DESIGN.template.md"):
            src, dst = os.path.join(TEMPLATE, f), os.path.join(root, f.replace(".template", ""))
            if os.path.isfile(src) and not os.path.exists(dst):
                shutil.copyfile(src, dst)

    print(root)
    print(f"skills: {len(ranked)} matched of {len(library)} scanned (detailed: {len(detail)}, "
          f"archived: {arch}) | domains: {', '.join(d['name'] for d in domains) or 'none'}")


if __name__ == "__main__":
    main()
