#!/usr/bin/env python3
"""
build_second_brain.py — Connected "second brain" indexer for Karim's Obsidian vault.

Reads (read-only): skills, Claude Code transcripts, vault Sessions/, Notion/,
Intel-Runs/, Fleet-Output/, Hermes-Knowledge/, and memory reference/playbook/project notes.
Writes (only): vault  Brain/  — topic MOCs that cross-link everything related to a topic,
plus a home dashboard, skills catalog, links index, and reports index.

Idempotent: regenerates Brain/ on every run. Safe to schedule hourly.
Tune by editing TOPICS and LINK_CATEGORY below.
"""
import os, re, glob, json, collections, datetime

# ---------- paths ----------
VAULT = r"C:/Users/user/.claude/projects/C--Users-user--claude-skills/memory"
SKILLS_DIR = r"C:/Users/user/.claude/skills"
# Every live skill root, priority order — first hit for a skill name wins.
SKILL_ROOTS = [
    SKILLS_DIR,
    r"C:/Users/user/.agents/skills",
    r"C:/Users/user/.adal/skills",
]
PROJECTS = r"C:/Users/user/.claude/projects"
BRAIN = os.path.join(VAULT, "Brain")

# ---------- topic taxonomy (keyword -> topic) ----------
# An item is tagged with EVERY topic whose keywords it matches (word-boundary match).
# Keep keywords DISTINCTIVE (tool/tech names, multi-word phrases) — bare generic words
# ("design", "data", "agent", "api") over-match and were removed.
TOPICS = {
    "design-web":        ["framer", "webflow", "tailwind", "landing page", "typography", "awwwards",
                          "lenis", "gsap", "figma", "design system", "hero section", "shadcn",
                          "ui component", "superdesign", "editorial", "color palette", "font pairing",
                          "css grid", "web design", "ui/ux"],
    "3d-animation":      ["three.js", "threejs", "r3f", "react three", "react-three", "webgl", "shader",
                          "spline", "blender", "gltf", "glb", "pixijs", "babylon", "webgpu", "drei",
                          "postprocessing", "3d model", "3d scene"],
    "motion-animation":  ["framer motion", "gsap", "lottie", "rive", "scrolltrigger", "keyframe",
                          "anime.js", "animejs", "kinetic typography", "motion design", "scroll animation"],
    "video-ugc":         ["ugc", "higgsfield", "seedance", "remotion", "ffmpeg", "hyperframes", "b-roll",
                          "kling", "runway", "veo", "sora", "capcut", "video ad", "reel", "tiktok video",
                          "shorts"],
    "image-gen":         ["nano banana", "imagen", "midjourney", "photoshoot", "rembg", "gpt image",
                          "firefly", "stable diffusion", "flux model", "image gen", "upscale"],
    "mobile-app":        ["expo", "react native", "swiftui", "app store", "aso", "eas build", "mmkv",
                          "ios app", "android app", "flutter", "mobile app"],
    "marketing-content": ["copywriting", "cold email", "advertising", "ad creative", "campaign",
                          "seo", "cro", "sales funnel", "brand voice", "newsletter", "content strategy",
                          "social media", "instagram", "linkedin", "email sequence"],
    "saas-web":          ["saas", "supabase", "stripe", "next.js", "nextjs", "postgres", "vercel deploy",
                          "subscription", "multitenant", "clerk", "webhook", "auth.js", "better auth",
                          "payment", "rest api"],
    "ai-agents":         ["hermes", "mcp server", "n8n", "claude code", "codex", "subagent",
                          "orchestrat", "prompt engineering", "agent fleet", "workflow automation",
                          "skill router", "ai agent"],
    "data-analytics":    ["analytics", "dashboard", "sql query", "statistical", "data viz",
                          "visualization", "d3.js", "bigquery", "kpi", "metrics definition", "chart"],
    "slides-docs":       ["slides", "deck", "pptx", "presentation", "keynote", "pdf", "docx", "carousel",
                          "gamma", "one-pager", "pitch deck"],
    "research-strategy": ["opportunity", "market research", "competitor", "deep research", "trend",
                          "validation", "tam", "icp", "pricing strategy", "market analysis",
                          "go-to-market", "gtm"],
    "audio-voice":       ["elevenlabs", "voice clone", "tts", "podcast", "dubbing", "fish audio",
                          "voiceover", "text to speech", "music generation"],
    "security":          ["pentest", "red team", "security audit", "vulnerab", "prompt injection",
                          "guardrail", "owasp", "cve", "threat model", "exploit"],
    "vmi-infra":         ["vmi", "docker", "devops", "nginx", "systemd", "rclone", "syncthing",
                          "37.60.243.30", "vps", "cron job"],
    "aistudiotoday":     ["aistudiotoday", "ai studio today", "darkroom", "clinic template", "safa"],
}

