<div align="center">

<img src="assets/infrasity_logo.avif" alt="Infrasity" height="64" />

# Claude Code Skills for SEO, GEO & Developer Marketing

**Free, open-source Claude skills that audit your docs, score your AI discoverability, and run developer-marketing workflows — so your product gets found, parsed, and cited by AI systems.**

[![Claude Compatible](https://img.shields.io/badge/Claude-Compatible-FF4A1C)](https://claude.ai/) [![GEO Optimized](https://img.shields.io/badge/GEO-Optimized-7F77DD)](https://www.infrasity.com/services/ai-geo-optimization-agency) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) [![GitHub stars](https://img.shields.io/github/stars/Infrasity-Labs/dev-gtm-claude-skills?style=social)](https://github.com/Infrasity-Labs/dev-gtm-claude-skills/stargazers) [![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/)

[Skills](#skills) · [Install](#installation) · [Commands](#commands) · [Who it's for](#who-its-for) · [FAQ](#faq) · [Website](https://www.infrasity.com/claude-skills)

</div>

---

## What this is

`dev-gtm-claude-skills` is a collection of open-source **Claude Code skills** for **SEO**, **GEO (Generative Engine Optimization)**, **AI discoverability**, and **developer marketing**. Each skill is a self-contained package — a `SKILL.md` that tells Claude when and how to use it, optional Python tooling, and a README with full usage docs. Install once, then run from Claude Code, Claude Desktop, or Claude.ai with a plain-language prompt.

These skills are built for **developer-focused companies** — DevTools, AI-agent platforms, observability, and B2B SaaS — that need their documentation and content to be **cited by AI systems like ChatGPT, Claude, Perplexity, and Gemini**, not just indexed by Google.

> **What is GEO?** Generative Engine Optimization is the practice of optimizing content so it gets surfaced and cited by AI answer engines. Traditional SEO tools optimize for search crawlers; these skills audit the signals — structured content, `llms.txt`, internal linking, and documentation completeness — that LLMs use when deciding what to recommend.

### What you can do in one prompt

- 📊 **Audit developer docs** for SEO and AI discoverability — 33 checks, scored 0–100
- 🔌 **Score API & SDK documentation** quality, endpoint by endpoint
- 🤖 **Check AI-readiness** — `robots.txt`, `llms.txt`, and `llms-full.txt` in one pass
- 📈 **Generate 3-month SEO performance reports** vs competitors
- 🔗 **Fix internal linking** — find orphan pages and dead-ends, get paste-ready suggestions
- ✍️ **Produce SEO content briefs** as formatted `.docx` outlines

---

## Table of contents

- [Installation](#installation)
- [Skills](#skills)
- [Commands](#commands)
- [Who it's for](#who-its-for)
- [Requirements](#requirements)
- [Sample outputs](#sample-outputs)
- [Repository structure](#repository-structure)
- [FAQ](#faq)
- [Contributing](#contributing)
- [License](#license)

---

## Installation

There are two ways to use these skills depending on how you access Claude. Most skills need **no API keys**; the SEO skills that pull live search data use a DataForSEO MCP server (setup below).

### Claude Code

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

Nine production-grade skills for SEO, GEO, and documentation workflows.

| Skill | Claude skill for… | What it does | Example trigger |
| --- | --- | --- | --- |
| **`docs-auditor`** | documentation SEO & AI discoverability | Audits a developer docs site across **33 checks in 7 categories** — AI discoverability, structure, content quality, SEO, internal linking, versioning — and returns a scored 0–100 report with pass/warn/fail per check. | `Audit the docs at docs.stripe.com` |
| **`sdk-docs-auditor`** | SDK documentation | Audits SDK docs across **6 sections** (Installation, Quick Start, Error Handling, Troubleshooting, Examples, Best Practices), scores each 0–100, cross-references gaps, and ships a downloadable HTML report. | `Audit the SDK docs at docs.example.com` |
| **`api-docs-quality-report`** | API documentation quality | Crawls **every endpoint page** and scores each across 5 checks. Outputs an interactive HTML report with a scorecard, pattern analysis, top issues, and per-endpoint fix guidance. | `Run an API docs audit on docs.company.com` |
| **`growth-report`** | SEO performance reports | Generates a **3-month SEO performance report** for any domain vs competitors using live DataForSEO data: traffic trends, keyword rankings, top content clusters, and competitive positioning. | `Generate SEO report for firefly.ai vs spacelift.io` |
| **`blog-post-counter`** | content research & competitive intel | Counts unique blog posts for any company from its sitemap or listing page, with a competitor-comparison mode to benchmark content volume across domains. | `How many blogs does hackmamba.io have vs infrasity.com` |
| **`brief-outline-generator-v2`** | SEO content briefs | Generates a fully structured SEO content outline and exports it as a formatted **`.docx`** with section headings, topic prompts, and angles for a writer to fill in. | `Generate a content brief for "developer marketing strategy"` |
| **`llms-txt-checker`** | GEO & AI readiness | Audits a domain's AI-readiness by probing `robots.txt`, `llms.txt`, and `llms-full.txt`, scoring each against a structured checklist with a pass/warn/fail report and prioritized fixes. **No API keys.** | `Check if stripe.com has llms.txt` |
| **`orphan-pages-internal-linking-opportunities`** | internal linking | Finds all **orphan pages** (zero incoming internal links) using Ahrefs, clusters them by topic, and generates 3 linking suggestions per orphan with anchor text and placement. Styled HTML report. | `Run an orphan page audit on example.com/blog/` |
| **`no-outlinks-audit`** | internal linking | Finds **dead-end pages** (zero outgoing internal links) and generates 3 outgoing link suggestions per page — anchor text, placement, ready-to-paste copy. Styled HTML report. | `Find pages with no outgoing links on example.com` |

---

## Commands

If you've installed the command pack, every skill is also a `/dev-gtm` subcommand.

<p align="center">
  <img src="./assets/claude-commands.png" alt="Claude Commands" width="400"/>
</p>

| Command | Description |
| --- | --- |
| `/dev-gtm docs-audit <docs-url>` | Run the full 33-check developer docs audit and return a scored report. |
| `/dev-gtm sdk-audit <docs-url>` | Audit SDK documentation across 6 sections; scored, downloadable HTML report. |
| `/dev-gtm api-audit <docs-url>` | Crawl every endpoint page and score each across 5 quality checks. |
| `/dev-gtm growth-report <target> vs <competitors>` | 3-month SEO performance report with traffic, keywords, and competitive positioning. |
| `/dev-gtm blog-count <domain>` | Count unique blog posts for one domain, or compare a target vs competitors. |
| `/dev-gtm brief-outline <topic>` | Generate an SEO content outline and export it as a formatted `.docx`. |
| `/dev-gtm llms-check <domain>` | Audit AI-readiness: probe `robots.txt`, `llms.txt`, `llms-full.txt`; scored report. |
| `/dev-gtm orphan-audit <domain>` | Discover orphan pages and generate 3 linking suggestions per orphan. |
| `/dev-gtm dead-ends <domain>` | Find dead-end pages and generate 3 outgoing link suggestions per page. |

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
│   ├── brief-outline-generator-v2/
│   ├── llms-txt-checker/
│   ├── orphan-pages-internal-linking-opportunities/
│   └── no-outlinks-audit/
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
