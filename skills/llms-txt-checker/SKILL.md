---
name: llms-txt-checker
description: >
  Checks whether a documentation site properly surfaces llms.txt and llms-full.txt for AI agents.
  Use this skill whenever a user provides a URL and wants to know if llms.txt or llms-full.txt is
  available, discoverable, or properly structured. Trigger on phrases like "check llms.txt for",
  "does this site have llms.txt", "find llms.txt", "check llms for this url", "audit llms.txt",
  "is llms-full.txt available", or any time a user shares a docs URL and wants AI-readiness checked.
  Also trigger when the user wants to verify GEO/AEO readiness of a documentation site.
---

# LLMs.txt Checker Skill

Check whether a given documentation URL properly surfaces `llms.txt` and `llms-full.txt` for AI agents, then audit the content for structural completeness.

---

## How it works

The core insight (learned from real behavior): Claude's fetch tool only allows fetching URLs that have either been **directly provided by the user** or have **appeared in a prior fetch/search result**. This means:

- `llms.txt` must be discoverable from the provided URL (linked in page content, footer, `.md` response, or page metadata)
- `llms-full.txt` must be discoverable from either the page OR from within `llms.txt` itself
- If neither surfaces organically, Claude cannot fetch them — and that itself is the finding

---

## Step-by-Step Workflow

### Step 1: Fetch the provided URL

Fetch the user-provided URL with `html_extraction_method: markdown`. Look for any of the following signals that surface `llms.txt`:

- Direct link in footer (e.g. `LLM usage: llms.txt`)
- Blockquote or banner at top of page (e.g. `Fetch the complete documentation index at: https://...llms.txt`)
- `<meta>` tags or HTTP headers referencing llms.txt
- `.md` version of the page (try appending `.md` to the URL) — Mintlify and some other platforms serve a markdown version that includes the llms.txt pointer in a blockquote at the top
- Sitemap or robots.txt link (only if URL surfaces organically)

**If the fetch is blocked by robots.txt**: Note this clearly — it means the site is actively disallowing crawlers, which is itself a GEO/AEO red flag. Tell the user.

---

### Step 2: Determine what surfaced

**Case A — Both `llms.txt` AND `llms-full.txt` surfaced**
- Fetch both files completely
- Proceed to the Audit Checklist (Step 3)

**Case B — Only `llms.txt` surfaced**
- Fetch `llms.txt` completely
- Scan its content for any mention of `llms-full.txt` (look in "Documentation Sets", links, or any section listing companion files)
- If found → fetch `llms-full.txt` and proceed to the Audit Checklist (Step 3)
- If not found → report that `llms-full.txt` is not referenced anywhere, and proceed to audit `llms.txt` alone

**Case C — Neither surfaced**
- Do not attempt to guess or construct the URL
- Report clearly to the user (see Response Templates section below)

---

### Step 3: Audit the files

#### `llms.txt` Audit

Check for the following. Mark each ✅ or ❌:

**Structure**
- [ ] Starts with a single `# H1` title (site/product name)
- [ ] Has a `> blockquote` summary immediately below H1 (1–2 sentence description)
- [ ] Uses `## H2` sections to group links (e.g. Docs, API Reference, Guides, OpenAPI Specs)
- [ ] Each link follows format: `- [Page Title](https://absolute-url): brief description`
- [ ] Has an `## Optional` section for secondary/non-essential content (not required but best practice)
- [ ] No nested headings inside H2 link sections
- [ ] No images, HTML, or tables (plain markdown only)

**Content completeness**
- [ ] Core product/feature pages are listed
- [ ] API reference pages are included (if applicable)
- [ ] Getting started / quickstart pages included
- [ ] SDK/integration guides included (if applicable)
- [ ] Link descriptions are meaningful (not just page titles repeated)
- [ ] All links use absolute URLs (not relative paths)
- [ ] No broken or 404 links visible

**AI-readiness signals**
- [ ] References `llms-full.txt` (either directly or in a Documentation Sets section)
- [ ] Segmented sets for different use cases (advanced but excellent — e.g. Scalekit's topic-specific .txt files)

#### `llms-full.txt` Audit (if available)

- [ ] File exists and is non-empty
- [ ] Contains full page content (not just links)
- [ ] Has clear document boundary markers between pages (e.g. `---` or `# DOCUMENT BOUNDARY`)
- [ ] Each section has a `Source:` URL reference
- [ ] Content is clean markdown (no raw HTML, no JS artifacts)
- [ ] Reasonably sized (warn if extremely large — may exceed LLM context windows)

#### `robots.txt` Signal (check opportunistically)

If robots.txt was surfaced during the process:
- [ ] `User-agent: *` with `Allow: /` — all bots permitted
- [ ] `ai-input=yes` — explicitly permits AI agents to use content
- [ ] `ai-train=no` — training blocked (common and acceptable)
- [ ] Any `Disallow` rules that would block AI crawlers

---

### Step 4: Deliver the report

Structure the output as:

```
## LLMs.txt Audit: [domain]

### Discovery
[What was found and how it was surfaced]

### llms.txt — ✅ Found / ❌ Not Found
[Audit results with ✅/❌ per checklist item]
[Notable strengths]
[Issues found]

### llms-full.txt — ✅ Found / ❌ Not Found / ⚠️ Not Referenced
[Audit results or explanation]

### robots.txt Signal
[If available — what it says about AI access]

### Summary & Recommendations
[3–5 actionable bullets]
```

---

## Response Templates

### Neither llms.txt nor llms-full.txt surfaced

> Neither `llms.txt` nor `llms-full.txt` was discoverable from the provided URL.
>
> This means AI agents and LLMs browsing your docs will have no structured index to work from — they'll need to crawl individual pages or guess at your content structure.
>
> **To fix this**, surface the `llms.txt` URL somewhere Claude (and other AI tools) can see it when fetching your page. Good options:
> - Add it to your page footer (e.g. `LLM usage: /llms.txt`)
> - Include it in a blockquote at the top of your docs homepage or `.md` page version (e.g. `> Documentation index available at: https://yourdomain.com/llms.txt`)
> - Reference it in your `robots.txt` or a `<meta>` tag
>
> Once it's linked from a page that AI agents naturally land on, it becomes discoverable automatically.

### llms.txt found but llms-full.txt not referenced

> `llms.txt` was found and audited. However, `llms-full.txt` was not referenced anywhere in the file.
>
> `llms-full.txt` is the companion file containing the **full content** of all documentation pages in a single file — useful for AI coding assistants (Cursor, Claude Code, Copilot) that need deep context without fetching dozens of individual pages.
>
> **To add it**: Reference it in your `llms.txt` under a `## Documentation Sets` section or similar, like:
> ```
> - [Complete documentation](https://yourdomain.com/llms-full.txt): full content of all pages
> ```
> If you're on Mintlify, it's auto-generated — just make sure it's linked.

---

## Key facts to keep in mind

- **Mintlify** auto-generates both `llms.txt` and `llms-full.txt` for all projects, and adds HTTP headers (`Link: </llms.txt>; rel="llms-txt"`) for discovery
- **Fern** also auto-generates both files
- **Starlight** (Astro) does not auto-generate — must be added manually
- **GitBook** auto-generates `llms.txt`
- The `llms.txt` standard was proposed by Jeremy Howard (fast.ai) in September 2024
- `llms-full.txt` is not part of the original spec but has become widely adopted as the companion file
- No major AI crawler has *officially* committed to following these files, but Cursor, Claude Code, and similar tools actively use them