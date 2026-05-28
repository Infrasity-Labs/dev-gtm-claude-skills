---
name: blog-post-counter
description: Counts blog posts for a target company and its competitors, then ranks them to show where the target stands. Use this skill whenever a user wants to compare blog post counts, content volume, or publishing output between companies — e.g. "how many blog posts does X have vs Y and Z", "compare blog content between these companies", "where does [company] rank for blog posts against competitors", "blog post count for [company]", or any request involving counting or comparing published blog content across multiple sites. Works from company names alone — no URLs needed. Always use this skill for multi-company blog comparison tasks.
---

# Blog Post Counter Skill

Counts and compares blog post output across a target company and its competitors, ranking them so the user can see where their target stands.

## Workflow

### Step 1 — Resolve each company to a URL

For each company name provided:
1. If a URL was given directly, use it.
2. If only a name was given, run `curl -sL "https://<likely-domain>/robots.txt"` to confirm the site exists and find the sitemap. If that 404s, do a quick web search for `"<company name>" official website` to get the correct domain.

### Step 2 — Find the sitemap

From the robots.txt, extract the `Sitemap:` line(s). Common patterns:
- Single sitemap: `Sitemap: https://example.com/sitemap.xml`
- Sitemap index: multiple `Sitemap:` lines, or a sitemap-index.xml that references sub-sitemaps

If no sitemap is in robots.txt, try these fallbacks in order:
```
/sitemap.xml
/sitemap_index.xml
/sitemap-index.xml
/blog/sitemap.xml
```

### Step 3 — Count blog posts

Fetch the sitemap and count URLs that are blog posts. Use this bash pattern:

```bash
curl -sL -A "Mozilla/5.0" "https://example.com/sitemap.xml" \
  | grep -o '<loc>[^<]*</loc>' \
  | grep -iE '/blog/|/posts?/|/articles?/|/news/' \
  | grep -v -E '^<loc>https://[^/]+/blog/?</loc>$' \
  | wc -l
```

**Important:** Exclude the blog index page itself (e.g. `/blog` or `/blog/`) — count only individual post URLs.

**Sitemap index handling:** If the sitemap is an index (contains `<sitemap>` tags rather than `<url>` tags), extract the sub-sitemap URLs and fetch the blog-specific one:
```bash
curl -sL -A "Mozilla/5.0" "https://example.com/sitemap-index.xml" \
  | grep -o '<loc>[^<]*</loc>' \
  | grep -i 'blog'
# Then fetch that sub-sitemap and count
```

**JS-rendered sites:** Some blog pages render via JavaScript and may not expose counts through sitemaps. In that case, fall back to `site:example.com/blog` search operator to estimate.

**Edge cases:**
- Some sites use `/resources/`, `/insights/`, `/learn/`, or `/hub/` instead of `/blog/` — check the sitemap structure if a `/blog/` grep returns 0.
- If the sitemap is very large (>1MB), grep for multiple blog path patterns.

### Step 4 — Build the output

Once all counts are collected, produce a ranked table with the target company highlighted:

```
Blog Post Count — [Target] vs Competitors
==========================================

Rank  Company          Posts   URL
────  ───────────────  ──────  ──────────────────────
 1    Hackmamba        137     hackmamba.io           ← COMPETITOR
 2    Infrasity        137     infrasity.com          ← COMPETITOR  
 3  ▶ Kubiya           95      kubiya.ai              ← TARGET
 4    Orgn             7       orgn.com               ← COMPETITOR

▶ = your company   Total companies analysed: 4
```

Then add a brief summary:
- Where the target ranks (e.g. "3rd out of 4")
- Gap to the leader (e.g. "42 posts behind the top competitor")
- Gap to the one above (if not already #1)
- Any notable observations (e.g. very new site, or tied for first)

## Output Format

```
Blog Post Count — [Target] vs Competitors
==========================================

Rank  Company          Posts   URL
────  ───────────────  ──────  ──────────────────────
 1    [Competitor A]   NNN     competitor-a.com       ← COMPETITOR
 2  ▶ [Target]         NNN     target.com             ← TARGET
 3    [Competitor B]   NNN     competitor-b.com       ← COMPETITOR

▶ = your company   Total companies analysed: N
```

## Notes

- Always count from the sitemap — it's the most accurate and complete source.
- Robots.txt is always the first place to look for the sitemap URL.
- The `/blog` index page should never be counted as a post.
- If a company has no blog section at all, report 0 and note it.
- Sitemap data can lag real-time by days; note this if relevant.
- Run all company lookups in sequence (one bash block per company) to avoid hitting rate limits.