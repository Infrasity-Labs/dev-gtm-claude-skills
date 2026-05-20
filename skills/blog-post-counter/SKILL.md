---
name: blog-post-counter
description: >
  Finds the blog page URL and counts the total number of unique blog posts for any company.
  Use this skill whenever a user provides a company name, domain, sitemap URL, or asks to find
  their blog, count blog posts, check how many articles they've published, or audit their
  content output. Also trigger when the user says things like "how many blogs does X have",
  "find the blog for X", "check X's content volume", or provides a list of company names
  and wants blog data for each. Works from a company name alone — no URL required.
  Always use this skill instead of manual searching when blog discovery + counting is the goal.
compatibility: "Requires web_fetch, web_search, and dataforseo:serp_organic_live_advanced tools"
---

# Blog Post Counter Skill

Given a sitemap URL (or a domain/company name), count the total number of unique blog posts published by the company.

---

## Workflow

### Step 1 — Resolve the sitemap URL
- If the user provides a **sitemap URL** (e.g. `https://domain.com/sitemap.xml`) → proceed directly to Step 2.
- If the user provides only a **domain or company name** → attempt to resolve the sitemap URL by trying these common paths in order:
  1. `https://<domain>/sitemap.xml`
  2. `https://<domain>/sitemap_index.xml`
  3. `https://www.<domain>/sitemap.xml`

  Use `web_fetch` to check each until one returns valid XML. If none work, run `web_search` for `"<domain> sitemap.xml"` to find the correct sitemap URL. If a sitemap still cannot be found, inform the user and stop.

### Step 2 — Fetch & extract all URLs from the sitemap

Call `web_fetch` on the sitemap URL.

- **If readable XML** → extract all `<loc>` URLs from the response.
- **If the sitemap is a sitemap index** (contains `<sitemap>` entries pointing to child sitemaps) → `web_fetch` each child sitemap and collect all `<loc>` URLs across all of them. Prioritize child sitemaps whose filename suggests blog content (e.g. `post-sitemap.xml`, `sitemap-blog.xml`, `blog-sitemap.xml`) — fetch those first.
- **If binary / unreadable / fetch fails** → fall back to `dataforseo:serp_organic_live_advanced` with query `site:<domain>` to get a list of indexed URLs.

### Step 3 — Filter to blog post URLs only

From the full list of extracted URLs, keep only those that match the following patterns:

**Path patterns** (match with or without trailing slash):
- `/blog/`
- `/blog-posts/`
- `/insights/`
- `/resources/`
- `/articles/`
- `/news/`
- `/posts/`
- `/learn/`
- `/academy/`
- `/tutorials/`
- `/guides/`
- `/knowledge-base/`

**Subdomain patterns** (present in the URL hostname):
- `blog.<domain>`
- `academy.<domain>`
- `learn.<domain>`
- `resources.<domain>`
- `insights.<domain>`

A URL is a **blog post** if it matches one of the above patterns AND has at least one additional path segment after the pattern (e.g. `/blog/my-post` ✓, `/blog` or `/blog/` alone ✗).

Then deduplicate by applying ALL of the following exclusion rules:

| Exclude | Reason |
|---------|--------|
| The listing page itself (e.g. `/blog`, `/blog/`, `/blog-posts`) | Not a post |
| Pagination pages (e.g. `/blog?page=2`, `/blog?e3085cf6_page=3`) | Not a post |
| URLs with query params that duplicate a clean URL (e.g. `?ref=`, `?utm_source=`, `?query=`) | Duplicate |
| RSS / Atom feeds (e.g. `/blog/rss.xml`, `/blog/feed`) | Not a post |
| Category / tag / author archive pages (e.g. `/blog/category/seo`, `/blog/tag/ai`) | Not a post |

Count what remains — these are unique blog posts.

---

## Output Format

Return **only** this, nothing more:

```
Company:        <Company Name>
Blog URL:       <https://domain.com/blog/>
Unique posts:   <N>
```

If the blog section cannot be identified in the sitemap, return:
```
Company:        <Company Name>
Blog URL:       Not found
Unique posts:   —
```

---

## Batch Mode

If the user provides multiple sitemap URLs or company names, process them **sequentially** and return a single table:

| Company | Blog URL | Unique Posts |
|---------|----------|-------------|
| ...     | ...      | ...         |

---

## Notes

- Sitemap data reflects what the site explicitly publishes — the count may be lower than reality if the sitemap is incomplete or capped.
- If the sitemap is an index with many child sitemaps, fetch ALL of them (not just the first) to avoid undercounting.
- If a site has multiple blog sections (e.g. both `/blog/` and `/insights/`), report each separately and sum them for the total.
- Do not mention internal tool names to the user — just present the result cleanly.