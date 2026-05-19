---
name: blog-post-counter
description: >
  Finds the blog page URL and counts the total number of unique blog posts for any company.
  Use this skill whenever a user provides a company name, domain, or URL and asks to find
  their blog, count blog posts, check how many articles they've published, or audit their
  content output. Also trigger when the user says things like "how many blogs does X have",
  "find the blog for X", "check X's content volume", or provides a list of company names
  and wants blog data for each. Works from a company name alone — no URL required.
  Always use this skill instead of manual searching when blog discovery + counting is the goal.
compatibility: "Requires Ahrefs MCP (site-explorer-crawled-pages) and web_search tool"
---

# Blog Post Counter Skill

Given a company name or domain, find their blog URL and return the unique blog post count.

---

## Workflow

### Step 1 — Resolve the domain
- If the user provides a **URL or domain** → skip to Step 2.
- If the user provides a **company name** → run `web_search` for `"<company name> official website"` and extract the primary domain from the top result. If multiple companies share the same name, ask the user to clarify before proceeding (show a short list of options with their domains).

### Step 2 — Crawl all pages via Ahrefs
Call `Ahrefs:site-explorer-crawled-pages` with:
```
target:    <domain>           (e.g. firefly.ai)
mode:      subdomains
select:    url, title, http_code, url_rating
order_by:  url_rating:desc
limit:     100
where:     { "field": "http_code", "is": ["eq", 200] }
```

### Step 3 — Identify the blog URL
Scan the crawled pages for URL patterns that indicate a blog listing page. Common patterns (in priority order):
- `/blog`
- `/blog/`
- `/insights`
- `/resources`
- `/articles`
- `/news`
- `/posts`
- `/learn`

Pick the one with the highest url_rating that appears to be a listing page (e.g., it has a shorter path like /blog/ rather than /blog/post-title). If none are found in the first 100 results, do a second crawl without the url_rating:desc sort to surface more paths.

### Step 4 — Count unique blog posts
Call `Ahrefs:site-explorer-crawled-pages` again with:
```
target:    <blog-url>         (e.g. https://www.firefly.ai/blog/)
mode:      prefix
select:    url, title, http_code
order_by:  last_crawled:desc
limit:     1000
where:     { "field": "http_code", "is": ["eq", 200] }
```

Then deduplicate by applying ALL of the following exclusion rules:

| Exclude | Reason |
|---------|--------|
| The listing page itself (e.g. `/blog`, `/blog/`) | Not a post |
| Pagination pages (e.g. `/blog?page=2`, `/blog?e3085cf6_page=3`) | Not a post |
| URLs with query params that are duplicates of a clean URL (e.g. `?ref=`, `?utm_source=`, `?query=`) | Duplicate |
| RSS / Atom feeds (e.g. `/blog/rss.xml`, `/blog/feed`) | Not a post |
| Category, Tag, or Author pages (e.g. /blog/category/..., /blog/tag/..., /blog/author/...) | Not a post |

Count what remains — these are unique blog posts.

---

## Output Format

Return **only** this, nothing more:

```
Company:        <Company Name>
Blog URL:       <https://...>
Unique posts:   <N>
```

If the blog page cannot be found, return:
```
Company:        <Company Name>
Blog URL:       Not found
Unique posts:   —
```

---

## Batch Mode

If the user provides multiple company names, process them **sequentially** (one Ahrefs crawl per company) and return a single table:

| Company | Blog URL | Unique Posts |
|---------|----------|-------------|
| ...     | ...      | ...         |

---

## Notes

- Ahrefs crawl data may not include every post ever published — the count reflects what Ahrefs has indexed, which is a reliable proxy for total public post count.
- If pagination pages go up to a high number (e.g. page 20+), note that the actual count may be slightly higher than what Ahrefs has crawled.
- Do not mention the Ahrefs tool to the user by name — just present the result cleanly.