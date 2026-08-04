# SFX & Music — Sources, Prompts, Design

Verified sources + the SFX vocabulary. Full sourcing + citations in the studio's
`research/03-sound-design-music.md`. Prices verified ~June 2026 — re-check before quoting a client.

## Music sources (pick ONE bed per video)

| Service | Type | License | Price | Best for |
|---|---|---|---|---|
| **Artlist Standard** | Human library | Full commercial, perpetual after cancel | $199/yr | **Best single pick** — cinematic premium beds for launch films |
| Artlist Music & SFX Pro | Library + SFX | Commercial, 3 ch/platform | $299/yr | Music + SFX in one bill |
| Musicbed | Boutique | Commercial, simple terms | $120/yr | Premium cinematic mood, filmmaker-grade |
| Epidemic Sound **Creator** | Human library | ⚠ Personal/YouTube ONLY — NOT commercial/ads | $99/yr | Trap for client work — avoid for promos |
| Epidemic Sound Pro | Human library | Commercial, paid ads | ~$360/yr | Agency/client |
| Soundstripe Pro | Library | Commercial | $239/yr | Mid-range commercial |
| AudioJungle | Per-track | 1 end-product/purchase | $29–199/track | Occasional one-offs |
| **ElevenLabs Music** (v2) | AI | Commercial from day one (licensed data), paid plan ≥$5/mo | $5–99+/mo | **In-stack AI** — safe for commercial, quality gap to Artlist narrowing |
| Venice Audio (`venice-audio-music`) | AI | Pro $18/mo; music commercial terms unconfirmed | $18/mo+ | Rapid internal prototypes |
| Suno / Udio | AI | ⚠ UNSETTLED 2026 — internal scratch only | free–$30/mo | Prototyping ONLY, not client work |

**Recommendation for Karim's client promos:** Artlist Standard ($199/yr) for the reliable
premium bed; ElevenLabs Music for fast in-stack generation when a subscription isn't worth it.
Avoid Suno/Udio and Epidemic Creator for anything commercial.

## SFX sources

- **ElevenLabs `generate_sound_effect`** (primary, in-stack): text→SFX, WAV 48kHz, 40 credits/sec,
  commercial on Starter ($5/mo)+. Generates anything from a prompt — no library hunting.
- **Epidemic Sound SFX** (200k+, included in any ES sub) — strong tech/UI category.
- **Soundsnap** ($149/6mo, 450k) — deep pro whooshes/impacts.
- **Splice** ($7.99/mo) — sample-based, better for music than video SFX.
- Free: freesound.org (check per-sound CC license).

## The 7 core SFX — prompts + placement

| SFX | ElevenLabs prompt | Where it lands | Design tip |
|---|---|---|---|
| Air whoosh | "fast clean air whoosh transition, short, no tail" | text sweeps, scene cuts | leads the cut by 80–120ms |
| Sub-bass boom | "deep cinematic sub bass impact boom, short tail, 60-80Hz" | product reveal, logo | the "weight"; pair with pre-silence |
| Soft UI tick | "soft minimal UI click tick, crisp, dry" | each word/element enter | keep tiny; it's seasoning |
| Typewriter taps | "mechanical keyboard soft typing taps, irregular" | terminal/code typing | sync to char cadence 35–55ms |
| Rising riser | "rising tension riser swell building over 2 seconds" | pre-reveal ramp | ends exactly on the boom |
| Digital data texture | "subtle digital data shimmer ambient, soft, looping" | under UI scenes | bed at low level for "AI/compute" feel |
| String/synth swell | "warm cinematic string swell crescendo" | emotional reveal/outro | for brand-film register (B-type) |

Each call yields ~4 variants — audition, keep the best, save as WAV in the project `sound/` folder.

## The 4 techniques that separate $80K from $500 (audio only)

1. **Sound-to-cut sync.** Every cut/enter/reveal lands on a sonic event (even a tick). The ear-eye
   lock IS the production value.
2. **Pre-silence → drop.** 0.5–2s stripped back, then the sub-bass hit on reveal. Tension/release.
3. **Ducking.** Music sits 6–12 dB under VO via sidechain — never fights the voice.
4. **Master discipline.** −14 LUFS / −1.5 dBTP. Consistent loudness reads as "professional".

## Brand audio personality

- **Engineering/precision** (Codex, Claude Code, dev tools): minimal, pulsing, restrained;
  staccato ticks; sparse low-end; little/no melody.
- **Consumer/creative/brand-film** (whop, Claude brand film): warm, melodic, building; string/synth
  swells; richer texture.

Map to the `launch-promo-studio` brand kit's `motionStyle` so audio and motion personality match.
