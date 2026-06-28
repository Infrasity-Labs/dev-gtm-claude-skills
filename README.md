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
- [Notion skills](#notion-skills)
- [Coding skills](#coding-skills)
- [Job search skills](#job-search-skills)
- [Product designer skills](#product-designer-skills)
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

Each script discovers all skills under `skills/`, `marketing-skills/`, `writing-skills/`, `notion-skills/`, and `seo-skills/` and installs them in the format that tool expects.

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

### Clay connector (for prospect enrichment and cold-email)

`dev-marketing-prospector` and `cold-email` use Clay's data enrichment tools to look up company funding, headcount, tech stack, and verified contact information — replacing manual research across Crunchbase, LinkedIn, and Apollo.

**Claude.ai / Claude Desktop** — Settings → Customize → Connectors → Connect Clay. Sign in with your Clay account. Once connected, the `find-and-enrich-company`, `ask-question-about-accounts`, and `find-and-enrich-contacts-at-company` tools become available automatically.

**Claude Code** — add to `.claude/settings.json` or `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "clay": {
      "command": "npx",
      "args": ["-y", "@clay-hq/mcp-server"],
      "env": {
        "CLAY_API_KEY": "your_clay_api_key"
      }
    }
  }
}
```

Get your API key at [clay.com](https://clay.com). Both skills degrade gracefully when Clay is not connected — `dev-marketing-prospector` falls back to manual web search across all source categories, and `cold-email` prompts the user for research signals instead.

### Notion connector (for saving outputs to your workspace)

`competitor-profiling`, `customer-research`, and `content-brief` save their outputs to Notion as structured databases — competitor profiles become queryable competitive intelligence records, VOC research becomes a searchable quote bank, and content briefs sync to a living Notion database your whole team can filter and reference.

**Claude.ai / Claude Desktop** — Settings → Customize → Connectors → Connect Notion. Sign in with your Notion account and grant access to the workspaces you want skills to write to. Once connected, the `notion-search`, `notion-create-database`, `notion-create-pages`, and `notion-update-page` tools become available automatically.

**Claude Code** — add to `.claude/settings.json` or `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@notionhq/notion-mcp-server"],
      "env": {
        "NOTION_API_KEY": "your_notion_integration_secret"
      }
    }
  }
}
```

Get your integration secret at [notion.so/my-integrations](https://www.notion.so/my-integrations). All skills degrade gracefully when Notion is not connected — outputs are returned in chat or saved locally, and each skill appends a 💡 note with setup instructions.

### Apify connector (for web scraping — reviews, Reddit, Google Maps)

`reddit-comments`, `competitor-profiling`, `customer-research`, `seo-maps`, and `programmatic-seo` use Apify actors to scrape data that WebFetch and Firecrawl can't reliably reach — Reddit threads blocked by rate limits, G2/Capterra/Trustpilot review pages with anti-bot protection, and live Google Maps business listings.

> **Note:** Apify is an **official Anthropic connector** and is available on **Claude Desktop only**. It cannot be configured as a Claude Code MCP server.

**Claude Desktop** — Settings → Customize → Connectors → Connect Apify. Sign in with your Apify account. Once connected, the following actors are available across skills:

| Actor | Used by |
|---|---|
| `apify/reddit-scraper` | `reddit-comments`, `customer-research` |
| `apify/g2-scraper`, `apify/capterra-scraper`, `apify/trustpilot-scraper` | `competitor-profiling`, `customer-research` |
| `apify/google-maps-scraper`, `apify/google-maps-reviews-scraper`, `apify/yelp-scraper` | `seo-maps` |
| `apify/youtube-scraper`, `apify/amazon-reviews-scraper` | `customer-research` |
| `apify/google-maps-scraper`, `apify/g2-scraper`, `apify/capterra-scraper` | `programmatic-seo` |

All skills degrade gracefully when Apify is not connected — each falls back to WebFetch or Firecrawl and appends a 💡 note explaining what Apify would unlock.

### Klaviyo connector (for email template and campaign sync)

`emails`, `churn-prevention`, `lead-magnets`, and `onboarding` use Klaviyo's MCP tools to read your existing email setup and push new templates directly into your account — auditing existing flows, creating HTML and drag-and-drop templates, building campaigns, and pulling open/click/revenue metrics per flow step.

> **Note:** The Klaviyo MCP can create templates and campaigns but **cannot create automated flows**. After the skill builds your templates, configure trigger conditions, delays, and branching logic in the Klaviyo UI.

**Claude.ai / Claude Desktop** — Settings → Customize → Connectors → Connect Klaviyo. Sign in with your Klaviyo account. Once connected, tools like `list_email_templates`, `create_email_template`, `get_flows`, `create_campaign`, and `query_metric_aggregates` become available automatically.

**Claude Code** — add to `.claude/settings.json` or `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "klaviyo": {
      "command": "npx",
      "args": ["-y", "@klaviyo/mcp-server"],
      "env": {
        "KLAVIYO_API_KEY": "your_klaviyo_private_api_key"
      }
    }
  }
}
```

Get your private API key at [klaviyo.com/account#api-keys-tab](https://www.klaviyo.com/account#api-keys-tab). All skills degrade gracefully when Klaviyo is not connected — they output email copy and sequence structure in chat, which you can manually import into any ESP.

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

## Notion skills

Seven personal-productivity and workflow skills under [`notion-skills/`](notion-skills/) — brain dumps, email triage, meeting notes, SEO content briefs, CLAUDE.md generation, mid-conversation reassessment, and multi-agent workflow scripting. Install via the standard Claude Code or CLI method.

| Skill | What it does | Example prompt |
| --- | --- | --- |
| **`capture`** | Transforms any chaotic brain dump into a clean four-section actionable system (Projects/Ideas, Tasks, Connections, Next Steps). Zero information loss, no upfront intake. | `brain dump: we need to redesign onboarding, fix the pricing page, interview 5 customers this week…` |
| **`inbox`** | Full email triage system — builds a personalized taxonomy KB on first run, then classifies, researches senders, and drafts replies (never sends). | `triage my inbox` |
| **`reflect`** | Pauses execution mid-conversation and reassesses direction, assumptions, and bias across 5 dimensions. Ends with a concrete continue/pivot/pause recommendation. | `step back — are we overthinking this?` |
| **`workflow-builder`** | Designs and writes deterministic multi-agent workflow scripts (`.js`) for Claude Code's Workflow tool — fan-out, pipeline, loop, and judge-panel topologies. | `Build a workflow that researches 10 companies and writes a cold email for each` |
| **`content-brief`** | Generates a fully structured SEO content brief for a target keyword and optionally pushes it to a Notion database. | `Create a content brief for "developer onboarding best practices"` |
| **`claude-md-starter`** | Scans the repo, infers tech stack and conventions, asks at most 3 questions, and writes a populated CLAUDE.md from scratch. | `Generate a CLAUDE.md for this repo` |
| **`meeting-notes`** | Structured meeting summaries with action items, decisions, and key discussion points. | `Summarize these meeting notes: [paste]` |

---

## Coding skills

Seven skills for software engineering workflows — code review, architecture, TDD, and LLM coding best practices. Install via the standard Claude Code method — they live in `coding-skills/`.

| Skill | What it does |
| --- | --- |
| **`code-reviewer`** | Automated code review for 13 languages — analyzes PRs for complexity and risk, detects code smells and SOLID violations, generates structured review reports. |
| **`pr-review-expert`** | Expert-level pull request review focused on security, correctness, and code quality across any diff or branch. |
| **`karpathy-guidelines`** | Behavioral guidelines derived from Andrej Karpathy's observations on LLM coding pitfalls — reduces overcomplication, surfaces assumptions, and enforces verifiable success criteria. |
| **`senior-architect`** | Architecture design and analysis toolkit — system design, microservices vs monolith evaluation, dependency analysis, ADRs, and Mermaid/PlantUML/ASCII diagrams. |
| **`brainstorming`** | Collaborative dialogue skill for exploring user intent, requirements, and design before any implementation work begins. Use before creating features or building components. |
| **`test-driven-development`** | TDD workflow — write the test first, watch it fail, write minimal code to pass. Applies to any feature or bugfix. |
| **`using-superpowers`** | Session-start skill that establishes how to find and invoke available skills before responding to any task. |

---

## Job search skills

Twenty-seven skills covering the full job search lifecycle — from finding roles and tailoring resumes to writing cover letters, prepping for interviews, and negotiating offers. Install via the standard Claude Code method — they live in `job-search/`.

### Search & Applications

| Skill | What it does |
| --- | --- |
| **`job-search`** | Automated job search using browser automation — finds roles matching your resume and preferences across job boards. |
| **`apply`** | Fills out job applications on Greenhouse, Lever, and Workday end-to-end using browser automation. |
| **`application-form-filler`** | Fills individual application form fields with context-aware, tailored answers drawn from your CV and the job description. |
| **`network-scan`** | Scans your LinkedIn contacts' companies for matching job openings — parallelized with caching for fast weekly reruns. |
| **`job-description-analyzer`** | Analyzes job postings, calculates a match score, identifies skill gaps, and builds an application strategy. |

### Resume Building

| Skill | What it does |
| --- | --- |
| **`tailor-resume`** | Full resume tailoring workflow with a profile interview step — fetches the job posting, tailors every section, critiques for AI writing patterns. |
| **`resume-tailor`** | Customize a resume for a specific role while maintaining truthfulness — reorders, reframes, and adds keywords from the job description. |
| **`resume-ats-optimizer`** | Optimizes resumes for Applicant Tracking Systems and analyzes keyword match against a job posting. |
| **`resume-bullet-writer`** | Transforms weak resume bullets into achievement-focused statements with metrics and measurable impact. |
| **`resume-formatter`** | Ensures ATS-friendly formatting and produces a clean, scannable resume layout. |
| **`resume-quantifier`** | Finds opportunities to add metrics and estimates reasonable numbers when exact data is unavailable. |
| **`resume-section-builder`** | Creates targeted resume sections optimized for different experience levels, roles, and industries. |
| **`resume-version-manager`** | Tracks multiple tailored resume versions against a master resume and logs which version went where. |
| **`tech-resume-optimizer`** | Optimizes resumes specifically for software engineering, product management, and other technical roles. |
| **`academic-cv-builder`** | Formats CVs for academic positions — publications, grants, teaching experience, and conference sections. |
| **`executive-resume-writer`** | Creates C-suite and VP-level resumes emphasizing strategic leadership, P&L ownership, and board interaction. |
| **`creative-portfolio-resume`** | Balances visual design with ATS compatibility for creative, design, and marketing roles. |

### Cover Letters & Outreach

| Skill | What it does |
| --- | --- |
| **`cover-letter`** | Full cover letter workflow — fetches the job posting, writes a tailored 250–350 word letter grounded in your resume. |
| **`cover-letter-generator`** | Generates a personalized, compelling cover letter directly from a pasted resume and job description. |
| **`cold-email-writer`** | Writes personalized cold outreach emails to hiring managers and founders — specific, human, and not a pitch deck. |

### Research & Prep

| Skill | What it does |
| --- | --- |
| **`interview-prep-generator`** | Generates STAR stories, role-specific practice questions, and talking points from your resume. |
| **`offer-comparison-analyzer`** | Compares multiple job offers side-by-side with total compensation analysis (base, equity, bonus, benefits). |
| **`salary-negotiation-prep`** | Researches market rates, builds a negotiation strategy, and writes counter-offer scripts. |

### Profile & Portfolio

| Skill | What it does |
| --- | --- |
| **`linkedin-profile-optimizer`** | Optimizes your LinkedIn profile for recruiter searchability, keyword density, and engagement signals. |
| **`portfolio-case-study-writer`** | Transforms resume bullets into detailed, narrative portfolio case studies. |
| **`career-changer-translator`** | Translates skills and experience from one industry to another, surfacing transferable skills and reframing language. |
| **`reference-list-builder`** | Formats professional references correctly and prepares reference sheets and briefing materials. |

---

## Product designer skills

Ninety-nine skills covering the full product design and UX practice — from early research and strategy through design systems, interface craft, critiques, accessibility, and handoff. Install via the standard Claude Code method — they live in `product-designers/`.

### Research & Discovery

| Skill | What it does |
| --- | --- |
| **`user-persona`** | Creates refined user personas from research data with demographics, goals, frustrations, and behavioral patterns. |
| **`empathy-map`** | Builds a 4-quadrant empathy map (Says, Thinks, Does, Feels) to synthesize user research into actionable insights. |
| **`interview-script`** | Creates structured user interview scripts with warm-up, core exploration, and wrap-up sections. |
| **`journey-map`** | Creates end-to-end user journey maps with stages, touchpoints, emotions, pain points, and opportunity areas. |
| **`affinity-diagram`** | Organizes qualitative research data into themes, clusters, and insight statements. |
| **`user-flow-diagram`** | Creates user flow diagrams showing paths, decisions, and branch logic. |
| **`experience-map`** | Maps the full ecosystem of user touchpoints, channels, and relationships across a service. |
| **`diary-study-plan`** | Designs diary studies with prompts, duration, participant criteria, and an analysis framework. |
| **`card-sort-analysis`** | Analyzes card sorting results to inform information architecture and navigation structure. |
| **`survey-design`** | Designs surveys that collect reliable, unbiased quantitative data to validate hypotheses. |
| **`summarize-interview`** | Summarizes a user interview transcript into structured insights with key themes, quotes, and action items. |
| **`research-repository`** | Builds and maintains a research repository that makes findings findable and reusable across teams. |

### Strategy & Planning

| Skill | What it does |
| --- | --- |
| **`design-brief`** | Writes a comprehensive design brief defining problem space, constraints, audience, and success criteria. |
| **`design-principles`** | Defines actionable design principles that guide decision-making and resolve trade-offs. |
| **`jobs-to-be-done`** | Maps user Jobs-to-Be-Done with functional, emotional, and social dimensions plus outcome expectations. |
| **`north-star-vision`** | Articulates a compelling north-star product vision that aligns teams and inspires strategic design decisions. |
| **`opportunity-framework`** | Identifies, evaluates, and prioritizes design opportunities using impact-effort frameworks. |
| **`business-design`** | Toolkit for thinking and communicating as a designer in a business context — financials, competitive landscapes, defending decisions in the language of value. |
| **`competitive-analysis`** | Structured competitive analysis comparing UX patterns, features, strengths, and gaps across rival products. |
| **`metrics-definition`** | Defines UX metrics and KPIs that connect design decisions to measurable business and user outcomes. |
| **`design-impact-reporting`** | Communicates design's contribution to business and user outcomes in stakeholder-friendly terms. |
| **`content-strategy`** | Defines what content a product needs, how it should be structured, and who owns it. |
| **`stakeholder-alignment`** | Creates responsibility matrices, decision frameworks, and communication plans to align stakeholders. |

### UX Laws & Frameworks

| Skill | What it does |
| --- | --- |
| **`fitts-law`** | Applies Fitts's Law to size and position interactive targets for fast, accurate interaction. |
| **`hicks-law`** | Applies Hick's Law to reduce decision time by limiting the number of simultaneous choices presented. |
| **`millers-law`** | Applies Miller's Law — chunks information into groups of ~4 to fit working memory limits. |
| **`doherty-threshold`** | Applies the Doherty Threshold — keeps system response times under 400ms to maintain user flow. |
| **`aesthetic-usability`** | Applies the Aesthetic-Usability Effect — visually polished interfaces are perceived as more usable. |
| **`law-of-proximity`** | Applies the Law of Proximity to group related elements through spatial relationships. |
| **`law-of-common-region`** | Applies the Law of Common Region to group elements using containers, backgrounds, and boundaries. |
| **`von-restorff-effect`** | Applies the Von Restorff Effect to make the most important element distinctly different from its surroundings. |

### Design System

| Skill | What it does |
| --- | --- |
| **`color-system`** | Builds a comprehensive color system with palette generation, semantic mapping, and accessibility compliance. |
| **`typography-scale`** | Creates a modular typography scale with size, weight, and line-height relationships. |
| **`spacing-system`** | Creates a consistent spacing system based on a base unit with contextual application rules. |
| **`layout-grid`** | Defines responsive layout grid systems with columns, gutters, margins, and breakpoint behavior. |
| **`design-token`** | Defines and organizes design tokens (color, spacing, typography, elevation) with naming conventions and usage guidance. |
| **`design-token-audit`** | Audits design token usage across a product for consistency and coverage. |
| **`naming-convention`** | Establishes naming convention systems for design elements, components, and tokens. |
| **`icon-system`** | Creates an icon system specification covering grid, sizing, naming, categories, and implementation guidance. |
| **`illustration-style`** | Defines an illustration style guide with visual language, color usage, and application rules. |
| **`motion-system`** | Defines a motion system with duration tokens, easing vocabulary, and reduced-motion handling. |
| **`pattern-library`** | Structures pattern library entries with problem context, solution pattern, usage examples, and related patterns. |
| **`theming-system`** | Designs theming architecture supporting brand variants, dark mode, and high-contrast modes. |
| **`dark-mode-design`** | Designs effective dark mode interfaces with proper color adaptation, contrast, and elevation. |
| **`readable-measure`** | Sets optimal line lengths for readability across typography scales and responsive layouts. |

### Interface Design

| Skill | What it does |
| --- | --- |
| **`interface-design`** | Craft-first interface design for dashboards, admin panels, SaaS apps, tools, and settings pages — the difference between designed and generated. |
| **`interfaces-that-feel`** | Applies an emotional resonance lens to technically correct but flat UIs — prescribes specific changes at the copy, motion, and interaction layer. |
| **`information-architecture`** | Designs the structure, hierarchy, and navigation model for a product's content and features. |
| **`navigation-patterns`** | Selects and designs navigation patterns matching product structure, user tasks, and platform conventions. |
| **`visual-hierarchy`** | Establishes clear visual hierarchy through size, weight, color, spacing, and positioning. |
| **`responsive-design`** | Designs adaptive layouts and interactions that work across all screen sizes and input methods. |
| **`form-design`** | Designs forms that minimize friction, prevent errors, and guide users to successful completion. |
| **`loading-states`** | Designs loading, skeleton, and progressive content reveal patterns. |
| **`error-handling-ux`** | Designs error prevention, detection, and recovery experiences. |
| **`onboarding-design`** | Designs first-run experiences that get users to value quickly without overwhelming them. |
| **`search-ux`** | Designs search experiences that help users find what they need, recover from failure, and refine results. |
| **`feedback-patterns`** | Designs system feedback for user actions including confirmations, status updates, and notifications. |
| **`data-visualization`** | Designs clear, accessible data visualizations with appropriate chart selection and styling. |
| **`animation-principles`** | Applies animation principles to UI motion for purposeful, polished interactions. |
| **`gesture-patterns`** | Designs gesture-based interactions for touch and pointer devices. |
| **`micro-interaction-spec`** | Specifies micro-interactions with trigger, rules, feedback, and loop/mode definitions. |
| **`state-machine`** | Models complex UI behavior as finite state machines with states, events, and transitions. |
| **`localization-design`** | Designs interfaces that adapt gracefully to multiple languages, writing directions, and cultural contexts. |

### Critique

| Skill | What it does |
| --- | --- |
| **`critique-affordance`** | Critiques a screen's interactive affordances — what looks clickable, state visibility, CTA clarity. |
| **`critique-brand-consistency`** | Critiques brand consistency against mood, voice, and token definitions. |
| **`critique-color`** | Critiques colour usage — contrast ratios, palette coherence, semantic meaning, and colour accessibility. |
| **`critique-composition`** | Critiques composition — balance, whitespace, rhythm, and gestalt principles. |
| **`critique-information-density`** | Critiques information density — cognitive load, content prioritisation, and progressive disclosure. |
| **`critique-typography`** | Critiques typography — scale usage, readability, consistency, and token compliance. |
| **`critique-visual-hierarchy`** | Critiques visual hierarchy — entry point, eye flow, weight distribution, and emphasis. |

### Testing & Evaluation

| Skill | What it does |
| --- | --- |
| **`accessibility-audit`** | Comprehensive accessibility audit against WCAG guidelines with severity ratings and remediation steps. |
| **`accessibility-test-plan`** | Creates accessibility testing plans covering assistive technologies and WCAG criteria. |
| **`a-b-test-design`** | Designs rigorous A/B tests with hypotheses, variants, metrics, and sample size calculations. |
| **`heuristic-evaluation`** | Conducts expert heuristic evaluations using Nielsen's heuristics and domain-specific criteria. |
| **`usability-test-plan`** | Designs usability test plans with tasks, success metrics, participant criteria, and a facilitation guide. |
| **`click-test-plan`** | Designs click/first-click tests to evaluate navigation and information findability. |
| **`test-scenario`** | Generates structured usability test scenarios with realistic tasks, success criteria, and facilitation notes. |
| **`design-qa-checklist`** | Creates QA checklists for verifying design implementation accuracy. |
| **`design-debt-audit`** | Identifies, categorizes, and prioritizes accumulated design inconsistencies and structural problems. |
| **`prototype-strategy`** | Chooses the right prototyping fidelity and method for the design question at hand. |

### Documentation & Handoff

| Skill | What it does |
| --- | --- |
| **`component-spec`** | Writes detailed component specifications including props, states, variants, accessibility requirements, and usage guidelines. |
| **`handoff-spec`** | Creates developer handoff specifications with measurements, behaviors, assets, and edge cases. |
| **`design-rationale`** | Writes clear design rationale connecting decisions to user needs, business goals, and principles. |
| **`design-review-process`** | Establishes design review gates with criteria, checklists, and approval workflows. |
| **`design-critique`** | Facilitates structured design critiques with clear feedback frameworks and actionable outcomes. |
| **`documentation-template`** | Generates structured documentation templates for components, patterns, or guidelines within a design system. |
| **`wireframe-spec`** | Specifies wireframe layouts with content priority, component placement, and annotation. |
| **`anydesign`** | Analyzes any visual source — website, screenshot, Figma file, or image — to extract its design system, tokens, and components into a `design.md`. |
| **`case-study`** | Crafts portfolio-ready case studies that tell the full story of a design project. |
| **`presentation-deck`** | Structures compelling design presentations for stakeholders, reviews, and showcases. |
| **`service-blueprint`** | Maps the end-to-end service delivery system including frontstage, backstage, and supporting infrastructure. |
| **`team-workflow`** | Designs team workflows covering task management, collaboration rituals, and tooling. |
| **`version-control-strategy`** | Defines version control strategies for design files, components, and libraries. |
| **`design-system-governance`** | Defines how a design system evolves — contribution models, versioning, change management, and deprecation. |
| **`design-system-adoption`** | Creates adoption strategies and materials to drive design system usage across teams. |
| **`design-sprint-plan`** | Plans and facilitates design sprints from challenge framing through prototype testing. |
| **`design-negotiation`** | Advocates for design quality, scope, and time with cross-functional partners using evidence and shared goals. |
| **`ux-writing`** | Writes effective UI copy including microcopy, error messages, empty states, and CTAs. |
| **`ux-researcher-designer`** | Full UX research and design toolkit — personas, journey mapping, usability testing frameworks, and research synthesis. |

---

## Commands

If you've installed the command pack, every skill is also a slash subcommand. The SEO, GEO, and docs skills run under `/dev-gtm`; the full-funnel marketing skills run under `/marketing`; the comprehensive SEO suite runs under `/seo`; the blog content engine runs under `/blog`; the web design skills run under `/web-design`; the product management skills run under `/pm`; the Notion and productivity skills run under `/notion`; the coding skills run under `/coding-skills`; the job search skills run under `/job-search`; and the product designer skills run under `/product-designers`.

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

### `/notion` — productivity & workflow

| Command | Description |
| --- | --- |
| `/notion capture` | Transform a messy brain dump into four structured sections (Projects/Ideas, Tasks, Connections, Next Steps). |
| `/notion inbox` | Run email triage — first run builds your taxonomy KB, recurring runs classify and draft replies. |
| `/notion reflect` | Pause mid-conversation for a frank 5-dimension reassessment with a concrete continue/pivot/pause recommendation. |
| `/notion workflow <task>` | Design and generate a multi-agent Claude Code workflow script for any repeatable multi-step task. |
| `/notion content-brief <keyword>` | Generate a full SEO content brief and optionally push it to Notion. |
| `/notion claude-md-starter` | Scan the current repo and auto-generate a populated CLAUDE.md. |
| `/notion meeting-notes` | Structure raw meeting notes into action items, decisions, and a summary. |

---

### `/coding-skills` — software engineering

| Command | Description |
| --- | --- |
| `/coding-skills code-reviewer <repo or file>` | Analyze PRs for complexity, risk, code smells, and SOLID violations across 13 languages. |
| `/coding-skills pr-review-expert <PR or diff>` | Expert-level PR review for security issues, correctness, and code quality. |
| `/coding-skills karpathy-guidelines` | Apply behavioral guidelines to reduce common LLM coding mistakes. |
| `/coding-skills senior-architect <system>` | Design system architecture, evaluate trade-offs, create diagrams, and write ADRs. |
| `/coding-skills brainstorming <idea or feature>` | Explore user intent, requirements, and design before any implementation begins. |
| `/coding-skills test-driven-development <feature>` | Write tests first, watch them fail, then write minimal passing code. |
| `/coding-skills using-superpowers` | Establish skill discovery and invocation at the start of a session. |

---

### `/job-search` — job search & career

| Command | Description |
| --- | --- |
| `/job-search job-search <keyword>` | Search jobs matching your resume and preferences across job boards. |
| `/job-search apply <job URL>` | Fill out a Greenhouse, Lever, or Workday application end-to-end. |
| `/job-search application-form-filler <job desc>` | Fill application form fields from your CV and the job description. |
| `/job-search network-scan <contacts or 'all'>` | Scan LinkedIn contacts' companies for matching job openings. |
| `/job-search job-description-analyzer <posting>` | Analyze a job posting, score the match, and identify gaps. |
| `/job-search tailor-resume <job URL>` | Full resume tailoring workflow — fetches posting, tailors, critiques. |
| `/job-search resume-tailor <job posting>` | Customize a resume for a specific role. |
| `/job-search resume-ats-optimizer <resume>` | Optimize for ATS and analyze keyword match. |
| `/job-search resume-bullet-writer <bullets>` | Transform weak bullets into achievement-focused statements. |
| `/job-search resume-formatter <resume>` | ATS-friendly formatting and clean scannable layout. |
| `/job-search resume-quantifier <resume>` | Add metrics and quantified impact to resume bullets. |
| `/job-search resume-section-builder <role>` | Build targeted sections for different experience levels and roles. |
| `/job-search resume-version-manager <context>` | Track and manage multiple resume versions. |
| `/job-search tech-resume-optimizer <resume>` | Optimize for engineering and technical roles. |
| `/job-search academic-cv-builder <CV>` | Format CVs for academic positions with publications and grants. |
| `/job-search executive-resume-writer <context>` | C-suite and VP level resume writing. |
| `/job-search creative-portfolio-resume <context>` | Visual resume balancing design with ATS compatibility. |
| `/job-search cover-letter <job URL>` | Write a tailored cover letter for a specific job posting. |
| `/job-search cover-letter-generator <resume + JD>` | Generate a cover letter from resume and job description. |
| `/job-search cold-email-writer <target>` | Personalized cold outreach emails to hiring managers. |
| `/job-search interview-prep-generator <resume>` | STAR stories, practice questions, and talking points. |
| `/job-search offer-comparison-analyzer <offers>` | Compare multiple offers with total compensation analysis. |
| `/job-search salary-negotiation-prep <role>` | Market rates, negotiation strategy, and counter-offer scripts. |
| `/job-search linkedin-profile-optimizer <profile>` | Optimize LinkedIn for recruiter searchability and engagement. |
| `/job-search portfolio-case-study-writer <project>` | Transform resume bullets into portfolio case studies. |
| `/job-search career-changer-translator <industries>` | Identify transferable skills across industries. |
| `/job-search reference-list-builder <context>` | Format and prepare professional references. |

---

### `/product-designers` — UX & product design

| Command | Description |
| --- | --- |
| `/product-designers user-persona <research>` | Create user personas from research data. |
| `/product-designers empathy-map <user>` | Build empathy maps (Says / Thinks / Does / Feels). |
| `/product-designers interview-script <topic>` | Create structured user interview scripts. |
| `/product-designers journey-map <user + product>` | End-to-end journey maps with stages and pain points. |
| `/product-designers affinity-diagram <data>` | Organize research into themes and clusters. |
| `/product-designers user-flow-diagram <task>` | Create flow diagrams with decisions and branches. |
| `/product-designers experience-map <service>` | Map full ecosystem of touchpoints and channels. |
| `/product-designers diary-study-plan <topic>` | Design diary studies for longitudinal research. |
| `/product-designers card-sort-analysis <data>` | Analyze card sorts for IA decisions. |
| `/product-designers survey-design <hypothesis>` | Design reliable quantitative surveys. |
| `/product-designers summarize-interview <transcript>` | Summarize interviews into structured insights. |
| `/product-designers research-repository <context>` | Build a findable, reusable research repository. |
| `/product-designers design-brief <problem>` | Write a comprehensive design brief. |
| `/product-designers design-principles <product>` | Define actionable design principles. |
| `/product-designers jobs-to-be-done <product>` | Map Jobs-to-Be-Done with full functional, emotional, and social dimensions. |
| `/product-designers north-star-vision <product>` | Articulate a compelling product vision. |
| `/product-designers opportunity-framework <problem>` | Identify and prioritize design opportunities. |
| `/product-designers business-design <context>` | Communicate design in the language of business value. |
| `/product-designers competitive-analysis <product>` | Compare UX patterns across competitors. |
| `/product-designers metrics-definition <feature>` | Define UX metrics and KPIs. |
| `/product-designers design-impact-reporting <project>` | Report design's business contribution to stakeholders. |
| `/product-designers content-strategy <product>` | Define content structure and ownership. |
| `/product-designers stakeholder-alignment <project>` | Build alignment with RACI and decision frameworks. |
| `/product-designers fitts-law <interface>` | Size and position targets for fast, accurate interaction. |
| `/product-designers hicks-law <interface>` | Reduce decision time by limiting simultaneous choices. |
| `/product-designers millers-law <content>` | Chunk information to fit working memory limits. |
| `/product-designers doherty-threshold <feature>` | Keep system response times under 400ms. |
| `/product-designers aesthetic-usability <interface>` | Polished interfaces feel more usable. |
| `/product-designers law-of-proximity <layout>` | Group elements through spatial relationships. |
| `/product-designers law-of-common-region <layout>` | Group elements with containers and backgrounds. |
| `/product-designers von-restorff-effect <interface>` | Make key elements distinctly different from surroundings. |
| `/product-designers color-system <product>` | Build a color palette with semantic mapping and a11y compliance. |
| `/product-designers typography-scale <product>` | Create a modular type scale with size, weight, and line-height. |
| `/product-designers spacing-system <product>` | Build consistent spacing from a base unit. |
| `/product-designers layout-grid <product>` | Define responsive grids with columns, gutters, and breakpoints. |
| `/product-designers design-token <system>` | Define and organize design tokens with naming conventions. |
| `/product-designers design-token-audit <codebase>` | Audit token usage for consistency and coverage. |
| `/product-designers naming-convention <system>` | Establish naming rules for components and tokens. |
| `/product-designers icon-system <product>` | Spec icon grid, sizing, naming, and categories. |
| `/product-designers illustration-style <product>` | Define illustration visual language and application rules. |
| `/product-designers motion-system <product>` | Define duration tokens, easing vocabulary, and reduced motion. |
| `/product-designers pattern-library <pattern>` | Structure pattern library entries with context and examples. |
| `/product-designers theming-system <product>` | Design theming for brand variants and dark mode. |
| `/product-designers dark-mode-design <interface>` | Adapt color, contrast, and elevation for dark mode. |
| `/product-designers readable-measure <typography>` | Set optimal line lengths for readability. |
| `/product-designers interface-design <product>` | Craft-first design for SaaS apps, dashboards, and tools. |
| `/product-designers interfaces-that-feel <interface>` | Apply emotional resonance to technically correct but flat UIs. |
| `/product-designers information-architecture <product>` | Design structure, hierarchy, and navigation model. |
| `/product-designers navigation-patterns <product>` | Select navigation patterns by task and platform. |
| `/product-designers visual-hierarchy <screen>` | Establish hierarchy through size, weight, and color. |
| `/product-designers responsive-design <product>` | Adaptive layouts across all screen sizes. |
| `/product-designers form-design <form>` | Design forms that minimize friction and prevent errors. |
| `/product-designers loading-states <component>` | Design skeleton and progressive reveal patterns. |
| `/product-designers error-handling-ux <flow>` | Design error prevention and recovery experiences. |
| `/product-designers onboarding-design <product>` | First-run experiences that reach value fast. |
| `/product-designers search-ux <product>` | Design search with findability and failure recovery. |
| `/product-designers feedback-patterns <product>` | Confirmations, status updates, and notifications. |
| `/product-designers data-visualization <data>` | Clear, accessible charts and data displays. |
| `/product-designers animation-principles <interface>` | Apply animation principles to UI motion. |
| `/product-designers gesture-patterns <touch interface>` | Design gesture interactions for touch and pointer. |
| `/product-designers micro-interaction-spec <action>` | Specify micro-interactions with trigger, rules, and feedback. |
| `/product-designers state-machine <component>` | Model UI behavior as finite state machines. |
| `/product-designers localization-design <product>` | Design for multiple languages and writing directions. |
| `/product-designers critique-affordance <screen>` | Critique what looks clickable and CTA clarity. |
| `/product-designers critique-brand-consistency <screen>` | Critique brand against mood and token definitions. |
| `/product-designers critique-color <screen>` | Critique contrast, palette, and colour accessibility. |
| `/product-designers critique-composition <screen>` | Critique balance, whitespace, and gestalt. |
| `/product-designers critique-information-density <screen>` | Critique cognitive load and content prioritisation. |
| `/product-designers critique-typography <screen>` | Critique scale, readability, and token compliance. |
| `/product-designers critique-visual-hierarchy <screen>` | Critique entry point, eye flow, and emphasis. |
| `/product-designers accessibility-audit <product>` | WCAG audit with severity ratings and remediation steps. |
| `/product-designers accessibility-test-plan <feature>` | Testing plan covering assistive technologies and WCAG. |
| `/product-designers a-b-test-design <hypothesis>` | Design A/B tests with metrics and sample sizes. |
| `/product-designers heuristic-evaluation <product>` | Expert evaluation using Nielsen's heuristics. |
| `/product-designers usability-test-plan <feature>` | Test plan with tasks, metrics, and facilitation guide. |
| `/product-designers click-test-plan <navigation>` | First-click tests for navigation findability. |
| `/product-designers test-scenario <feature>` | Structured usability test scenarios ready to run. |
| `/product-designers design-qa-checklist <release>` | QA checklist for design implementation accuracy. |
| `/product-designers design-debt-audit <product>` | Identify and prioritize design inconsistencies. |
| `/product-designers prototype-strategy <question>` | Choose the right fidelity and prototyping method. |
| `/product-designers component-spec <component>` | Props, states, variants, and accessibility specification. |
| `/product-designers handoff-spec <design>` | Dev handoff with measurements, behaviors, and edge cases. |
| `/product-designers design-rationale <decision>` | Rationale connecting decisions to user needs and goals. |
| `/product-designers design-review-process <team>` | Review gates with criteria and approval workflows. |
| `/product-designers design-critique <design>` | Facilitate structured critique sessions. |
| `/product-designers documentation-template <pattern>` | Generate documentation templates for components. |
| `/product-designers wireframe-spec <screen>` | Wireframe spec with content priority and annotations. |
| `/product-designers anydesign <URL or image>` | Extract design system from any visual source. |
| `/product-designers case-study <project>` | Portfolio-ready design case studies. |
| `/product-designers presentation-deck <project>` | Compelling design presentations for stakeholders. |
| `/product-designers service-blueprint <service>` | Map frontstage, backstage, and supporting infrastructure. |
| `/product-designers team-workflow <team>` | Design team rituals, task management, and tooling. |
| `/product-designers version-control-strategy <files>` | Version control for design files and libraries. |
| `/product-designers design-system-governance <system>` | Contribution models, versioning, and deprecation. |
| `/product-designers design-system-adoption <system>` | Drive design system adoption across teams. |
| `/product-designers design-sprint-plan <challenge>` | Plan design sprints from brief to prototype. |
| `/product-designers design-negotiation <context>` | Advocate for design with evidence and shared goals. |
| `/product-designers ux-writing <screen>` | Microcopy, error messages, empty states, and CTAs. |
| `/product-designers ux-researcher-designer <context>` | Full UX research and design toolkit. |

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
├── notion-skills/                   # 7 personal-productivity and workflow skills (/notion)
│   ├── capture/                     # brain-dump organizer
│   ├── inbox/                       # email triage system
│   ├── reflect/                     # mid-conversation reassessment
│   ├── workflow-builder/            # multi-agent workflow script generator
│   ├── content-brief/               # keyword → SEO brief → Notion
│   ├── claude-md-starter/           # repo scanner + CLAUDE.md generator
│   └── meeting-notes/               # structured meeting summaries
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
