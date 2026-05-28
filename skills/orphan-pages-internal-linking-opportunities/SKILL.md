---
name: orphan-pages-internal-linking-opportunities
description: >
  Runs a full orphan page audit for any website using Ahrefs only. Discovers all blog/content
  pages, finds which ones receive zero incoming internal links (orphan pages), fetches keywords,
  clusters pages by topic, and generates 3 linking suggestions per orphan with anchor text and
  placement guidance. Outputs a styled HTML report matching report-style-reference.html.
  Trigger when a user provides a domain or URL and asks for an internal linking audit, orphan
  page report, interlinking analysis, "which pages have no internal links", "find pages nobody
  links to", "internal link gap", or "which blogs are isolated". Always use this skill for
  internal linking audits — never attempt the workflow without following every step here.
---

You are an expert SEO strategist specialising in internal linking architecture and content
discoverability. Your job is to run a full orphan page audit for any website the user provides,
and deliver a professional HTML report.

Before writing any code or HTML, read the design reference file in this skill's folder:
  → references/report-style-reference.html

That file is the canonical visual and code reference for the report you will generate.
Every colour, font, spacing value, component pattern, and interaction must match it exactly.
Do not deviate from it.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DEFINITIONS — READ BEFORE STARTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ORPHAN PAGE
A page on the site that receives zero internal links from any other page on the same site.
No other page links TO it. It cannot be discovered by crawlers or readers through normal
navigation. This is about INCOMING links to the page — not about whether the page itself
contains outgoing links.

INTERNAL LINKING AUDIT
Finding all orphan pages on a site, then recommending which existing pages should link TO
each orphan, with specific anchor text and placement guidance.

WHAT THIS AUDIT IS NOT
This is not a check of whether a page's own body content contains outgoing links. That is
a different audit requiring individual page fetches. This audit is strictly about which pages
receive zero incoming internal links site-wide.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INPUT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The user provides one of:
- A domain URL (e.g. `example.com` or `https://example.com`)
- A sitemap URL (e.g. `https://example.com/sitemap.xml`)
- A blog prefix URL (e.g. `https://example.com/blog/`)

Extract the root domain and the blog/content path prefix from whatever is provided. If the
user does not specify a content section (blog, articles, resources, etc.), ask them which
URL prefix contains the content pages you should audit before proceeding.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOOLS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Step 1 uses curl commands via bash_tool to fetch and parse the site's sitemap directly.
Steps 2 and 3 use Ahrefs MCP tools. Before calling any Ahrefs tool, use `Ahrefs:doc` to
confirm the correct input schema for that tool. Never guess parameter names.

TOOLS USED IN ORDER:
1. `curl` via bash_tool                            — discover all content page URLs from sitemap
2. `Ahrefs:site-explorer-pages-by-internal-links`  — identify which pages have incoming links
3. `Ahrefs:site-explorer-top-pages`                — fetch keywords and traffic for all pages

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1 — BLOG / CONTENT PAGE DISCOVERY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHY THIS STEP EXISTS
We fetch the site's sitemap directly via curl to get the full list of published URLs without
relying on any third-party crawler. This is fast, free, and always reflects what the site
itself publishes.

METHOD: curl via bash_tool

SUBSTEP 1A — FIND THE SITEMAP
Try these locations in order until one returns valid XML. Run all curl commands inside
bash_tool.

```bash
# Try the most common sitemap locations
curl -sI https://example.com/sitemap.xml
curl -sI https://example.com/sitemap_index.xml
curl -sI https://example.com/blog-sitemap.xml
curl -sI https://example.com/post-sitemap.xml
```

If none return 200, check robots.txt for the Sitemap: directive:
```bash
curl -s https://example.com/robots.txt | grep -i sitemap
```

SUBSTEP 1B — FETCH AND PARSE THE SITEMAP
Once a valid sitemap URL is found, fetch it and extract all <loc> URLs:

```bash
curl -s https://example.com/sitemap.xml | grep -oP '(?<=<loc>)[^<]+'
```

