# doc-metadata-analyzer

A Python skill for AI agents that validates SEO metadata on documentation pages. Checks `<title>` and `<meta name="description">` tags against search engine best practices and returns structured, actionable results.

---

## Features

- Validates meta title length (ideal: 50–60 chars)
- Validates meta description length (ideal: 140–160 chars)
- Returns structured `CheckResult` objects — no parsing required
- CLI script for quick one-off checks
- Fallback workflow for sites that block automated user-agents (403s)
- Never raises exceptions — errors are returned in the result object

---

<p align="center">
  <a href="../../assets/doc-metadata-analyzer-video.mp4">
    <img 
      src="../../assets/doc-metadata-analyzer-video.gif" 
      width="100%" 
      alt="Documentation Metadata Analyzer Demo"
    />
  </a>
</p>

## Installation

There are two ways to install this skill depending on how you use Claude.

### Option A — Claude.ai (Free, Pro, Max, Team, Enterprise)

No Python or CLI needed. Skills are supported on all plans, including free.

1. Go to **[Settings → Capabilities](https://claude.ai/settings/capabilities)** and enable **Code execution and file creation**.
2. Go to **[Customize → Skills](https://claude.ai/customize/skills)**.
3. Click **+** → **Create skill** → **Upload a skill**.
4. Upload a ZIP of the skill folder:

```bash
git clone https://github.com/infrasity-labs/dev-gtm-claude-skills.git
cd dev-gtm-claude-skills/skills
zip -r doc-metadata-analyzer.zip doc-metadata-analyzer/
```

Upload `doc-metadata-analyzer.zip`, then toggle the skill on. Claude will install required packages automatically on first use.

Once enabled, just describe your task in any chat — Claude activates the skill automatically when it recognises the intent, or you can invoke it directly:

```
Analyze metadata for https://docs.yourproduct.com
```

> Skills you upload are private to your account.

---

### Option B — Claude Code (CLI)

**Prerequisites:** Python 3.9+, [Claude Code](https://claude.ai/code)

```bash
git clone https://github.com/infrasity-labs/dev-gtm-claude-skills.git

mkdir -p ~/.claude/skills/ && cp -r skills/doc-metadata-analyzer ~/.claude/skills/

cd ~/.claude/skills/doc-metadata-analyzer
pip install -r requirements.txt --break-system-packages
```

Claude Code picks up skills from `~/.claude/skills/` automatically.

**Dependencies:**
- `requests>=2.31.0` — HTTP fetching
- `beautifulsoup4>=4.12.0` — HTML parsing

---

## Quick start

### CLI

```bash
python check_metadata.py https://docs.python.org/3/
```

Example output:

```
🔍 Checking: https://docs.python.org/3/

============================================================
📄 TITLE: 3.13.3 Documentation
   Length: 20 chars
   Status: WARNING
   ⚠️  Title slightly short (20 chars, ideal: 50-60)

📝 DESCRIPTION: Missing
   Length: 0 chars
   Status: MISSING
============================================================
```

### Python API

```python
from scripts import check_documentation_metadata

result = check_documentation_metadata("https://docs.python.org/3/")

if result.success:
    print(result.title.value)   # "3.13.3 Documentation"
    print(result.title.status)  # "warning"
    print(result.title.issues)  # ["Title slightly short (20 chars, ideal: 50-60)"]
else:
    print(result.error)
```

---

## API reference

### `check_documentation_metadata(url, timeout=30, user_agent="DocMetadataChecker/1.0")`

Fetches a URL and validates its metadata. Returns a `CheckResult`. Never raises — all errors surface as `result.success = False`.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `url` | `str` | — | Page URL to check (HTTP/HTTPS only) |
| `timeout` | `int` | `30` | Request timeout in seconds |
| `user_agent` | `str` | `"DocMetadataChecker/1.0"` | User-agent header for the HTTP request |

### `CheckResult`

```python
result.url               # str   — the checked URL
result.success           # bool  — False if fetch or parse failed
result.error             # str | None — error message when success=False

result.title.value       # str | None — raw title text
result.title.exists      # bool
result.title.length      # int  — character count
result.title.status      # "ideal" | "warning" | "missing"
result.title.issues      # list[str] — human-readable problems

result.description.value    # str | None — raw description text
result.description.exists   # bool
result.description.length   # int
result.description.status   # "ideal" | "warning" | "missing"
result.description.issues   # list[str]
```

Serialize to JSON with `result.to_dict()`:

```python
import json
print(json.dumps(result.to_dict(), indent=2))
```

```json
{
  "url": "https://docs.example.com",
  "title": {
    "value": "Example Docs",
    "exists": true,
    "length": 12,
    "status": "warning",
    "issues": ["Title too short (12 chars, recommended: 50-60)"]
  },
  "description": {
    "value": null,
    "exists": false,
    "length": 0,
    "status": "missing",
    "issues": ["Description is missing"]
  },
  "success": true,
  "error": null
}
```

---

## SEO thresholds

| Field | Ideal | Warning |
|-------|-------|---------|
| Meta title | 50–60 chars | < 30 or > 65 chars |
| Meta description | 140–160 chars | < 70 or > 165 chars |

Values in between ideal and warning boundaries still return `"warning"` with a "slightly short/long" message.

---

## Handling 403s (fallback workflow)

Many documentation sites block the default user-agent. When the CLI returns a 403, fetch the HTML via a browser-like client (e.g. Claude's `web_fetch` tool) and pass the raw HTML directly into the checker:

```python
import sys, json
sys.path.insert(0, "/path/to/doc-metadata-analyzer")
from scripts.checker import MetadataChecker
from scripts.models import CheckResult

raw_html = "..."  # HTML string from web_fetch or requests with a browser UA

checker = MetadataChecker()
title_text, desc_text = checker._extract_metadata(raw_html)
title_check = checker._validate_title(title_text)
desc_check  = checker._validate_description(desc_text)

result = CheckResult(
    url="https://docs.example.com",
    title=title_check,
    description=desc_check,
    success=True,
    error=None
)

print(json.dumps(result.to_dict(), indent=2))
```

This gives identical output to the normal flow — just without the HTTP layer.

---

## Project structure

```
doc-metadata-analyzer/
├── scripts/
│   ├── __init__.py      # Public API — check_documentation_metadata()
│   ├── checker.py       # MetadataChecker class
│   ├── models.py        # CheckResult, TitleCheck, DescriptionCheck
│   └── constants.py     # SEO length thresholds
├── check_metadata.py    # CLI entry point
├── SKILL.md             # Agent skill instructions
├── README.md
└── requirements.txt
```
