"""Stop hook: enforce skill usage.

Reads stdin Stop hook payload. Allows the turn if any of:
  a) stop_hook_active is true (prevents infinite loops)
  b) the user's last message is < 15 chars (trivial confirmation)
  c) the assistant invoked Skill / Agent / mcp__* in this turn
  d) the assistant made >= MIN_TOOLS_FOR_WORK other tool calls (Bash/Edit/WebSearch/...) —
     grounded work, not an answer from memory, which is what this hook guards against
  e) the assistant's text output across the turn is < 300 chars (brief action)
Otherwise prints {"decision":"block","reason":"..."} to stdout (which the runtime treats as a block + retry signal).
Always exits 0 — the JSON output is the control channel, not the exit code.
"""
import datetime
import json
import os
import sys

USAGE_LOG = r"C:/Users/user/.claude/skill-usage.jsonl"
# Non-Skill tool calls that count as "this turn did real work" (Bash, Edit, WebSearch...).
# 1+ means the answer was grounded in something read/run, not recalled — which is the thing
# this hook guards. Was 2, which blocked legitimate single-command lookups (a one-Bash answer
# citing its own output is grounded; the real failure mode is ZERO tools plus confident prose).
MIN_TOOLS_FOR_WORK = 1
# Session ids used by scripts/check_system.py fixtures — never logged as real turns.
SYNTHETIC_SESSIONS = {"healthcheck", "chk", "testsess"}


def log_usage(session_id: str, prompt: str, skills: list, agents: list,
              mcp: int, tools: list, blocked: bool) -> None:
    """Append one line per turn — the data source for tuning skill-routes.json."""
    if session_id in SYNTHETIC_SESSIONS:
        return  # health-check fixtures must not pollute the tuning data
    try:
        entry = {
            "ts": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
            "session": session_id[:8],
            "prompt": prompt.strip()[:160],
            "skills": skills,
            "agents": agents,
            "mcp_calls": mcp,
            "tools": tools,
            "blocked": blocked,
        }
        with open(USAGE_LOG, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except Exception:
        pass


def main() -> None:
    try:
        inp = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    if inp.get("stop_hook_active"):
        sys.exit(0)

    transcript_path = inp.get("transcript_path", "")
    if not transcript_path or not os.path.exists(transcript_path):
        sys.exit(0)

    last_user_text = ""
    last_assistant_blocks = []

    with open(transcript_path, encoding="utf-8") as fh:
        lines = fh.readlines()

    for line in reversed(lines):
        try:
            entry = json.loads(line)
        except Exception:
            continue
        etype = entry.get("type")
        if etype == "user":
            msg = entry.get("message", {}) or {}
            content = msg.get("content")
            # Skip tool_result echoes (Skill/Agent/mcp__ outputs come back as user-role messages).
            # Only break on real human user messages.
            if isinstance(content, list) and any(
                isinstance(b, dict) and b.get("type") == "tool_result"
                for b in content
            ):
                continue
            if isinstance(content, str):
                last_user_text = content
            elif isinstance(content, list):
                last_user_text = " ".join(
                    c.get("text", "")
                    for c in content
                    if isinstance(c, dict) and c.get("type") == "text"
                )
            # Skill-launch echoes come back as user-role messages; they are
            # not the human prompt — keep walking back to the real one.
            # Both forms seen in the wild: the first load prints the skill's base
            # directory, a repeat load prints "is already loaded above". Missing the
            # second form made the hook block 9 turns on its own re-injection message.
            _head = last_user_text.lstrip()
            if (_head.startswith("Base directory for this skill:")
                    or (_head.startswith("Skill /") and "already loaded" in _head[:120])):
                last_user_text = ""
                continue
            break
        if etype == "assistant":
            msg = entry.get("message", {}) or {}
            content = msg.get("content", []) or []
            if isinstance(content, list):
                last_assistant_blocks.extend(content)

    if len(last_user_text.strip()) < 15:
        sys.exit(0)

    # Background-task notifications and hook feedback are harness events, not
    # user prompts — a brief status reply to them needs no skill invocation.
    head = last_user_text.lstrip()
    if head.startswith(("[SYSTEM NOTIFICATION", "<task-notification>", "Stop hook feedback:",
                        "<ci-monitor-event>", "<system-reminder>")):
        sys.exit(0)

    used_skill = False
    text_chars = 0
    skills_used = []
    agents_used = []
    other_tools = []
    mcp_calls = 0
    for block in last_assistant_blocks:
        if not isinstance(block, dict):
            continue
        btype = block.get("type")
        if btype == "tool_use":
            name = block.get("name", "") or ""
            tin = block.get("input", {}) or {}
            if name == "Skill":
                used_skill = True
                skills_used.append(tin.get("skill", "?"))
            elif name == "Agent":
                used_skill = True
                agents_used.append(tin.get("subagent_type", "?"))
            elif name.startswith("mcp__"):
                used_skill = True
                mcp_calls += 1
            elif name:
                other_tools.append(name)
        elif btype == "text":
            text_chars += len(block.get("text", "") or "")

    # A turn that did real tool work (edits, searches, commands) is grounded work,
    # not an answer from memory — which is what this hook exists to catch.
    did_work = len(other_tools) >= MIN_TOOLS_FOR_WORK
    blocked = not used_skill and not did_work and text_chars >= 300

    log_usage(session_id=inp.get("session_id", ""), prompt=last_user_text,
              skills=skills_used, agents=agents_used, mcp=mcp_calls,
              tools=other_tools, blocked=blocked)

    if used_skill or did_work:
        sys.exit(0)

    if text_chars < 300:
        sys.exit(0)

    out = {
        "decision": "block",
        "reason": (
            "STOP HOOK: This turn finished without invoking any Skill, Agent, or "
            "mcp__* tool, and the response wasn't a brief action. Per user "
            "preference, installed skills must be used proactively. Re-read the "
            "SKILL ROUTER block injected with this prompt and invoke its listed "
            "skills (or a better-fit one from the available-skills list) before completing."
        ),
    }
    print(json.dumps(out))
    sys.exit(0)


if __name__ == "__main__":
    main()
