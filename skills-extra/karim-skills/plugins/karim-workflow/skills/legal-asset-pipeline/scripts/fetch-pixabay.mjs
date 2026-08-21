#!/usr/bin/env node
// Fetch photos from Pixabay, save to assets/images/, and log each to the license ledger.
// Usage: node scripts/fetch-pixabay.mjs "<query>" [count]
// Needs PIXABAY_API_KEY in .env (free: https://pixabay.com/api/docs/). Node 18+.
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
  console.error('usage: node scripts/fetch-pixabay.mjs "<query>" [count]');
  process.exit(1);
}
const count = Math.min(Math.max(parseInt(countArg || '5', 10) || 5, 1), 200);

await loadEnv();
const key = process.env.PIXABAY_API_KEY;
if (!key) { console.error('Missing PIXABAY_API_KEY in .env'); process.exit(1); }

// Pixabay requires per_page >= 3; we fetch at least 3 then slice to the requested count.
const per = Math.max(count, 3);
const url = `https://pixabay.com/api/?key=${key}&q=${encodeURIComponent(query)}&per_page=${per}&image_type=photo&safesearch=true`;
const res = await fetch(url);
if (!res.ok) { console.error(`Pixabay API ${res.status}: ${await res.text()}`); process.exit(1); }
const { hits = [] } = await res.json();
const chosen = hits.slice(0, count);

await mkdir('assets/images', { recursive: true });
await ensureLedger();
for (const h of chosen) {
  const file = `pixabay-${h.id}.jpg`;
  const dest = `assets/images/${file}`;
  await download(h.largeImageURL, dest);
  await addRow({
    file, path: dest, source: h.pageURL,
    license: 'Pixabay Content License (https://pixabay.com/service/license-summary/)',
    author: h.user, note: query,
  });
  console.log(`saved ${dest}`);
}
console.log(`\n${chosen.length} image(s) + ledger rows written. Delete the ones you don't use (their rows too).`);
