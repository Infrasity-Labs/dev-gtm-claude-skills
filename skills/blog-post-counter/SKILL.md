---
name: blog-post-counter
description: >
  Finds the blog page URL and counts the total number of unique blog posts for any company.
  Use this skill whenever a user provides a company name, domain, sitemap URL, or asks to find
  their blog, count blog posts, check how many articles they've published, or audit their
  content output. Also trigger when the user says things like "how many blogs does X have",
  "find the blog for X", "check X's content volume", or provides a list of company names
  and wants blog data for each. ALSO trigger when the user provides a target domain AND one
  or more competitor domains and wants a comparison of blog post counts — phrases like
  "compare my blog with competitors", "how do I stack up against X", "benchmark my content
  vs Y and Z", or "target domain vs competitor" all indicate competitor comparison mode.
  Works from a company name alone — no URL required.
  Always use this skill instead of manual searching when blog discovery + counting is the goal.
compatibility: >
  Core workflow (Steps 3a–3b) requires only web_fetch and web_search — compatible with
  Claude Desktop and Claude Code. Step 3c (DataForSEO fallback) additionally requires the
  dataforseo MCP server. Do NOT use Bash/curl — it is unavailable on Claude Desktop and
  blocked by many hosts even on Claude Code.
---

# Blog Post Counter Skill

Given a sitemap URL (or a domain/company name), count the total number of unique blog posts published by the company.

Supports two modes:
- **Single mode** — count posts for one domain
- **Competitor comparison mode** — count posts for a target domain AND one or more competitor domains, then present a ranked comparison with insights

---

## Workflow

### Step 1 — Detect mode

- If the user provides **one domain/company** → run Single mode (Steps 2–4, then Single Output).
- If the user provides **a target domain + one or more competitor domains** → run Competitor Comparison mode: execute Steps 2–4 **for each domain** (target first, then competitors), then produce the Comparison Output.

---

### Step 2 — Resolve the sitemap URL (per domain)

- If the user provides a **sitemap URL** directly → attempt to parse it in Step 3a. If the response is binary or unreadable, fall back to Step 3b (listing page scraping) — do not stop.
- If the user provides only a **domain or company name** → try these sitemap paths in order using `web_fetch`, stopping as soon as one returns readable XML:
  1. `https://<domain>/sitemap.xml`
  2. `https://<domain>/sitemap_index.xml` ← underscore
  3. `https://<domain>/sitemap-index.xml` ← hyphen (common in Ghost, WordPress Yoast)
  4. `https://www.<domain>/sitemap.xml`
  5. `https://www.<domain>/sitemap_index.xml`
  6. `https://www.<domain>/sitemap-index.xml`

  Once readable XML is found, check what type it is before proceeding:
  - **Flat sitemap** (contains <url> / <loc> entries directly) → parse it in Step 3a as-is. No child fetching needed.
  - **Sitemap index** (contains <sitemap> entries pointing to child sitemaps) → fetch every child sitemap in Step 3a and union all <loc> URLs.
  - If none of the 6 paths return readable XML → fall back to Step 3b (listing page scraping).

---

### Step 3 — Extract all blog URLs (per domain)

Work through all three sources below. Do not stop after the first one succeeds — run all that are available and take the highest count. The sitemap is the authoritative source; DataForSEO is a reliable independent cross-check.

#### 3a. Parse the sitemap via web_fetch (PRIMARY — always attempt first)

The sitemap is the ground truth — it lists every URL the site explicitly publishes.

1. `web_fetch` the sitemap URL with this exact prompt:
   > "This is a sitemap XML file. List only the URLs from `<loc>` tags whose path contains any of these segments: `/blog/`, `/engineering/`, `/technical-writing/`, `/developer-marketing/`, `/technical-documentation/`, `/technical-content/`, `/developer-community/`, `/insights/`, `/articles/`, `/resources/`, `/posts/`, `/academy/`, `/learn/`, `/tutorials/`, `/guides/`, `/knowledge-base/`. Output only the matching URLs, one per line. Do not include homepage, service pages, or any other URLs. Do not summarize or truncate."

   Asking only for blog-path URLs (not all 300+ URLs in the sitemap) keeps the response small and prevents summarization.

2. **Sitemap index** (contains `<sitemap>` child entries): first fetch the index with prompt "List every child sitemap URL from the sitemap loc tags. Output only the URLs, one per line." — this returns a small list of 3–10 URLs. Then fetch **every child sitemap** individually with the blog-path prompt above. Never skip a child — blog posts may live in `sitemap-blogs.xml`, `post-sitemap.xml`, `sitemap-posts.xml`, or any other name.

3. **If a sitemap path returns binary/gzip/404** → try the next variant from Step 2 immediately. Only mark sitemap as failed after all 6 variants are exhausted.

#### 3b. Scrape the blog listing page via web_fetch (SECONDARY — run in parallel with 3a when possible)

Useful for sites where the sitemap is fully gzip-compressed. Only works for server-rendered listing pages (not JS-rendered ones).

1. `web_fetch` `https://<domain>/blog` with prompt: "List every blog post URL linked on this page. Output only the full URLs, one per line, no descriptions."
2. Paginate (`/blog/page/2`, `/blog?page=2`, etc.) until no new URLs appear.
3. Try alternate paths: `/insights`, `/articles`, `/resources`, `/posts`.

