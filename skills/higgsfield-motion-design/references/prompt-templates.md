# Prompt Templates

Copy-paste scaffolds for Phase 2 (GPT Image 2 storyboard) and Phase 3 (Seedance 2.0 animation). Tuned against the public Higgsfield motion-design demo (2026-05-18) plus Karim's own UGC wave runs.

The whole reason these templates exist: prompt structure matters *more* than prompt length on GPT Image 2 and Seedance. Lead with the subject, lock the style anchors, then end with the constraints. Anything that contradicts itself between sections will be picked up and ruined.

---

## Phase 2 — Storyboard frame (per scene)

### Master template

```
{theme_sentence}. Scene {n}: {scene_focus}.

Style anchors:
- {medium}  (e.g. "Japanese sumi-e ink wash painting")
- {palette} (e.g. "deep indigo and weathered cream")
- {texture} (e.g. "aged paper grain, ink bleed at edges")
- {composition_rule} (e.g. "off-center subject, generous negative space on right")

On-screen text: single bold display line reading exactly:
"{LINE_N}"
— sans-serif display, all-caps, placed in the negative space, sized to occupy
roughly 25% of the frame height, never occluding the focal subject.

Aspect ratio: {aspect}.
Constraints: no watermarks, no UI chrome, no additional text anywhere in the
frame, no logos, no border/frame around the image.
```

### Plug-and-play example — bushido scene 1

```
The discipline of a samurai. Scene 1: A lone figure facing the sunrise from a misty cliff edge.

Style anchors:
- Japanese sumi-e ink wash painting
- deep indigo, ochre dawn, weathered cream
- aged rice-paper grain, soft ink bleed
- off-center subject (left third), generous negative space on right

On-screen text: single bold display line reading exactly:
"THE DAWN BREAKS"
— sans-serif display, all-caps, placed in the negative space, sized to occupy
roughly 25% of the frame height, never occluding the focal subject.

Aspect ratio: 9:16.
Constraints: no watermarks, no UI chrome, no additional text anywhere in the
frame, no logos, no border/frame around the image.
```

### Per-scene variations

You don't need to write 6 unique style-anchor sections. Lock the style anchors once and only vary `{scene_focus}` and the on-screen line. The visual cohesion that makes the final video feel like one piece comes from keeping the anchors identical across all 6.

For escalating energy across the 6 scenes, vary the **subject pose / camera distance** in this order:
1. Wide establishing — subject is small in the frame, lots of negative space (the text-heavy frame).
2. Medium — subject midway in.
3. Tight — close on the subject's silhouette / face.
4. Action / motion implied — subject mid-gesture.
5. Symbolic / object — an emblem of the theme (a sword, a clock, a coin, a wave) without the subject.
6. Resolution — wide again, mirror of frame 1 to close the loop. The "answer" to frame 1.

### Arabic / RTL variant

```
{theme_sentence_in_arabic}. مشهد {n}: {scene_focus_arabic}.

Style anchors:
- {medium_arabic_aware}  (e.g. "خط عربي مصمم بأسلوب مجلة فاخرة")
- {palette}
- {texture}
- {composition_rule}: نص يمين الإطار، الفراغ الأيسر للموضوع

النص الظاهر: سطر واحد بخط عربي عريض يقرأ تماماً:
"{LINE_N_ARABIC}"
— خط عرض عربي ثقيل، يحتل حوالي 25% من ارتفاع الإطار، لا يحجب الموضوع الرئيسي.

نسبة العرض إلى الارتفاع: {aspect}.
قيود: لا توجد علامات مائية، لا توجد عناصر واجهة، لا توجد أي حروف لاتينية في
الإطار، لا توجد شعارات.
```

---

## Phase 3 — Seedance 2.0 video (per scene)

### Master template

