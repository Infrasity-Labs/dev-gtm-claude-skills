# Brief Outline Generator

Turns a blog title and a focus keyword into a structured, formatted Word document — a **content outline** a writer can fill in. Not a finished article: section headings, short topic prompts, and FAQ questions, formatted and ready to hand to a writer.

<p align="center">
  <img
    src="../../assets/brief-outline-generator-ss.png"
    width="100%"
    alt="Brief Outline Generator output"
  />
</p>

<!-- Video demo -->
<!-- <video src="../../assets/brief-outline-generator-demo.mp4" width="100%" controls></video> -->

---

## What this skill does

You provide a title, a focus keyword, and a domain URL. The skill runs domain analysis to extract product context, fetches keyword volumes from DataForSEO, classifies the content archetype, selects the right section set, runs a 12-point quality check, and renders a `.docx` file with a metadata table, keyword volume block, and full outline.

Built for:
- **SEO and content teams** who want consistent outlines without writing them by hand
- **Developer marketing** producing technical content at scale
- **Agencies** delivering structured briefs to freelance writers

---

## Installation

### Claude Code (Recommended)

Clone the repo — the skill activates automatically when you open it in Claude Code:

```bash
git clone https://github.com/Infrasity-Labs/dev-gtm-claude-skills.git
cd dev-gtm-claude-skills
claude
```

Then trigger it with:

```
/dev-gtm brief-outline "How to Build Claude Skills"
```

Or describe what you want naturally — Claude activates the skill when you provide a title or keyword and ask for an outline or brief.

### Claude Web (Free / Pro)

1. Go to **[Settings → Capabilities](https://claude.ai/settings/capabilities)** and enable **Code execution and file creation**
2. Go to **[Customize → Skills](https://claude.ai/customize/skills)**
3. Click **+** → **Create skill** → **Upload a skill**
4. Zip this skill folder and upload it:

```bash
cd dev-gtm-claude-skills/skills
zip -r brief-outline-generator.zip brief-outline-generator/
```

Upload `brief-outline-generator.zip` and toggle it on.

---

## DataForSEO Setup (Required for keyword volumes)

This skill uses DataForSEO to fetch US monthly search volumes for the focus keyword and secondary keywords. Without it, volumes show as `N/A` but the outline still generates correctly.

### Claude Code

Open `.claude/settings.json` in the cloned repo and replace the placeholder credentials:

```json
{
  "mcpServers": {
    "dataforseo": {
      "command": "npx",
      "args": ["-y", "@dataforseo/mcp-server"],
      "env": {
        "DATAFORSEO_USERNAME": "your-dataforseo-username",
        "DATAFORSEO_PASSWORD": "your-dataforseo-password"
      }
    }
  }
}
```

### Claude Web (Free / Pro)

Go to **[Settings → Integrations](https://claude.ai/settings/integrations)**, find **DataForSEO**, and connect your account.

---

## How to use

```
Generate an outline for "How Do Platform Teams Implement Cloud Disaster Recovery"
```

```
Create a brief for the keyword: observability for platform teams
```

```
/dev-gtm brief-outline "API authentication best practices"
```

Claude asks for any missing required inputs before starting.

### Inputs

| Field | Required | Notes |
|-------|----------|-------|
| Title | ✅ | Blog post title |
| Focus keyword | ✅ | Primary SEO keyword |
| Domain URL | ✅ | Used to fetch product context |
| Word count range | ✅ | e.g. `1500-2000` |
| Target intent | ✅ | `Informational`, `Commercial`, `Transactional`, or `Navigational` |
| Target product | ⬜ | Optional. Adds a "How [Product] Helps with X" section |
| Secondary keywords | ⬜ | Optional. If omitted, the skill generates five |

<p align="center">
  <img
    src="../../assets/brief-outline-generator-gif.gif"
    width="100%"
    alt="Brief Outline Generator demo"
  />
</p>

---

## Output

A `.docx` file named `outline-{slug}.docx` containing:

**Metadata + keyword volume table** — title, URL slug, word count, target intent, target audience, focus keyword and secondary keywords with their US monthly search volumes.

**H1 title** — the full blog post title.

**Sections** — each heading prefixed with a `[H2]` or `[H3]` label so the writer can never misread the level. Bullets under each section are short topic prompts. Subsections are indented and styled consistently.

Saved to `/mnt/user-data/outputs/outline-{slug}.docx` (or your Downloads folder in Claude Code).

---

## Things to know

**Volume mismatch flag.** If your focus keyword has 10× less monthly search volume than any secondary keyword, the skill flags it before generating and asks whether you want to swap. You decide — it never auto-swaps.

**Domain fetch can fail.** Some sites (Cloudflare-protected, bot-blockers) return 403. The skill continues and skips product-specific context. The outline still generates correctly.

**DataForSEO is optional.** If credentials aren't configured, all volumes show as `N/A` and the skill warns you once. Everything else works.

---

## How it works

1. **Validate inputs** — checks all required fields are present and well-formed before any work starts
2. **Read section rules** — reads `references/section-rules.md` for the outline structure rules
3. **Domain analysis** — fetches the homepage and sitemap, extracts key product terms and context
4. **Keyword volumes** — calls DataForSEO for US monthly search volumes on the focus keyword and all secondaries
5. **Volume mismatch check** — flags and asks about swaps if the focus keyword is significantly lower volume than a secondary
6. **Build the outline** — assembles the section set based on detected archetype (`how_to`, `listicle`, `comparison`, `concept`)
7. **Quality check** — runs 12 checks on the assembled outline; revises and re-checks until all pass
8. **Render the `.docx`** — calls `scripts/generate-brief.py` to produce the formatted Word document

---

## Config schema reference

The JSON Claude assembles before calling the renderer:

```json
{
  "title": "How to Build Claude Skills",
  "focus_keyword": "building claude skills",
  "focus_keyword_volume": "30",
  "domain_url": "https://example.com/",
  "word_count_range": "1500-2000",
  "target_intent": "Informational",
  "target_product": "OptionalProductName",
  "archetype": "how_to",
  "secondary_keywords": [
    { "keyword": "Claude Code Skills", "volume": "3,400" }
  ],
  "output_path": "/path/to/outline.docx",
  "outline": [
    {
      "heading": "H2",
      "title": "Section Title",
      "rules": ["short topic prompt", "another prompt"],
      "subsections": []
    }
  ]
}
```

---

## File structure

```
brief-outline-generator/
├── SKILL.md                   # Skill instructions Claude follows
├── README.md                  # This file
├── references/
│   └── section-rules.md       # Outline rules, archetypes, per-section rules, examples
├── scripts/
│   ├── generate-brief.py      # DOCX renderer
│   └── domain-analyzer.py     # Domain fetcher and term extractor
└── examples/
    └── *.docx                 # Reference outlines
```