If the page returns no links or only navigation links, it is JS-rendered — skip further pagination attempts.

#### 3c. DataForSEO `relevant_pages` (ALWAYS run this as a cross-check when DataForSEO is available)

Do not treat this as a last resort — run it alongside 3a and 3b whenever DataForSEO is configured. It independently reflects DataForSEO's crawl of the domain and catches posts missed by gzip sitemaps or JS-rendered listing pages.

Call `dataforseo_labs_google_relevant_pages` with:
```
target:          <domain>
location_name:   United States
language_code:   en
order_by:        ["metrics.organic.etv,desc"]
limit:           500
ignore_synonyms: false
```

Filter returned pages to blog-path URLs (Step 4 patterns). Deduplicate by stripping trailing slashes. Take this count as the floor — the sitemap count (if available) is more complete.

**Final count rule:** Use the highest count across all sources that successfully returned data. If the sitemap returned 137 and DataForSEO returned 112, report 137 (sitemap). If only DataForSEO succeeded, report that count and note it may undercount.

---

### Step 4 — Filter to blog post URLs only (per domain)

From the full URL list, keep only those matching:

**Path patterns** (with at least one slug segment after the prefix):
- `/blog/<slug>` ✓ — `/blog` or `/blog/` alone ✗
- `/blog-posts/<slug>`
- `/insights/<slug>`
- `/resources/<slug>`
- `/articles/<slug>`
- `/news/<slug>`
- `/posts/<slug>`
- `/learn/<slug>`
- `/academy/<slug>`
- `/tutorials/<slug>`
- `/guides/<slug>`
- `/knowledge-base/<slug>`

**Subdomain patterns**: `blog.`, `academy.`, `learn.`, `resources.`, `insights.` as subdomain prefix.

**Exclude** (deduplicate after filtering):

| Exclude | Reason |
|---------|--------|
| Listing / index pages (e.g. `/blog`, `/blog/`) | Not a post |
| Pagination (e.g. `/blog?page=2`, `/blog/page/3`) | Not a post |
| Query-param duplicates (`?ref=`, `?utm_source=`) | Duplicate |
| RSS / Atom feeds (`/blog/feed`, `/blog/rss.xml`) | Not a post |
| Category / tag / author archives (`/blog/category/`, `/blog/tag/`, `/blog/author/`) | Not a post |

Count what remains — these are unique blog posts.

---

## Output Format

### Single Mode

```
Company:        <Company Name>
Blog URL:       <https://domain.com/blog/>
Unique posts:   <N>
Source:         <sitemap | blog page scrape | search index (may undercount)>
```

If the blog section cannot be identified:
```
Company:        <Company Name>
Blog URL:       Not found
Unique posts:   —
```

---

### Competitor Comparison Mode

After processing all domains, present:

**1. Ranked comparison table** — sorted by unique post count descending, target domain bolded and labeled *(you)*:

| Rank | Company | Blog URL | Unique Posts | vs Target |
|------|---------|----------|-------------|-----------|
| 1 | CompetitorA | /blog | 210 | +141 |
| 2 | **YourCompany** *(you)* | /blog | 69 | — |
| 3 | CompetitorB | /blog | 45 | −24 |

- **vs Target**: `+N` = competitor has more posts; `−N` = competitor has fewer. Blank for target row.
- If a blog is not found, show `—` for both count and vs Target.

**2. Content gap summary** (2–4 sentences) — plain-language insight: where the target stands, size of the gap, and what it implies for content investment.

---

## Batch Mode (single mode only)

If the user provides multiple domains/companies **without** designating target vs competitors, process sequentially and return:

| Company | Blog URL | Unique Posts |
|---------|----------|-------------|
| ...     | ...      | ...         |

---

## Notes

- **Do not use Bash or curl** — unavailable on Claude Desktop, and many hosts return 403 to curl's user-agent even on Claude Code. The entire workflow uses only `web_fetch` and `web_search`.
- **Run all three sources, take the highest count** — do not stop after the first source returns results. A listing page that returns 86 posts is not "done" if the sitemap has 137.
- **Sitemap is the authoritative source** — it lists every published URL. Use the targeted blog-path prompt to avoid summarization of large flat sitemaps.
- **DataForSEO `relevant_pages` is a cross-check, not a last resort** — run it whenever DataForSEO is available, even if the sitemap already returned results. It catches posts missed by gzip sitemaps or JS-rendered listing pages and provides an independent floor count.
- **Gzip-compressed / binary sitemaps** — try all 6 sitemap path variants before giving up. Different variants (e.g. `www.` prefix, `sitemap-index.xml` vs `sitemap_index.xml`) may be served uncompressed even when the primary path is gzip. Only fall to Step 3c after all 6 have failed.
- **JS-rendered listing pages** — web_fetch cannot execute JavaScript. If a blog listing page returns no post links, it is JS-rendered. Skip to sitemap (Step 3a) or DataForSEO (Step 3c) rather than retrying the listing page with different prompts.
- If a site has multiple blog sections (e.g. `/blog/` and `/insights/`), report each separately and sum for the total.
- In competitor comparison mode, process all domains before presenting output — do not show partial results mid-way.
- Do not mention internal tool names to the user — just present results cleanly.
- When DataForSEO is used as fallback, note "Source: search index (may undercount)" in output.