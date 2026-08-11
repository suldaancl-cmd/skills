"""Prove the two new exemptions work and that real blocking still fires."""
import json, os, subprocess, tempfile

HOOK = r"C:\Users\user\.claude\hooks\skill-stop-check.py"
LONG = "x" * 400  # >= 300 chars of prose, no tools, no skills -> the blockable shape


def transcript(user_text):
    return [
        {"type": "user", "message": {"role": "user",
                                     "content": [{"type": "text", "text": user_text}]}},
        {"type": "assistant", "message": {"role": "assistant",
                                          "content": [{"type": "text", "text": LONG}]}},
    ]


def run(user_text):
    fd, path = tempfile.mkstemp(suffix=".jsonl")
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        for e in transcript(user_text):
            fh.write(json.dumps(e) + "\n")
    payload = json.dumps({"session_id": "healthcheck", "stop_hook_active": False,
                          "transcript_path": path})
    r = subprocess.run(["python", HOOK], input=payload, capture_output=True, text=True)
    os.unlink(path)
    out = r.stdout.strip()
    return "BLOCK" if '"block"' in out else "allow"


cases = [
    ("Skill /using-superpowers is already loaded above; instructions unchanged.", "allow"),
    ("<ci-monitor-event>CI checks failed on branch main and here is the detail", "allow"),
    ("<task-notification>agent finished</task-notification>", "allow"),
    ("Write me a full marketing campaign for the new product launch next quarter", "BLOCK"),
]
fails = 0
for text, want in cases:
    got = run(text)
    ok = "PASS" if got == want else "FAIL"
    if got != want:
        fails += 1
    print(f"{ok}  want={want:5} got={got:5}  <- {text[:62]}")
print("\nall passed" if not fails else f"\n{fails} FAILURES")
