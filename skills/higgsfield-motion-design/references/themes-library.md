# Themes Library

Pre-built theme packs lifted directly from the Higgsfield demo (2026-05-18) and the patterns that have shipped in Karim's UGC wave so far. Each pack is *just enough* to skip the line-writing and style-anchor phase when the user is vague — never paste these verbatim if the user has specific copy in mind.

## How to use

Pick the pack whose theme matches the user's ask, then:
- Copy the 6 lines into `storyboard/lines.txt` (in order).
- Use the **style anchors** verbatim in the Phase 2 prompt's "Style anchors:" slot.
- Adjust 1–2 lines if the user's brand voice demands it; don't rewrite all six.

If the user's theme isn't in the library, build a new pack on the fly using the same shape (6 lines, 2–3 style anchor adjectives, 1 mood adjective).

---

## bushido — discipline / honor / stillness

**Lines (matches the Higgsfield demo):**
1. THE DAWN BREAKS
2. EVEN WARRIORS REST
3. STILL WATER RUNS DEEP
4. FEAR NOTHING
5. SEASONS CHANGE — THE WARRIOR ENDURES
6. THE MOUNTAIN DOES NOT MOVE, NOR DO I

**Style anchors:** sumi-e Japanese ink wash, weathered cream paper, deep indigo and umber palette, lone samurai silhouette, conical hat in negative space.

**Mood:** stoic, patient, silent.

**Best aspect:** 9:16 (it's a TikTok/IG piece for masculine self-discipline audiences).

---

## time-currency — finance / mortality / urgency

**Lines (matches the Higgsfield demo):**
1. TIME IS THE ONLY CURRENCY
2. SPEND IT WELL
3. TODAY IS THE MOMENT
4. LIVE NOW
5. CHOOSE THE HOURS
6. THE CLOCK DOES NOT WAIT

**Style anchors:** flat editorial illustration, deep red accent on cream and black, oversized clock and coin motifs, mid-century newspaper print texture.

**Mood:** kinetic, urgent, journalistic.

**Best aspect:** 1:1 or 9:16. Pairs well as a money-mindset hook for IG carousels too.

---

## skate-summer — lifestyle / play / freedom

**Lines:**
1. WEEKEND MODE
2. NO BRAKES
3. CHASE THE LIGHT
4. PALMS AND PAVEMENT
5. SUMMER WON'T WAIT
6. RIDE IT OUT

**Style anchors:** golden-hour cinematic photography, motion-blur, palm trees, magenta-and-cyan color grade, anamorphic flare, low-angle skate-park concrete.

**Mood:** joyful, kinetic, weightless.

**Best aspect:** 9:16 for IG Reels, 16:9 if it's a YouTube short.

---

## hustle — entrepreneur / building / grind

**Lines:**
1. NO ONE IS COMING
2. BUILD IT ANYWAY
3. SLEEP IS A LIE
4. SHIP TODAY
5. THE MARKET DOESN'T CARE
6. KEEP MOVING

**Style anchors:** high-contrast monochrome with single neon accent (acid yellow or hazard orange), brutalist serif display type, gritty paper grain, late-night studio lighting.

**Mood:** urgent, contrarian, masculine.

**Best aspect:** 9:16. This is the format Karim's brand voice usually rides.

---

## fitness-stoic — training / pain / repetition

**Lines:**
1. ONE MORE REP
2. PAIN IS DATA
3. THE BODY OBEYS THE MIND
4. SHOW UP
5. NO REST DAYS FROM SHOWING UP
6. BECOME UNRECOGNIZABLE

**Style anchors:** desaturated film grain, single hard rim light, sweat detail, chalk-dust particulates, charcoal grey on bone palette.

**Mood:** brutal, focused, monastic.

**Best aspect:** 9:16.

---

## money-mindset — Karim-flavored, English/Arabic dual mode

**Lines (English):**
1. WEALTH IS DISCIPLINE
2. POOR MEN SPEND, RICH MEN COMPOUND
3. EVERY DIRHAM IS A SOLDIER
4. BUY BACK YOUR TIME
5. SCARCITY IS A CHOICE
6. PLAY THE LONG GAME

**Lines (Arabic):**
1. الثروة انضباط
2. الفقير ينفق، الغني يضاعف
3. كل درهم جندي
4. اشترِ وقتك
5. الندرة قرار
6. العب لعبة طويلة

**Style anchors:** editorial gold-on-black, brushed metal texture, Arabic display typography (e.g. 29LT Bukra Bold) when in Arabic mode, Latin display serif (Druk or Canela) when in English mode.

**Mood:** confident, patriarchal, money-conscious.

**Best aspect:** 9:16 for IG, 1:1 for LinkedIn carousels.

**RTL note:** When generating Arabic scenes, prompt GPT Image 2 with: *"right-to-left Arabic display text reading exactly: \"<line>\" in bold Arabic display typography. No Latin characters anywhere in the frame."* This stops it from sprinkling Latin garbage into the scene.

---

## Custom theme template

When inventing a new pack, fill this shape:

```
## <slug> — <one-line theme>

**Lines:**
1. ALL CAPS, 1–5 WORDS
2. ESCALATING TENSION
3. KEEP MOMENTUM
4. SHARPER STILL
5. CLOSE TO PEAK
6. THE PUNCHLINE

**Style anchors:** <2–3 visual adjectives>, <medium>, <palette>, <texture>.

**Mood:** <one or two words>.

**Best aspect:** <9:16 | 16:9 | 1:1>.
```
