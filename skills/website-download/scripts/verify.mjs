#!/usr/bin/env node
/**
 * Verify a mirror renders fully offline, in a real browser, at real widths.
 *
 * The number that decides pass/fail is firstPartyRemote = 0. A mirror can look
 * perfect while streaming every image from the origin CDN; you would only find
 * out with the network off. Third-party analytics/CRM staying remote is
 * correct and is not counted against the mirror.
 *
 * Usage:
 *   node verify.mjs <mirror-dir> [--port 8399] [--origin example.com]
 *                   [--widths 1440,1280,1024,768,390] [--shot]
 *
 * Requires PLAYWRIGHT_BROWSERS_PATH when the default browser dir is empty:
 *   PLAYWRIGHT_BROWSERS_PATH="C:\\Users\\user\\AppData\\Local\\pw-browsers-alt"
 */
import { chromium } from 'playwright';
import { spawn } from 'node:child_process';
import { readdirSync, statSync, existsSync } from 'node:fs';
import { join, resolve } from 'node:path';

const argv = process.argv.slice(2);
const flag = (n, d) => { const i = argv.indexOf('--' + n); return i > -1 ? argv[i + 1] : d; };
const has = n => argv.includes('--' + n);

const mirrorArg = argv.find(a => !a.startsWith('--') && !argv[argv.indexOf(a) - 1]?.startsWith('--'));
if (!mirrorArg) { console.error('usage: verify.mjs <mirror-dir> [--port N] [--origin host]'); process.exit(2); }

const port = Number(flag('port', 8399));
const widths = flag('widths', '1440,1280,1024,768,390').split(',').map(Number);
let root = resolve(mirrorArg);

// Serve the HOST folder as web root — framework routers assume base "/", and
// the repair step rewrote every asset ref to root-absolute against it.
if (existsSync(root)) {
  const hostDir = readdirSync(root).find(
    d => d.includes('.') && statSync(join(root, d)).isDirectory() && existsSync(join(root, d, 'index.html'))
  );
  if (hostDir) root = join(root, hostDir);
}
const origin = flag('origin', readdirSync(resolve(mirrorArg)).find(d => d.includes('.')) || '');
const firstParty = origin ? origin.replace(/^www\./, '').split('.').slice(-2).join('.') : null;

console.log(`serving ${root} on :${port}`);
const server = spawn('python', ['-m', 'http.server', String(port)], { cwd: root, stdio: 'ignore' });
const stop = () => { try { server.kill(); } catch {} };
process.on('exit', stop); process.on('SIGINT', () => { stop(); process.exit(1); });

await new Promise(r => setTimeout(r, 1200));

const browser = await chromium.launch();
let worstRemote = 0, worstFailed = 0;

for (const w of widths) {
  // NOTE: the option is `viewport`, not `viewportSize`. Getting this wrong
  // silently runs every width at the 1280 default and the numbers look
  // identical across widths — that is the tell.
  const page = await browser.newPage({ viewport: { width: w, height: w >= 1024 ? 900 : 800 } });
  await page.goto(`http://localhost:${port}/`, { waitUntil: 'networkidle' }).catch(() => {});

  // Lazy assets need real scrolling; IntersectionObserver ignores a jump.
  await page.evaluate(async () => {
    const h = document.body.scrollHeight;
    for (let y = 0; y < h; y += 500) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 90)); }
    window.scrollTo(0, 0);
    await new Promise(r => setTimeout(r, 800));
    await document.fonts.ready;
  }).catch(() => {});

  const m = await page.evaluate((fp) => {
    const res = performance.getEntriesByType('resource');
    const remote = res.filter(e => !e.name.includes('localhost'));
    const imgs = [...document.images];
    return {
      vw: document.documentElement.clientWidth,
      overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth + 1,
      failed: res.filter(e => e.responseStatus >= 400).map(e => e.name.replace(location.origin, '')),
      local: res.length - remote.length,
      firstPartyRemote: fp ? [...new Set(remote.map(e => new URL(e.name).host).filter(h => h.includes(fp)))] : [],
      thirdParty: [...new Set(remote.map(e => new URL(e.name).host).filter(h => !fp || !h.includes(fp)))],
      imgBroken: imgs.filter(i => i.complete && i.naturalWidth === 0).length,
      imgTotal: imgs.length,
      fontsLoaded: document.fonts.size,
    };
  }, firstParty);

  if (has('shot') && (w === widths[0] || w === widths.at(-1))) {
    await page.screenshot({ path: join(resolve(mirrorArg), `verify-${w}.png`) });
  }
  await page.close();

  worstRemote = Math.max(worstRemote, m.firstPartyRemote.length);
  worstFailed = Math.max(worstFailed, m.failed.length);

  const fpr = m.firstPartyRemote.length ? `LEAK ${m.firstPartyRemote.join(',')}` : 'none';
  console.log(
    `${String(w).padStart(4)}px  failed=${String(m.failed.length).padStart(2)}  ` +
    `imgBroken=${m.imgBroken}/${m.imgTotal}  local=${m.local}  fonts=${m.fontsLoaded}  ` +
    `overflow=${m.overflow ? 'YES' : 'no'}  first-party-remote=${fpr}`
  );
  if (m.failed.length) console.log(`        failing: ${m.failed.slice(0, 4).join(' | ')}`);
  if (w === widths[0] && m.thirdParty.length) {
    console.log(`        third-party (expected remote): ${m.thirdParty.slice(0, 6).join(', ')}`);
  }
}

await browser.close();
stop();

const ok = worstRemote === 0 && worstFailed === 0;
console.log(`\n${ok ? 'PASS' : 'INCOMPLETE'} — first-party remote calls: ${worstRemote}, failed requests: ${worstFailed}`);
if (!ok) console.log('Re-run `mirror.py repair`, then verify again ON A FRESH PORT (browsers cache 404s per origin).');
process.exit(ok ? 0 : 1);
