<p align="center">
  <img src="./assets/infrasity_logo.avif" alt="Infrasity Logo" width="400"/>
</p>

<p align="center">
  Production-grade Claude skills for SEO, GEO, AI discoverability, developer GTM, and technical content workflows.
</p>

<p align="center">
  <a href="https://claude.ai/">
    <img src="https://img.shields.io/badge/Claude-Compatible-orange" />
  </a>
  <a href="https://img.shields.io/badge/Claude_Code-Supported-blue">
    <img src="https://img.shields.io/badge/Claude_Code-Supported-blue" />
  </a>
  <a href="https://img.shields.io/badge/Claude_Desktop-Supported-green">
    <img src="https://img.shields.io/badge/Claude_Desktop-Supported-green" />
  </a>
  <a href="https://img.shields.io/badge/GEO-Optimized-purple">
    <img src="https://img.shields.io/badge/GEO-Optimized-purple" />
  </a>
  <a href="https://img.shields.io/badge/Agentic_AI-Ready-red">
    <img src="https://img.shields.io/badge/Agentic_AI-Ready-red" />
  </a>
</p>

<p align="center">
  <img src="./assets/dev-gtm-claude-skills.png" width="100%" alt="dev-gtm-claude-skills"/>
</p>

---

## Dev-GTM-Claude-Skills

Dev-GTM-Claude-Skills is a collection of modular skills for Claude that automate developer GTM and AI discoverability workflows. Each skill is a self-contained package: a `SKILL.md` that tells Claude when and how to use it, optional Python tooling or agent-led workflows, and a README with full usage docs.

**GEO (Generative Engine Optimization)** is the practice of making your content and documentation discoverable and citable by AI systems: ChatGPT, Claude, Perplexity, and others. These skills are built specifically for developer-focused companies that need to measure and improve their AI visibility, not just their traditional SERP rankings.

---

## Table of Contents