# ---------- link category (domain substring -> category) ----------
LINK_CATEGORY = [
    ("design-inspiration", ["mobbin", "awwwards", "dribbble", "behance", "readdy", "website-files.com",
                            "godly", "land-book", "lapa.ninja", "cssdesignawards", "siteinspire"]),
    ("code-dev",           ["github.com", "gitlab", "vercel.com", "supabase", "nextjs.org", "npmjs",
                            "stackoverflow", "developer.mozilla", "railway", "netlify", "cloudflare"]),
    ("video-social",       ["youtube.com", "youtu.be", "instagram.com", "tiktok", "x.com", "twitter.com",
                            "reddit.com", "vimeo", "facebook.com", "linkedin.com"]),
    ("fonts-assets",       ["fonts.google", "fonts.gstatic", "unsplash", "cloudfront.net", "pexels",
                            "fontshare", "cdnfonts", "iconify", "lottiefiles"]),
    ("figma",              ["figma.com"]),
    ("docs-research",      ["docs.google", "news.ycombinator", "arxiv", "medium.com", "notion.so",
                            "substack", "huggingface"]),
    ("own-sites",          ["aistudiotoday", "37.60.243.30"]),
]

SKIP_URL = ("anthropic.com", "json-schema", "w3.org", "schemas.", "avatars.githubusercontent",
            "sentry.io", "statsig", "claude.ai/api", "localhost", "127.0.0.1", "registry.npm",
            "googleapis.com/auth", "gstatic.com/recaptcha")

TOPIC_TITLES = {
    "design-web": "Design & Web", "3d-animation": "3D & WebGL", "motion-animation": "Motion & Animation",
    "video-ugc": "Video & UGC", "image-gen": "Image Generation", "mobile-app": "Mobile Apps",
    "marketing-content": "Marketing & Content", "saas-web": "SaaS & Backend", "ai-agents": "AI Agents & Automation",
    "data-analytics": "Data & Analytics", "slides-docs": "Slides & Documents", "research-strategy": "Research & Strategy",
    "audio-voice": "Audio & Voice", "security": "Security", "vmi-infra": "vmi & Infra", "aistudiotoday": "AISTUDIOTODAY",
}

# pre-compile word-boundary matchers per topic
_TOPIC_RE = {t: [re.compile(r"\b" + re.escape(kw) + r"\b") for kw in kws] for t, kws in TOPICS.items()}

def classify(text):
    t = text.lower()
    hits = set()
    for topic, regexes in _TOPIC_RE.items():
        for rx in regexes:
            if rx.search(t):
                hits.add(topic); break
    return hits

def wl(basename):
    """Obsidian wikilink from a basename (strip .md)."""
    return "[[%s]]" % os.path.splitext(os.path.basename(basename))[0]

