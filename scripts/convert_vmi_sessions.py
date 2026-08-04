#!/usr/bin/env python3
"""
convert_vmi_sessions.py — Convert pulled vmi Claude transcripts to vault markdown.

Reuses the parser in sync_sessions_to_vault.py (export_one/build_index) so there is
ONE jsonl->md implementation. Reads  ~/.claude/from-vmi/projects/  (populated by the
tar-over-ssh pull), writes  vault/Sessions/vmi--<project>/  so the second-brain indexer
and the Sessions index pick them up automatically.

Pull step (run before this):
  ssh vmi "cd /root/.claude/projects && find . -name '*.jsonl' -print0 | tar --null -czf - -T -" \
     | tar xzf - -C "C:/Users/user/.claude/from-vmi/projects"
"""
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import sync_sessions_to_vault as S   # reuse export_one, build_index, DST

SRC = Path(r"C:\Users\user\.claude\from-vmi\projects")

def main():
    written = skipped = empty = 0
    for proj_dir in sorted(p for p in SRC.iterdir() if p.is_dir()):
        proj_name = "vmi--" + proj_dir.name.lstrip("-").replace("--", "-") or "vmi--root"
        for jsonl in proj_dir.glob("*.jsonl"):
            r = S.export_one(jsonl, proj_name)
            if r == "written": written += 1
            elif r == "skipped": skipped += 1
            else: empty += 1
    S.build_index()   # rebuild unified Sessions index (local + vmi)
    print(f"vmi sessions: written={written} skipped={skipped} empty={empty}")

if __name__ == "__main__":
    main()
