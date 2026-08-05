---
description: Run lint + validate + inspect on the Calaf Hyperframes project. Reports errors, WCAG contrast, and layout overflow.
---

Run the full Hyperframes verification on `C:\Users\user\.claude\_projects\hyperframes`:

```bash
cd /c/Users/user/.claude/_projects/hyperframes && npm run check
```

After the command finishes, summarise in 4 lines:
- errors count
- warnings count
- WCAG contrast pass/fail
- layout issues count

If anything is non-zero except the `composition_file_too_large` advisory, list each issue with element id and the precise fix. Do not narrate beyond that.
