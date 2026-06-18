# AGENTS.md — Claude Code Skills Library

This repo is a library of **Claude Code skills, agents, and extensions** — reusable AI-powered workflows for SEO, marketing, content, web design, and product management. Skills are invoked as slash commands inside Claude Code (e.g. `/seo-audit`, `/blog-write`, `/analytics`).

---

## Repo Structure

```
dev-gtm-claude-skills/
├── seo-skills/                  # SEO cluster (~35 skills + 8 extensions)
│   ├── seo/                     # Master SEO orchestrator
│   ├── seo-audit/               # Full site audit
│   ├── seo-cluster/             # Topic clustering
│   ├── ...                      # 30+ more SEO skills
│   └── extensions/              # MCP-backed extension plugins
│       ├── dataforseo/          # DataForSEO MCP (install.sh)
│       ├── ahrefs/              # Ahrefs MCP (install.sh)
│       ├── firecrawl/           # Firecrawl MCP (install.sh)
│       ├── bing-webmaster/      # Bing Webmaster MCP (install.sh)
│       ├── profound/            # Profound MCP (install.sh)
│       ├── seranking/           # SERanking MCP (install.sh)
│       ├── unlighthouse/        # Unlighthouse MCP (install.sh)
│       └── banana/              # Image generation MCP (install.sh)
│
├── writing-skills/              # Blog & content cluster (~35 skills)
│   ├── blog/                    # Master blog orchestrator
│   ├── blog-write/              # Full blog post writer
│   ├── blog-audit/              # Quality audit
│   └── ...
│
├── marketing-skills/            # Marketing cluster (~27 skills)
│   ├── analytics/               # GA4 / tracking setup
│   ├── ads/                     # Paid ads strategy
│   ├── competitor-profiling/    # Competitor research
│   ├── revops/                  # Revenue operations
│   └── ...
│
├── web-design/                  # Web design cluster (~4 skills)
│   ├── frontend-design/
│   ├── landing-page-auditor/
│   ├── site-architecture/
│   └── web-design-guidelines/
│
├── product-management-skills/   # PM cluster (~8 skills)
│   ├── product-manager-toolkit/ # Full PM toolkit (RICE, PRDs, interviews)
│   ├── agile-product-owner/     # Agile PO workflows
│   ├── prd-development/         # PRD creation
│   └── ...
│
├── skills/                      # Utility skills (~10 skills)
│   ├── docs-auditor/
│   ├── growth-report/
│   ├── orphan-pages-internal-linking-opportunities/
│   └── ...
│
├── .claude/                     # Claude Code runtime config (do not edit manually)
│   ├── settings.json            # MCP server config + permissions
│   ├── skills/                  # Installed skill copies (managed by install scripts)
│   ├── agents/                  # Installed agent copies (managed by install scripts)
│   └── extensions/              # Installed extension copies (managed by install scripts)
│
└── agents/                      # Source agent definitions
    ├── blog-researcher.md
    ├── blog-writer.md
    └── ...
```

---

## How Skills Work

Each skill lives in its own directory with a single `SKILL.md` file.

### SKILL.md Format

```markdown
---
name: skill-name
description: >
  One-paragraph description used for trigger matching. This is what Claude
  reads to decide when to invoke the skill. Be specific about trigger phrases.
user-invokable: true
argument-hint: "[url] [optional-flags]"
metadata:
  category: seo | blog | marketing | web-design | pm | utility
---

# Skill Title

Skill body — instructions, frameworks, prompts, and workflow steps.
```

**Key frontmatter fields:**
- `name` — must match the directory name exactly
- `description` — trigger-matching text; include all phrases that should activate this skill
- `user-invokable` — `true` means users can call it via `/skill-name`
- `argument-hint` — shown in autocomplete to guide input format
- `metadata.category` — used for grouping and discovery

---

## How Extensions Work

Extensions add MCP server integrations on top of base skills. Each extension ships with:

```
extensions/<name>/
├── install.sh       # Installs skill, agent, and MCP config into ~/.claude/
├── uninstall.sh     # Removes all installed files and MCP config
├── install.ps1      # Windows equivalent
├── uninstall.ps1
├── README.md        # Setup guide + usage examples
├── agents/          # Agent definition(s) for this extension
├── skills/          # Skill(s) this extension provides
└── docs/            # Setup documentation
```

