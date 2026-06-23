# marketing-skills-plugin

28 marketing skills for Claude Code — paid ads, analytics, CRO, copywriting, email sequences, competitor research, SEO, and more.

---

## What's included

| # | Skill | What it does |
|---|-------|-------------|
| 1 | `/ab-testing` | Plan, design, and analyse A/B tests and experiments |
| 2 | `/ad-creative` | Generate and scale ad copy across Google, Meta, LinkedIn |
| 3 | `/ads` | Paid advertising strategy (Google Ads, Meta, LinkedIn, TikTok) |
| 4 | `/ai-seo` | Optimise content to get cited by LLMs and AI search engines |
| 5 | `/analytics` | Set up, audit, and improve analytics tracking and GA4 |
| 6 | `/churn-prevention` | Reduce churn with cancellation flows and save offers |
| 7 | `/cold-email` | Write B2B cold email and follow-up sequences that get replies |
| 8 | `/community-marketing` | Build and leverage online communities for product growth |
| 9 | `/competitor-profiling` | Research and profile competitors from their URLs |
| 10 | `/competitors` | Create competitor comparison and alternative pages for SEO |
| 11 | `/content-strategy` | Plan content strategy and decide what to create and prioritise |
| 12 | `/copywriting` | Write and improve marketing copy for any page or format |
| 13 | `/cro` | Optimise conversions on landing pages, funnels, and flows |
| 14 | `/customer-research` | Conduct, analyse, and synthesise customer research |
| 15 | `/emails` | Create and optimise email sequences, drip campaigns, and automations |
| 16 | `/free-tools` | Plan, evaluate, and build free tools for marketing purposes |
| 17 | `/launch` | Plan a product launch, feature announcement, or release strategy |
| 18 | `/lead-magnets` | Create and optimise lead magnets for email capture |
| 19 | `/marketing-ideas` | Generate marketing ideas and strategies for SaaS and startups |
| 20 | `/onboarding` | Optimise post-signup onboarding and user activation flows |
| 21 | `/pricing` | Pricing decisions, packaging strategy, and monetisation |
| 22 | `/programmatic-seo` | Create SEO-driven pages at scale using templates and data |
| 23 | `/referrals` | Create and optimise referral programs and affiliate systems |
| 24 | `/revops` | Revenue operations, lead lifecycle management, and CRM setup |
| 25 | `/sales-enablement` | Create sales collateral, pitch decks, and objection-handling guides |
| 26 | `/schema` | Add, fix, and optimise schema markup and structured data |
| 27 | `/seo-audit` | Audit and diagnose SEO issues on any site |
| 28 | `/social` | Create, schedule, and optimise social media content |

---

## Prerequisites

- **Claude Code CLI** — latest version
- **Node.js 20+** — required only if you use optional MCP servers

No Python dependencies for this plugin.

---

## Installation

### Method 1 — Shell script (recommended)

```bash
cd plugins/marketing-skills
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

Zip the entire `plugins/marketing-skills/` directory and upload it via Claude Desktop → Settings → Plugins.

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

Does **not** touch `settings.json` — remove MCP entries manually if needed.

---

## Quick start

After installing and restarting Claude Code:

```
/ads "Google Ads campaign for a B2B SaaS tool targeting HR managers"
/copywriting "rewrite our pricing page to increase conversions"
/analytics "set up GA4 for an e-commerce store"
/cro "audit our checkout flow for conversion issues"
/cold-email "outreach sequence for a devtools product targeting CTOs"
```

---

## Optional MCP Setup

Five optional MCP servers unlock live data integrations. All skills work without them.

| Server | Skills it unlocks | Credential needed |
|--------|------------------|-------------------|
| `dataforseo` | `/seo-audit`, `/programmatic-seo`, `/ai-seo` | `DATAFORSEO_USERNAME` + `DATAFORSEO_PASSWORD` |
| `apollo.io` | `/cold-email`, `/sales-enablement`, `/revops` | `APOLLO_API_KEY` |
| `slack` | `/community-marketing`, `/launch`, `/social` | `SLACK_BOT_TOKEN` + `SLACK_TEAM_ID` |
| `firecrawl` | `/competitor-profiling`, `/competitors`, `/content-strategy` | `FIRECRAWL_API_KEY` |
| `google-analytics` | `/analytics`, `/cro` | Google OAuth |

Add to `~/.claude/settings.json` (copy templates from `.mcp.json` and fill in your credentials):

```json
{
  "mcpServers": {
    "dataforseo": {
      "type": "http",
      "url": "https://YOUR_USERNAME:YOUR_PASSWORD@mcp.dataforseo.com/http"
    }
  }
}
```

---

## Updating

Re-run `./install.sh --force` after pulling the latest repo changes.

---

## Project structure

```
plugins/marketing-skills/
├── .claude-plugin/plugin.json   # Plugin manifest
├── .mcp.json                    # MCP server templates
├── install.sh                   # macOS/Linux installer
├── install.ps1                  # Windows installer
├── uninstall.sh                 # Teardown script
└── skills/                      # 28 skill directories (each with SKILL.md)
```