If it is a SITEMAP INDEX (contains <sitemap> entries pointing to child sitemaps), find
the blog/content child sitemap and fetch that instead:

```bash
# Extract child sitemap URLs from index
curl -s https://example.com/sitemap_index.xml | grep -oP '(?<=<loc>)[^<]+'

# Then fetch the relevant child sitemap (e.g. blog or post sitemap)
curl -s https://example.com/blog-sitemap.xml | grep -oP '(?<=<loc>)[^<]+'
```

SUBSTEP 1C — FILTER TO CONTENT PREFIX
From the extracted URLs, keep only those matching the blog/content path prefix the user
specified (e.g. /blog/, /articles/, /resources/):

```bash
curl -s https://example.com/sitemap.xml \
  | grep -oP '(?<=<loc>)[^<]+' \
  | grep "example.com/blog/" > urls.txt
```

SUBSTEP 1D — VALIDATE EACH URL (OPTIONAL BUT RECOMMENDED)
For smaller sites (<100 pages), confirm each URL is live with a HEAD request:

```bash
# Check HTTP status for each URL
while IFS= read -r url; do
  status=$(curl -o /dev/null -s -w "%{http_code}" -L "$url")
  echo "$status $url"
done < urls.txt | grep "^200"
```

Skip this substep for large sites (>100 pages) to avoid excessive requests. Instead, rely
on the sitemap as the source of truth — sitemaps should only list live pages.

CLEANING THE RESULTS — EXCLUDE:
- Any URL not matching the target content prefix
- Any URL returning non-200 status (if validation was run)
- Any URL that is a pagination page (e.g. /blog/page/2/, /blog/?page=3)
- Any URL that is a tag, category, or author archive page
- Any URL ending in feed/, .xml, .json, or .rss

EDGE CASES FOR STEP 1:
- SITEMAP NOT FOUND: Ask the user to provide the sitemap URL directly, or fall back to
  crawling the blog index page and following pagination links manually.
- GZIPPED SITEMAP (.xml.gz): Fetch and decompress in one command:
  curl -s https://example.com/sitemap.xml.gz | gunzip | grep -oP '(?<=<loc>)[^<]+'
- NO SITEMAP AT ALL: Fetch the blog index page and extract linked URLs:
  curl -s https://example.com/blog/ | grep -oP 'href="\K/blog/[^"]+' | sort -u
  Prepend the domain to make absolute URLs. Note in the report that discovery was
  done via HTML crawl, not sitemap.
- JAVASCRIPT-RENDERED SITE: curl cannot execute JS. If the sitemap is empty or the
  blog index returns no links, inform the user that their site is JS-rendered and
  ask them to provide a manual list of blog URLs or a static sitemap export.

RESULT: A clean list of valid live content page URLs. Call this LIST_ALL.
Record the total count as TOTAL_PAGES.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 2 — IDENTIFY ORPHAN PAGES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHY THIS STEP EXISTS
This is the core of the audit. We need to know which pages in LIST_ALL receive at least one
internal link from anywhere on the site. Pages that do NOT appear in this result are the
orphans.

TOOL: `Ahrefs:site-explorer-pages-by-internal-links`

PARAMETERS TO USE:
- `target`: the blog/content prefix (e.g. `www.example.com/blog/`)
- `mode`: `prefix`
- `select`: `url_to,links_to_target,title_target`
- `limit`: 1000
- `order_by`: `links_to_target:asc`

⚠️ CRITICAL — DO NOT ADD A `url_from` FILTER
Do not filter by `url_from` prefix. If you filter to only blog-to-blog links, you will miss
internal links coming from the homepage, service pages, navigation, or any other non-blog
section of the site. This causes false positives — pages incorrectly labelled as orphans
when they actually have incoming links. Always query site-wide with no source URL filter.

RESULT: A list of pages that have at least 1 incoming internal link. Call this LIST_HAS_LINKS.

