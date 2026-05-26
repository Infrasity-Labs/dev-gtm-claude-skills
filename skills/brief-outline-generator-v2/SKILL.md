---
name: brief-outline-generator
description: >
  Generates a fully structured SEO content **outline** (not a finished brief) and exports it as a
  formatted .docx Word document. The output is a skeleton for a writer to fill in — section
  headings, topic prompts, angles — not pre-written paragraphs. Use this skill whenever a user
  provides a blog title, focus keyword, domain URL, or any combination of those and asks to
  generate an outline, brief, blog brief, SEO brief, article structure, or content plan. Also
  trigger when the user says "create a brief for X", "generate an outline for [topic]", "make a
  content brief", "I need a brief for [URL or keyword]", or pastes a title and asks what the
  structure should look like. This skill handles input validation, domain analysis, keyword
  enrichment, audience inference, archetype-aware section selection, and full .docx generation
  — always use it rather than writing ad-hoc outlines.
---

# Brief Outline Generator

Generates a content **outline** as a formatted `.docx` file. The output is a skeleton — section headings, short topic prompts, angles for each section — that a writer fills in with their own conclusions, numbers, and prose.

**This is an outline generator, not a brief generator.** If your output reads like an article in note form, you've gone too far. Read `references/section-rules.md` before generating anything.

**The DOCX is always produced by running `scripts/generate-brief.py`. Do not reimplement the renderer. Do not write inline docx code. Assemble the config JSON and run the script.**

---

## Inputs — collect from user before proceeding

| Field | Required | Notes |
|---|---|---|
| `title` | ✅ | Blog post title. Warn if > 70 chars. |
| `focus_keyword` | ✅ | Primary keyword |
| `sitemap_url` | ✅ | Full sitemap URL, e.g. `https://firefly.ai/sitemap.xml`. `domain_url` is derived from this automatically. |
| `word_count_range` | ✅ | e.g. `1500-2000` |
| `target_intent` | ✅ | `Informational`, `Commercial`, `Transactional`, or `Navigational` |
| `target_product` | ⬜ | Product name — triggers a product integration section if provided |
| `secondary_keywords` | ⬜ | Pre-supplied list; skip generation if provided |

---

## Execution workflow — follow these steps in order

### Step 1 — Validate inputs

