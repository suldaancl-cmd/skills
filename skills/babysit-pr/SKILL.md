---
name: babysit-pr
description: Watch an open pull request and keep it healthy — monitor CI and mergeability, auto-diagnose and fix failing checks (lint, types, tests, build), push the fixes, and report when it's green (or auto-merge only if explicitly told to). Designed to be run on a timer via `/loop <interval> babysit-pr`. Use this when the user says "babysit this PR", "watch the PR", "keep fixing CI until it's green", "auto-fix the checks", or wants a PR shepherded to mergeable without hand-holding every failure.
---

# Babysit PR

Shepherd one pull request from "opened" to "green and mergeable" with minimal human babysitting. Every tick: look at the PR's checks, fix whatever's red, and get out of the way once it's green.

Built to run on a loop: `/loop 2m babysit-pr` runs this roughly every two minutes. Each run is one quick pass — check, fix if needed, report, exit. It is **not** a long-lived watcher; the loop provides the heartbeat.

## Each pass

1. **Find the PR.** Default to the PR for the current branch: `gh pr view --json number,state,mergeable,statusCheckRollup,url`. If the user named a specific PR number, use that.
2. **If already merged or closed:** report that and stop — nothing to babysit.
3. **Read the check rollup.** Categorize each failing check: lint / formatting, type errors, unit or integration tests, build, deploy preview, or (for mobile) an EAS build.
4. **If everything is green and mergeable:** go to **When it's green** below.
5. **If something is red:** diagnose and fix.

## Fixing red checks

Pull the failing job's logs (`gh run view <run-id> --log-failed` or the check's detail URL) and fix the actual cause in the working tree:

- **Lint / format** → run the project's formatter/linter with `--fix` and commit the result.
- **Type errors** → read the reported file:line, fix the type, re-run the type checker locally to confirm.
- **Failing tests** → read the assertion. Decide honestly: is the *code* wrong or the *test* wrong? Fix the real defect. Do not delete or skip a test to make CI pass — that's faking green, and it's worse than a red check because it hides the bug. If a test is genuinely obsolete, say so and ask.
- **Build** → reproduce the build locally, fix, confirm.

Commit each fix with a clear message and push. The next loop tick will re-check.

If the **same check fails the same way two passes in a row** after your fix, stop auto-fixing and surface it to the human with the log excerpt — you're likely missing context, and looping on a fix that isn't working just burns time.

## When it's green

**Default: do not auto-merge.** Report that the PR is green and mergeable, link it, and let the human merge. Auto-merging removes the last human checkpoint, so it's opt-in only.

**Auto-merge only if the user explicitly said so** this session (e.g. "merge automatically when green"). If they did, merge with the project's preferred strategy (`gh pr merge --squash` unless told otherwise) and report the result.

## Guardrails (and why)

- **Never force-push** to a shared branch to "fix" history — you can destroy a collaborator's work. Only ever add commits.
- **Never touch production directly.** This skill works through the PR/CI, never around it.
- **Don't fake green.** Skipping tests, `--no-verify`, or loosening CI config to pass are all off the table unless the human explicitly asks — the point of babysitting is a *genuinely* healthy PR, not a green checkmark over broken code.
