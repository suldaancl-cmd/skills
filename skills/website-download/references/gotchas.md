# Gotchas

Traps that make a correct mirror look broken, or a broken mirror look correct.
Most of these were learned by getting them wrong first.

## Verification traps

**A cached 404 lies to you.** Browsers cache failed requests per origin. Test
a broken build on port 8300, repair it, retest on 8300, and you will still see
the old failures. **Use a fresh port for every verification round.** This is
cheap and it is the single most common source of false "still broken" reports.

**A zero viewport means the measurement is broken, not the page.** The in-app
browser pane reports `viewportW: 0` when it is not displayed, and every
derived number becomes garbage. If widths report identical values across
different sizes, or a viewport of 0, stop trusting the reading and use the
headless script.

**Playwright's option is `viewport`, not `viewportSize`.** With the wrong key
the option is silently ignored and every "width" runs at the 1280 default. The
tell is identical font sizes and identical breakpoint behaviour across widths
that should differ. If a mobile run reports a desktop nav, this is why.

**`document.fonts.check()` returns false until the text is painted.** It is
lazy. `await document.fonts.load("700 16px 'Family'")` first, then check, or
you will "prove" a correctly-localized font is missing.

**Lazy images need real scrolling.** A single `scrollTo(0, bottom)` does not
trip IntersectionObserver. Step through in ~500px increments with a short
pause, then settle. Even then, a low loaded-count with **zero broken** images
is normal and not a defect — `imgBroken` is the signal, not `imgLoaded`.

**Screenshots time out on heavy pages.** The tool can fail at 5s on a page
full of hi-res images even when rendering is fine, and the browser pane cannot
composite frames when it is not displayed. Fall back to headless Playwright
for a real screenshot, or to `page.evaluate` measurements.

## "Missing" assets that are not missing

**Check the live site before reporting a gap.** A sizeable share of 404s in
any repair round are dead links the site itself emits — orphaned icon paths,
stale OG images, references to files they deleted. `curl` the exact URL
against production: if it 404s there too, it is their bug. Reporting it as a
mirror defect is a false negative that wastes everyone's time.

**Decode `&amp;` before curling a mirrored URL.** HTML-escaped ampersands in
a query string will 404 if you test them literally. A failing test is not the
same as a failing mirror — this one produced a "repair" that broke a working
file before being reverted.

**Do not "fix" double-encoded Google Fonts filenames.** A path like
`css2@family=Inter%253Awght@...` looks wrong but is correct: the on-disk
filename literally contains `%3A` because Windows forbids `:`, so the `%`
must itself be escaped. Leave it alone.

**Compare URL-decoded, not raw.** wget saves `%20` as a space. Comparing
encoded referenced URLs against encoded disk names flags every file as
missing. Decode both sides first.

## Windows specifics

**`Get-ChildItem -Recurse` silently under-counts** directories containing
paths over 260 characters — it reported 1386 files where the true count was
1422. Never use it to prove a copy is complete. Use `robocopy /L /E` and read
the Extras/FAILED columns, or compare total bytes.

**wget exit 3 = a path exceeded 260 chars.** Almost always one file with a
very long generated name. Re-fetch it to a short name and patch references.
Exit 8 is not an error; it means a 4xx was seen during the crawl.

**Never `/MIR` or `/PURGE` onto a destination you have not inspected.** Plain
`/E` is the safe copy. Inspect the destination first — a previous session may
already have a complete copy, and the one you are about to overwrite it with
may be the degraded one.

**Never write the output zip inside the folder being zipped** — self-reference
file lock. Write it outside the tree, and use `Fastest` compression since web
media is already compressed.

## Command guards (dcg)

The hook blocks these shapes. Each has a working alternative:

| Blocked shape | Why | Alternative |
|---|---|---|
| `X="/path/bin"; "$X" --flags` | Executable assembled at runtime cannot be statically verified | Call the binary by literal path |
| `cmd > "$VAR/file"` | Redirect target expands at runtime, could truncate anything | Write from inside Python, or use a literal path |
| `shutil.rmtree(...)` in `python -c` | Recursive delete | `os.rmdir` for empty dirs; put real cleanup in a script file |
| `sleep 30 && next-cmd` | Blocking sleep chains | `run_in_background: true`, or Monitor with an until-loop |

## Storage

Mirrors go to `C:\Users\user\.claude\_projects\site-mirrors\`. Not Downloads
(Storage Sense permanently deleted a mirror there, no Recycle Bin entry, no
audit trail). Not `D:\site-mirrors\` — something clears it on a rolling ~7-day
window, and by 2026-07-24 it was deleting **individual files inside folders
that still existed**, so a surviving folder is not evidence of a surviving
mirror. Count files before trusting one.

## Third-party hosts stay remote — by design

Analytics, CRM, chat widgets, form endpoints, and tag managers should keep
pointing at their origins. They are not design assets and localizing them
achieves nothing. Forms will not submit from a static mirror; that is
inherent. Only **first-party** hosts still being fetched remotely count as a
mirror failure.
