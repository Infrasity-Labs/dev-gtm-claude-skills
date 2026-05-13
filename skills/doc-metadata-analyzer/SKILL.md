---
name: doc-metadata-analyzer
version: 1.1.0
description: Check documentation pages for SEO metadata compliance
author: Dev GTM
tags: [seo, metadata, documentation, validation, agent-skill]
---

# Documentation Metadata Analyzer

Validates `<title>` and `<meta name="description">` tags on documentation pages against SEO best practices.

## Quick start

```bash
cd /mnt/skills/user/doc-metadata-analyzer
pip install -r requirements.txt --break-system-packages -q
python check_metadata.py https://docs.example.com
```

**Important:** Many sites return 403 to the default user-agent. If the CLI fails with a 403 or fetch error, use the fallback workflow below instead.

---

## Workflow: choosing the right approach

### Step 1 — Try the CLI

```bash
python check_metadata.py https://docs.example.com
```

If it succeeds, you're done. Read the JSON output at the bottom of stdout.

### Step 2 — Fallback when the CLI gets a 403 or network error

Sites like react.dev, Next.js docs, and others block the default user-agent. When this happens:

1. Fetch the page HTML using the `web_fetch` tool (it uses a browser-like user-agent).
2. Pass the raw HTML directly into the checker's internal methods, bypassing the HTTP layer.

```python
import sys
sys.path.insert(0, "/mnt/skills/user/doc-metadata-analyzer")
from scripts.checker import MetadataChecker
from scripts.models import CheckResult

# raw_html = the string returned by web_fetch
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

This gives identical output to the CLI with no network call from Python.

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

Always show:
- The raw value found (or "not found")
- Character count and status (✓ ideal / ⚠ warning / ✗ missing)
- The specific issue string from `result.title.issues` / `result.description.issues`
- A concrete rewrite suggestion when a tag is missing or out of range

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