# ---------- 1. SKILLS ----------
def load_skills():
    skills = []
    seen = set()
    paths = []
    for root in SKILL_ROOTS:
        for dirpath, _dirs, files in os.walk(root):
            if "SKILL.md" in files:
                paths.append(os.path.join(dirpath, "SKILL.md"))
    for sk in sorted(paths, key=lambda p: os.path.basename(os.path.dirname(p))):
        name = os.path.basename(os.path.dirname(sk))
        if name in seen:
            continue
        seen.add(name)
        desc = ""
        try:
            with open(sk, encoding="utf-8", errors="ignore") as f:
                head = f.read(4000)
            m = re.search(r"description:\s*(.+?)(?:\n[a-z_]+:|\n---)", head, re.S)
            if m:
                desc = " ".join(m.group(1).split())[:300]
        except Exception:
            pass
        topics = classify(name.replace("-", " ") + " " + desc)
        skills.append({"name": name, "desc": desc, "topics": topics})
    return skills

# ---------- 2. LINKS ----------
URL_RE = re.compile(r'https?://[^\s"\'\)\]\}<>\\]+')
def load_links():
    links = {}  # url -> {count, sessions:set}
    for f in glob.glob(os.path.join(PROJECTS, "*", "*.jsonl")):
        sess = os.path.basename(f)
        try:
            with open(f, encoding="utf-8", errors="ignore") as fh:
                for line in fh:
                    for u in URL_RE.findall(line):
                        u = u.rstrip('.,";)”')
                        if any(s in u for s in SKIP_URL):
                            continue
                        if len(u) < 12:
                            continue
                        d = links.setdefault(u, {"count": 0, "sessions": set()})
                        d["count"] += 1
                        d["sessions"].add(sess)
        except Exception:
            pass
    # categorize + topic-tag
    for u, d in links.items():
        dom = u.split("/")[2] if len(u.split("/")) > 2 else u
        cat = "other"
        for c, subs in LINK_CATEGORY:
            if any(s in u for s in subs):
                cat = c; break
        d["domain"] = dom
        d["cat"] = cat
        d["topics"] = classify(u)
    return links

# ---------- 3. SESSIONS ----------
def load_sessions():
    out = []
    for f in glob.glob(os.path.join(VAULT, "Sessions", "**", "*.md"), recursive=True):
        base = os.path.basename(f)
        if base in ("INDEX.md",) or base.startswith("INVENTORY") or base.startswith("SKILL"):
            continue
        title = base
        try:
            with open(f, encoding="utf-8", errors="ignore") as fh:
                header = fh.read(300)
        except Exception:
            header = ""
        # title carries most signal; header is a short, curated topical lead
        topics = classify(base.replace("-", " ").replace("_", " ") + " " + header)
        out.append({"title": title, "topics": topics})
    return out

# ---------- 4. REPORTS / RESEARCHES / NOTES ----------
def load_reports():
    out = []
    sources = [
        ("Intel-Runs", glob.glob(os.path.join(VAULT, "Intel-Runs", "*.md"))),
        ("Notion", glob.glob(os.path.join(VAULT, "Notion", "**", "*.md"), recursive=True)),
        ("Fleet-Output", glob.glob(os.path.join(VAULT, "Fleet-Output", "**", "*.md"), recursive=True)),
        ("Hermes-Knowledge", glob.glob(os.path.join(VAULT, "Hermes-Knowledge", "**", "*.md"), recursive=True)),
        ("GoogleDocs", glob.glob(os.path.join(BRAIN, "Reports", "GoogleDocs", "*.md"))),
        ("Memory", [p for p in glob.glob(os.path.join(VAULT, "*.md"))
                    if os.path.basename(p).startswith(("reference_", "playbook_", "project_"))]),
    ]
    for src, files in sources:
        for f in files:
            base = os.path.basename(f)
            # classify on TITLE ONLY — cleanest signal; timestamp-named auto-logs
            # (e.g. Intel-Runs "2026-05-04_07h.md") match nothing and stay out of hubs.
            topics = classify(base.replace("_", " ").replace("-", " "))
            # GoogleDocs are hand-curated with frontmatter `tags:` = topic slugs — honor them.
            if src == "GoogleDocs":
                try:
                    with open(f, encoding="utf-8", errors="ignore") as fh:
                        header = fh.read(400).lower()
                    topics |= {t for t in TOPICS if t in header}
                except Exception:
                    pass
            out.append({"title": base, "source": src, "topics": topics})
    return out

