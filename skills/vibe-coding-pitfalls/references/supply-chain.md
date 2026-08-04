# Supply-chain & dependency failures

AI doesn't just write your code — it picks your dependencies. That's a new, AI-specific attack surface.

## 1. Slopsquatting — hallucinated package names

**What:** LLMs confidently suggest `npm install` / `pip install` of packages that **don't exist** — usually a plausible conflation of two real names. Attackers pre-register the hallucinated names with malicious payloads, so the next developer who runs the AI's command installs malware.

**Why it's dangerous:**
- **19.7%** of package names in AI-generated code are hallucinated (USENIX Security 2025, across 576,000 samples).
- **43%** of hallucinated names repeat across identical prompts — they're *predictable*, so attackers can farm and pre-register them.
- Real cases: a researcher's empty `huggingface-cli` (a hallucination of the real `huggingface_hub` CLI) got **30,000+ downloads in 3 months**, partly because Alibaba pasted the hallucinated install command into public docs. `react-codeshift` (conflation of `jscodeshift` + `react-codemod`) appeared in 237 repos before being claimed.

**Catch it:** For every install command the AI produced, **verify the package exists on the official registry** (npmjs.com / pypi.org), check the publisher, download count, and publish date. A brand-new package with the exact name the AI invented is the trap.

**Fix:**
- Never blind-run AI-generated install commands. Verify names first.
- Lockfiles committed (`package-lock.json`, `poetry.lock`) with integrity hashes; use `npm ci` (not `npm install`) in CI.
- SCA on every dependency: `npm audit` / `pip-audit`, plus Socket.dev or Snyk (which specifically flag hallucination/typosquat patterns). <25% of developers run SCA on AI-suggested packages — be in the 25%.

## 2. Known-vulnerable pinned dependencies

**What:** AI pins a specific version that was fine at training time but now has a known CVE. The app runs normally and passes functional tests, so the vulnerability is invisible until exploited.

**Real case:** an AI-generated Next.js app pinned a version vulnerable to **CVE-2025-29927** (middleware auth bypass); attackers exploited it to run a cryptominer. As one engineer put it: *"auditing generated code requires higher skill than writing it"* — which is exactly why juniors/vibe coders miss it.

**Fix:** `npm audit --audit-level=high` / `pip-audit` in CI; Dependabot/Renovate for automated updates; don't accept old pinned versions without a documented reason.

## 3. Compromised build pipeline / poisoned model output (OWASP-LLM03/04)

**What:** The supply chain extends to your CI credentials and to the model itself — the Nx compromise used AI-code vulnerabilities as a foothold to steal publishing credentials, then weaponized that to steal *vibe coders'* crypto wallets downstream.

**Fix:** Least-privilege CI tokens; SBOM generation (OWASP 2025 A03 guidance); pin and verify your own build toolchain; treat publishing credentials as crown jewels.

## The dependency rule

> Every package the AI names is a claim, not a fact. Verify it exists, verify it's the real one, scan it, and lock it — before it's ever installed. The cheapest supply-chain attack in 2026 is the one where you typed the malware's name yourself because the AI told you to.
