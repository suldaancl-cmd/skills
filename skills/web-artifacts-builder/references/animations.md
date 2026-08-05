# Animation Components Library

Complete, copy-paste-ready animation code for cinematic websites. Each component is self-contained.

---

## Table of Contents
1. [Preloader](#preloader)
2. [Particle System](#particle-system)
3. [Scroll Reveal](#scroll-reveal)
4. [Counter Animation](#counter-animation)
5. [3D Card Hover](#3d-card-hover)
6. [CSS Cityscape / Skyline](#css-cityscape)
7. [Glassmorphism](#glassmorphism)
8. [Text Stagger Reveal](#text-stagger-reveal)
9. [Ambient Glow Blobs](#ambient-glow-blobs)
10. [Navigation Scroll State](#navigation-scroll-state)
11. [Grid Overlay System](#grid-overlay-system)
12. [Scanning Circle](#scanning-circle)
13. [Fabric Texture Simulation](#fabric-texture-simulation)
14. [CSS Mannequin / Silhouette](#css-mannequin)
15. [Floating Ticker / Marquee](#floating-ticker)

---

## Preloader

### CSS
```css
.preloader {
  position: fixed; inset: 0; z-index: 10000;
  background: var(--bg);
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  transition: opacity .8s, visibility .8s;
}
.preloader.hidden {
  opacity: 0; visibility: hidden; pointer-events: none;
}
.preloader-logo {
  font-family: 'Playfair Display', serif;
  font-size: clamp(2rem, 5vw, 3.5rem);
  font-weight: 800; color: var(--gold);
  letter-spacing: .15em;
  animation: pulse-gold 1.5s ease infinite;
}
.preloader-bar {
  width: 200px; height: 2px;
  background: rgba(255,255,255,.1);
  margin-top: 2rem; border-radius: 2px; overflow: hidden;
}
.preloader-bar span {
  display: block; width: 0; height: 100%;
  background: linear-gradient(90deg, var(--gold), var(--cyan));
  animation: load-bar 2s ease forwards;
}
@keyframes load-bar { to { width: 100% } }
@keyframes pulse-gold {
  0%, 100% { opacity: 1 } 50% { opacity: .5 }
}
```

### HTML
```html
<div class="preloader" id="preloader">
  <div class="preloader-logo">BRAND NAME</div>
  <div class="preloader-bar"><span></span></div>
</div>
```

### JS
```js
window.addEventListener('load', () => {
  setTimeout(() => {
    document.getElementById('preloader').classList.add('hidden');
  }, 2200);
});
```

---

## Particle System

### CSS
```css
.particles {
  position: fixed; inset: 0; z-index: 0; pointer-events: none;
}
.particle {
  position: absolute; border-radius: 50%;
  animation: float-particle linear infinite;
}
@keyframes float-particle {
  0%   { transform: translateY(100vh) rotate(0deg); opacity: 0; }
  10%  { opacity: 1; }
  90%  { opacity: 1; }
  100% { transform: translateY(-10vh) rotate(360deg); opacity: 0; }
}
```

### HTML
```html
<div class="particles" id="particles"></div>
```

### JS
```js
(function() {
  const container = document.getElementById('particles');
  const colors = [
    'rgba(212,168,83,',   // gold
    'rgba(78,205,196,',   // cyan
    'rgba(255,107,53,'    // warm orange
  ];
  for (let i = 0; i < 40; i++) {
    const p = document.createElement('div');
    p.className = 'particle';
    const size = Math.random() * 3 + 1;
    const color = colors[Math.floor(Math.random() * colors.length)];
    const opacity = Math.random() * 0.5 + 0.2;
    p.style.cssText = `
      width: ${size}px; height: ${size}px;
      left: ${Math.random() * 100}%;
      background: ${color}${opacity});
      box-shadow: 0 0 ${size * 3}px ${color}0.3);
      animation-duration: ${Math.random() * 15 + 10}s;
      animation-delay: ${Math.random() * 10}s;
    `;
    container.appendChild(p);
  }
})();
```

---

## Scroll Reveal

### CSS
```css
.reveal {
  opacity: 0;
  transform: translateY(40px);
  transition: all .8s cubic-bezier(.4, 0, .2, 1);
}
.reveal.visible {
  opacity: 1;
  transform: none;
}
```

### JS
```js
const observer = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) e.target.classList.add('visible');
  });
}, { threshold: 0.15 });

document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
```

---

## Counter Animation

### JS
```js
function animateCount(elementId, target) {
  const el = document.getElementById(elementId);
  let current = 0;
  const step = target / 60;
  const interval = setInterval(() => {
    current += step;
    if (current >= target) { current = target; clearInterval(interval); }
    el.textContent = target >= 1000
      ? Math.floor(current).toLocaleString() + '+'
      : Math.floor(current) + '+';
  }, 30);
}

// Trigger on scroll
let counted = false;
const statsObserver = new IntersectionObserver(entries => {
  if (entries[0].isIntersecting && !counted) {
    counted = true;
    animateCount('stat1', 247);
    animateCount('stat2', 1200);
    animateCount('stat3', 18);
  }
}, { threshold: 0.5 });

const statsSection = document.querySelector('.stats');
if (statsSection) statsObserver.observe(statsSection);
```

---

## 3D Card Hover

### CSS
```css
.card-3d {
  background: var(--glass);
  border: 1px solid var(--glass-border);
  border-radius: 12px;
  padding: 2rem;
  transition: all .5s cubic-bezier(.4, 0, .2, 1);
  transform-style: preserve-3d;
}
.card-3d:hover {
  transform: perspective(1000px) rotateY(-3deg) rotateX(2deg) translateY(-8px);
  box-shadow:
    10px 20px 40px rgba(0,0,0,.4),
    0 0 30px rgba(212,168,83,.08);
  border-color: rgba(212,168,83,.15);
}
```

---

## CSS Cityscape

### CSS
```css
.skyline {
  position: relative;
  width: 100%; height: 300px;
  overflow: hidden;
}
.building {
  position: absolute; bottom: 0;
  background: linear-gradient(180deg, #1a1a2e 0%, #0a0a15 100%);
}
.window-light {
  position: absolute;
  width: 4px; height: 6px;
  background: rgba(255, 200, 100, 0.7);
  box-shadow: 0 0 4px rgba(255, 200, 100, 0.4);
  animation: flicker var(--duration, 3s) ease-in-out infinite;
  animation-delay: var(--delay, 0s);
}
@keyframes flicker {
  0%, 100% { opacity: 0.7; }
  30% { opacity: 1; }
  50% { opacity: 0.3; }
  80% { opacity: 0.9; }
}
.city-glow {
  position: fixed; bottom: 0; left: 0; right: 0;
  height: 40vh; pointer-events: none; z-index: 0;
  background: radial-gradient(
    ellipse 80% 50% at 50% 100%,
    rgba(212,168,83,.06) 0%,
    transparent 70%
  );
}
.star {
  position: absolute;
  width: 2px; height: 2px;
  background: white; border-radius: 50%;
  animation: twinkle 3s ease-in-out infinite;
}
@keyframes twinkle {
  0%, 100% { opacity: 0.3; } 50% { opacity: 1; }
}
```

### JS (Dynamic window lights)
```js
const buildings = [
  { left: 5, w: 12, h: 55 },
  { left: 18, w: 8, h: 72 },
  { left: 28, w: 14, h: 60 },
  { left: 44, w: 10, h: 85 },
  { left: 56, w: 12, h: 50 },
  { left: 70, w: 9, h: 68 },
  { left: 81, w: 14, h: 58 }
];

buildings.forEach(b => {
  for (let i = 0; i < 8; i++) {
    const wl = document.createElement('div');
    wl.className = 'window-light';
    wl.style.cssText = `
      left: ${b.left + Math.random() * b.w}%;
      bottom: ${Math.random() * b.h * 0.8 + b.h * 0.1}%;
      --duration: ${Math.random() * 3 + 2}s;
      --delay: ${Math.random() * 4}s;
    `;
    document.querySelector('.skyline').appendChild(wl);
  }
});
```

---

## Glassmorphism

### CSS
```css
.glass-card {
  background: rgba(255, 255, 255, 0.04);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 12px;
  padding: 2rem;
}
/* Glassmorphism CTA button */
.glass-btn {
  padding: 12px 28px;
  background: rgba(255, 255, 255, 0.06);
  backdrop-filter: blur(8px);
  border: 1px solid var(--gold);
  border-radius: 6px;
  color: white;
  font-size: 0.8rem;
  letter-spacing: 2px;
  text-transform: uppercase;
  cursor: pointer;
  transition: all .3s;
}
.glass-btn:hover {
  background: var(--gold);
  color: var(--bg);
  transform: scale(1.02);
}
```

---

## Text Stagger Reveal

### CSS
```css
.hero h1 .line {
  overflow: hidden;
}
.hero h1 .line span {
  display: inline-block;
  transform: translateY(100%);
  animation: text-rise 0.8s cubic-bezier(.16, 1, .3, 1) forwards;
}
.hero h1 .line:nth-child(1) span { animation-delay: 0.3s; }
.hero h1 .line:nth-child(2) span { animation-delay: 0.5s; }
.hero h1 .line:nth-child(3) span { animation-delay: 0.7s; }

@keyframes text-rise {
  to { transform: translateY(0); }
}
```

### HTML
```html
<h1>
  <div class="line"><span>Premium</span></div>
  <div class="line"><span>Living <em>Awaits</em></span></div>
  <div class="line"><span>You</span></div>
</h1>
```

---

## Ambient Glow Blobs

### CSS
```css
.ambient-glow {
  position: fixed; pointer-events: none; z-index: 0;
}
.glow-blob {
  position: absolute;
  border-radius: 50%;
  filter: blur(100px);
  opacity: 0.12;
  animation: glow-drift 15s ease-in-out infinite alternate;
}
.glow-blob.gold {
  width: 400px; height: 400px;
  background: var(--gold);
  top: 20%; left: 10%;
}
.glow-blob.cyan {
  width: 300px; height: 300px;
  background: var(--cyan);
  bottom: 30%; right: 15%;
  animation-delay: -5s;
}
@keyframes glow-drift {
  0%   { transform: translate(0, 0); }
  50%  { transform: translate(-20px, -30px); }
  100% { transform: translate(15px, 20px); }
}
```

---

## Navigation Scroll State

### CSS
```css
.nav {
  position: fixed; top: 0; left: 0; right: 0;
  z-index: 100; padding: 18px 40px;
  display: flex; align-items: center; justify-content: space-between;
  background: linear-gradient(to bottom, rgba(5,5,8,.95) 60%, transparent);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  transition: background .3s;
}
.nav.scrolled {
  background: rgba(5, 5, 8, 0.95);
  box-shadow: 0 1px 0 rgba(255,255,255,0.05);
}
```

### JS
```js
window.addEventListener('scroll', () => {
  document.getElementById('nav')
    .classList.toggle('scrolled', window.scrollY > 50);
});
```

---

## Grid Overlay System

### CSS — Technical Precision Markers
```css
/* Crosshair marker */
.crosshair {
  position: absolute; width: 18px; height: 18px; opacity: 0.25;
}
.crosshair::before, .crosshair::after {
  content: ''; position: absolute; background: var(--gold);
}
.crosshair::before { width: 1px; height: 100%; left: 50%; }
.crosshair::after  { height: 1px; width: 100%; top: 50%; }

/* Corner bracket (L-shape) */
.bracket-tl {
  position: absolute; top: 12px; left: 12px;
  width: 24px; height: 24px;
  border-top: 1px solid var(--gold);
  border-left: 1px solid var(--gold);
  opacity: 0.3;
}
.bracket-br {
  position: absolute; bottom: 12px; right: 12px;
  width: 24px; height: 24px;
  border-bottom: 1px solid var(--gold);
  border-right: 1px solid var(--gold);
  opacity: 0.3;
}
```

---

## Scanning Circle

### CSS
```css
.scan-circle {
  position: absolute; right: 18%; top: 50%;
  transform: translateY(-50%);
  width: 520px; height: 520px; border-radius: 50%;
  border: 1px solid rgba(200,212,42,.08);
  animation: circ 8s ease-in-out infinite;
}
.scan-circle::after {
  content: ''; position: absolute; inset: 40px;
  border: 1px solid rgba(200,212,42,.04); border-radius: 50%;
}
.scan-circle::before {
  content: ''; position: absolute; inset: -30px;
  border: 1px solid rgba(200,212,42,.03); border-radius: 50%;
}
@keyframes circ {
  0%, 100% { transform: translateY(-50%) scale(1); opacity: .6; }
  50%      { transform: translateY(-50%) scale(1.04); opacity: 1; }
}
```

---

## Fabric Texture Simulation

### CSS
```css
.swatch-silk {
  background: linear-gradient(135deg, #c4b39a 0%, #e8dcc8 40%, #c4b39a 100%);
  animation: silk-shimmer 3s ease infinite;
}
@keyframes silk-shimmer {
  0%, 100% { background-position: 0% 50%; }
  50%      { background-position: 100% 50%; }
}
.swatch-velvet {
  background: linear-gradient(180deg, #3A1855 0%, #2a1040 50%, #1a0d20 100%);
  box-shadow: inset 0 -10px 20px rgba(0,0,0,0.3);
}
.swatch-linen {
  background: #d4c8b0;
  background-image: repeating-linear-gradient(
    0deg, transparent, transparent 2px,
    rgba(0,0,0,0.04) 2px, rgba(0,0,0,0.04) 4px
  ), repeating-linear-gradient(
    90deg, transparent, transparent 2px,
    rgba(0,0,0,0.04) 2px, rgba(0,0,0,0.04) 4px
  );
}
```

---

## CSS Mannequin

### CSS
```css
.mannequin {
  position: relative; width: 240px; height: 420px;
}
.mannequin-body {
  position: absolute; bottom: 0; left: 50%;
  transform: translateX(-50%);
  width: 200px; height: 380px;
  background: linear-gradient(180deg, #3d1858 0%, #2a1040 40%, #1a0d20 100%);
  clip-path: polygon(
    35% 0%, 65% 0%, 72% 10%, 78% 30%,
    82% 55%, 88% 80%, 94% 100%, 6% 100%,
    12% 80%, 18% 55%, 22% 30%, 28% 10%
  );
  box-shadow: 0 15px 50px rgba(42,16,64,.5);
}
.mannequin-head {
  position: absolute; top: -5px; left: 50%;
  transform: translateX(-50%);
  width: 80px; height: 100px;
  background: radial-gradient(ellipse at 50% 30%, #4a2060, #2a1040);
  border-radius: 50% 50% 40% 40%;
}
```

---

## Floating Ticker

### CSS
```css
.ticker {
  position: fixed; bottom: 0; left: 0; right: 0;
  overflow: hidden; height: 36px; z-index: 50;
  background: rgba(0,0,0,0.6);
  backdrop-filter: blur(8px);
}
.ticker-content {
  display: flex; gap: 3rem;
  white-space: nowrap;
  animation: ticker-scroll 20s linear infinite;
  font-size: 0.7rem; letter-spacing: 2px;
  color: var(--text-dim); text-transform: uppercase;
  line-height: 36px;
}
@keyframes ticker-scroll {
  0%   { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
```
