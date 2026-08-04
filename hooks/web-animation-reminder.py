#!/usr/bin/env python3
"""UserPromptSubmit hook: when the prompt is about a web/animation build, nudge the
model to consult the `web-animation-effects` skill (22-effect catalog + project->animation
recommender). Conditional on keywords so it stays quiet on unrelated turns.
"""
import sys, json

def main():
    try:
        raw = sys.stdin.buffer.read().decode("utf-8", errors="replace")
        data = json.loads(raw)
    except Exception:
        return  # no/invalid input -> stay silent
    prompt = (data.get("prompt") or data.get("user_prompt") or "")
    p = prompt.lower()

    keywords = [
        # English — web build / animation context
        "website", "web site", "landing", "landing page", "web design", "frontend",
        "front-end", "animation", "animate", "animated", "scroll", "scrolltrigger",
        "parallax", "hero section", "webgl", "shader", "gsap", "three.js", "threejs",
        "awwwards", "page transition", "transition effect", "micro-interaction",
        "micro interaction", "lenis", "portfolio site", "calaf", "fluid shader",
        # Arabic — same context
        "موقع",            # موقع
        "أنيميشن",  # أنيميشن
        "انميشن",        # انميشن
        "تحريك",      # تحريك
        "سكرول",      # سكرول
        "هيرو",            # هيرو
        "تصميم ويب",  # تصميم ويب
        "انتقال",  # انتقال
    ]

    if any(k in p for k in keywords):
        reminder = (
            "[web-animation-effects] Reminder: a skill catalogs 22 web animations ranked by "
            "build difficulty, with a project->animation recommender, real example sites, and "
            "which installed skill builds each. Consult it to pick the right effects and justify "
            "the tier/price for this web build."
        )
        out = {"hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": reminder,
        }}
        sys.stdout.write(json.dumps(out))  # ensure_ascii=True -> safe on Windows stdout

if __name__ == "__main__":
    main()
