#!/usr/bin/env node
/*
 * export_slides.js — render an AI Studio Today carousel HTML into post-ready PNGs.
 *
 * Each <section class="slide"> is captured at exactly 1080×1350 (×scale for retina),
 * named slide-01.png, slide-02.png, … in swipe order.
 *
 * Usage:
 *   node export_slides.js "<path/to/carousel.html>" [--out <dir>] [--scale 2]
 *
 * Requires Playwright (already present on this machine: `node playwright OK`).
 * If a fresh machine lacks it:  npm i -D playwright && npx playwright install chromium
 */
const path = require('path');
const fs = require('fs');

function arg(flag, def) {
  const i = process.argv.indexOf(flag);
  return i !== -1 && process.argv[i + 1] ? process.argv[i + 1] : def;
}

(async () => {
  const htmlArg = process.argv[2];
  if (!htmlArg || htmlArg.startsWith('--')) {
    console.error('Usage: node export_slides.js <carousel.html> [--out <dir>] [--scale 2]');
    process.exit(1);
  }
  const htmlPath = path.resolve(htmlArg);
  if (!fs.existsSync(htmlPath)) { console.error('Not found: ' + htmlPath); process.exit(1); }

  const outDir = path.resolve(arg('--out', path.join(path.dirname(htmlPath), 'slides')));
  const scale = parseFloat(arg('--scale', '2'));
  fs.mkdirSync(outDir, { recursive: true });

  let chromium;
  try { ({ chromium } = require('playwright')); }
  catch (e) {
    console.error('Playwright not found. Run: npm i -D playwright && npx playwright install chromium');
    process.exit(1);
  }

  // file:// URL with ?export=1 so the tweak panel is hidden
  const fileUrl = 'file:///' + htmlPath.replace(/\\/g, '/') + '?export=1';

  const browser = await chromium.launch();
  const ctx = await browser.newContext({ deviceScaleFactor: scale, viewport: { width: 1180, height: 1400 } });
  const page = await ctx.newPage();
  await page.goto(fileUrl, { waitUntil: 'networkidle' });
  // Webfonts (Anton/Inter/IBM Plex Mono) must be loaded or headlines render wrong.
  await page.evaluate(() => document.fonts && document.fonts.ready);
  await page.waitForTimeout(400);

  const slides = await page.locator('section.slide').all();
  if (!slides.length) { console.error('No <section class="slide"> found.'); await browser.close(); process.exit(1); }

  let n = 0;
  for (const slide of slides) {
    n += 1;
    const file = path.join(outDir, 'slide-' + String(n).padStart(2, '0') + '.png');
    await slide.screenshot({ path: file });
    console.log('✓ ' + file);
  }
  await browser.close();
  console.log('\nExported ' + n + ' slide(s) at ' + (1080 * scale) + '×' + (1350 * scale) + ' → ' + outDir);
})();
