#!/usr/bin/env node
// Fetch photos from Pexels, save to assets/images/, and log each to the license ledger.
// Usage: node scripts/fetch-pexels.mjs "<query>" [count]
// Needs PEXELS_API_KEY in .env (free: https://www.pexels.com/api/). Node 18+.
import { writeFile, mkdir, appendFile, readFile } from 'node:fs/promises';
import { existsSync } from 'node:fs';

async function loadEnv() {
  try {
    const txt = await readFile('.env', 'utf8');
    for (const line of txt.split(/\r?\n/)) {
      const m = line.match(/^\s*([\w.-]+)\s*=\s*(.*)\s*$/);
      if (m && !(m[1] in process.env)) process.env[m[1]] = m[2].replace(/^["']|["']$/g, '');
    }
  } catch { /* no .env, fall back to real env */ }
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
  console.error('usage: node scripts/fetch-pexels.mjs "<query>" [count]');
  process.exit(1);
}
const count = Math.min(Math.max(parseInt(countArg || '5', 10) || 5, 1), 80);

await loadEnv();
const key = process.env.PEXELS_API_KEY;
if (!key) { console.error('Missing PEXELS_API_KEY in .env'); process.exit(1); }

const url = `https://api.pexels.com/v1/search?query=${encodeURIComponent(query)}&per_page=${count}`;
const res = await fetch(url, { headers: { Authorization: key } });
if (!res.ok) { console.error(`Pexels API ${res.status}: ${await res.text()}`); process.exit(1); }
const { photos = [] } = await res.json();

await mkdir('assets/images', { recursive: true });
await ensureLedger();
for (const p of photos) {
  const file = `pexels-${p.id}.jpg`;
  const dest = `assets/images/${file}`;
  await download(p.src.original, dest);
  await addRow({
    file, path: dest, source: p.url,
    license: 'Pexels License (https://www.pexels.com/license/)',
    author: p.photographer, note: query,
  });
  console.log(`saved ${dest}`);
}
console.log(`\n${photos.length} image(s) + ledger rows written. Delete the ones you don't use (their rows too).`);