- [Installation](#installation)
- [Skills](#skills)
- [Commands](#commands)
- [Sample Output](#sample-output)
- [Requirements](#requirements)
- [Repository Structure](#repository-structure)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## Installation

### Claude Code

Clone the repo and copy the skills into your Claude Code skills directory:

```bash
git clone https://github.com/infrasity-labs/dev-gtm-claude-skills.git
```

**Project-level** (available only in this project):
```bash
mkdir -p .claude/skills
cp -r dev-gtm-claude-skills/skills/<skill-name> .claude/skills/
```

**User-level** (available across all projects):
```bash
mkdir -p ~/.claude/skills
cp -r dev-gtm-claude-skills/skills/<skill-name> ~/.claude/skills/
```

Skills activate automatically. Claude reads every `SKILL.md` in `.claude/skills/` at the start of each session. Trigger them by describing the task in plain language, or type `/<skill-name>` directly.

<p align="center">
  <img src="./assets/clone-repo.png" width="100%" alt="clone repo"/>
</p>

<p align="center">
  <img src="./assets/activate-skills.gif" width="100%" alt="Activate skills GIF"/>
</p>

---

### Claude Desktop

Skills are uploaded as ZIP files via **Settings → Customize → Skills → Create skill → Upload a skill**.

```bash
git clone https://github.com/infrasity-labs/dev-gtm-claude-skills.git
cd dev-gtm-claude-skills/skills

# Zip the skill you want to install
zip -r docs-auditor.zip docs-auditor/
```

Upload the `.zip` in Claude Desktop. Toggle the skill on and it is immediately active across all chats.

<p align="center">
  <img src="./assets/converting-to-zip.gif" width="100%" alt="Converting to zip GIF"/>
</p>

<p align="center">
  <img src="./assets/add-to-claude.gif" width="100%" alt="Add to Claude GIF"/>
</p>

---

### DataForSEO MCP

Some skills require a DataForSEO MCP server. Add this to your Claude config:

**Claude Code** (`.claude/settings.json` or `~/.claude/settings.json`):
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

**Claude Desktop** (**Customize → Connectors → Add Custom Connector**):
```json
https://your_email:your_api_password@mcp.dataforseo.com/http
```

Get your DataForSEO credentials at [dataforseo.com](https://dataforseo.com).

---

## Skills

| Skill | What it does | Example trigger |
|---|---|---|
| [`docs-auditor`](./skills/docs-auditor/) | Audits any developer docs site across 33 checks in 7 categories. Produces a scored report (out of 100) with pass/warn/fail per check covering AI discoverability, structure, content quality, SEO, and more. | `Audit the docs at docs.stripe.com` |
| [`api-docs-quality-report`](./skills/api-docs-quality-report/) | Crawls every endpoint page of an API docs site and scores each across 5 checks. Outputs an interactive HTML report with a scorecard, pattern analysis, top issues, and per-endpoint fix guidance. | `Run an API docs audit on docs.company.com` |
| [`growth-report`](./skills/growth-report/) | Generates a 3-month SEO performance HTML report for any domain vs competitors using live DataForSEO data: traffic trends, keyword rankings, top content clusters, and competitive positioning. | `Generate SEO report for firefly.ai vs spacelift.io, env0.com` |
| [`blog-post-counter`](./skills/blog-post-counter/) | Counts unique blog posts for any company from its sitemap or listing page. Supports competitor comparison mode to benchmark content volume across multiple domains. | `How many blogs does hackmamba.io have vs infrasity.com` |
| [`brief-outline-generator-v2`](./skills/brief-outline-generator-v2/) | Generates a fully structured SEO content outline and exports it as a formatted `.docx` Word document with section headings, topic prompts, and angles for a writer to fill in. | `Generate a content brief for "developer marketing strategy"` |

---

## Commands

<p align="center">
  <img src="./assets/claude-commands.png" alt="Claude Commands" width="400"/>
</p>

| Command | Description |
|---|---|
| `/dev-gtm docs-auditor <docs-url>` | Run the full 33-check developer docs audit and return a scored report. |
| `/dev-gtm api-docs-quality-report <docs-url>` | Crawl every endpoint page and score each across 5 quality checks. |
| `/growth-report <target> vs <competitors>` | Generate a 3-month SEO performance HTML report with traffic, keywords, and competitive positioning. |
| `/blog-post-counter <domain>` | Count unique blog posts for one domain, or compare a target vs competitors. |
| `/brief-outline-generator-v2 <topic>` | Generate an SEO content outline and export it as a formatted `.docx`. |

---
## Sample Outputs

<p align="center">
  <img src="./assets/docs-auditor-gif-cc.gif" width="100%" alt="Docs Auditor Claude Code"/>
</p>

<p align="center">
  <img src="./assets/growth-report-cc.gif" width="100%" alt="Growth Report Claude Code"/>
</p>

---

## Requirements

- **Claude Code**, **Claude Desktop**, or **Claude.ai** 
- **Python 3.10+**
- **Node.js** with `npx` to run the DataForSEO MCP server locally.
- **DataForSEO API** for the SEO skills that pull live search data: [`growth-report`](./skills/growth-report/), [`blog-post-counter`](./skills/blog-post-counter/), and [`api-docs-quality-report`](./skills/api-docs-quality-report/).

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
│   ├── api-docs-quality-report/
│   ├── growth-report/
│   ├── blog-post-counter/
│   ├── brief-outline-generator-v2/
│   └── docx-to-md/
└── README.md
```

---

## Contributing

To add a skill, create a folder under `skills/` with the following structure:

```
skills/your-skill-name/
├── SKILL.md          # Required: agent instructions
├── README.md         # Required: human-facing docs
├── requirements.txt  # If the skill has Python dependencies
└── references/       # Templates, scoring guides, or other reference files
```

**`SKILL.md` must include a frontmatter block:**

```markdown
---
name: your-skill-name
description: >
  One paragraph describing exactly when Claude should activate this skill.
  Write it to match the natural language a user would use.
---
```

The `description` field is what Claude uses to decide when to activate the skill. Be specific about trigger phrases and input formats.

Open a PR with your skill folder and a one-line summary of what it covers.

---

## Let's Connect

<p align="center">
  <a href="https://infrasity.com">
    <img src="https://img.shields.io/badge/INFRASITY.COM-000000?style=for-the-badge&logo=googlechrome&logoColor=white" />
  </a>
  <a href="https://www.linkedin.com/company/infrasity/posts/?feedView=all">
    <img src="https://img.shields.io/badge/LINKEDIN-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  <a href="https://www.youtube.com/@Infrasity">
    <img src="https://img.shields.io/badge/YOUTUBE-FF0000?style=for-the-badge&logo=youtube&logoColor=white" />
  </a>
</p>

## License

MIT License. See [LICENSE](./LICENSE) for details.

## Author

Built by [Infrasity](https://infrasity.com).