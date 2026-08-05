---
name: "source-command-hf-render"
description: "Render the Calaf Hyperframes composition to MP4. Runs check first; aborts on errors."
---

# source-command-hf-render

Use this skill when the user asks to run the migrated source command `hf-render`.

## Command Template

Render the Calaf Hyperframes composition to MP4. Steps:

1. **Pre-render check** — run `npm run check` from `C:\Users\user\.claude\_projects\hyperframes` and abort if any errors are reported (warnings OK). Do not proceed past errors.
2. **Render** — execute:
   ```bash
   cd /c/Users/user/hyperframes && npm run render
   ```
   Use a timeout of at least 300000ms (5 min) for the bash call.
3. **Locate the MP4** — list `dist/` (or whatever output dir hyperframes writes to) and report:
   - file path
   - file size (MB)
   - duration confirmation (15s expected)
4. **Open the file** — print the absolute Windows path so the user can double-click to play.

Do NOT preview/run the dev server during a render.
