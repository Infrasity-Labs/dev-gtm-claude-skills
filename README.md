<p align="center">
  <img src="./assets/infrasity_logo.avif" alt="Infrasity Logo" width="400"/>
</p>

<h1 align="center">Infrasity AI Skills</h1>

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

  <a href="https://www.linkedin.com/company/infrasity/posts/?feedView=all">
    <img src="https://img.shields.io/badge/LinkedIn-Infrasity-0A66C2?logo=linkedin&logoColor=white" />
  </a>

  <a href="https://www.instagram.com/infrasity/">
    <img src="https://img.shields.io/badge/Instagram-@infrasity-E4405F?logo=instagram&logoColor=white" />
  </a>

</p>

<p align="center">
  <img src="./assets/dev-gtm-claude-skills.png" width="100%" alt="dev-gtm-claude-skills"/>
</p>

---

## What this is

Infrasity AI Skills is a collection of modular skills for Claude that automate developer GTM and AI discoverability workflows. Each skill is a self-contained package — a `SKILL.md` that tells Claude when and how to use it, Python tooling that does the work, and a README with full usage docs.

**GEO (Generative Engine Optimization)** is the practice of making your content and documentation discoverable and citable by AI systems — ChatGPT, Claude, Perplexity, and others. These skills are built specifically for developer-focused companies that need to measure and improve their AI visibility, not just their traditional SERP rankings.

---

## Skills

| Skill | What it does | Trigger phrase |
|---|---|---|
| [`doc-metadata-analyzer`](./skills/doc-metadata-analyzer/) | Audits documentation pages for meta title and description quality against SEO/GEO best practices | `Analyze metadata for https://...` |

More skills are in development. See [Contributing](#contributing) to add your own.

---

## Installation

There are two ways to use these skills depending on how you access Claude.

### Option A — Claude.ai (Free, Pro, Max, Team, Enterprise)

Skills are natively supported in Claude.ai on all plans, including free. No Python or CLI required.

**One-time setup (do this once):**

1. Go to **[Settings → Capabilities](https://claude.ai/settings/capabilities)** and make sure **Code execution and file creation** is enabled.
2. Go to **[Customize → Skills](https://claude.ai/customize/skills)**.
3. Click **+** → **Create skill** → **Upload a skill**.
4. Upload the skill as a ZIP file (see below).

**To upload `doc-metadata-analyzer`:**

```bash
# Clone the repo
git clone https://github.com/infrasity-labs/dev-gtm-claude-skills.git

# Zip the skill folder
cd dev-gtm-claude-skills/skills
zip -r doc-metadata-analyzer.zip doc-metadata-analyzer/
```

<p align="center">
  <img src="./assets/converting-to-zip.gif" width="100%" alt="Converting to zip GIF"/>
</p>

Then upload `doc-metadata-analyzer.zip` in the Skills settings above. Once uploaded, toggle the skill on — it's immediately active across all your chats.

> Skills you upload are private to your account. Claude installs any required packages automatically the first time it uses the skill.

<p align="center">
  <img src="./assets/add-to-claude.gif" width="100%" alt="Add to claude GIF"/>
</p>

---

### Option B — Claude Code (CLI)

**Prerequisites:** Python 3.9+, [Claude Code](https://claude.ai/code)

```bash
# 1. Clone the repo
git clone https://github.com/infrasity-labs/dev-gtm-claude-skills.git
cd dev-gtm-claude-skills

# 2. Copy a skill into Claude Code's skills directory
mkdir -p ~/.claude/skills/ && cp -r skills/doc-metadata-analyzer ~/.claude/skills/

# 3. Install the skill's dependencies
cd ~/.claude/skills/doc-metadata-analyzer
pip install -r requirements.txt --break-system-packages
```

Claude Code picks up skills automatically from `~/.claude/skills/`. No further configuration needed.

---

## How skills work

Each skill folder contains a `SKILL.md` — a structured instruction file that tells Claude what the skill does, when to use it, and how to invoke the underlying tooling. When you describe a task that matches a skill's description, Claude reads the `SKILL.md` and follows its workflow automatically.

You can also invoke a skill explicitly:

```
Read skills/doc-metadata-analyzer/SKILL.md and analyze https://docs.yourproduct.com
```

---

## Quick example

Once `doc-metadata-analyzer` is installed:

```
Analyze metadata for https://docs.stripe.com/api
```

Claude fetches the page, validates the `<title>` and `<meta name="description">` tags, and returns a structured report:

```
📄 TITLE: Stripe API Reference
   Length: 21 chars
   Status: WARNING
   ⚠️  Title slightly short (21 chars, ideal: 50–60)

📝 DESCRIPTION: "A complete reference to Stripe's API..."
   Length: 143 chars
   Status: IDEAL ✓
```

Full output also includes a JSON payload suitable for piping into other tools or dashboards.

---

## Repository structure

```
dev-gtm-claude-skills/
├── assets/                    # Logos and images for this README
├── skills/
│   └── doc-metadata-analyzer/
│       ├── SKILL.md           # Agent instructions — Claude reads this
│       ├── README.md          # Full usage docs for humans
│       ├── check_metadata.py  # CLI entry point
│       ├── requirements.txt
│       └── scripts/           # Core Python library
└── README.md
```

---

## Contributing

To add a new skill, create a folder under `skills/` with this structure:

```
skills/your-skill-name/
├── SKILL.md          # Required — agent instructions (see below)
├── README.md         # Required — human-facing docs
├── requirements.txt  # Required if the skill has dependencies
└── scripts/          # Python tooling (if applicable)
```

**`SKILL.md` must include:**

```markdown
---
name: your-skill-name
version: 1.0.0
description: One sentence — what does this skill check or produce?
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

The `description` field in the frontmatter is what Claude uses to decide when to activate the skill — write it to match the natural language a user would use when asking for this task.

Open a PR with your skill folder and a brief description of what it covers.

---

## License

MIT — see [LICENSE](./LICENSE).

Built by [Infrasity](https://www.linkedin.com/company/infrasity/).