- `title`: non-empty; warn (don't block) if > 70 chars
- `focus_keyword`: non-empty
- `sitemap_url`: non-empty, starts with `http://` or `https://` (accept any path — `.xml`, `.xml.gz`, or extensionless dynamic URLs are all valid)
- `word_count_range`: two positive integers separated by `-` (e.g. `1500-2000`)
- `target_intent`: one of `Informational`, `Commercial`, `Transactional`, `Navigational` (case-insensitive)

Derive two values from `sitemap_url`:
- `domain_url` — strip the path to get the origin, e.g. `https://firefly.ai/sitemap.xml` → `https://firefly.ai`. Used in the config JSON.
- `domain_hostname` — strip the protocol too, e.g. `https://firefly.ai` → `firefly.ai`. Used in tool calls that require a bare hostname (e.g. `site:firefly.ai`).

Stop and report all validation errors before proceeding.

---

### Step 2 — Read the rules

**Read `references/section-rules.md` in full now.** It contains:

- The outline-vs-brief distinction (the most important rule)
- Hard bullet rules (≤ 12 words, no invented numbers, no conclusions, no em-dash clauses)
- Hard structure rules (no `topic_summary`, no Writer Directives box, TLDR carries 2–3 topic pointers)
- The four archetypes (Listicle, Comparison, How-to, Concept/Explainer) and their section sets
- Per-section rules and good/bad bullet examples
- A final quality check to run before generating the DOCX

**Do not skip this step.** Generating without reading the rules produces brief-style output every time.

---

### Step 3 — Domain analysis

**DataForSEO tools are deferred — load them before calling.** Call `tool_search(query="on_page content parsing")` at the start of this step.

#### 3a — Discover site URLs

Call `web_fetch` on `sitemap_url`.

- **Readable XML** (response contains `<loc>` tags) → extract every `<loc>` URL. These are your site URLs.
- **Binary / compressed** (unreadable response) → fall back: call `dataforseo:serp_organic_live_advanced` with `keyword="site:{domain_hostname}"` (e.g. `site:firefly.ai`) to get all indexed URLs.

Cap at **20 URLs**. If more exist, prioritise: homepage → product/use-case pages → blog/resource pages.

#### 3b — Read full page content

For each URL from 3a, call `dataforseo:on_page_content_parsing` with `enable_javascript: true`.

This returns fully rendered page text — headings, body copy, product descriptions, etc. Collect all output.

If a page fails (bot protection, timeout), skip it and continue — do not abort.

#### 3c — Extract meta title and description

From the **homepage** content parsed in 3b, extract:
- Page `<title>` → `meta_title`
- `<meta name="description">` content → `meta_description`

Surface character count advisories if outside recommended ranges:
- `meta_title` outside 50–60 chars → *"Note: fetched meta title is N chars (recommended: 50–60)."*
- `meta_description` outside 150–160 chars → *"Note: fetched meta description is N chars (recommended: 150–160)."*

These are passed into the config as `meta_title` and `meta_description` and rendered in the metadata table.

#### 3d — Compile domain_context

From all parsed page content, extract and store:
- Product name and core value proposition
- Key technical terms and vocabulary used on the site
- Target audience signals (roles, team types, use cases mentioned)
- Existing content topics — used to avoid duplication in the outline

Store as `domain_context`. **Do not render `domain_context` in the output document.** If all fetches fail, set `domain_context = null` and continue.

---

### Step 4 — Classify the title's archetype

Based on the title pattern, pick one of:

- **Listicle / Tool Roundup** — "Top N", "Best X", "X Alternatives"
- **Comparison / Versus** — "X vs Y", "X or Y"
- **How-to / Implementation Guide** — "How to X", "How do X teams Y", "Implementing X"
- **Concept / Explainer** — "What is X", "Designing X", "[Function/Pattern]: Designing X"

If multiple seem to fit, use the defaults from `section-rules.md`. If still unclear, ask the user.

**Announce the chosen archetype to the user before generating** — one line, e.g. *"Detected archetype: How-to. Generating outline with intro → strategies → case studies → implementation → FAQs."* Let them override if they disagree.

---

### Step 5 — Generate keyword volumes

Fetch USA monthly search volumes for the focus keyword and each secondary keyword using DataForSEO.

**DataForSEO tools are deferred — load them before calling.**

1. Call `tool_search(query="keyword search volume google ads")` to load the DataForSEO keyword tools.
2. Call `dataforseo:kw_data_google_ads_search_volume` with the full list of keywords (focus + all secondaries) in a single call. Use `location_code` for the USA (`2840`).
3. From the response, extract the `search_volume` field for each keyword.
4. Format each volume as a thousands-separated string (e.g. `3400` → `"3,400"`). Volumes under 1,000 stay as plain digits (e.g. `"500"`, `"30"`). Volume of `0` should be rendered as `"0"`, not `"N/A"` — it's a real datapoint.
5. If a keyword returns no data, set its volume to `"N/A"` and continue. Don't abort the whole run.
6. If `tool_search` returns no DataForSEO tools (connector not installed), set every volume to `"N/A"` and surface a one-line warning: *"DataForSEO connector not available — keyword volumes set to N/A."*

**Never omit the volume field on any keyword.** Every row must have one.

**Flag volume mismatches.** If the focus keyword's volume is more than 10× smaller than any secondary keyword's volume, tell the user before generating: *"Note: your focus keyword has volume X, but secondary keyword Y has volume Z. Consider whether Y should be the focus."* Let them decide; don't auto-swap.

Store as:
```json
"focus_keyword_volume": "2,400",
"secondary_keywords": [
  { "keyword": "disaster recovery plan", "volume": "1,900" },
  { "keyword": "cloud DR strategy",      "volume": "N/A"   }
]
```

If no secondary keywords were supplied, generate 5 by combining base terms from the focus keyword, top domain key terms, and modifiers (`"best practices"`, `"guide"`, `"checklist"`, `"for teams"`, current year). Then fetch volumes for them the same way.

---

### Step 6 — Build the outline using the archetype's section set

Use the section set for the archetype you chose in Step 4. **Do not force every topic into a how-to template.** A listicle has no Problem or Case Studies section. A comparison has no Implementation steps.

**Each section object shape:**
```json
{
  "heading": "H2",
  "title": "Section Title",
  "rules": ["short topic prompt 1", "short topic prompt 2"],
  "subsections": [
    {
      "heading": "H3",
      "title": "Subsection Title",
      "rules": ["..."],
      "subsections": []
    }
  ]
}
```

**Fields removed from the previous schema (do not use):**
- ~~`topic_summary`~~ — removed. Outlines don't have abstracts.
- ~~`directives`~~ — removed. The bullets themselves carry the direction.
- ~~`visual`~~ — removed. If a visual matters, write it as a bullet prompt: *"Include a comparison table: dimension × tool"*.
- ~~`faqs`~~ — removed. FAQs are questions only (in `rules`); the writer drafts answers.

**Bullets in `rules` follow the hard rules in `section-rules.md`:**
- ≤ 12 words each
- Must be specific and a complete thought
- No invented numbers
- No conclusions — topic prompts only
- No em-dash explanatory clauses

**Length follows substance, not a fixed cap.** Use as many bullets as the section honestly needs — 2 if 2, 9 if 9. The "typical ranges" in `section-rules.md` are orientation, not limits. Padding to hit a target number is wrong; truncating to hit one is also wrong.

**TLDR section:** include a TLDR heading with **2–3 short topic pointers** (each ≤ 12 words) that name what the writer should cover in the TLDR. Pointers are topics, not finished takeaways. Pull from the article's central tension, the main shift the reader should make, and the practical next step. See the TLDR section in `references/section-rules.md` for good/bad examples.

**FAQs section:** Use the `rules` field with a list of question strings — questions only, no answers. The writer drafts the actual answers. Each question is one bullet. Focus on **how questions are framed**: concrete and action-oriented (`"How do I install a Claude skill?"`), not abstract (`"How does Claude decide which skill to invoke?"`). All user-supplied keywords (focus + each secondary) must appear naturally across the question set — paraphrased into something a real searcher would type, never keyword-stuffed. Typically 5–8 questions but no fixed cap. See the FAQs section in `section-rules.md` for examples.

---

### Step 7 — Run the final quality check

Before assembling the config, walk the outline and verify (this is from `section-rules.md`):

1. Could a writer publish this by adding transition words? → If yes, strip back.
2. Does every bullet read as a topic prompt, not a sentence? (except FAQ questions, which are naturally full sentences) → If no, rewrite.
3. Could a writer guess each bullet's meaning in 3 different ways? → If yes, the bullet is too abstract. Name the actual thing (files, components, technical terms).
4. Is every bullet a complete thought when read aloud? → If a bullet is a sentence fragment with no meaning ("Who this is for: builders doing X"), finish the thought.
5. Is every technical claim accurate? → Skills are packages not folders; Claude reads SKILL.md, not the whole skill eagerly. If unsure, rewrite to avoid the claim.
6. Any invented numbers? → Remove.
7. Any sub-bullet that feels like its own H2? → Promote it.
8. Are H2 titles specific to the article's topic (not generic verb phrases)? → "Define the task narrowly" → "Define what your skill should do."
9. Section order matches the archetype? → Verify.
10. No `topic_summary`, `directives`, or `faqs` fields present? → Strip if present. FAQ questions live in `rules` as flat bullets.
11. Do all user-supplied keywords (focus + each secondary) appear naturally across the FAQ questions? → If any is missing, rewrite a question to incorporate it.
12. Are FAQ questions concrete and action-oriented (`"How do I install..."`, `"What is the difference between..."`), not abstract (`"How does Claude decide..."`)? → Rewrite vague ones.

If all 12 pass, proceed.

---

### Step 8 — Assemble the config JSON

Write the complete config to `/home/claude/brief-config.json`:

```json
{
  "title": "...",
  "focus_keyword": "...",
  "focus_keyword_volume": "N/A",
  "domain_url": "...",
  "word_count_range": "...",
  "target_intent": "...",
  "target_product": "...",
  "archetype": "how_to",
  "meta_title": "...",
  "meta_description": "...",
  "secondary_keywords": [
    { "keyword": "...", "volume": "N/A" }
  ],
  "output_path": "/mnt/user-data/outputs/outline-{file_slug}.docx",
  "outline": [ ... ]
}
```

**Slug note:** Two slugs are generated internally:
- **URL Slug** (shown in the metadata table) — derived from `focus_keyword`, e.g. `"cloud disaster recovery"` → `cloud-disaster-recovery`.
- **File slug** (used in the filename) — derived from `title`, e.g. `"How Do Platform Teams Implement Cloud Disaster Recovery"` → `outline-how-do-platform-teams-implement-cloud-disaster-recovery.docx`.

The `output_path` in the config should reflect the title-based file slug.

**Do not include `domain_context` in the config.** It informs generation upstream; it never appears in the rendered doc.

---

### Step 9 — Run the generator script

```bash
python /path/to/skill/scripts/generate-brief.py --config /home/claude/brief-config.json
```

The script handles all DOCX rendering. Do not write any docx code yourself.

If the script exits non-zero, report the error from stdout/stderr and show the outline as plain text as a fallback.

---

### Step 10 — Present the file

Call `present_files` with the output path. Report:
```
✅ Outline generated: outline-{file_slug}.docx
   Archetype:     {archetype}
   Slug (URL):    {url_slug}  (from focus keyword)
   Slug (file):   {file_slug}  (from title)
   Audience:      {audience}
   Focus KW:      {focus_keyword} ({volume})
   Secondary KWs: {kw} ({vol}), ...
   Sections:      {N} sections
```

---

## What the script renders (reference only — do not reimplement)

The script produces a `.docx` with:

1. **Metadata + keyword table** — 3 columns: Field | Value | USA Search Volume. Standard rows (Title, URL Slug, Word Count, Target Intent, Target Audience, Meta Title (50-60 chars), Meta Description (150-160 chars)) span cols 2+3. **URL Slug is derived from `focus_keyword`, not the title.** Focus keyword and each secondary keyword get their own row with volume in col 3 (amber background). **Domain and Domain Context rows are NOT included in the table.**
2. **H1 title**
3. **Sections** — each `heading` field renders as `[H2]` or `[H3]` grey label prefix + heading text. `rules` render as bullet points. **No `topic_summary` block, no Writer Directives box** — those have been removed from the format.

---

## Reference files

- `references/section-rules.md` — Outline-first rules, archetypes, per-section rules, good/bad examples. **Read in Step 2 before doing anything else.**
- `scripts/generate-brief.py` — The DOCX renderer. Always run this. Never reimplement it.
- `examples/` — Canonical good outlines, for **reference only**. Read these to calibrate bullet length, density, and tone — *not* to copy section structure, headings, or topics. The archetype rules in `references/section-rules.md` decide structure for the current topic. Never use an example outline as a template for the user's outline, even if the topic looks similar.