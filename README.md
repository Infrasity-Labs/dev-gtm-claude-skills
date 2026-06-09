<div align="center">

<img src="assets/infrasity_logo.avif" alt="Infrasity" height="64" />

# Claude Code Skills for SEO, GEO & Developer Marketing

**Free, open-source Claude skills that audit your docs, score your AI discoverability, and run developer-marketing workflows — so your product gets found, parsed, and cited by AI systems.**

[![Claude Compatible](https://img.shields.io/badge/Claude-Compatible-FF4A1C)](https://claude.ai/) [![GEO Optimized](https://img.shields.io/badge/GEO-Optimized-7F77DD)](https://www.infrasity.com/services/ai-geo-optimization-agency) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) [![GitHub stars](https://img.shields.io/github/stars/Infrasity-Labs/dev-gtm-claude-skills?style=social)](https://github.com/Infrasity-Labs/dev-gtm-claude-skills/stargazers) [![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/) [![skills.sh](https://skills.sh/b/Infrasity-Labs/dev-gtm-claude-skills)](https://skills.sh/Infrasity-Labs/dev-gtm-claude-skills)

[Skills](#skills) · [Install](#installation) · [Commands](#commands) · [Who it's for](#who-its-for) · [FAQ](#faq) · [Website](https://www.infrasity.com/claude-skills)

**Works with:** Claude Code · OpenAI Codex · Gemini CLI · OpenClaw · Hermes Agent[^hermes] · Mistral Vibe[^vibe] · Cursor · Aider · Windsurf · Kilo Code · OpenCode · Augment · Antigravity

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

This repo ships both: the SEO/GEO/docs **skills** under [`skills/`](skills/), the full-funnel marketing **skills** under [`marketing-skills/`](marketing-skills/), and a set of blog-production **agents** under [`agents/`](agents/).

---

## Table of contents

- [What Are Claude Code Skills & Agent Plugins?](#what-are-claude-code-skills--agent-plugins)
- [Multi-Tool Support](#multi-tool-support)
- [Installation](#installation)
- [Skills](#skills)
- [Marketing skills](#marketing-skills)
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

| Tool | Format | Install command |
| --- | --- | --- |
| **Claude Code** | Native `SKILL.md` | `npx skills add Infrasity-Labs/dev-gtm-claude-skills` |
| **Claude Desktop / Claude.ai** | ZIP upload | See [Installation](#claude-desktop--claudeai) |
| **OpenAI Codex** | `~/.codex/skills/` | `python3 scripts/sync-codex-skills.py && ./scripts/codex-install.sh` |
| **Gemini CLI** | `.gemini/skills/` | `./scripts/gemini-install.sh` |
| **OpenClaw** | `~/.openclaw/workspace/skills/` | `./scripts/openclaw-install.sh` |
| **Hermes Agent**[^hermes] | `~/.hermes/skills/` | `python3 scripts/sync-hermes-skills.py --verbose` |
| **Mistral Vibe**[^vibe] | `~/.vibe/skills/` | `./scripts/vibe-install.sh` |
| **Cursor** | `.cursor/rules/*.mdc` | `./scripts/convert.sh --tool cursor && ./scripts/install.sh --tool cursor --target .` |
| **Aider** | `CONVENTIONS.md` | `./scripts/convert.sh --tool aider && ./scripts/install.sh --tool aider --target .` |
| **Windsurf** | `.windsurf/skills/` | `./scripts/convert.sh --tool windsurf && ./scripts/install.sh --tool windsurf --target .` |
| **Kilo Code** | `.kilocode/rules/` | `./scripts/convert.sh --tool kilocode && ./scripts/install.sh --tool kilocode --target .` |
| **OpenCode** | `.opencode/skills/` | `./scripts/convert.sh --tool opencode && ./scripts/install.sh --tool opencode --target .` |
| **Augment** | `.augment/skills/` | `./scripts/convert.sh --tool augment && ./scripts/install.sh --tool augment --target .` |
| **Antigravity** | `~/.gemini/antigravity/skills/` | `./scripts/convert.sh --tool antigravity && ./scripts/install.sh --tool antigravity` |

**How the scripts work:**

- **`convert.sh --tool <name>`** rewrites each `SKILL.md` into the target tool's format (Cursor `.mdc` rules, Aider `CONVENTIONS.md`, Kilo Code markdown rules, or `SKILL.md` bundles for Windsurf/OpenCode/Augment/Antigravity) and writes the result to `integrations/<tool>/`. Use `--tool all` to build every format at once.
- **`install.sh --tool <name> [--target <dir>]`** copies the converted output from `integrations/<tool>/` into the right place — a project directory (`--target .`) for the rule-based tools, or your home directory for Antigravity. Re-run with `--force` to overwrite.
- **`sync-codex-skills.py`**, **`sync-gemini-skills.py`**, **`sync-hermes-skills.py`**, and **`sync-vibe-skills.py`** symlink (or `--copy`) the skills straight into each tool's directory — no conversion needed, since those tools read the agentskills.io `SKILL.md` standard directly. Pass `--dry-run` to preview.

The Python tooling that ships with the live-data skills is stdlib-only, so it runs anywhere Python runs.

[^hermes]: **Hermes Agent** is BYO-sync: run `python3 scripts/sync-hermes-skills.py` once to install into `~/.hermes/skills/`. Uses the same agentskills.io `SKILL.md` standard — no format conversion.
[^vibe]: **Mistral Vibe** is also BYO-sync: run `./scripts/vibe-install.sh` once to install into `~/.vibe/skills/`. Same agentskills.io `SKILL.md` standard — no conversion. Docs: <https://docs.mistral.ai/mistral-vibe/agents-skills>.

---

## Installation

Most skills need **no API keys**; the SEO skills that pull live search data use a DataForSEO MCP server (setup below).

### Quick install (recommended)

Install every skill in this repo with one command — no cloning, no copying:

```bash
npx skills add Infrasity-Labs/dev-gtm-claude-skills
```

This pulls the latest skills straight into your Claude Code skills directory. Re-run it any time to update. Prefer to install manually or use Claude Desktop / Claude.ai? Use one of the methods below.

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

## Commands

If you've installed the command pack, every skill is also a slash subcommand. The SEO, GEO, and docs skills run under `/dev-gtm`; the full-funnel marketing skills run under `/marketing`.

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
└── README.md
```

---

## FAQ

**Are these Claude skills free?**
Yes — every skill is free and MIT-licensed. No license fees, no paywalls.

**Do I need Claude Code?**
No. Skills run in Claude Code, Claude Desktop, or Claude.ai. Desktop and web use the ZIP upload method above.

**Which skills need API keys?**
Most need none. Only the live-search skills (`growth-report`, `blog-post-counter`, `api-docs-quality-report`) use DataForSEO, and the internal-linking skills (`orphan-pages…`, `no-outlinks-audit`) use Ahrefs.

**How is this different from a standard SEO audit tool?**
Traditional tools optimize for Google crawlers. These skills are built for developer documentation and AI discoverability — they check whether your docs can be parsed, cited, and recommended by LLMs.

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
