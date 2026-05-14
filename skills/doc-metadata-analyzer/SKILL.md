---
name: doc-metadata-analyzer
version: 1.3.0
description: Check documentation pages for SEO metadata compliance
author: Dev GTM
tags: [seo, metadata, documentation, validation, agent-skill]
---

# Documentation Metadata Analyzer

Validates `<title>` and `<meta name="description">` tags on documentation pages against SEO best practices.

**Key output:** For each URL checked, you MUST show:
1. The **exact text** of the title and description tags (quoted)
2. The **character count** and how it compares to ideal ranges
3. The **status** (ideal/warning/missing) with specific issues
4. A **concrete recommendation** for improvement

---

## Quick start

```bash
cd /mnt/skills/user/doc-metadata-analyzer
pip install -r requirements.txt --break-system-packages -q
python check_metadata.py https://docs.example.com
```

**Important:** Many sites return 403 to the default user-agent. **If the CLI fails, you MUST try the fallback workflow using `web_fetch`** (see below). Do not stop at the first error.

---

## Workflow: choosing the right approach

**IMPORTANT:** Always try BOTH methods if the first one fails.

### Method 1 — Try the CLI first (fastest)

```bash
python check_metadata.py https://docs.example.com
```

If it succeeds, you're done. Read the JSON output at the bottom of stdout.

### Method 2 — Fallback using web_fetch (REQUIRED if CLI fails)

**When to use:** CLI returns 403, network error, or any fetch failure.

**Why it works:** Sites like Stripe, React, Next.js docs block the default Python user-agent but allow browser-like requests. The `web_fetch` tool uses a browser user-agent.

**Steps:**
1. Use `web_fetch` tool to get the HTML
   - **CRITICAL:** `web_fetch` may return markdown-converted content by default
   - You need the **raw HTML source**, not markdown
   - Look for the raw HTML in the response (may be in a `source` or `content` field)
2. Pass the raw HTML to the checker's internal methods

**Important:** If `web_fetch` returns markdown (no `<title>` or `<meta>` tags visible), the regex fallback in `_extract_metadata()` will handle it, but you should try to get raw HTML first.

```python
import sys
sys.path.insert(0, "/mnt/skills/user/doc-metadata-analyzer")
from scripts.checker import MetadataChecker
from scripts.models import CheckResult

# Get raw HTML from web_fetch (not markdown-converted)
# raw_html should contain actual HTML tags like <title> and <meta>
checker = MetadataChecker()
title_text, desc_text = checker._extract_metadata(raw_html)
title_check    = checker._validate_title(title_text)
desc_check     = checker._validate_description(desc_text)

result = CheckResult(
    url=url,
    title=title_check,
    description=desc_check,
    success=True,
    error=None
)

import json
print(json.dumps(result.to_dict(), indent=2))
```

**Note:** The `_extract_metadata()` method now includes regex fallback, so it will work even if BeautifulSoup fails (e.g., when given markdown instead of HTML).

---

## SEO thresholds (from `scripts/constants.py`)

| Field | Ideal | Warning |
|---|---|---|
| Meta title | 50–60 chars | < 30 or > 65 chars |
| Meta description | 140–160 chars | < 70 or > 165 chars |

Statuses: `"ideal"` · `"warning"` · `"missing"`

---

## Return value

`check_documentation_metadata()` and the fallback both return a `CheckResult`:

```python
result.url               # str
result.success           # bool
result.error             # str | None

result.title.value       # str | None
result.title.exists      # bool
result.title.length      # int
result.title.status      # "ideal" | "warning" | "missing"
result.title.issues      # list[str]  — human-readable problems

result.description.value   # str | None
result.description.exists  # bool
result.description.length  # int
result.description.status  # "ideal" | "warning" | "missing"
result.description.issues  # list[str]
```

Serialize to dict/JSON with `result.to_dict()`.

---

## What this skill does NOT check

- Open Graph tags (`og:title`, `og:description`, `og:image`)
- Twitter Card tags
- Canonical URL
- JavaScript-rendered metadata (only static HTML is parsed)
- Keyword optimization or content quality

To check OG/Twitter/canonical tags, parse them manually from the raw HTML after running the fallback workflow.

---

## Presenting results to the user

**CRITICAL — Never infer or hardcode metadata values:**
- The `value` field in the result MUST come directly from the HTML parsing
- Do NOT substitute values from page headings, document source tags, or your knowledge of the site
- If `value` is `None`, report it as "Not found" — do not guess or infer content
- Only show what the actual HTML `<title>` and `<meta name="description">` tags contain

**Required format for each field (title and description):**

1. **Status indicator** — ✓ Ideal / ⚠ Warning / ✗ Missing
2. **Actual content** — Show the exact text found (or "Not found" if missing)
   - Format: `"[exact text here]"`
   - If missing, explicitly state: "No [title/description] tag found"
3. **Character count** — Show length and compare to ideal range
4. **Specific issues** — List all items from `result.title.issues` / `result.description.issues`
5. **Recommendation** — Provide a concrete rewrite suggestion when needed

**Example output format:**

```
Title — ⚠ Warning
Content: "Vercel Documentation"
Length: 20 characters (ideal: 50-60)
Issue: Title too short — missing key information about platform capabilities
Recommendation: "Vercel Documentation: Deploy, Scale & Build with Serverless, Edge & AI"

Meta description — ✗ Missing  
Content: Not found
Issue: No meta description tag present
Recommendation: Add a 140-160 character description covering deployment, serverless functions, edge networking, and AI infrastructure
```

**Critical:** Always quote the actual content found so users can see exactly what's on the page

---

## Multiple URLs

The library has no batch mode. Loop manually:

```python
urls = ["https://docs.stripe.com/api", "https://docs.github.com/en"]
for url in urls:
    result = check_documentation_metadata(url)
    print(url, result.title.status, result.description.status)
```

For sites likely to 403, fetch each via `web_fetch` first and use the fallback.