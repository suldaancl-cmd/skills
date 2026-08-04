# The build loop and the launch gate

What happens after `PLANMAP.md` exists. Hand this to Karim at the end of phase 7.

## The loop, one feature at a time

The source video's whole method in one line: build one feature, prove it, review it, commit it,
tick the box, next. No parallel half-finished features.

1. **Pick the top unchecked box** in `PLANMAP.md` section 11. One feature, not three.
2. **Design it first** if it has a UI. Karim's standing rule holds: no code until he picks a
   colors-and-fonts deck option.
3. **Implement it.** Surgical — touch only what this feature needs.
4. **Self-test on the real thing.** Simulator, then an actual device for anything touching the
   camera, notifications, or payments. A feature that only works in a simulator is not done.
5. **AI code review.** A fresh pass with `code-reviewer`, or the platform's own review tool,
   looking for what the implementer missed rather than confirming it.
6. **Failed?** Back to step 3. Loop as many times as it takes. Do not tick the box.
7. **Passed?** Commit, tick the box, update `NOTES.md`, next feature.

Done is when no unchecked box remains. Not before, and there is no partial credit.

## Where the loop breaks

- **Ticking on "it compiles".** The box means tested, reviewed, committed.
- **Batching five features into one commit.** The review has nothing to bite on and the revert
  is all-or-nothing.
- **Skipping the device test** for camera, push, in-app purchase or deep links. Those are
  exactly the four that behave differently on real hardware.
- **Letting the plan drift silently.** A feature that changed shape mid-build gets its line in
  `PLANMAP.md` rewritten, not quietly reinterpreted.

## The launch gate

Append this to `MANUAL-SETUP.md` as blocking rows for any app that ships to a store. Each one
below is a rejection, not a nice-to-have. Verify against current store policy before submitting
— these are as described in the source video, dated 2026-07-31, and store rules change.

| Gate | Why | Who |
|---|---|---|
| Privacy policy page, publicly reachable | Rejection without it | you write it, Karim hosts and links it |
| Terms of service page | Same | same |
| Delete-account, reachable inside the app | Rejection without it. Deleting from the app must actually delete | build it |
| Apple Sign-In whenever Google Sign-In exists | Offering a third-party sign-in without Apple's is a rejection on iOS | build it |
| Support or contact route | Reviewers check it resolves | you draft, Karim hosts |
| Store listing: screenshots, description, keywords, age rating | Submission blocks without them | you draft, **Karim submits** |
| Developer account enrolled and paid | Nothing ships without it, and it takes days | **Karim only** |

## Before the first submission

- Every legal page live on a real URL, linked from inside the app, not just written.
- Delete-account tested end to end on a real account.
- Both sign-in paths tested on a real device.
- Error tracking receiving events from a production build, not just locally.
- Every secret in the platform's secret store, none in the repo.
- One person other than Karim has completed onboarding without being told what to do.
