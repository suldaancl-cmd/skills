#!/usr/bin/env node
// Fetch photos from Unsplash, save to assets/images/, and log each to the license ledger.
// Usage: node scripts/fetch-unsplash.mjs "<query>" [count]
// Needs UNSPLASH_ACCESS_KEY in .env (free: https://unsplash.com/developers). Node 18+.
// Note: Unsplash API terms require crediting the photographer + linking back — recorded in the ledger.
import { writeFile, mkdir, appendFile, readFile } from 'node:fs/promises';
import { existsSync } from 'node:fs';

async function loadEnv() {
  try {
    const txt = await readFile('.env', 'utf8');
    for (const line of txt.split(/\r?\n/)) {
      const m = line.match(/^\s*([\w.-]+)\s*=\s*(.*)\s*$/);
      if (m && !(m[1] in process.env)) process.env[m[1]] = m[2].replace(/^["']|["']$/g, '');
    }
  } catch { /* no .env */ }
}

const LEDGER = 'assets/licenses/assets.md';
const HEADER = `# Asset license ledger\n\nEvery asset used in this project. No row here = it does not ship.\n\n| File | Path | Source | License | Author | Note |\n|------|------|--------|---------|--------|------|\n`;

async function ensureLedger() {
  await mkdir('assets/licenses', { recursive: true });
  if (!existsSync(LEDGER)) await writeFile(LEDGER, HEADER);
}
async function addRow(r) {
  await appendFile(LEDGER, `| ${r.file} | ${r.path} | ${r.source} | ${r.license} | ${r.author} | ${r.note} |\n`);
}
async function download(url, dest) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`download failed ${res.status}`);
  await writeFile(dest, Buffer.from(await res.arrayBuffer()));
}

const [query, countArg] = process.argv.slice(2);
if (!query) {
  console.error('usage: node scripts/fetch-unsplash.mjs "<query>" [count]');
  process.exit(1);
}
const count = Math.min(Math.max(parseInt(countArg || '5', 10) || 5, 1), 30);

await loadEnv();
const key = process.env.UNSPLASH_ACCESS_KEY;
if (!key) { console.error('Missing UNSPLASH_ACCESS_KEY in .env'); process.exit(1); }

const url = `https://api.unsplash.com/search/photos?query=${encodeURIComponent(query)}&per_page=${count}`;
const res = await fetch(url, { headers: { Authorization: `Client-ID ${key}` } });
if (!res.ok) { console.error(`Unsplash API ${res.status}: ${await res.text()}`); process.exit(1); }
const { results = [] } = await res.json();

await mkdir('assets/images', { recursive: true });
await ensureLedger();
for (const r of results) {
  const file = `unsplash-${r.id}.jpg`;
  const dest = `assets/images/${file}`;
  await download(r.urls.full, dest);
  // Unsplash guideline: ping the download endpoint when a photo is actually used.
  try { await fetch(r.links.download_location, { headers: { Authorization: `Client-ID ${key}` } }); } catch { /* non-fatal */ }
  await addRow({
    file, path: dest, source: r.links.html,
    license: 'Unsplash License (https://unsplash.com/license)',
    author: `${r.user.name} (${r.user.links.html})`, note: query,
  });
  console.log(`saved ${dest}`);
}
console.log(`\n${results.length} image(s) + ledger rows written. Delete the ones you don't use (their rows too).`);
