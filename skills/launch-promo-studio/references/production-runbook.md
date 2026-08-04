# Production Runbook

The stage-by-stage pipeline to take a launch promo from brief to shipped social cuts. Each stage
names its deliverable — don't start a stage until the prior deliverable exists. Full theory in the
studio's `research/04-editing-post-workflow.md`.

## 0. Brief (deliverable: a filled brief)
Capture: **audience**, the **ONE message** (if it has two, it has zero), **brand** (which kit),
**length** (15/30/60s), **platforms** (drives aspect ratios), **CTA**. If any are missing, ask —
don't invent a brand or message.

## 1. Script (deliverable: ~65–75 words for 30s)
One idea per beat. Write the **accent words** explicitly (they get the brand color). Hook in the
first line. End on a single CTA. Dev/B2B → precise/technical tone; consumer → warm/benefit tone.

## 2. Beat sheet (deliverable: timecoded archetype map)
Map script → archetypes on the master timeline (see SKILL.md). A1 opens, A9 closes, A3 carries the
claims, A4 is the proof spine. Pick A5 (dev) or A7 (consumer) for the proof beat. Lock durations
from `templates/scene-archetypes/INDEX.md`.

## 3. Brand kit (deliverable: brand-kits/<kit>.json)
Pick a pre-built kit or copy one and edit the 12 keys. This is the ONLY place brand identity
lives. Verify: one accent, one bg texture, display + mono fonts, logo asset present, fps, motionStyle.

## 4. Style frame (deliverable: 1 still that sells the look)
Before animating anything, render ONE still of the key A3 or A4 frame (Remotion `remotion still`)
and confirm it reads "expensive": one accent, framed UI, correct type. Approve the still first —
it's cheap to change here, expensive later.

## 5. Build (deliverable: per-beat Remotion Sequences)
Implement each beat as a `<Sequence>` (or HyperFrames scene for A4 DOM UI). Use motion tokens
verbatim (`motion-tokens.md`). Honor the 5 rules. Frame all UI. Convert ms→frames at the kit fps.
Compose the beats on one `<Composition>` timeline.

## 6. Render (deliverable: master_4k.mp4, silent)
`remotion render src/index.ts <Comp> exports/master_4k.mp4` at 4K (or 1080p) — ProRes or
high-bitrate H.264. This silent master is the negative; never throw it away.

## 7. Sound (deliverable: mixed stereo track at −14 LUFS)
Invoke **`motion-sound-design`**. Generate music bed + the 7 core SFX, place hits on every cut,
duck music under any VO, master to −14 LUFS / −1.5 dBTP. Output one mixed WAV/AAC.

## 8. Mux + derive (deliverable: master + social cuts)
Mux audio onto the silent master, then derive 9:16 / 1:1 / 4:5 via the commands in
`export-specs.md`. Master once; never re-render per format.
```bash
ffmpeg -i master_4k.mp4 -i mix_master.wav -c:v copy -c:a aac -b:a 320k -shortest master_4k_audio.mp4
```

## 9. QA + ship (deliverable: approved files)
Run the pre-ship checklist in `export-specs.md`. Burn captions for sound-off autoplay. Confirm the
first frame works as a thumbnail. Then deliver.

## Pacing reference (30s)
`3s hook / 14s body / 3s proof / 7s brand+claims / 3s CTA`. Body cuts every 2–4s, front-loaded
info density, single CTA. Hook must land in 0–3s.

## Re-skin / re-version (the leverage)
- New brand → swap the kit JSON, re-render. Same template, new film.
- New length → re-cut the beat sheet per the INDEX duration table; reuse the same Sequences.
- New platform → derive another aspect ratio; no re-render.
