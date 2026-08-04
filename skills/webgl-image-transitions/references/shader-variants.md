# Shader variants

Each snippet is a `transition(vec2 uv)` body using the gl-transitions contract
(`progress`, `ratio`, `getFromColor`, `getToColor`). Drop any of them into the
Recipe 2 host program in SKILL.md. All code here is original; reference the
gl-transitions collection for the math behind each family.

## Wave / ripple

Displacement from a `sin` field instead of a texture. `uv` warps most at the
transition midpoint.

```glsl
uniform float amplitude; // = 0.05
uniform float freq;      // = 12.0
vec4 transition(vec2 uv) {
  float envelope = sin(progress * 3.14159265);      // 0 -> 1 -> 0
  float w = sin(uv.y * freq + progress * 6.2831) * amplitude * envelope;
  vec2 p = vec2(uv.x + w, uv.y);
  return mix(getFromColor(p), getToColor(p), progress);
}
```

## Curl

Rotate the sample point around the center; the rotation unwinds as progress
advances so both images swirl in opposite directions.

```glsl
uniform float turns; // = 1.5
vec4 transition(vec2 uv) {
  vec2 c = uv - 0.5;
  float aFrom =  turns * 6.2831 * progress;
  float aTo   = -turns * 6.2831 * (1.0 - progress);
  mat2 rFrom = mat2(cos(aFrom), -sin(aFrom), sin(aFrom), cos(aFrom));
  mat2 rTo   = mat2(cos(aTo),   -sin(aTo),   sin(aTo),   cos(aTo));
  vec4 from = getFromColor(rFrom * c + 0.5);
  vec4 to   = getToColor(rTo * c + 0.5);
  return mix(from, to, progress);
}
```

## Slices

Quantize UVs into vertical bands that slide at staggered offsets, so the image
tears into strips that resolve into the next one.

```glsl
uniform float count; // = 12.0
vec4 transition(vec2 uv) {
  float band = floor(uv.x * count);
  float stagger = fract(sin(band) * 43758.5453);    // per-band phase
  float p = clamp((progress - stagger * 0.3) / 0.7, 0.0, 1.0);
  vec2 off = vec2(0.0, (1.0 - p) * (stagger - 0.5));
  return mix(getFromColor(uv + off), getToColor(uv + off), p);
}
```

## Zoom-blur

Accumulate samples along the vector toward center for a punch-in dissolve.

```glsl
uniform float strength; // = 0.4
const int STEPS = 12;
vec4 transition(vec2 uv) {
  vec2 dir = (uv - 0.5);
  vec4 acc = vec4(0.0);
  float envelope = sin(progress * 3.14159265) * strength;
  for (int i = 0; i < STEPS; i++) {
    float t = float(i) / float(STEPS);
    vec2 p = uv - dir * t * envelope;
    acc += mix(getFromColor(p), getToColor(p), progress);
  }
  return acc / float(STEPS);
}
```

WebGL1 loops need a constant bound, hence `const int STEPS`. Lower it on mobile.
