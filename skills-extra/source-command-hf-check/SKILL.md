---
name: "source-command-hf-check"
description: "Run lint + validate + inspect on the Calaf Hyperframes project. Reports errors, WCAG contrast, and layout overflow."
---

# source-command-hf-check

Use this skill when the user asks to run the migrated source command `hf-check`.

## Command Template

Run the full Hyperframes verification on `C:\Users\user\hyperframes`:

```bash
cd /c/Users/user/hyperframes && npm run check
```

After the command finishes, summarise in 4 lines:
- errors count
- warnings count
- WCAG contrast pass/fail
- layout issues count

If anything is non-zero except the `composition_file_too_large` advisory, list each issue with element id and the precise fix. Do not narrate beyond that.
