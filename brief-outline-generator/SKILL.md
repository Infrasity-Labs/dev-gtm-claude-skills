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
| `domain_url` | ✅ | Client site, e.g. `https://firefly.ai` |
| `word_count_range` | ✅ | e.g. `1500-2000` |
| `target_intent` | ✅ | `Informational`, `Commercial`, `Transactional`, or `Navigational` |
| `target_product` | ⬜ | Product name — triggers a product integration section if provided |
| `secondary_keywords` | ⬜ | Pre-supplied list; skip generation if provided |

---

## Execution workflow — follow these steps in order

### Step 1 — Validate inputs

- `title`: non-empty; warn (don't block) if > 70 chars
- `focus_keyword`: non-empty
- `domain_url`: non-empty, starts with `http://` or `https://`
- `word_count_range`: two positive integers separated by `-` (e.g. `1500-2000`)
- `target_intent`: one of `Informational`, `Commercial`, `Transactional`, `Navigational` (case-insensitive)

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

### Step 3 — Run domain analysis

```bash
python /path/to/skill/scripts/domain-analyzer.py --url {domain_url}
```

Parse the JSON output. Use `domain_context` to inform generation (product name, key terms, audience). **Do not render `domain_context` in the output document.** If the script fails or returns `success: false`, set `domain_context` to `null` and continue.

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

Fetch USA monthly search volumes for the focus keyword and each secondary keyword from Ahrefs.

**Critical: Ahrefs tools are deferred — you must load them before calling them.**

1. Call `tool_search(query="keyword search volume Ahrefs")` to load the Ahrefs keyword tools. Do NOT skip this step. The tools won't appear in your tool list until you load them.
2. For each keyword (focus + secondaries), call `Ahrefs:keywords-explorer-volume-by-country` with `keyword=<the keyword>` and `limit=1`. The response contains a `countries` array; take the `volume` field where `country == "us"`.
3. Format each volume as a thousands-separated string (e.g. `3400` → `"3,400"`). Volumes under 1,000 stay as plain digits (e.g. `"500"`, `"30"`). Volume of `0` should be rendered as `"0"`, not `"N/A"` — it's a real datapoint.
4. If a specific keyword call fails or returns no data, set that keyword's volume to `"N/A"` and continue. Don't abort the whole run.
5. If `tool_search` returns no Ahrefs tools at all (the connector isn't installed in this session), set every volume to `"N/A"` and surface a one-line warning to the user: *"Ahrefs connector not available — keyword volumes set to N/A."*

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

**Bullets in `rules` follow the hard rules in `section-rules.md`:**
- ≤ 12 words each
- No invented numbers
- No conclusions — topic prompts only
- No em-dash explanatory clauses

**TLDR section:** include a TLDR heading with **2–3 short topic pointers** (each ≤ 12 words) that name what the writer should cover in the TLDR. Pointers are topics, not finished takeaways. Pull from the article's central tension, the main shift the reader should make, and the practical next step. See the TLDR section in `references/section-rules.md` for good/bad examples.

---

### Step 7 — Run the final quality check

Before assembling the config, walk the outline and verify (this is from `section-rules.md`):

1. Could a writer publish this by adding transition words? → If yes, strip back.
2. Does every bullet read as a topic prompt, not a sentence? → If no, rewrite.
3. Any invented numbers? → Remove.
4. Section order matches the archetype? → Verify.
5. H2 titles are plain and descriptive (not clever hooks)? → Verify.
6. No `topic_summary` or `directives` fields present? → Strip if present.

If all 6 pass, proceed.

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
  "secondary_keywords": [
    { "keyword": "...", "volume": "N/A" }
  ],
  "output_path": "/mnt/user-data/outputs/outline-{slug}.docx",
  "outline": [ ... ]
}
```

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
✅ Outline generated: outline-{slug}.docx
   Archetype:     {archetype}
   Slug:          {slug}
   Audience:      {audience}
   Focus KW:      {focus_keyword} ({volume})
   Secondary KWs: {kw} ({vol}), ...
   Sections:      {N} sections
```

---

## What the script renders (reference only — do not reimplement)

The script produces a `.docx` with:

1. **Metadata + keyword table** — 3 columns: Field | Value | USA Search Volume. Standard rows (Title, URL Slug, Word Count, Target Intent, Target Audience) span cols 2+3. Focus keyword and each secondary keyword get their own row with volume in col 3 (amber background). **Domain and Domain Context rows are NOT included in the table.**
2. **H1 title**
3. **Sections** — each `heading` field renders as `[H2]` or `[H3]` grey label prefix + heading text. `rules` render as bullet points. **No `topic_summary` block, no Writer Directives box** — those have been removed from the format.

---

## Reference files

- `references/section-rules.md` — Outline-first rules, archetypes, per-section rules, good/bad examples. **Read in Step 2 before doing anything else.**
- `scripts/generate-brief.py` — The DOCX renderer. Always run this. Never reimplement it.
- `scripts/domain-analyzer.py` — Domain fetcher. Run in Step 3.
- `examples/` — Canonical good outlines, for **reference only**. Read these to calibrate bullet length, density, and tone — *not* to copy section structure, headings, or topics. The archetype rules in `references/section-rules.md` decide structure for the current topic. Never use an example outline as a template for the user's outline, even if the topic looks similar.