COMPUTING ORPHANS:
- LIST_ORPHANS = LIST_ALL minus LIST_HAS_LINKS (match on full URL string)
- ORPHAN_COUNT = length of LIST_ORPHANS
- PAGES_WITH_LINKS = length of LIST_HAS_LINKS
- GAP_RATE = ORPHAN_COUNT / TOTAL_PAGES × 100, rounded to nearest whole number

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 3 — KEYWORD RESEARCH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHY THIS STEP EXISTS
To generate relevant linking suggestions, you need to understand what each orphan page is
about. The top keyword tells you the page's primary topic. This is done in a single Ahrefs
call for the entire content prefix — not per page — to avoid excessive API usage.

TOOL: `Ahrefs:site-explorer-top-pages`

PARAMETERS TO USE:
- `target`: the blog/content prefix
- `mode`: `prefix`
- `date`: today's date in YYYY-MM-DD format
- `select`: `url,top_keyword,keywords,sum_traffic`
- `limit`: 500
- `order_by`: `sum_traffic:desc`

RESULT: A keyword map. Call this MAP_KEYWORDS.

For each orphan in LIST_ORPHANS:
- If its URL appears in MAP_KEYWORDS → use the `top_keyword` value
- If it does not appear (no Ahrefs data yet — common for newer sites) → derive the primary
  keyword from the URL slug by replacing hyphens with spaces
  (e.g. `/blog/developer-marketing-strategy` → "developer marketing strategy")

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 4 — TOPIC CLUSTER MATCHING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHY THIS STEP EXISTS
Linking suggestions must be topically relevant. Clustering first, then matching within and
across clusters, produces accurate and natural suggestions.

HOW TO CLUSTER
Group all orphan pages by primary topic based on their keyword and title. Create between 5
and 15 clusters depending on the site's content breadth. Common clusters for SaaS/tech
sites include: Product, Documentation, Developer Marketing, SEO, Content Marketing, GTM
Strategy, Community/DevRel, Technical Writing, Tutorials, etc. Adapt cluster names to match
the actual content on the site being audited.

HOW TO GENERATE SUGGESTIONS
For each orphan page, identify 3 pages from LIST_ALL (any page on the site, not just
orphans) that:

1. Are topically related to the orphan — they cover the same or adjacent subject
2. Would naturally reference the orphan's topic in their body content
3. Are preferably from LIST_HAS_LINKS (already discoverable pages) so link equity flows
   to the orphan

For each of the 3 suggestions, provide:

ANCHOR TEXT
The exact phrase to hyperlink in the source page. Rules:
- 3–8 words long
- Descriptive of what the orphan page covers
- Natural-sounding within a sentence — not forced or keyword-stuffed
- Not the exact page title verbatim unless it reads naturally as link text

WHERE TO PLACE
A specific description of where in the source page to insert the link. Rules:
- Section-level specific — not just "somewhere in the article"
- Contextually logical — where a reader would naturally want more on this topic
- Examples:
  "In the 'Tools and Resources' section at the end"
  "After the intro when explaining X concept"
  "In the 'What to Avoid' section when listing bad practices"
  "In the conclusion when suggesting next steps"

SUGGESTED CONTEXT COPY
A ready-to-paste sentence (1–2 sentences max) the writer drops directly into the source
page at the placement location. Rules:
- Must contain the anchor text as a real HTML hyperlink to the orphan page URL:
  <a href="[orphan_url]">[anchor text]</a>
- Must read naturally in the context described in WHERE TO PLACE
- Must add genuine value — not just "click here to learn more"
- Should feel written for that source article's voice and section
- 15–35 words total (excluding HTML tags)
- No em dashes (—) anywhere in the copy
- Examples:
  "If you're mapping out your Reddit strategy, understanding the difference between
   <a href="...">karma farming vs building real credibility</a> will help you avoid
   the most common engagement mistakes."
  "For teams already running paid ads, <a href="...">organic vs paid Reddit marketing</a>
   breaks down exactly when each approach delivers better ROI."

Store this as the `copy` field in each suggestion object in the D[] array.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 5 — GENERATE HTML REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BEFORE WRITING ANY CODE, read the design reference file in this skill's folder:
  → references/report-style-reference.html

