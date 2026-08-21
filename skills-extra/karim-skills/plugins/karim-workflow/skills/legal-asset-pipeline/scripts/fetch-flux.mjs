#!/usr/bin/env node
// Generate images with fal.ai FLUX.1-schnell, save to assets/images/, log each to the ledger + design/image-prompts.md.
// Usage: node scripts/fetch-flux.mjs "<prompt>" [count]
// Needs FAL_KEY in .env (https://fal.ai/dashboard/keys). Node 18+.
// FLUX.1-schnell is Apache-2.0 (commercial-safe); fal.ai is a metered API — verify pricing before you spend.
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
const PROMPTS = 'design/image-prompts.md';
const PROMPTS_HEADER = `# Image prompts\n\nPrompts used to generate images in this project.\n\n| File | Model | Prompt |\n|------|-------|--------|\n`;

async function ensureLedger() {
  await mkdir('assets/licenses', { recursive: true });
  if (!existsSync(LEDGER)) await writeFile(LEDGER, HEADER);
}
async function addRow(r) {
  await appendFile(LEDGER, `| ${r.file} | ${r.path} | ${r.source} | ${r.license} | ${r.author} | ${r.note} |\n`);
}
async function ensurePrompts() {
  await mkdir('design', { recursive: true });
  if (!existsSync(PROMPTS)) await writeFile(PROMPTS, PROMPTS_HEADER);
}
async function addPrompt(file, prompt) {
  await appendFile(PROMPTS, `| ${file} | FLUX.1-schnell | ${prompt} |\n`);
}
async function download(url, dest) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`download failed ${res.status}`);
  await writeFile(dest, Buffer.from(await res.arrayBuffer()));
}

const [prompt, countArg] = process.argv.slice(2);
if (!prompt) {
  console.error('usage: node scripts/fetch-flux.mjs "<prompt>" [count]');
  process.exit(1);
}
const count = Math.min(Math.max(parseInt(countArg || '1', 10) || 1, 1), 4);

await loadEnv();
const key = process.env.FAL_KEY;
if (!key) { console.error('Missing FAL_KEY in .env'); process.exit(1); }

const res = await fetch('https://fal.run/fal-ai/flux/schnell', {
  method: 'POST',
  headers: { Authorization: `Key ${key}`, 'Content-Type': 'application/json' },
  body: JSON.stringify({ prompt, num_images: count }),
});
if (!res.ok) { console.error(`fal.ai API ${res.status}: ${await res.text()}`); process.exit(1); }
const { images = [], seed } = await res.json();

await mkdir('assets/images', { recursive: true });
await ensureLedger();
await ensurePrompts();
let i = 0;
for (const img of images) {
  const ext = img.content_type === 'image/png' ? 'png' : 'jpg';
  const file = `flux-${seed ?? Date.now()}-${i}.${ext}`;
  const dest = `assets/images/${file}`;
  await download(img.url, dest);
  await addRow({
    file, path: dest,
    source: 'https://fal.ai/models/fal-ai/flux/schnell (generated)',
    license: 'Apache-2.0 (FLUX.1-schnell, https://huggingface.co/black-forest-labs/FLUX.1-schnell)',
    author: 'Black Forest Labs FLUX.1-schnell (AI-generated)',
    note: prompt,
  });
  await addPrompt(file, prompt);
  console.log(`saved ${dest}`);
  i++;
}
console.log(`\n${images.length} image(s) + ledger rows + prompt log written. Delete the ones you don't use (their rows too).`);