### Installing an extension

```bash
# From the repository root
./seo-skills/extensions/dataforseo/install.sh    # prompts for API credentials
./seo-skills/extensions/ahrefs/install.sh
./seo-skills/extensions/firecrawl/install.sh
```

The install script:
1. Copies skill files into `~/.claude/skills/`
2. Copies agent files into `~/.claude/agents/`
3. Writes MCP server config into `~/.claude/settings.json`
4. Pre-warms the npm package

### Uninstalling

```bash
./seo-skills/extensions/dataforseo/uninstall.sh
```

---

## Adding a New Skill

1. Create a directory under the appropriate cluster:
   ```bash
   mkdir seo-skills/my-new-skill
   ```

2. Create `SKILL.md` using the format above.

3. Test it in Claude Code:
   ```
   /my-new-skill
   ```

4. If the skill needs an MCP server, create an extension under `extensions/` following the existing pattern (copy `extensions/dataforseo/` as a template).

---

## Runtime Requirements

| Requirement | Version | Used By |
|------------|---------|---------|
| Node.js | 20+ | All MCP-backed extensions |
| npx | ships with npm | Extension installers |
| Python | 3.10+ | SEO scripts, PM scripts, Writing analysis |
| Claude Code CLI | latest | Running all skills |

### Python packages (SEO cluster)

```bash
pip install -r seo-skills/requirements.txt
```

### Python packages (Writing cluster)

```bash
pip install -r writing-skills/requirements.txt
```

PM scripts (`rice_prioritizer.py`, `okr_cascade_generator.py`, `user_story_generator.py`) use stdlib only — no pip install needed.

---

## API Credentials by Cluster

| Cluster | Credentials Required |
|---------|---------------------|
| SEO | DataForSEO, Ahrefs, Firecrawl, Bing Webmaster, Profound, SERanking, Google Search Console (OAuth), Google Analytics 4 (OAuth) |
| Writing | Ahrefs, DataForSEO, Google Search Console (OAuth), Google Analytics 4 (OAuth), NotebookLM (Google account) |
| Marketing | GA4 (OAuth), GSC (OAuth), Ahrefs, DataForSEO, Firecrawl, Bing Webmaster, Apollo.io, Slack Bot token, Figma PAT |
| Web Design | Slack Bot token |
| Product Management | Figma PAT, Canva API key, Slack Bot token, Linear API key, Notion integration token, Jira API token |
| Utility | Ahrefs, DataForSEO, Apollo.io, Slack Bot token |

Credentials are set during `install.sh` — they are stored in `~/.claude/settings.json` under `mcpServers.env`, never committed to the repo.

---

## What NOT to Do

- **Do not edit `.claude/` files directly.** They are managed by install/uninstall scripts. Manual edits will be overwritten.
- **Do not commit `~/.claude/settings.json`.** It contains API credentials.
- **Do not rename skill directories** without updating the `name:` field in `SKILL.md` — they must match exactly.
- **Do not run `install.sh` from a different working directory** — scripts resolve paths relative to their location.
- **Do not modify extension skill files in `.claude/extensions/`** — edit the source files in `seo-skills/extensions/` and re-run the install script.

---

## Cluster Overview

| Cluster | Directory | Skills | Extensions |
|---------|-----------|--------|------------|
| SEO | `seo-skills/` | ~35 | 8 (DataForSEO, Ahrefs, Firecrawl, Bing, Profound, SERanking, Unlighthouse, Banana) |
| Writing / Blog | `writing-skills/` | ~35 | 0 (gsc-ga4, notebooklm planned) |
| Marketing | `marketing-skills/` | ~27 | 0 (gsc-ga4, slack, apollo, figma planned) |
| Web Design | `web-design/` | 4 | 0 (slack planned) |
| Product Management | `product-management-skills/` | 8 | 0 (figma, canva, slack, linear, notion, jira planned) |
| Utility | `skills/` | ~10 | 0 (apollo, slack planned) |