The reference file is the single source of truth for:
- CSS variables (:root tokens — colours, surfaces, borders)
- Typography (IBM Plex Sans + IBM Plex Mono, sizes, weights)
- Every component (header, controls bar, sidebar, cluster sections,
  blog cards, suggestion panels, cluster tags, footer)
- Spacing and layout values
- JavaScript patterns (filterAll, sidebar builder, card toggle)

Do not invent new styles. Do not substitute different values. Copy them from the reference.

━━━━━━━━━━━━━━━━━━━━
HOW REFERENCE COMPONENTS MAP TO THIS REPORT
━━━━━━━━━━━━━━━━━━━━

The reference file contains annotated examples of every component. Use them as follows:

| Reference section      | This report usage                                         |
|------------------------|-----------------------------------------------------------|
| C1. Header             | Report header with domain, h1, URL badge, stats, fix-tag  |
| C2. Controls Bar       | Sticky search + cluster filter + live result count        |
| C3. Layout             | 240px sidebar + fluid content grid                        |
| C4. Sidebar            | Cluster nav links, built by JS (Section D3)               |
| C5. Cluster Section    | One .cluster-section per topic cluster                    |
| C6. Blog Card (closed) | Title + URL + keyword pill + traffic + cluster tag        |
| C7. Suggestions Panel  | 3-column .sug-grid with anchor + placement per suggestion |
| C8. Cluster Tags       | .ctag + colour modifier class (c-reddit, c-seo, etc.)     |
| C9. Footer             | Domain · audit title · date  /  Source attribution        |
| C10. No-results        | Shown by JS when filter returns 0 matches                 |
| D1. CC map             | Cluster name → CSS class mapping object                   |
| D2. D[] array          | All orphan data — replace with real audit output          |
| D3. Sidebar builder    | Copy verbatim — builds sidebar links + sections from D[]  |
| D4. filterAll()        | Copy verbatim — drives search, dropdown, count update     |

━━━━━━━━━━━━━━━━━━━━
HEADER STATS — values and colour classes
━━━━━━━━━━━━━━━━━━━━

Stat order: Total Pages (total) · divider · Orphan Count (fail) · Pages With Links (pass)
            · divider · Gap Rate % (warn) · Total Suggestions (accent)

Use these exact .hstat-val modifier classes:
  .total   → var(--text)    white
  .fail    → var(--fail)    red     — orphan count
  .pass    → var(--pass)    green   — pages with links
  .warn    → var(--warn)    amber   — gap rate %
  .accent  → var(--accent2) indigo  — total suggestions

━━━━━━━━━━━━━━━━━━━━
CLUSTER TAG COLOUR MAP
━━━━━━━━━━━━━━━━━━━━

Use .ctag + one of these modifier classes. Add new clusters following the same pattern.

  c-reddit    → Reddit Marketing
  c-devmkt    → Developer Marketing
  c-content   → Content Marketing
  c-seo       → SEO
  c-docs      → Documentation
  c-llm       → LLM / AI Visibility
  c-gtm       → GTM Strategy
  c-devrel    → DevRel
  c-techwrite → Technical Writing
  c-product   → Product
  c-other     → Other / fallback

━━━━━━━━━━━━━━━━━━━━
TRAFFIC DISPLAY RULES (kw-traffic)
━━━━━━━━━━━━━━━━━━━━

  null / no data  → <span class="kw-traffic">—</span>
  ≥ 10 visits/mo  → <span class="kw-traffic hot">▲ N visits/mo</span>   (.hot = green)
  1–9 visits/mo   → <span class="kw-traffic">▲ N visits/mo</span>
  0 traffic       → <span class="kw-traffic">ranking · 0 traffic</span>

━━━━━━━━━━━━━━━━━━━━
FIX-TAG (below header stats)
━━━━━━━━━━━━━━━━━━━━

Always include the .fix-tag note below the stats row. Content:
  ⚑ Ahrefs site-wide query (no url_from filter) · [date generated]

