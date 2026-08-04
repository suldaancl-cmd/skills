# ffmpeg Audio Recipes

Runnable mix/master/mux commands. No DAW. Use the bundled ffmpeg:
`C:\Users\user\aistudiotoday-promo\node_modules\@remotion\compositor-win32-x64-msvc\ffmpeg.exe`.
Full rationale + sources in the studio's `research/03-sound-design-music.md`.

## Step 1 — Place each SFX at its cut offset

`seconds = frame / fps`. Delay a mono/stereo SFX to land at its event (`adelay` is in ms,
per-channel). A whoosh leads the cut ~80–120ms; an impact lands on it.

```bash
# boom should land at 5.00s → delay 5000ms on both channels
ffmpeg -i boom.wav -af "adelay=5000|5000" boom_at_5s.wav
# whoosh leads a 2.00s cut by 100ms → place at 1.90s
ffmpeg -i whoosh.wav -af "adelay=1900|1900" whoosh_at_1_9s.wav
# trim a raw SFX to length first if needed
ffmpeg -i whoosh_raw.wav -ss 0 -t 1.2 whoosh.wav
```

## Step 2 — Mix all SFX into one stem

```bash
ffmpeg \
  -i whoosh_at_1_9s.wav -i boom_at_5s.wav -i tick_at_0s.wav -i riser_at_4s.wav \
  -filter_complex "[0:a][1:a][2:a][3:a]amix=inputs=4:duration=longest:normalize=0[sfx_out]" \
  -map "[sfx_out]" -c:a pcm_s16le sfx_mix.wav
```
`normalize=0` keeps your manual levels (amix otherwise auto-attenuates by input count).

## Step 3 — Duck music under VO + mix everything

```bash
ffmpeg \
  -i music.wav -i vo.wav -i sfx_mix.wav \
  -filter_complex "
    [0:a]volume=0.7[music_raw];
    [2:a]volume=1.5[sfx_boosted];
    [music_raw][1:a]sidechaincompress=threshold=0.02:ratio=4:attack=20:release=400:level_sc=1.0[music_ducked];
    [music_ducked][1:a][sfx_boosted]amix=inputs=3:duration=longest:normalize=0[mixed];
    [mixed]alimiter=limit=0.891:level=false[out]
  " \
  -map "[out]" -c:a pcm_s16le mix_raw.wav
```
- `volume=0.7` music: pre-attenuate ~3 dB so it sits under everything.
- `sidechaincompress threshold=0.02 ratio=4 attack=20 release=400`: music ducks 6–12 dB when VO
  is present, breathes back over 400ms. Fast 20ms attack catches speech onsets.
- `alimiter=limit=0.891`: true-peak ceiling ≈ −1 dBTP, stops overs.
- **No VO?** Drop the `[1:a]` inputs and the sidechain line; just `amix` music+SFX then limit.

## Step 4 — Master to −14 LUFS / −1.5 dBTP (two-pass loudnorm)

Pass 1 — measure:
```bash
ffmpeg -hide_banner -i mix_raw.wav \
  -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null - 2> measure.log
```
Read `measure.log` JSON → take `input_i, input_tp, input_lra, input_thresh, target_offset`.

Pass 2 — apply (substitute measured values):
```bash
ffmpeg -hide_banner -i mix_raw.wav \
  -af loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=-18.7:measured_TP=-3.2:measured_LRA=9.4:measured_thresh=-29.1:offset=0.3:linear=true:print_format=summary \
  -c:a aac -b:a 320k -ar 48000 final_master.m4a
```
(For lossless delivery swap the output to `-c:a pcm_s24le final_master.wav`.)
Quick one-pass (acceptable for fast social cuts): `-af loudnorm=I=-14:TP=-1.5:LRA=11`.

## Step 5 — Mux audio onto the silent video master

```bash
ffmpeg -i master_4k.mp4 -i final_master.m4a \
  -c:v copy -c:a aac -b:a 320k -map 0:v:0 -map 1:a:0 -shortest master_4k_audio.mp4
```
`-c:v copy` = no video re-encode (instant, lossless). `-shortest` trims to the shorter stream.

## Verify

```bash
# loudness check (should report ~ -14 LUFS, TP < -1)
ffmpeg -i master_4k_audio.mp4 -af loudnorm=I=-14:TP=-1.5:print_format=json -f null -
# confirm audio stream present + codec
ffprobe -v error -select_streams a:0 -show_entries stream=codec_name,sample_rate,channels master_4k_audio.mp4
```

## Notes

- Generate SFX as WAV from ElevenLabs MCP, save locally, then run the above.
- If sample rates differ, normalize first: `ffmpeg -i in.wav -ar 48000 out48.wav`.
- Keep a `sound/` folder per project: `music.wav`, `vo.wav`, raw SFX, `sfx_mix.wav`,
  `mix_raw.wav`, `final_master.*`.