# ---------- writers ----------
def ensure(path):
    os.makedirs(path, exist_ok=True)

def write(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

def main():
    ensure(BRAIN); ensure(os.path.join(BRAIN, "Topics"))
    ensure(os.path.join(BRAIN, "Skills")); ensure(os.path.join(BRAIN, "Links"))
    ensure(os.path.join(BRAIN, "Reports"))
    today = os.environ.get("SB_DATE", datetime.date.today().isoformat())

    skills = load_skills()
    links = load_links()
    sessions = load_sessions()
    reports = load_reports()

    # ----- Skills catalog -----
    by_topic_sk = collections.defaultdict(list)
    for s in skills:
        for t in (s["topics"] or {"_uncategorized"}):
            by_topic_sk[t].append(s)
    lines = ["---", "tags: [second-brain, skills]", "---",
             "# Skills Catalog  #second-brain/skills", "",
             f"**{len(skills)} skills** grouped by topic. Invoke any via the Skill tool.  ·  Home: [[HOME]]", ""]
    for t in list(TOPICS) + ["_uncategorized"]:
        items = by_topic_sk.get(t, [])
        if not items:
            continue
        lines.append(f"## {TOPIC_TITLES.get(t, t)}  ({len(items)})")
        if t in TOPICS:
            lines.append(f"→ hub: [[{t}]]")
        for s in sorted(items, key=lambda x: x["name"]):
            d = (s["desc"][:130] + "…") if len(s["desc"]) > 130 else s["desc"]
            lines.append(f"- `{s['name']}` — {d}")
        lines.append("")
    write(os.path.join(BRAIN, "Skills", "CATALOG.md"), "\n".join(lines))

    # ----- Links index -----
    by_cat = collections.defaultdict(list)
    for u, d in links.items():
        by_cat[d["cat"]].append((u, d))
    idx = ["---", "tags: [second-brain, links]", "---",
           f"# Links Index  #second-brain/links", "",
           f"**{len(links)} unique links** harvested from Claude Code chats.  ·  Home: [[HOME]]", "",
           "| Category | Links |", "|---|---|"]
    for cat, _ in LINK_CATEGORY + [("other", None)]:
        idx.append(f"| [[links-{cat}\\|{cat}]] | {len(by_cat.get(cat, []))} |")
    write(os.path.join(BRAIN, "Links", "INDEX.md"), "\n".join(idx))
    for cat, items in by_cat.items():
        items.sort(key=lambda x: -x[1]["count"])
        L = ["---", "tags: [second-brain, links]", "---",
             f"# Links — {cat}  ({len(items)})", "", "Back: [[Brain/Links/INDEX|Links index]] · [[HOME]]", ""]
        for u, d in items[:600]:
            L.append(f"- [{d['domain']}]({u}) ×{d['count']}")
        if len(items) > 600:
            L.append(f"\n_+{len(items)-600} more_")
        write(os.path.join(BRAIN, "Links", f"links-{cat}.md"), "\n".join(L))

    # ----- Reports index -----
    by_src = collections.defaultdict(list)
    for r in reports:
        by_src[r["source"]].append(r)
    R = ["---", "tags: [second-brain, reports]", "---",
         f"# Reports & Researches  ({len(reports)})  #second-brain/reports", "",
         "All research/report/knowledge notes in the vault, by source.  ·  Home: [[HOME]]", ""]
    for src, items in sorted(by_src.items()):
        R.append(f"## {src}  ({len(items)})")
        for r in sorted(items, key=lambda x: x["title"])[:200]:
            R.append(f"- {wl(r['title'])}")
        if len(items) > 200:
            R.append(f"_+{len(items)-200} more_")
        R.append("")
    write(os.path.join(BRAIN, "Reports", "INDEX.md"), "\n".join(R))

    # ----- Topic hubs (the CONNECTIONS) -----
    counts = {}
    for t in TOPICS:
        sk = sorted([s for s in skills if t in s["topics"]], key=lambda x: x["name"])
        lk = sorted([(u, d) for u, d in links.items() if t in d["topics"]], key=lambda x: -x[1]["count"])
        se = sorted([s for s in sessions if t in s["topics"]], key=lambda x: x["title"], reverse=True)
        rp = sorted([r for r in reports if t in r["topics"]], key=lambda x: x["title"])
        counts[t] = (len(sk), len(lk), len(se), len(rp))
        H = ["---", f"tags: [second-brain, topic]", f"aliases: [{TOPIC_TITLES[t]}]", "---",
             f"# {TOPIC_TITLES[t]}  #second-brain/topic", "",
             f"Everything related to **{TOPIC_TITLES[t]}** — connected. Home: [[HOME]]", "",
             f"`{len(sk)} skills` · `{len(lk)} links` · `{len(se)} chats` · `{len(rp)} reports`", ""]
        H.append(f"## 🛠 Skills ({len(sk)})")
        for s in sk:
            d = (s["desc"][:120] + "…") if len(s["desc"]) > 120 else s["desc"]
            H.append(f"- `{s['name']}` — {d}")
        H.append(f"\n## 📄 Reports & Research ({len(rp)})")
        for r in rp[:120]:
            H.append(f"- {wl(r['title'])}  _({r['source']})_")
        if len(rp) > 120: H.append(f"_+{len(rp)-120} more_")
        H.append(f"\n## 💬 Related chats ({len(se)})")
        for s in se[:80]:
            H.append(f"- {wl(s['title'])}")
        if len(se) > 80: H.append(f"_+{len(se)-80} more_")
        H.append(f"\n## 🔗 Links ({len(lk)})")
        for u, d in lk[:120]:
            H.append(f"- [{d['domain']}]({u}) ×{d['count']}")
        if len(lk) > 120: H.append(f"_+{len(lk)-120} more_")
        write(os.path.join(BRAIN, "Topics", f"{t}.md"), "\n".join(H))

    # ----- HOME dashboard -----
    HM = ["---", "tags: [second-brain, home]", "---",
          "# 🧠 Second Brain — HOME", "",
          f"_Generated {today}. Regenerate: `python ~/.claude/scripts/build_second_brain.py`_", "",
          "One entry point connecting every skill, link, report, and chat by topic. "
          "Agents (Claude / Codex / Hermes) read these hubs to pull everything related to a task.", "",
          "## Corpus",
          f"- **{len(skills)}** skills → [[Brain/Skills/CATALOG|Skills catalog]]",
          f"- **{len(links)}** links → [[Brain/Links/INDEX|Links index]]",
          f"- **{len(reports)}** reports/researches → [[Brain/Reports/INDEX|Reports index]]",
          f"- **{len(sessions)}** chat sessions (local + vmi) → [[Sessions/INDEX|Sessions index]]", "",
          "## Topic hubs — everything connected", "",
          "| Topic | Skills | Links | Chats | Reports |", "|---|--:|--:|--:|--:|"]
    for t in TOPICS:
        sk, lk, se, rp = counts[t]
        HM.append(f"| [[{t}\\|{TOPIC_TITLES[t]}]] | {sk} | {lk} | {se} | {rp} |")
    HM += ["", "## How agents use this",
           "Ask for a topic (e.g. *design*) → open its hub (e.g. [[design-web]]) → it lists the "
           "matching **skills to invoke**, **reports to read**, **past chats**, and **reference links** "
           "in one place. Cross-topic overlap (a shader skill under both Design and 3D) is the connective tissue."]
    write(os.path.join(BRAIN, "HOME.md"), "\n".join(HM))

    # summary to stdout
    print("Second brain built at:", BRAIN)
    print(f"skills={len(skills)} links={len(links)} sessions={len(sessions)} reports={len(reports)}")
    print("topic | skills links chats reports")
    for t in TOPICS:
        print(f"  {t:18} {counts[t]}")

if __name__ == "__main__":
    main()