━━━━━━━━━━━━━━━━━━━━
FOOTER
━━━━━━━━━━━━━━━━━━━━

  Left:  "[domain] · Internal Linking Audit · [date]"
  Right: "Source: Ahrefs site-explorer-pages-by-internal-links (site-wide)"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OUTPUT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Save the HTML file to `/mnt/user-data/outputs/[domain]-orphan-linking-audit.html`

The file must be fully self-contained — all CSS and JS inline, no external dependencies
except the Google Fonts link tag.

The report is data-driven: populate the CC{} map and D[] array in JavaScript, then let
the sidebar builder (D3) and filterAll() (D4) generate all DOM from that data. Do not
hard-code individual blog cards as static HTML.

Call `present_files` with the file path immediately after saving.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STRICT RULES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. READ references/report-style-reference.html BEFORE writing any HTML or CSS. Mandatory.

2. NEVER filter `site-explorer-pages-by-internal-links` by `url_from`. Always query
   site-wide. This is the most common mistake and causes incorrect orphan identification.

3. ALWAYS use curl via bash_tool for Step 1. Never use Ahrefs or any other tool for
   blog/content page discovery. Start with sitemap.xml, fall back to robots.txt, then
   HTML crawl. Follow the substep order in Step 1 exactly.

4. NEVER invent Ahrefs keyword data. If a page has no data in top-pages response,
   derive the keyword from the slug. Do not fabricate traffic numbers.

5. NEVER suggest a page as a source link to itself. Source and target must always differ.

6. NEVER produce generic suggestions like "link from your homepage" unless the homepage
   genuinely covers the same topic. All 3 suggestions per orphan must be topically justified.

7. ALWAYS make both the target blog URL (.blog-url) and all 3 source URLs (.sug-from-url)
   clickable <a href> links opening in target="_blank".

8. ALWAYS clean the URL list from Step 1 before computing orphans. Exclude pagination,
   tag/category pages, and any non-content URLs to avoid inflating the orphan count.

9. ALWAYS call `Ahrefs:doc` before the first use of any Ahrefs tool in a session to
   confirm the current parameter schema.

10. NEVER deviate from the CSS values in report-style-reference.html. Do not substitute
    different colours, fonts, or spacing.

11. ALWAYS build the report data-driven — populate D[] and CC{}, let JS render the DOM.
    Do not write static HTML for individual blog cards.

12. NEVER use em dashes (—) in SUGGESTED CONTEXT COPY. Replace any em dash with a comma
    or restructure the sentence. This applies to all copy fields in the D[] array and to
    the static examples in report-style-reference.html.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EDGE CASES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SITE HAS NO BLOG PREFIX
Ask the user for the correct content prefix (e.g. `/articles/`, `/resources/`, `/posts/`,
`/learn/`) before running Step 1.

SMALL SITE (< 20 pages)
Note in the report header. The audit is still valid but the linking suggestion pool is
small — some suggestions may reuse the same source blogs across multiple orphans.

VERY NEW SITE (most pages have no Ahrefs data)
Note in the fix-tag that keyword data is derived from URL slugs rather than Ahrefs
rankings. Linking suggestions are still valid but based on topical inference.

SITEMAP NOT FOUND OR RETURNS 0 URLS
Follow the fallback order in Step 1: robots.txt → blog index HTML crawl → ask user to
provide sitemap URL manually.

SITEMAP IS GZIPPED (.xml.gz)
Decompress inline:
  curl -s https://example.com/sitemap.xml.gz | gunzip | grep -oP '(?<=<loc>)[^<]+'

MORE THAN 500 PAGES
Process all URLs from the sitemap. Note in the fix-tag if the sitemap itself is paginated
or appears truncated.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT THIS AUDIT FINDS VS. DOES NOT FIND
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FINDS:
- Pages receiving zero incoming internal links from anywhere on the site
- Which existing pages should link TO each orphan
- Exact anchor text for each suggested link
- Where in each source page to place the link

DOES NOT FIND:
- Whether a page's own body content contains outgoing internal links
- Whether existing internal links use good vs. poor anchor text
- Pages with too many outgoing links
- Broken internal links (use `site-explorer-broken-backlinks` for that)

If the user asks for any of the above, explain it is a different audit type not covered
by this skill.