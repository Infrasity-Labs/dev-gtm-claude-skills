<div align="center">

<img src="assets/infrasity_logo.avif" alt="Infrasity" height="64" />

# Claude Code Skills for SEO, GEO & Developer Marketing

**Free, open-source Claude skills that audit your docs, score your AI discoverability, and run developer-marketing workflows — so your product gets found, parsed, and cited by AI systems.**

[![Claude Compatible](https://img.shields.io/badge/Claude-Compatible-FF4A1C)](https://claude.ai/) [![GEO Optimized](https://img.shields.io/badge/GEO-Optimized-7F77DD)](https://www.infrasity.com/services/ai-geo-optimization-agency) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) [![GitHub stars](https://img.shields.io/github/stars/Infrasity-Labs/dev-gtm-claude-skills?style=social)](https://github.com/Infrasity-Labs/dev-gtm-claude-skills/stargazers) [![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/) [![skills.sh](https://skills.sh/b/Infrasity-Labs/dev-gtm-claude-skills)](https://skills.sh/Infrasity-Labs/dev-gtm-claude-skills)

[Skills](#skills) · [Install](#installation) · [Commands](#commands) · [Who it's for](#who-its-for) · [FAQ](#faq) · [Website](https://www.infrasity.com/claude-skills)

**Works with:** Claude Code · OpenAI Codex · OpenClaw · Hermes Agent[^hermes] · Mistral Vibe[^vibe] · Cursor · Aider · Windsurf · Kilo Code · OpenCode · Augment · Antigravity

<p align="center">
  <img src="./assets/dev-gtm-claude-skills.png" width="100%" alt="dev-gtm-claude-skills"/>
</p>

</div>

---

`dev-gtm-claude-skills` is a collection of open-source **Claude Code skills** for **SEO**, **GEO (Generative Engine Optimization)**, **AI discoverability**, and **developer marketing**. Each skill is a self-contained package — a `SKILL.md` that tells Claude when and how to use it, optional Python tooling, and a README with full usage docs. Install once, then run from Claude Code, Claude Desktop, or Claude.ai with a plain-language prompt.

These skills are built for **developer-focused companies** — DevTools, AI-agent platforms, observability, and B2B SaaS — that need their documentation and content to be **cited by AI systems like ChatGPT, Claude, Perplexity, and Gemini**, not just indexed by Google.

> **What is GEO?** Generative Engine Optimization is the practice of optimizing content so it gets surfaced and cited by AI answer engines. Traditional SEO tools optimize for search crawlers; these skills audit the signals — structured content, `llms.txt`, internal linking, and documentation completeness — that LLMs use when deciding what to recommend.

### What you can do in one prompt

- **Audit developer docs** for SEO and AI discoverability — 33 checks, scored 0–100
- **Score API & SDK documentation** quality, endpoint by endpoint
- **Check AI-readiness** — `robots.txt`, `llms.txt`, and `llms-full.txt` in one pass
- **Generate 3-month SEO performance reports** vs competitors
- **Fix internal linking** — find orphan pages and dead-ends, get paste-ready suggestions
- **Produce SEO content briefs** as formatted `.docx` outlines

---

## What Are Claude Code Skills & Agent Plugins?

Claude Code skills (also called agent skills or coding-agent plugins) are modular instruction packages that give AI coding agents domain expertise they don't have out of the box. Each skill in this repo includes:

- **`SKILL.md`** — structured instructions, workflows, and decision frameworks that tell the agent when and how to act
- **Python tools** — optional stdlib-only CLI scripts for the skills that crawl, score, or render reports
- **Reference docs** — templates, scoring guides, and checklists the skill loads on demand

Because every skill follows the open `SKILL.md` standard, it isn't locked to a single product. The same package runs in Claude Code, Claude Desktop, Claude.ai, and any other agent that reads the standard (see [Multi-Tool Support](#multi-tool-support)).

### Skills vs Agents

|  | Skills | Agents |
| --- | --- | --- |
| **Purpose** | _How_ to execute a task | _What_ task to do |
| **Scope** | A single, well-defined workflow | An end-to-end job, often composing skills |
| **Example** | "Follow these 33 checks to audit docs" | "Research, write, and review this blog post" |

This repo ships several bundles: the SEO/GEO/docs **skills** under [`skills/`](skills/), the full-funnel marketing **skills** under [`marketing-skills/`](marketing-skills/), the blog content engine under [`writing-skills/`](writing-skills/), a comprehensive **SEO suite** under [`seo-skills/`](seo-skills/), and blog-production **agents** under [`agents/`](agents/).

---

## Table of contents

- [What Are Claude Code Skills & Agent Plugins?](#what-are-claude-code-skills--agent-plugins)
- [Multi-Tool Support](#multi-tool-support)
- [Installation](#installation)
- [Skills](#skills)
- [Marketing skills](#marketing-skills)
- [Writing skills](#writing-skills)
- [SEO skills](#seo-skills)
- [Commands](#commands)
- [Who it's for](#who-its-for)
- [Requirements](#requirements)
- [Sample outputs](#sample-outputs)
- [Repository structure](#repository-structure)
- [FAQ](#faq)
- [Contributing](#contributing)
- [License](#license)

---

## Multi-Tool Support

Every skill here is written to the open `SKILL.md` standard, so it isn't tied to a single agent. **Claude Code**, **Claude Desktop**, and **Claude.ai** read the skills natively (see [Installation](#installation)). For every other tool, the repo ships converter and installer scripts under [`scripts/`](scripts/) — clone the repo, then run the one-liner for your tool.

```bash
git clone https://github.com/infrasity-labs/dev-gtm-claude-skills.git
cd dev-gtm-claude-skills
```

Each script discovers all skills under `skills/`, `marketing-skills/`, and `writing-skills/` and installs them in the format that tool expects.

| Tool | Tested | Skills land in |
| --- | --- | --- |
| **Claude Code** | ✅ | `~/.claude/skills/` |
| **Claude Desktop / Claude.ai** | ✅ | ZIP upload |
| **Hermes Agent** | ✅ | `~/.hermes/skills/` |
| **Kilo Code** | ✅ | `~/.claude/skills/` (via `claudeCodeCompat`) |
| **Mistral Vibe** | ✅ | `~/.vibe/skills/` |
| **OpenAI Codex** | ✅ | `~/.codex/skills/` |
| **OpenClaw** | ✅ | `~/.openclaw/skills/` |
| **Augment** | ✅ | `.augment/skills/` (project-local) |
| **Antigravity** | ✅ | `~/.gemini/antigravity/skills/` |
| **Cursor** | 🔜 | `.cursor/rules/` (project-local) |
| **Aider** | 🔜 | `CONVENTIONS.md` (project-local) |
| **Windsurf** | 🔜 | `.windsurf/skills/` (project-local) |
| **OpenCode** | 🔜 | `.opencode/skills/` (project-local) |

See [full install steps per tool](#per-tool-install-steps) below.

---

## Installation

Most skills need **no API keys**; the SEO skills that pull live search data use a DataForSEO MCP server (setup below).

### Quick install (recommended)

Install every skill in this repo with one command — no cloning, no copying:

```bash
npx skills add Infrasity-Labs/dev-gtm-claude-skills
```

This pulls the latest skills straight into your Claude Code skills directory. Re-run it any time to update. Prefer to install manually or use Claude Desktop / Claude.ai? Use one of the methods below.

### Blog skills runtime (agents + scripts)

The [writing skills](#writing-skills) add a `/blog` content engine built from 30 sub-skills, **5 subagents**, and **shared Python scripts**. `npx skills add` installs the skill instructions, but the subagents and shared scripts need one extra step so the `/blog write` pipeline (research → write → SEO → review) runs end-to-end:

```bash
# Clone the repository to access the installer
git clone https://github.com/Infrasity-Labs/dev-gtm-claude-skills.git
cd dev-gtm-claude-skills
./scripts/claude-blog-install.sh                  # agents → ~/.claude/agents, scripts → ~/.claude/scripts
pip install -r writing-skills/requirements.txt    # textstat + beautifulsoup4
```

Use `--project` to install into the current project's `./.claude/` instead of `~/.claude/` (make sure to run the script from your project's root directory, e.g., `path/to/cloned-repo/scripts/claude-blog-install.sh --project`), and `--dry-run` to preview. A few sub-skills need their own credentials — `blog-google` (Google API OAuth), `blog-audio` / `blog-image` (`GOOGLE_AI_API_KEY` + nanobanana MCP), `blog-notebooklm` (browser login) — and all degrade gracefully when unconfigured.

### Claude Code (manual)

Clone the repo and copy the skill into your Claude Code skills directory.

```bash
git clone https://github.com/infrasity-labs/dev-gtm-claude-skills.git
```

**Project-level** (available only in the current project):

```bash
mkdir -p .claude/skills
cp -r dev-gtm-claude-skills/skills/<skill-name> .claude/skills/
```

**User-level** (available across all projects):

```bash
mkdir -p ~/.claude/skills
cp -r dev-gtm-claude-skills/skills/<skill-name> ~/.claude/skills/
```

Skills activate automatically — Claude reads every `SKILL.md` in `.claude/skills/` at the start of each session. Trigger them by describing the task in plain language, or type `/<skill-name>` directly.

<p align="center">
  <img src="./assets/clone-repo.png" width="100%" alt="clone repo"/>
</p>

<p align="center">
  <img src="./assets/activate-skills.gif" width="100%" alt="Activate skills GIF"/>
</p>

### Claude Desktop / Claude.ai

Skills upload as ZIP files via **Settings → Customize → Skills → Create skill → Upload a skill**.

```bash
git clone https://github.com/infrasity-labs/dev-gtm-claude-skills.git
cd dev-gtm-claude-skills/skills

# Zip the skill you want to install
zip -r docs-auditor.zip docs-auditor/
```

Upload the `.zip`, toggle the skill on, and it's active across all your chats. Uploaded skills stay private to your account; Claude installs any required packages the first time it runs them.

<p align="center">
  <img src="./assets/converting-to-zip.gif" width="100%" alt="Converting to zip GIF"/>
</p>

<p align="center">
  <img src="./assets/add-to-claude.gif" width="100%" alt="Add to Claude GIF"/>
</p>

### DataForSEO MCP (for the live-search skills)

`growth-report`, `blog-post-counter`, and `api-docs-quality-report` pull live search data via a DataForSEO MCP server.

**Claude Code** — add to `.claude/settings.json` or `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "dataforseo": {
      "command": "npx",
      "args": ["-y", "@dataforseo/mcp-server"],
      "env": {
        "DATAFORSEO_USERNAME": "your@email.com",
        "DATAFORSEO_PASSWORD": "your_api_password"
      }
    }
  }
}
```

**Claude Desktop** — Customize → Connectors → Add Custom Connector:

```
https://your_email:your_api_password@mcp.dataforseo.com/http
```

Get credentials at [dataforseo.com](https://dataforseo.com).

---

## Install Steps for Every Tool

All CLI installs start with cloning the repo:

```bash
git clone https://github.com/infrasity-labs/dev-gtm-claude-skills.git
cd dev-gtm-claude-skills
```

### Hermes Agent ✅

1. Run the sync script:
   ```bash
   python3 scripts/sync-hermes-skills.py
   ```
2. Skills are symlinked into `~/.hermes/skills/`. Add `--copy` if you want to delete the repo clone after install.
3. Open Hermes and describe your task — the agent auto-loads the matching skill. You can also invoke by name: `/docs-auditor`.

> Pass `--verbose` to see each skill as it syncs, `--dry-run` to preview without installing.

---

### Kilo Code ✅

1. In VS Code settings, enable the compatibility flag:
   ```
   kilo-code.new.claudeCodeCompat: true
   ```
   (Search "kilo-code claudeCodeCompat" in the VS Code settings UI.)
2. Install skills using the standard Claude Code method — either the quick install:
   ```bash
   npx skills add Infrasity-Labs/dev-gtm-claude-skills
   ```
   or manual copy to `~/.claude/skills/`:
   ```bash
   mkdir -p ~/.claude/skills
   cp -r skills/<skill-name> ~/.claude/skills/
   ```
3. Open a Kilo Code chat and describe your task. Kilo Code reads from `~/.claude/skills/` when `claudeCodeCompat` is on.

> **Note:** Placing `.md` files in `.kilocode/rules/` only injects passive context — it does not enable skill invocation. The `claudeCodeCompat` path is the correct approach.

---

### Mistral Vibe ✅

1. Run the install script:
   ```bash
   ./scripts/vibe-install.sh
   ```
2. Skills are symlinked flat into `~/.vibe/skills/<skill-name>/`. Add `--copy` to copy instead of symlink.
3. Open Vibe and describe your task, or invoke directly: `/docs-auditor`. Vibe auto-discovers skills from `~/.vibe/skills/`.

> Pass `--dry-run` to preview without installing, `--verbose` to list each skill.

---

### OpenAI Codex ✅

1. Generate local symlinks:
   ```bash
   python3 scripts/sync-codex-skills.py
   ```
2. Copy skills to the Codex global directory:
   ```bash
   ./scripts/codex-install.sh
   ```
3. Skills land in `~/.codex/skills/<skill-name>/`. Open Codex and describe your task — the model reads the skill automatically.

> Use `./scripts/codex-install.sh --dry-run` to preview, `--list` to see all available skills.

---

### OpenClaw ✅

1. Run the install script:
   ```bash
   ./scripts/openclaw-install.sh
   ```
2. Restart the OpenClaw gateway to pick up the new skills:
   ```bash
   openclaw gateway restart
   ```
3. Verify the skills are visible:
   ```bash
   openclaw skills list
   ```
4. Open an OpenClaw chat and describe your task. The agent auto-loads the matching skill. You can also invoke explicitly: `/docs-auditor`.

> Use `--dry-run` to preview without installing, `--force` to overwrite existing skills.

---

### Augment ✅

Augment reads skills from the `.augment/skills/` directory inside your **project** — run these commands from your project root, not from the cloned repo.

1. Convert skills to Augment format:
   ```bash
   cd /path/to/dev-gtm-claude-skills
   ./scripts/convert.sh --tool augment
   ```
2. Install into your project:
   ```bash
   ./scripts/install.sh --tool augment --target /path/to/your/project
   ```
   Skills land in `/path/to/your/project/.augment/skills/<skill-name>/SKILL.md`.
3. Open Augment in that project and describe your task — Augment detects the matching skill from `.augment/skills/` automatically.

> Re-run both commands whenever you want to update to the latest skills. Use `--force` on `install.sh` to overwrite.

---

### Antigravity ✅

1. Convert skills to Antigravity format:
   ```bash
   ./scripts/convert.sh --tool antigravity
   ```
2. Install globally:
   ```bash
   ./scripts/install.sh --tool antigravity
   ```
3. Skills land in `~/.gemini/antigravity/skills/<skill-name>/SKILL.md`. Open Antigravity and describe your task — the agent auto-loads the matching skill.

> Re-run both commands to update. Use `--force` on `install.sh` to overwrite existing skills.

---

### Cursor 🔜 *(steps ready, not yet tested)*

1. Convert skills to Cursor `.mdc` rule format:
   ```bash
   ./scripts/convert.sh --tool cursor
   ```
2. Install into your project:
   ```bash
   ./scripts/install.sh --tool cursor --target /path/to/your/project
   ```
   Skills land in `/path/to/your/project/.cursor/rules/<skill-name>.mdc`.
3. Open Cursor in that project — rules are applied automatically per the `globs` and `alwaysApply` settings in each `.mdc` file.

---

### Aider 🔜 *(steps ready, not yet tested)*

1. Convert all skills into a single `CONVENTIONS.md`:
   ```bash
   ./scripts/convert.sh --tool aider
   ```
2. Install into your project:
   ```bash
   ./scripts/install.sh --tool aider --target /path/to/your/project
   ```
3. Run Aider with the conventions file:
   ```bash
   aider --read CONVENTIONS.md
   ```

---

### Windsurf 🔜 *(steps ready, not yet tested)*

1. Convert skills to Windsurf skill bundle format:
   ```bash
   ./scripts/convert.sh --tool windsurf
   ```
2. Install into your project:
   ```bash
   ./scripts/install.sh --tool windsurf --target /path/to/your/project
   ```
   Skills land in `/path/to/your/project/.windsurf/skills/<skill-name>/SKILL.md`.
3. Open Windsurf in that project and describe your task.

---

## Skills

Ten production-grade skills for SEO, GEO, documentation, and developer-marketing workflows.

| Skill | Claude skill for… | What it does | Example trigger |
| --- | --- | --- | --- |
| **`docs-auditor`** | documentation SEO & AI discoverability | Audits a developer docs site across **33 checks in 7 categories** — AI discoverability, structure, content quality, SEO, internal linking, versioning — and returns a scored 0–100 report with pass/warn/fail per check. | `Audit the docs at docs.stripe.com` |
| **`sdk-docs-auditor`** | SDK documentation | Audits SDK docs across **6 sections** (Installation, Quick Start, Error Handling, Troubleshooting, Examples, Best Practices), scores each 0–100, cross-references gaps, and ships a downloadable HTML report. | `Audit the SDK docs at docs.example.com` |
| **`api-docs-quality-report`** | API documentation quality | Crawls **every endpoint page** and scores each across 5 checks. Outputs an interactive HTML report with a scorecard, pattern analysis, top issues, and per-endpoint fix guidance. | `Run an API docs audit on docs.company.com` |
| **`growth-report`** | SEO performance reports | Generates a **3-month SEO performance report** for any domain vs competitors using live DataForSEO data: traffic trends, keyword rankings, top content clusters, and competitive positioning. | `Generate SEO report for firefly.ai vs spacelift.io` |
| **`blog-post-counter`** | content research & competitive intel | Counts unique blog posts for any company from its sitemap or listing page, with a competitor-comparison mode to benchmark content volume across domains. | `How many blogs does hackmamba.io have vs infrasity.com` |
| **`brief-outline-generator`** | SEO content briefs | Generates a fully structured SEO content outline and exports it as a formatted **`.docx`** with section headings, topic prompts, and angles for a writer to fill in. | `Generate a content brief for "developer marketing strategy"` |
| **`llms-txt-checker`** | GEO & AI readiness | Audits a domain's AI-readiness by probing `robots.txt`, `llms.txt`, and `llms-full.txt`, scoring each against a structured checklist with a pass/warn/fail report and prioritized fixes. **No API keys.** | `Check if stripe.com has llms.txt` |
| **`orphan-pages-internal-linking-opportunities`** | internal linking | Finds all **orphan pages** (zero incoming internal links) using Ahrefs, clusters them by topic, and generates 3 linking suggestions per orphan with anchor text and placement. Styled HTML report. | `Run an orphan page audit on example.com/blog/` |
| **`no-outlinks-audit`** | internal linking | Finds **dead-end pages** (zero outgoing internal links) and generates 3 outgoing link suggestions per page — anchor text, placement, ready-to-paste copy. Styled HTML report. | `Find pages with no outgoing links on example.com` |
| **`dev-marketing-prospector`** | prospecting & lead lists | Builds an exact-fit prospect list for any developer-focused vertical (AI agents, IaC, DevTools, observability, FinOps…), mapping a real outreach signal and email pain point per company, each sourced with a URL. | `Prospect AI agent companies, Series A, 50–200 headcount` |

---

## Marketing skills

A full-funnel pack of **28 developer-marketing skills** under [`marketing-skills/`](marketing-skills/) — covering demand gen, content, lifecycle, conversion, and retention. Install the whole set with the [quick install](#quick-install-recommended) command above.

| Skill | Claude skill for… |
| --- | --- |
| **`ab-testing`** | Designing A/B tests and building an experimentation program |
| **`ad-creative`** | Generating and iterating ad copy at scale for any platform |
| **`ads`** | Paid campaign strategy, targeting, and bidding (Google, Meta, LinkedIn) |
| **`ai-seo`** | Optimizing content to be cited by ChatGPT, Perplexity, Claude & AI Overviews |
| **`analytics`** | Setting up tracking, GA4, events, UTMs, and conversion measurement |
| **`churn-prevention`** | Cancel flows, save offers, dunning, and retention strategy |
| **`cold-email`** | B2B cold outreach and multi-touch follow-up sequences |
| **`community-marketing`** | Building and growing Discord/Slack communities and advocates |
| **`competitor-profiling`** | Researching and profiling competitors from their URLs |
| **`competitors`** | Building comparison, alternative, and "vs" pages |
| **`content-strategy`** | Planning topics, clusters, pillars, and editorial calendars |
| **`copywriting`** | Writing and improving landing, pricing, and product page copy |
| **`cro`** | Conversion rate optimization for pages and forms |
| **`customer-research`** | VOC, personas, JTBD, review mining, and transcript analysis |
| **`emails`** | Lifecycle, drip, onboarding, and re-engagement email flows |
| **`free-tools`** | Engineering-as-marketing — calculators, graders, and lead-gen tools |
| **`launch`** | Product launches, Product Hunt, and go-to-market planning |
| **`lead-magnets`** | Gated content, templates, checklists, and opt-in offers |
| **`marketing-ideas`** | Brainstorming growth tactics and channels when you're stuck |
| **`onboarding`** | Activation, first-run experience, and time-to-value |
| **`pricing`** | Pricing, packaging, freemium, and monetization strategy |
| **`programmatic-seo`** | Building templated SEO pages at scale from data |
| **`referrals`** | Referral, affiliate, and word-of-mouth program design |
| **`revops`** | Lead scoring, routing, and marketing-to-sales handoff |
| **`sales-enablement`** | Pitch decks, one-pagers, objection handling, and demo scripts |
| **`schema`** | Structured data and JSON-LD for rich results |
| **`seo-audit`** | Technical and on-page SEO audits and diagnostics |
| **`social`** | Social content, repurposing, and short-form video scripts |

---

## Writing skills

A full **blog content engine** under [`writing-skills/`](writing-skills/) — **30 sub-skills** routed by a `blog` orchestrator, plus 5 production subagents ([`agents/`](agents/)) and shared Python tooling ([`scripts/`](scripts/)). Dual-optimized for Google rankings (E-E-A-T, Dec 2025 Core Update) and AI citations (GEO/AEO). Invoke everything through `/blog <subcommand>` — see the [`/blog` command table](#blog--blog-content-engine). The same folder also ships **4 standalone writing skills** for copy, social, and prose quality.

These need one extra setup step beyond `npx skills add` — see [Blog skills runtime](#blog-skills-runtime-agents--scripts).

| Skill | Claude skill for… |
| --- | --- |
| **`blog`** | Orchestrator — routes `/blog <subcommand>` to the right sub-skill |
| **`blog-write`** | Writing new articles from scratch (research → write → SEO → review pipeline) |
| **`blog-rewrite`** | Optimizing/refreshing existing posts with anti-AI-detection patterns |
| **`blog-analyze`** | 5-category 100-point quality audit with AI-content detection |
| **`blog-brief`** | Content briefs with template recommendation and distribution plan |
| **`blog-outline`** | SERP-informed outlines with competitive gap analysis |
| **`blog-strategy`** | Positioning, topic clusters, and AI-citation surface strategy |
| **`blog-calendar`** | Editorial calendars with decay detection and 60/30/10 content mix |
| **`blog-cluster`** | Semantic topic-cluster planning + execution (hub-and-spoke) |
| **`blog-seo-check`** | Post-writing SEO validation (title, meta, headings, links, OG) |
| **`blog-schema`** | JSON-LD schema (BlogPosting, Person, FAQ, Breadcrumb) |
| **`blog-geo`** | AI-citation readiness audit with a 0–100 GEO score |
| **`blog-audit`** | Full-site blog health assessment across all posts |
| **`blog-factcheck`** | Verifying statistics against their cited sources |
| **`blog-cannibalization`** | Keyword-overlap / cannibalization detection across posts |
| **`blog-repurpose`** | Cross-platform repurposing (social, email, YouTube, Reddit) |
| **`blog-persona`** | Writing-voice and persona management (NNGroup framework) |
| **`blog-brand`** | Generating BRAND.md + VOICE.md context auto-loaded by all sub-skills |
| **`blog-discourse`** | Last-30-days discourse research (API-free via WebSearch) |
| **`blog-taxonomy`** | Tag/category management across CMS platforms |
| **`blog-chart`** | Inline SVG data-viz charts (internal-only, called by write/rewrite) |
| **`blog-image`** | AI image generation/editing via Gemini (nanobanana MCP) |
| **`blog-audio`** | Audio narration via Gemini TTS (summary/full/dialogue) |
| **`blog-notebooklm`** | Source-grounded research from your NotebookLM documents |
| **`blog-google`** | Google API data: PSI, CrUX, GSC, GA4, NLP, YouTube, Keywords |
| **`blog-flow`** | FLOW framework prompts (evidence-led, find/optimize/win) |
| **`blog-multilingual`** | One-command international publishing (write + translate + localize + hreflang) |
| **`blog-translate`** | SEO-optimized translation with format preservation |
| **`blog-localize`** | Cultural deep-adaptation per locale (DACH, FR, ES, JA, custom) |
| **`blog-locale-audit`** | Multilingual content QA (completeness, hreflang, parity, freshness) |

### Standalone writing skills

Beyond the `/blog` engine, [`writing-skills/`](writing-skills/) ships **4 standalone craft skills** for copy, social, and prose quality — usable on their own, no runtime setup required.

| Skill | Claude skill for… |
| --- | --- |
| **`ogilvy-copywriting`** | Sales-driven copy, headlines, and landing pages using David Ogilvy's advertising principles |
| **`social-media-posts`** | Platform-specific posts for LinkedIn, Facebook, Instagram & Reddit (limits, hooks, hashtags) |
| **`reddit-comments`** | Drafting on-brand Reddit comments from a domain + thread, with voice derived from the site |
| **`stop-slop`** | Stripping predictable AI writing tells from prose for more human-like output |

---

## SEO skills

A comprehensive **SEO suite** under [`seo-skills/`](seo-skills/) — **25 sub-skills** routed by a `seo` orchestrator, plus **18 specialist subagents** ([`agents/`](agents/)), shared Python tooling ([`scripts/`](scripts/)), and **8 optional MCP extensions** ([`seo-skills/extensions/`](seo-skills/extensions/)). Dual-optimized for Google rankings (technical SEO, E-E-A-T, Core Web Vitals with INP) and AI visibility (GEO for AI Overviews/ChatGPT/Perplexity). Detects business type (SaaS, e-commerce, local, publisher, agency) and delegates to the right specialists. Invoke everything through `/seo <subcommand>` — see the [`/seo` command table](#seo--comprehensive-seo-suite).

| Skill | Claude skill for… |
| --- | --- |
| **`seo`** | Orchestrator — routes `/seo <subcommand>` and runs full-audit delegation |
| **`seo-audit-full`** | Full-site audit with parallel subagent delegation (up to 500 pages) |
| **`seo-page`** | Deep single-page SEO analysis |
| **`seo-technical`** | Technical SEO audit across 9 categories (crawl, index, CWV, JS rendering) |
| **`seo-content`** | E-E-A-T and content-quality analysis with AI-citation readiness |
| **`seo-content-brief`** | Competitive SEO content briefs with per-section word counts |
| **`seo-schema`** | Schema.org detection, validation, and JSON-LD generation |
| **`seo-sitemap`** | XML sitemap analysis and generation |
| **`seo-images`** | Image SEO, image SERP, and file optimization (WebP/AVIF, IPTC) |
| **`seo-geo`** | GEO for AI Overviews, ChatGPT, and Perplexity |
| **`seo-plan`** | Strategic SEO planning with industry templates |
| **`seo-programmatic`** | Programmatic SEO at scale with thin-content safeguards |
| **`seo-competitor-pages`** | Comparison, "vs", and alternatives page generation |
| **`seo-local`** | Local SEO — GBP, NAP, citations, reviews, map pack |
| **`seo-maps`** | Maps intelligence — geo-grid rank tracking, GBP audit |
| **`seo-hreflang`** | Hreflang and international SEO audit/generation |
| **`seo-google`** | Google APIs — GSC, PageSpeed, CrUX, Indexing, GA4 |
| **`seo-backlinks`** | Backlink profile analysis (free: Moz/Bing/Common Crawl) |
| **`seo-cluster`** | SERP-based semantic topic clustering (hub-and-spoke) |
| **`seo-sxo`** | Search Experience Optimization — page-type mismatch detection |
| **`seo-drift`** | SEO drift monitoring — baseline, compare, history |
| **`seo-ecommerce`** | E-commerce SEO — product schema, marketplace intelligence |
| **`seo-dataforseo`** | Live SEO data via DataForSEO (extension) |
| **`seo-image-gen`** | AI image generation for SEO assets via Gemini (extension) |
| **`seo-flow`** | FLOW framework prompts (evidence-led: find/leverage/optimize/win) |

### Standalone SEO skill

Alongside the suite, [`seo-skills/`](seo-skills/) ships **`geo-seo-claude`** — a self-contained SEO/GEO/AEO optimizer (audit, schema generation, metadata validation, keyword/entity extraction, IndexNow) with its own bundled scripts and reference library.

### SEO extensions

**8 optional MCP extensions** under [`seo-skills/extensions/`](seo-skills/extensions/) add live data and AI-visibility coverage — each installed on demand via its own `install.sh`:

| Extension skill | Adds |
| --- | --- |
| **`seo-dataforseo`** | Live SERP, keyword, backlink, and AI-visibility data (DataForSEO MCP) |
| **`seo-image-gen`** | AI image generation via Gemini/nanobanana MCP |
| **`seo-firecrawl`** | Full-site crawling and site mapping (Firecrawl MCP) |
| **`seo-ahrefs`** | Referring domains, backlinks, and organic keywords (Ahrefs MCP) |
| **`seo-bing`** | Bing Webmaster Tools + IndexNow submission |
| **`seo-seranking`** | AI Share-of-Voice across ChatGPT, Gemini, Perplexity, AI Overviews, AI Mode |
| **`seo-profound`** | Time-series LLM citation tracking |
| **`seo-unlighthouse`** | Multi-page Lighthouse audits via the Unlighthouse CLI |

---

## Web design skills

Four skills for visual design, UI auditing, and site planning. Install via the standard Claude Code or CLI method — they live in `web-design/`.

| Skill | What it does | Example prompt |
| --- | --- | --- |
| **`frontend-design`** | Distinctive visual design direction, typography, palette, and aesthetic choices for new UI or redesigns. Rejects templated defaults. | `Give me frontend design direction for a devtools dashboard` |
| **`landing-page-auditor`** | Audits any landing or service page across 48 checks in 10 categories — LLM/AI discoverability, GEO readiness, content clarity, schema, internal linking, freshness, and technical hygiene. | `Audit the landing page at stripe.com/payments` |
| **`site-architecture`** | Plans page hierarchy, navigation, URL structure, and internal linking for a website or product. Use when figuring out what pages a site needs and how they connect. | `Plan the site architecture for a B2B SaaS docs portal` |
| **`web-design-guidelines`** | Reviews UI code against accessibility, UX, and web design best practices. | `Review my UI component for accessibility and UX issues` |

---

## Product management skills

Eight skills for PM workflows — strategy, PRDs, prioritization, backlog, and growth. Install via the standard Claude Code or CLI method — they live in `product-management-skills/`.

| Skill | What it does | Example prompt |
| --- | --- | --- |
| **`product-strategist`** | Strategic product leadership toolkit: OKR cascades, quarterly planning, competitive analysis, product vision documents, and team scaling proposals. | `Build a quarterly OKR cascade for our AI platform` |
| **`prd-development`** | Builds a structured, engineering-ready PRD from discovery notes — problem, users, solution, and success criteria. | `Write a PRD for our new API key management feature` |
| **`prioritization-advisor`** | Chooses the right prioritization framework (RICE, ICE, value/effort, etc.) based on product stage, team context, and decision type. | `Help me pick a prioritization framework for our early-stage product` |
| **`agile-product-owner`** | Agile backlog management: user stories, acceptance criteria, sprint planning, velocity tracking, and epic breakdown. | `Write user stories for our onboarding flow` |
| **`user-story-mapping`** | Creates a user story map — activities, steps, tasks, and release slices organized around the user journey. | `Map the user story for our checkout flow` |
| **`organic-growth-advisor`** | Diagnoses which organic growth path fits the current constraint: new segments, geographies, channels, or products. Uses a 2×2 framework. | `We've plateaued in our core market — what's the next growth move?` |
| **`product-manager-toolkit`** | Comprehensive PM toolkit: RICE scoring, customer interview analysis, PRD templates, discovery frameworks, and go-to-market strategy. | `Help me run a RICE prioritization session` |
| **`pm-skill-creator`** | Designs a new PM skill through guided conversation — from raw idea to a structured, repo-compliant `SKILL.md` draft. | `Help me create a skill for competitive positioning` |

---

## Commands

If you've installed the command pack, every skill is also a slash subcommand. The SEO, GEO, and docs skills run under `/dev-gtm`; the full-funnel marketing skills run under `/marketing`; the comprehensive SEO suite runs under `/seo`; the blog content engine runs under `/blog`; the web design skills run under `/web-design`; and the product management skills run under `/pm`.

<p align="center">
  <img src="./assets/claude-commands.png" alt="Claude Commands" width="400"/>
</p>

### `/dev-gtm` — SEO, GEO & docs

| Command | Description |
| --- | --- |
| `/dev-gtm docs-audit <url>` | Run the full 33-check developer docs audit and return a scored report. |
| `/dev-gtm sdk-audit <url>` | Audit SDK documentation across 6 sections; scored, downloadable HTML report. |
| `/dev-gtm api-audit <url>` | Crawl every endpoint page and score each across 5 quality checks. |
| `/dev-gtm blog-count <company or domain>` | Count unique blog posts for one company, or compare a target vs competitors. |
| `/dev-gtm brief-outline <keyword or title>` | Generate an SEO content outline and export it as a formatted `.docx`. |
| `/dev-gtm growth-report <domain> [competitors...]` | 3-month SEO performance report with traffic, keywords, and competitive positioning. |
| `/dev-gtm llms-check <domain>` | Audit AI-readiness: probe `robots.txt`, `llms.txt`, `llms-full.txt`; scored report. |
| `/dev-gtm orphan-pages <domain>` | Discover pages with zero incoming internal links; 3 linking suggestions per orphan. |
| `/dev-gtm dead-end-pages <domain>` | Find pages with zero outgoing internal links; 3 outgoing link suggestions per page. |
| `/dev-gtm prospect <domain or ICP>` | Build an exact-fit developer-marketing prospect list with signals and pain points. |

### `/marketing` — full-funnel growth

| Command | Description |
| --- | --- |
| `/marketing seo-audit <domain or url>` | Diagnose technical & on-page SEO issues. |
| `/marketing ai-seo <url or topic>` | Optimize for AI search engines & LLM citations. |
| `/marketing schema <url or page type>` | Add or fix structured data markup. |
| `/marketing programmatic-seo <keyword pattern>` | Build SEO pages at scale from templates. |
| `/marketing content-strategy <product or niche>` | Plan what content to create. |
| `/marketing copywriting <page or url>` | Write or improve marketing copy. |
| `/marketing social <platform or topic>` | Create & schedule social content. |
| `/marketing lead-magnets <topic or audience>` | Plan a lead magnet. |
| `/marketing free-tools <product or idea>` | Plan a free marketing tool. |
| `/marketing ads <product or goal>` | Paid campaign strategy & targeting. |
| `/marketing ad-creative <product or offer>` | Generate ad copy variations at scale. |
| `/marketing ab-testing <what to test>` | Design an A/B test or experiment. |
| `/marketing cro <page url>` | Improve conversion rate. |
| `/marketing launch <product or feature>` | Plan a product/feature launch. |
| `/marketing marketing-ideas <product>` | Brainstorm growth ideas. |
| `/marketing referrals <product>` | Design a referral/affiliate program. |
| `/marketing community-marketing <product or goal>` | Plan community-led growth. |
| `/marketing emails <sequence type>` | Build a lifecycle/drip email flow. |
| `/marketing cold-email <target or offer>` | Write cold outreach sequences. |
| `/marketing onboarding <product>` | Optimize post-signup activation. |
| `/marketing churn-prevention <context>` | Reduce churn & build retention flows. |
| `/marketing customer-research <source or topic>` | Conduct or analyze customer research. |
| `/marketing competitor-profiling <competitor URLs>` | Produce structured competitor profiles. |
| `/marketing competitors <you vs competitor>` | Create comparison/alternative pages. |
| `/marketing analytics <what to track>` | Set up or audit measurement. |
| `/marketing pricing <product or context>` | Pricing & packaging strategy. |
| `/marketing revops <context>` | Lead lifecycle & marketing-to-sales handoff. |
| `/marketing sales-enablement <asset type>` | Create sales collateral. |

### `/blog` — blog content engine

Single entry point for all 30 writing skills. Requires the [Blog skills runtime](#blog-skills-runtime-agents--scripts) step.

| Command | Description |
| --- | --- |
| `/blog write <topic>` | Write a new post from scratch (research → write → SEO → review). |
| `/blog rewrite <file>` | Rewrite/optimize an existing post. |
| `/blog update <file>` | Update an existing post with fresh statistics (routes to rewrite). |
| `/blog analyze <file-or-url>` | Audit quality with a 0–100 score. |
| `/blog brief <topic>` | Generate a detailed content brief. |
| `/blog outline <topic>` | SERP-informed content outline. |
| `/blog strategy <niche>` | Blog strategy and topic ideation. |
| `/blog calendar [monthly\|quarterly]` | Generate an editorial calendar. |
| `/blog cluster [plan\|execute] <seed>` | Semantic topic-cluster planning + execution. |
| `/blog seo-check <file>` | Post-writing SEO validation checklist. |
| `/blog schema <file>` | Generate JSON-LD schema markup. |
| `/blog geo <file>` | AI-citation readiness audit. |
| `/blog audit [directory]` | Full-site blog health assessment. |
| `/blog factcheck <file>` | Verify statistics against cited sources. |
| `/blog cannibalization [dir]` | Detect keyword cannibalization across posts. |
| `/blog repurpose <file>` | Repurpose content for other platforms. |
| `/blog persona [create\|list\|use\|show]` | Manage writing personas and voice profiles. |
| `/blog brand [init\|show\|update]` | Generate BRAND.md + VOICE.md context files. |
| `/blog discourse <topic>` | Research what people said in the last 30 days. |
| `/blog taxonomy [suggest\|sync\|audit]` | Tag/category management across CMS platforms. |
| `/blog image [generate\|edit\|setup]` | AI image generation via Gemini. |
| `/blog audio [generate\|voices\|setup]` | Generate audio narration of a post. |
| `/blog notebooklm <question>` | Query NotebookLM for source-grounded research. |
| `/blog google [command] [args]` | Google API data: PSI, CrUX, GSC, GA4, NLP, YouTube. |
| `/blog flow [find\|optimize\|win\|prompts\|sync]` | FLOW framework prompts. |
| `/blog multilingual <topic> --languages <codes>` | Write + translate + localize + hreflang. |
| `/blog translate <file> --to <codes>` | SEO-optimized translation. |
| `/blog localize <file> --locale <code>` | Cultural deep-adaptation. |
| `/blog locale-audit <directory>` | Multilingual content QA. |

### `/seo` — comprehensive SEO suite

Single entry point for the SEO suite. The `seo` orchestrator detects business type and delegates to specialist subagents in parallel for full audits.

| Command | Description |
| --- | --- |
| `/seo audit <url>` | Full website audit with parallel subagent delegation. |
| `/seo page <url>` | Deep single-page SEO analysis. |
| `/seo technical <url>` | Technical SEO audit (9 categories). |
| `/seo content <url>` | E-E-A-T and content-quality analysis. |
| `/seo content-brief <topic or url>` | Generate a competitive SEO content brief. |
| `/seo schema <url>` | Detect, validate, and generate Schema.org markup. |
| `/seo sitemap <url or generate>` | Analyze or generate XML sitemaps. |
| `/seo images <url or optimize>` | Image SEO audit, SERP analysis, file optimization. |
| `/seo geo <url>` | AI Overviews / Generative Engine Optimization. |
| `/seo plan <business-type>` | Strategic SEO planning. |
| `/seo programmatic [url\|plan]` | Programmatic SEO analysis and planning. |
| `/seo competitor-pages [url\|generate]` | Competitor comparison page generation. |
| `/seo local <url>` | Local SEO (GBP, citations, reviews, map pack). |
| `/seo maps [command] [args]` | Maps intelligence (geo-grid, GBP audit, reviews). |
| `/seo hreflang [url]` | Hreflang / i18n SEO audit and generation. |
| `/seo google [command] [url]` | Google SEO APIs (GSC, PageSpeed, CrUX, Indexing, GA4). |
| `/seo backlinks <url>` | Backlink profile analysis (free + DataForSEO). |
| `/seo cluster <seed-keyword>` | SERP-based semantic clustering and content architecture. |
| `/seo sxo <url>` | Search Experience Optimization — page-type and persona scoring. |
| `/seo drift [baseline\|compare\|history] <url>` | Capture and track SEO changes over time. |
| `/seo ecommerce <url>` | E-commerce SEO (product schema, marketplace intelligence). |
| `/seo flow [stage] [url\|topic]` | FLOW framework prompts (find/leverage/optimize/win/local). |
| `/seo dataforseo [command]` | Live SEO data via DataForSEO (extension). |
| `/seo image-gen [use-case] <description>` | AI image generation for SEO assets (extension). |
| `/seo firecrawl [command] <url>` | Full-site crawling and site mapping (extension). |

---

### `/web-design` — design & UI

| Command | Description |
| --- | --- |
| `/web-design frontend-design <brief or url>` | Get distinctive visual design direction, typography, and aesthetic guidance. |
| `/web-design landing-page-auditor <url>` | Audit a page across 48 checks — LLM/AI discoverability, GEO readiness, content clarity, schema, and technical crawlability. Produces a scored HTML report. |
| `/web-design site-architecture <domain or goal>` | Plan page hierarchy, navigation, URL structure, and internal linking. |
| `/web-design web-design-guidelines <file or pattern>` | Audit UI code for accessibility, UX, and web design best practices. |

---

### `/pm` — product management

| Command | Description |
| --- | --- |
| `/pm strategy <product or context>` | Drive vision, OKR cascades, quarterly planning, roadmaps, and team scaling. |
| `/pm prd <feature or notes>` | Build a structured, engineering-ready PRD from discovery notes. |
| `/pm prioritize <context>` | Choose the right prioritization framework (RICE, ICE, value/effort, etc.). |
| `/pm backlog <story or sprint context>` | Write user stories, define acceptance criteria, plan sprints, and track velocity. |
| `/pm story-map <product or journey>` | Build a user story map (activities, steps, tasks, release slices). |
| `/pm growth <growth constraint>` | Diagnose which organic growth path to pursue next. |
| `/pm toolkit <PM task>` | RICE prioritization, customer interview analysis, PRD templates, discovery frameworks, and GTM strategy. |
| `/pm create-skill <idea or content>` | Design a new PM skill through guided conversation. |

---

## Who it's for

These skills are built for technical teams who care about being discoverable by AI, not just by Google:

- **DevTool & infrastructure startups** measuring whether their docs are LLM-citable
- **AI-agent and LLM platforms** that need their API/SDK docs parsed correctly by agents
- **Developer marketing & DevRel teams** running SEO + GEO audits without a dedicated SEO hire
- **Technical content teams** producing briefs and benchmarking content against competitors
- **Founders** who want a fast, honest read on their AI visibility before investing in it

---

## Requirements

- Claude Code, Claude Desktop, or Claude.ai
- Python 3.10+
- Node.js with `npx` (to run the DataForSEO MCP server locally)
- A DataForSEO API account — only for the live-search skills: `growth-report`, `blog-post-counter`, `api-docs-quality-report`

---

## Sample outputs

| Docs Auditor | Growth Report |
| --- | --- |
| ![Docs Auditor running in Claude Code](./assets/docs-auditor-gif-cc.gif) | ![Growth Report running in Claude Code](./assets//growth-report-cc.gif) |

---

## Repository structure

```
dev-gtm-claude-skills/
├── assets/                          # Logos, images, and GIFs for this README
├── skills/
│   ├── docs-auditor/
│   │   ├── SKILL.md                 # Agent instructions (Claude reads this)
│   │   ├── README.md                # Human-facing usage docs
│   │   └── references/              # Scoring guide, widget template, fetch strategy
│   ├── sdk-docs-auditor/
│   ├── api-docs-quality-report/
│   ├── growth-report/
│   ├── blog-post-counter/
│   ├── brief-outline-generator/
│   ├── llms-txt-checker/
│   ├── orphan-pages-internal-linking-opportunities/
│   ├── no-outlinks-audit/
│   └── dev-marketing-prospector/
├── marketing-skills/                # 28 full-funnel developer-marketing skills
│   ├── seo-audit/
│   ├── content-strategy/
│   ├── cro/
│   ├── emails/
│   └── …                            # ad-creative, ads, pricing, launch, and more
├── writing-skills/                  # 30 blog/content-engine sub-skills (/blog) + 4 standalone
│   ├── blog/                        # orchestrator
│   ├── blog-write/
│   ├── blog-analyze/
│   ├── ogilvy-copywriting/          # standalone: sales-driven copy
│   ├── social-media-posts/          # standalone: per-platform social posts
│   ├── reddit-comments/             # standalone: on-brand Reddit replies
│   ├── stop-slop/                   # standalone: strip AI writing tells
│   └── …                            # rewrite, brief, schema, translate, and more
├── seo-skills/                      # 25 SEO sub-skills (/seo) + geo-seo-claude + 8 extensions
│   ├── seo/                         # orchestrator
│   ├── seo-audit/                   # full-site audit (installs as seo-audit-full)
│   ├── seo-technical/
│   ├── seo-geo/
│   ├── geo-seo-claude/              # standalone SEO/GEO/AEO optimizer (own scripts)
│   ├── extensions/                  # 8 optional MCP extensions (dataforseo, firecrawl, …)
│   └── …                            # schema, local, maps, backlinks, cluster, and more
├── agents/                          # blog + 18 SEO specialist subagents (Task subagents)
├── data/                            # shared data (e.g., google-updates.json)
├── scripts/                         # shared blog + SEO scripts + multi-tool installers
└── README.md
```

---

## FAQ

**Are these Claude skills free?**
Yes, every skill is free and MIT-licensed. No license fees, no paywalls.

**Do I need Claude Code?**
No. Skills run in Claude Code, Claude Desktop, or Claude.ai. Desktop and web use the ZIP upload method above.

**Which skills need API keys?**
Most need none. Only the live-search skills (`growth-report`, `blog-post-counter`, `api-docs-quality-report`) use DataForSEO, and the internal-linking skills (`orphan-pages…`, `no-outlinks-audit`) use Ahrefs.

**How is this different from a standard SEO audit tool?**
Traditional tools optimize for Google crawlers. These skills are built for developer documentation and AI discoverability. They check whether your docs can be parsed, cited, and recommended by LLMs.

**How often do new skills ship?**
Regularly. Star or watch the repo to get notified.

---

## Contributing

To add a skill, create a folder under `skills/`:

```
skills/your-skill-name/
├── SKILL.md          # Required: agent instructions
├── README.md         # Required: human-facing docs
├── requirements.txt  # If the skill has Python dependencies
└── references/       # Templates, scoring guides, or other reference files
```

`SKILL.md` must include a frontmatter block:

```yaml
---
name: your-skill-name
description: >
  One paragraph describing exactly when Claude should activate this skill.
  Write it to match the natural language a user would use.
---
```

The `description` field is what Claude uses to decide when to activate the skill — be specific about trigger phrases and input formats. Open a PR with your skill folder and a one-line summary.

---

## License

MIT — see [LICENSE](LICENSE).

## Built by Infrasity

Infrasity is a developer-marketing agency for DevTools, AI-agent platforms, and B2B SaaS. We help technical products get found, parsed, and cited by AI systems.

🌐 [infrasity.com](https://www.infrasity.com) · 🔗 [LinkedIn](https://www.linkedin.com/company/infrasity/) · 📸 [Instagram](https://www.instagram.com/infrasity/)

**Want a GEO audit of your own docs?** → [infrasity.com/claude-skills](https://www.infrasity.com/claude-skills)
