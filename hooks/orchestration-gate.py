"""PreToolUse gate: no fleets, workflows, or model upgrades without Karim asking.

Karim's rule (2026-08-05): "most time he run orchestrator agents and I don't know,
then I'll be surprised by token burn — he must ask me, or only when I type skills
like deep research / workflows / dynamic."

So: Workflow and Agent calls surface a permission prompt UNLESS the user's own last
message opted in. Reads the real user message from the transcript (tool_result echoes
and skill-launch echoes are skipped, same as the Stop hook).

Emits permissionDecision "ask" — Karim decides per call; nothing is silently blocked.
Always exits 0; any error falls through to normal permission handling.
"""
import json
import os
import sys

# Typing any of these IS the opt-in — the gate stays quiet for that turn.
OPT_IN = (
    "deep research", "deepresearch", "workflow", "dynamic", "ultracode", "swarm",
    "orchestrate", "orchestrator", "fleet", "parallel agents", "subagents", "sub agents",
    "spawn agents", "fan out", "fanout", "use agents", "run agents",
    "بحث عميق", "وكلاء", "شغل الوكلاء",
)
GATED = ("Workflow", "Agent")


def last_user_message(transcript_path: str) -> str:
    if not transcript_path or not os.path.exists(transcript_path):
        return ""
    try:
        with open(transcript_path, encoding="utf-8") as fh:
            lines = fh.readlines()
    except OSError:
        return ""
    for line in reversed(lines):
        try:
            entry = json.loads(line)
        except Exception:
            continue
        if entry.get("type") != "user":
            continue
        content = (entry.get("message", {}) or {}).get("content")
        if isinstance(content, list) and any(
            isinstance(b, dict) and b.get("type") == "tool_result" for b in content
        ):
            continue  # tool output, not a human turn
        if isinstance(content, str):
            text = content
        elif isinstance(content, list):
            text = " ".join(c.get("text", "") for c in content
                            if isinstance(c, dict) and c.get("type") == "text")
        else:
            continue
        if text.lstrip().startswith("Base directory for this skill:"):
            continue  # skill-launch echo
        return text
    return ""


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    tool = payload.get("tool_name", "")
    if tool not in GATED:
        sys.exit(0)

    prompt = last_user_message(payload.get("transcript_path", "")).lower()
    if any(word in prompt for word in OPT_IN):
        sys.exit(0)  # Karim asked for it

    tin = payload.get("tool_input", {}) or {}
    what = tin.get("description") or tin.get("subagent_type") or tin.get("name") or "unnamed"
    reason = (
        f"ORCHESTRATION GATE — you did not ask for this. Claude wants to run `{tool}` "
        f"({what}), which spawns background agents and burns tokens outside your view. "
        "Approve only if you want that now. To skip this prompt in future, include a word "
        "like \"deep research\", \"workflow\", \"dynamic\", \"swarm\" or \"use agents\" in "
        "your message. Otherwise decline and Claude will do the work in this session."
    )
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": reason,
        }
    }))
    sys.exit(0)


if __name__ == "__main__":
    main()
