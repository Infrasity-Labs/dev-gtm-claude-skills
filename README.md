<p align="center">
  <img src="./assets/infrasity_logo.avif" alt="Infrasity Logo" width="400"/>
</p>

<p align="center">
  Production-grade Claude skills for GEO, AI discoverability, developer GTM, and technical content workflows.
</p>

<p align="center">

  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.9+-blue" />
  </a>

  <a href="https://claude.ai/">
    <img src="https://img.shields.io/badge/Claude-Compatible-orange" />
  </a>

  <a href="https://img.shields.io/badge/GEO-Optimized-purple">
    <img src="https://img.shields.io/badge/GEO-Optimized-purple" />
  </a>

  <a href="https://img.shields.io/badge/AI_Visibility-Enabled-blueviolet">
    <img src="https://img.shields.io/badge/AI_Visibility-Enabled-blueviolet" />
  </a>

  <a href="https://img.shields.io/badge/Developer_GTM-Infrastructure-darkgreen">
    <img src="https://img.shields.io/badge/Developer_GTM-Infrastructure-darkgreen" />
  </a>

  <a href="https://img.shields.io/badge/LLM-Citation_Ready-8A2BE2">
    <img src="https://img.shields.io/badge/LLM-Citation_Ready-8A2BE2" />
  </a>

  <a href="https://img.shields.io/badge/AI_Discoverability-Infrastructure-black">
    <img src="https://img.shields.io/badge/AI_Discoverability-Infrastructure-black" />
  </a>

  <a href="https://img.shields.io/badge/Technical_Content-Intelligence-informational">
    <img src="https://img.shields.io/badge/Technical_Content-Intelligence-informational" />
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

## Skills

| Skill | What it does | Trigger phrase |
|---|---|---|
| [`docs-auditor`](./skills/docs-auditor/) | Audits any developer documentation site across 33 checks in 7 categories and produces a scored report (out of 100) covering AI/LLM discoverability, structure, content completeness, content quality, technical SEO, internal linking, and versioning | `Analyze docs for https://...` |

More skills are in development. See [Contributing](#contributing) to add your own.

---

## Installation

1. Go to **[Settings -> Capabilities](https://claude.ai/settings/capabilities)** and make sure **Code execution and file creation** is enabled.
2. Go to **[Customize -> Skills](https://claude.ai/customize/skills)**.
3. Click **+** -> **Create skill** -> **Upload a skill**.
4. Upload the skill as a ZIP file (see below).

**To upload `docs-auditor`:**

```bash
# Clone the repo
git clone https://github.com/infrasity-labs/dev-gtm-claude-skills.git

# Zip the skill folder
cd dev-gtm-claude-skills/skills
zip -r docs-auditor.zip docs-auditor/
```

<p align="center">
  <img src="./assets/converting-to-zip.gif" width="100%" alt="Converting to zip GIF"/>
</p>

Then upload `docs-auditor.zip` in the Skills settings above. Once uploaded, toggle the skill on and it is immediately active across all your chats.


<p align="center">
  <img src="./assets/add-to-claude.gif" width="100%" alt="Add to claude GIF"/>
</p>

---

## Quick example

Once `docs-auditor` is installed:

```
Analyze docs for https://docs.stripe.com
```

Claude fetches the docs site and its key sub-pages (`/quickstart`, `/changelog`, `/robots.txt`, `/llms.txt`, `/sitemap.xml`, and more), then runs 33 checks across 7 categories and returns a scored visual report.

The report renders as an interactive visual widget in claude.ai, with pass/warn/fail badges per check and short evidence notes for every finding.

<p align="center">
  <a href="./assets/docs-auditor-gif.gif">
    <img
      src="./assets/docs-auditor-gif.gif"
      width="100%"
      alt="Docs Auditor Demo"
    />
  </a>
</p>

---

## What the 7 categories cover

The audit runs checks across 7 categories. Each check is marked **pass**, **warn**, or **fail** based on evidence fetched from the live site.

| # | Category | Checks |
|---|----------|--------|
| 1 | **AI & LLM Discoverability** | `llms.txt`, `llms-full.txt`, docs pages listed in llms.txt, AI bots in robots.txt, docs in sitemap.xml |
| 2 | **Structure & Navigation** | Overview page, quickstart, API reference, sidebar, breadcrumbs, search |
| 3 | **Content Completeness** | Tutorials/examples, code snippets, multi-language examples, changelog, FAQ/troubleshooting, error codes |
| 4 | **Content Quality** | Intro clarity, quickstart completeness, page depth (no stubs) |
| 5 | **Technical SEO & Crawlability** | HTTPS, meta titles, meta descriptions, canonical URLs, noindex directives |
| 6 | **Internal Linking & Flow** | Cross-links between pages, prev/next navigation, GitHub links, community/support links |
| 7 | **Versioning & Maintenance** | Version badge, freshness signals, pinned install commands, deprecation notices |

---

## Repository structure

```
dev-gtm-claude-skills/
├── assets/                    # Logos and images for this README
├── skills/
│   └── docs-auditor/
│       ├── SKILL.md           # Agent instructions - Claude reads this
│       ├── README.md          # Full usage docs for humans
│       └── references/        # Widget template, scoring guide, fetch strategy
└── README.md
```

---

## Contributing

To add a new skill, create a folder under `skills/` with this structure:

```
skills/your-skill-name/
├── SKILL.md          # Required - agent instructions (see below)
├── README.md         # Required - human-facing docs
├── requirements.txt  # Required if the skill has dependencies
└── scripts/          # Python tooling (if applicable)
```

**`SKILL.md` must include:**

```markdown
---
name: your-skill-name
version: 1.0.0
description: One sentence - what does this skill check or produce?
author: Your Name
tags: [relevant, tags]
---

# Skill Title

## When to use
- Trigger condition 1
- Trigger condition 2

## Workflow
...

## Return value
...
```

The `description` field in the frontmatter is what Claude uses to decide when to activate the skill. Write it to match the natural language a user would use when asking for this task.

Open a PR with your skill folder and a brief description of what it covers.

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

MIT - see [LICENSE](./LICENSE).

Built by [Infrasity](https://www.linkedin.com/company/infrasity/).