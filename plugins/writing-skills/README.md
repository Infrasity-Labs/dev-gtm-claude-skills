# writing-skills-plugin

34 blog and content writing skills for Claude Code — full blog orchestration, SEO, AI citation readiness, multilingual publishing, social media, and more.

---

## What's included

| # | Skill | What it does |
|---|-------|-------------|
| 1 | `/blog` | Master orchestrator — routes to all 30 sub-skills |
| 2 | `/blog-write` | Write a new article from scratch (6-pillar optimisation) |
| 3 | `/blog-rewrite` | Optimise and freshen an existing post |
| 4 | `/blog-brief` | Generate a detailed content brief with SERP analysis |
| 5 | `/blog-outline` | SERP-informed outline with competitive gap analysis |
| 6 | `/blog-audit` | Full-site blog health assessment |
| 7 | `/blog-analyze` | 100-point quality scoring + AI content detection |
| 8 | `/blog-strategy` | Blog positioning and topic ideation |
| 9 | `/blog-cluster` | Semantic topic clustering + hub-and-spoke execution |
| 10 | `/blog-flow` | FLOW framework integration (30 evidence-led prompts) |
| 11 | `/blog-audio` | Gemini TTS narration (30 voices, 3 formats) |
| 12 | `/blog-image` | AI image generation and editing via Gemini |
| 13 | `/blog-google` | Google API integration (PSI, CrUX, GSC, GA4, NLP, YouTube) |
| 14 | `/blog-notebooklm` | NotebookLM source-grounded research |
| 15 | `/blog-seo-check` | Post-writing SEO validation |
| 16 | `/blog-schema` | JSON-LD schema generation (BlogPosting, FAQ, Person) |
| 17 | `/blog-geo` | AI citation readiness audit (0-100 GEO score) |
| 18 | `/blog-repurpose` | Cross-platform repurposing (social, email, YouTube, Reddit) |
| 19 | `/blog-chart` | Built-in SVG chart generation (no external library) |
| 20 | `/blog-persona` | Writing voice and persona management |
| 21 | `/blog-brand` | Generate durable BRAND.md + VOICE.md context files |
| 22 | `/blog-discourse` | 30-day voice-of-customer research (API-free) |
| 23 | `/blog-cannibalization` | Keyword overlap detection with severity scoring |
| 24 | `/blog-factcheck` | Statistics verification against cited sources |
| 25 | `/blog-translate` | SEO-optimised translation with format preservation |
| 26 | `/blog-localize` | Cultural deep-adaptation (DACH, FR, ES, JA, custom) |
| 27 | `/blog-locale-audit` | Multilingual QA (completeness, hreflang, parity) |
| 28 | `/blog-multilingual` | Write + translate + localize + hreflang in one command |
| 29 | `/blog-calendar` | Editorial calendar generation with decay detection |
| 30 | `/blog-taxonomy` | CMS taxonomy management (WordPress, Ghost, Shopify, Strapi) |
| 31 | `/ogilvy-copywriting` | David Ogilvy advertising principles for persuasive copy |
| 32 | `/social-media-posts` | LinkedIn, Facebook, Instagram, Reddit posts |
| 33 | `/reddit-comments` | Domain-aware Reddit engagement |
| 34 | `/stop-slop` | Remove AI writing patterns from prose |

**Sub-agents** (spawned automatically by skills):

| Agent | Role |
|-------|------|
| `blog-writer` | Article drafting specialist |
| `blog-researcher` | Statistics, images, video discovery |
| `blog-reviewer` | 100-point quality scoring |
| `blog-seo` | On-page SEO validation |
| `blog-translator` | SEO-optimised translation |

---

## Prerequisites

- **Claude Code CLI** — latest version
- **Python 3.10+** — for shared runtime scripts
- **Node.js 20+** — required only if you use optional MCP servers

---

## Installation

### Method 1 — Shell script (recommended)

```bash
cd writing-skills-plugin
./install.sh
```

Installs to `~/.claude/` by default. Options:

```bash
./install.sh --project       # install into ./.claude/ (project-level)
./install.sh --dry-run       # preview without writing anything
./install.sh --force         # overwrite existing files without prompting
./install.sh --configure-mcp # print MCP configuration instructions
```

### Method 2 — Windows (PowerShell)

```powershell
.\install.ps1
# or with options:
.\install.ps1 -Project -DryRun -Force -ConfigureMcp
```

### Method 3 — ZIP upload (Claude Desktop)

Zip the entire `writing-skills-plugin/` directory and upload it via Claude Desktop → Settings → Plugins.

### Method 4 — npx (all clusters at once)

```bash
npx skills add Infrasity-Labs/dev-gtm-claude-skills
```

---

## Uninstall

```bash
./uninstall.sh
# or project-level:
./uninstall.sh --project
```

This removes all skills, agents, and scripts that were installed. It does **not** touch `settings.json`.

---

## Quick start

After installing and restarting Claude Code:

```
/blog write "10 best project management tools for remote teams"
/blog-rewrite path/to/existing-post.md
/blog-brief "email marketing automation"
/blog-analyze path/to/post.md
/blog-cluster "content marketing" --depth 5
/stop-slop path/to/draft.md
```

---

## Optional MCP Setup

Three optional MCP servers unlock advanced features. All skills degrade gracefully when they are absent.

### Gemini (audio + image generation)

Used by `/blog-audio` and `/blog-image`.

1. Get a key from [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Add to your environment: `export GOOGLE_AI_API_KEY=your_key`
3. Add to `~/.claude/settings.json` (copy from `.mcp.json` in this plugin):

```json
{
  "mcpServers": {
    "google-ai": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@google/generative-ai-mcp@latest"],
      "env": { "GOOGLE_AI_API_KEY": "your_key_here" }
    },
    "nanobanana-mcp": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "nanobanana-mcp@latest"],
      "env": { "GOOGLE_AI_API_KEY": "your_key_here" }
    }
  }
}
```

### Google APIs (Search Console + GA4)

Used by `/blog-google`.

Follow the setup guide in `skills/blog-google/references/auth-setup.md` to configure OAuth or a service account.

---

## How the delivery contract works

Every article produced by `/blog-write` or `/blog-rewrite` must pass 5 gates before delivery:

1. **Hero image** — generated or preserved
2. **Format completeness** — rendered to `.md`, `.html`, `.pdf`
3. **Content review** — score ≥ 90/100 + zero P0 issues
4. **Asset verification** — viewport test, link integrity
5. **Iteration cap** — max 3 loops; diagnostic shown on 3rd failure

---

## Updating

Re-run `./install.sh --force` from the plugin directory after pulling the latest repo changes. The `--force` flag skips per-file overwrite prompts.

---

## Project structure

```
writing-skills-plugin/
├── .claude-plugin/plugin.json   # Plugin manifest
├── .mcp.json                    # MCP server templates
├── install.sh                   # macOS/Linux installer
├── install.ps1                  # Windows installer
├── uninstall.sh                 # Teardown script
├── requirements.txt             # Python dependencies
├── agents/                      # 5 blog sub-agent files
├── scripts/                     # 9 shared runtime Python scripts
└── skills/                      # 34 skill directories (each with SKILL.md)
```