```
Animate the provided still image with subtle, cinematic motion.

Camera:
- Slow {camera_move}: {push-in | dolly out | parallax pan left | parallax pan right
  | gentle rise | gentle descent} over the full duration.

Foreground:
- {subject} holds its pose. Add the implied motion of {motion_cue: hair drift,
  cloth ripple, slow breath, ember drift, sword tip catching light}.

Background:
- {ambient_motion: drifting mist, particle dust, water ripple, soft snowfall,
  shimmer haze}.

On-screen text:
- Text remains absolutely stationary, fully legible, no warping, no flicker.
  Do not stylize or animate the text — it is a fixed graphic element.

Mood: {mood_words}.

Duration: {5–6 seconds}.
Aspect ratio: {aspect}.
```

### Plug-and-play example — bushido scene 1

```
Animate the provided still image with subtle, cinematic motion.

Camera:
- Slow dolly push-in toward the lone figure over the full 5 seconds.

Foreground:
- The samurai figure holds its pose. Add the implied motion of his cloak
  rippling lightly in the dawn wind, ink lines softly breathing.

Background:
- Mist rolling slowly across the cliff edge, sun rays brightening
  imperceptibly across the frame.

On-screen text:
- The phrase "THE DAWN BREAKS" remains absolutely stationary, fully legible,
  no warping, no flicker. Do not stylize or animate the text — it is a fixed
  graphic element.

Mood: stoic, patient, expectant.

Duration: 5 seconds.
Aspect ratio: 9:16.
```

### Camera-move palette (vary across the 6 clips for rhythm)

- Scene 1: slow push-in
- Scene 2: slow dolly out (releases tension built in 1)
- Scene 3: parallax pan left or right (introduces lateral motion)
- Scene 4: gentle handheld micro-motion (heartbeat / breath feel)
- Scene 5: slow vertical rise (lifts the symbolic object)
- Scene 6: slow push-in (mirrors scene 1, closes the loop)

If you give all 6 clips the same camera move, the final cut feels static even with motion. Vary deliberately.

---

## Regeneration rules

These are the moves to make when a frame comes back wrong. Apply them *before* you advance to the next phase — never animate a bad still.

### GPT Image 2 mangled the text

- If the text is missing entirely: re-prompt with the line in quotes appearing **twice** in the prompt (once in the anchors section, once in the "On-screen text" section).
- If the text is misspelled (one letter wrong): shorten the line to 1–3 words and retry. GPT Image 2 is more reliable on short type.
- If the text wraps awkwardly: explicitly state line-break behavior: `"... rendered on a single line, no wrap"` or `"... broken across exactly two lines on a single word break"`.
- If the text overlaps the subject: bump the "negative space" instruction more aggressively — *"the right third of the frame is empty, reserved for the text — the subject occupies only the left two-thirds"*.

### GPT Image 2 broke the style

- If a scene looks like a different visual language: re-paste the style anchors verbatim, in the same order. Mid-prompt style drift is the most common failure mode.
- If you have Pinterest refs, attach the closest 1–2 as reference images to the regen call and write *"strictly match the style of the attached references"*.

### Seedance produced a glitchy clip

- Reduce duration to 4 seconds. Seedance is most reliable in 4–5s.
- Simplify the camera move. Two compound motions ("dolly in AND pan left") can fight each other.
- If the text warps: explicitly state *"the text is rendered as flat, baked, non-animated typography — treat it as if it were painted onto the camera lens, not part of the 3D scene"*.

### Seedance ignored the still image

- Confirm `medias=[media_id]` is set, not empty.
- Increase the prompt's reliance on the still: *"the provided still image is the exact first frame of the video — do not regenerate the scene, only add motion"*.

---

## Sanity check before shipping

Before you concatenate and deliver, view the 6 clips back-to-back and ask:

1. Do the 6 lines, read aloud in order, form a satisfying narrative arc? (build → tension → resolution)
2. Does scene 1 visually rhyme with scene 6? (closes the loop)
3. Are the camera moves varied enough that the rhythm has dynamics?
4. Is every text element legible at 1080×1920?
5. If you took the audio away from a competitor's reel, would yours stand next to it?

If any answer is no, fix it before the user sees the deliverable.
