---
name: motion-sound-design
description: >-
  Add pro sound design + music to motion-graphics / promo / launch videos — the layer that makes
  a video feel "expensive". Use WHENEVER a video, animation, promo, ad, teaser, reel, or motion
  graphic needs SOUND: background music, sound effects (whooshes, UI ticks, risers, sub-bass
  impacts/booms, typewriter, ambient textures), voiceover, sound-to-cut sync, audio mixing,
  ducking music under VO, or loudness mastering to platform spec (−14 LUFS). Also use when the
  user says "add music", "pro sound effects", "sound design", "mix the audio", "the video feels
  flat/cheap", or "make it sound like an Apple/OpenAI/Anthropic launch". Generates audio on
  Karim's stack (ElevenLabs MCP, Venice audio) and mixes/masters entirely in ffmpeg — no DAW.
  Pairs with `launch-promo-studio` (it owns Stage 7: Sound).
---

# Motion Sound Design

Sound is ~50% of why a launch video feels premium, and it's the cheapest 50% to get wrong. This
skill turns a silent render into a mixed, mastered track using only ElevenLabs/Venice for
generation and ffmpeg for the mix — no DAW required.

The sonic signature of Apple / OpenAI / Anthropic-tier launch films:
> sparse low-frequency foundation (sub-bass pad/drone 60–80 Hz) → precise UI ticks + whoosh
> transitions synced **frame-accurately to cuts** → a single "big drop" on the product reveal →
> ambient textures under VO with music **ducked 6–12 dB** by sidechain → master at
> **−14 LUFS / −1.5 dBTP**.

## The expensive secret

**Near-silence for 0.5–2s before the reveal hit.** One stripped-back moment, then a sub-bass boom
on the product reveal. This single move creates more perceived "weight" than any plugin or library.
Build tension → release. Silence is a sound-design tool, not dead air.

## The 7 core SFX (generate these every time)

Generate with ElevenLabs MCP `generate_sound_effect` (text-prompt → 4 WAV variants, 48kHz,
40 credits/sec; commercial license on any paid plan). Prompts + uses in `references/sfx-and-music.md`.

| # | SFX | Lands on | Prompt seed |
|---|-----|----------|-------------|
| 1 | Air whoosh | scene transitions / text sweeps | "fast clean air whoosh transition, short" |
| 2 | Sub-bass boom | product reveal / logo hit | "deep cinematic sub bass impact boom, short tail" |
| 3 | Soft UI tick | element/word enters | "soft minimal UI click tick, crisp" |
| 4 | Typewriter taps | terminal/code typing | "mechanical keyboard typing soft taps" |
| 5 | Rising riser | pre-reveal tension | "rising tension riser swell, 2 seconds, building" |
| 6 | Digital data texture | ambient under UI scenes | "subtle digital data shimmer ambient texture" |
| 7 | String/synth swell | emotional reveal | "warm string swell crescendo, cinematic" |

## Music bed

- **Best for client work:** Artlist Standard (~$199/yr, full commercial, perpetual) or Epidemic
  Sound Creator (~$99/yr). Verify current pricing/license before quoting (don't guess).
- **AI music (fast, in-stack):** ElevenLabs Music (trained on licensed data — safe for commercial)
  or Venice audio (`venice-audio-music`). Avoid Suno/Udio for client work — commercial terms
  unsettled as of 2026.
- Pick ONE bed that matches brand motion personality: engineering/precision = minimal, pulsing,
  restrained; consumer/creative = warm, melodic, building.

## The mix pipeline (all ffmpeg)

Use the bundled ffmpeg (`...\@remotion\compositor-win32-x64-msvc\ffmpeg.exe`). Full runnable
commands with parameter explanations in `references/ffmpeg-audio-recipes.md`. The flow:

1. **Generate** music bed + 7 SFX (ElevenLabs/Venice) + optional VO (ElevenLabs TTS — Karim has a
   10-voice library; see vault `reference_elevenlabs_voices.md`).
2. **Place SFX on cuts** — get frame timecodes of every key visual event from the Remotion
   timeline, convert to seconds, delay each SFX to that offset (`adelay`), mix SFX into one stem.
3. **Duck + mix** — sidechain-compress music under VO (ratio 4, attack 20ms, release 400ms →
   6–12 dB duck), then `amix` music+VO+SFX, then `alimiter` at ~−1 dBTP.
4. **Master** — two-pass `loudnorm I=-14:TP=-1.5:LRA=11` (measure, then apply with `linear=true`).
5. **Mux** onto the silent video master (`-c:v copy`).

## Sound-to-motion sync (non-negotiable)

Every cut, every text enter, every reveal lands on a sonic event — not always loud, sometimes just
a tick. The ear-eye lock is what reads as production value. Method: export key-event frame numbers
from the Remotion comp → `seconds = frame / fps` → place each SFX at that exact offset with
`adelay=<ms>|<ms>`. A whoosh typically *leads* the cut by ~80–120ms; an impact lands *on* it.

## Loudness targets

Universal: **−14 LUFS integrated, −1.5 dBTP**. YouTube documents −14; TikTok/IG/X/FB publish none
(industry consensus −12 to −14). −14/−1.5 is loud enough everywhere without normalization clipping.
Verify the result: `ffmpeg -i out.wav -af loudnorm=I=-14:TP=-1.5:print_format=json -f null -`.

## Stack mapping

- Generate SFX/music: ElevenLabs MCP (`generate_sound_effect`, `generate_music`, `play_audio`),
  Venice (`venice-audio-music`, `venice-audio-speech`), skill `speech`, `ai-music-album`.
- VO: ElevenLabs TTS (Karim's custom voices) or `venice-audio-speech`.
- Mix/master/mux: ffmpeg (`references/ffmpeg-audio-recipes.md`).
- This skill = Stage 7 of `launch-promo-studio`. Other audio-needing skills (`remotion`,
  `hyperframes`, `cinematic-video-ads`, `ai-video-director`) should call it for the sound layer.

## Success criteria

Cuts land on sonic events; music ducks cleanly under VO; one intentional silence→drop moment;
master measures −14 LUFS / sub −1 dBTP; track muxed to the video with no drift.
