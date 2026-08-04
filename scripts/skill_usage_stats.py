"""Count how often each Claude Code skill has actually been invoked.

Parses every JSONL under ~/.claude/projects/**/*.jsonl, scans assistant turns
for `tool_use` blocks where the tool name is "Skill", extracts the `skill`
input, and aggregates by name + first-seen / last-seen timestamps.

Output: a dated markdown rank table to the vault Sessions/ folder. Skills not
invoked in 30+ days are flagged.

Usage:
    python scripts/skill_usage_stats.py
    python scripts/skill_usage_stats.py --since 2026-04-01
"""
import argparse, json, re, sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

PROJECTS = Path(r"C:\Users\user\.claude\projects")
VAULT_SESSIONS = Path(r"C:\Users\user\.claude\projects\C--Users-user--claude-skills\memory\Sessions")


def parse_jsonl_for_skill_calls(path: Path):
    try:
        with path.open(encoding="utf-8", errors="replace") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except Exception:
                    continue
                ts = rec.get("timestamp")
                msg = rec.get("message") or {}
                content = msg.get("content") or rec.get("content")
                if not isinstance(content, list):
                    continue
                for block in content:
                    if not isinstance(block, dict):
                        continue
                    if block.get("type") != "tool_use":
                        continue
                    if block.get("name") != "Skill":
                        continue
                    inp = block.get("input") or {}
                    skill_name = inp.get("skill") or inp.get("name")
                    if not skill_name:
                        continue
                    yield skill_name, ts
    except Exception as e:
        print(f"  warn: {path}: {e}", file=sys.stderr)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", help="ISO date — only count invocations after this date")
    ap.add_argument("--out-dir", type=Path, default=VAULT_SESSIONS)
    args = ap.parse_args()

    since_dt = None
    if args.since:
        since_dt = datetime.fromisoformat(args.since).replace(tzinfo=timezone.utc)

    counts = defaultdict(int)
    first_seen = {}
    last_seen = {}
    files_scanned = 0

    for jl in PROJECTS.rglob("*.jsonl"):
        files_scanned += 1
        for skill, ts in parse_jsonl_for_skill_calls(jl):
            ts_dt = None
            if ts:
                try:
                    ts_dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                except Exception:
                    pass
            if since_dt and ts_dt and ts_dt < since_dt:
                continue
            counts[skill] += 1
            if ts_dt:
                if skill not in first_seen or ts_dt < first_seen[skill]:
                    first_seen[skill] = ts_dt
                if skill not in last_seen or ts_dt > last_seen[skill]:
                    last_seen[skill] = ts_dt

    if not counts:
        print("No skill invocations found.")
        return 0

    now = datetime.now(timezone.utc)
    threshold_30 = now - timedelta(days=30)
    ranked = sorted(counts.items(), key=lambda x: -x[1])

    today = now.date().isoformat()
    out = args.out_dir / f"SKILL_USAGE_{today}.md"
    out.parent.mkdir(parents=True, exist_ok=True)

    stale = [s for s, _ in ranked if s in last_seen and last_seen[s] < threshold_30]
    never_dated = [s for s, _ in ranked if s not in last_seen]

    lines = [
        "---",
        f"name: Skill usage stats — {today}",
        f"description: Invocation counts per skill across all Claude Code session JSONLs.",
        "type: usage-stats",
        f"date: {today}",
        f"files-scanned: {files_scanned}",
        "---",
        "",
        f"# Skill usage — {today}",
        "",
        f"Scanned **{files_scanned}** JSONL files. Counted **{sum(counts.values())}** total skill invocations across **{len(counts)}** distinct skills.",
        "",
        "## Top 30 most invoked",
        "",
        "| Rank | Skill | Calls | First seen | Last seen |",
        "|---:|---|---:|---|---|",
    ]
    for i, (s, n) in enumerate(ranked[:30], 1):
        fs = first_seen.get(s, "")
        ls = last_seen.get(s, "")
        lines.append(f"| {i} | `{s}` | {n} | {fs.date() if fs else '—'} | {ls.date() if ls else '—'} |")

    lines += [
        "",
        f"## Stale: not invoked in 30+ days ({len(stale)})",
        "",
    ]
    for s in stale[:50]:
        lines.append(f"- `{s}` (last: {last_seen[s].date()}, total calls: {counts[s]})")
    if len(stale) > 50:
        lines.append(f"- _...and {len(stale)-50} more_")

    lines += [
        "",
        f"## Never dated ({len(never_dated)})",
        "",
        "Invocations found but timestamps couldn't be parsed.",
        "",
    ]
    for s in never_dated[:20]:
        lines.append(f"- `{s}` (calls: {counts[s]})")

    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {out}")
    print(f"  total invocations: {sum(counts.values())}")
    print(f"  distinct skills: {len(counts)}")
    print(f"  stale (30+ days): {len(stale)}")


if __name__ == "__main__":
    sys.exit(main())
