# Documentation Metadata Analyzer

A Python agent skill that enables AI agents to check documentation pages for proper SEO metadata. Validates meta titles and meta descriptions against SEO best practices.

## Features

- ✅ **Meta Title Validation**: Checks existence and character length (ideal: 50-60 chars)
- ✅ **Meta Description Validation**: Checks existence and character length (ideal: 140-160 chars)
- ✅ **SEO Best Practices**: Validates against search engine optimization guidelines
- ✅ **Simple Python API**: Direct function calls without protocol complexity
- ✅ **Clear Responses**: Structured result objects with actionable recommendations

## Installation

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Method 1: Clone Repository

```bash
# Clone the entire repository
git clone https://github.com/infrasity-labs/dev-gtm-claude-skills.git
cd dev-gtm-claude-skills/skills/doc-metadata-analyzer

# Add skill to your AI agent
cp -r doc-metadata-analyzer /path-to-agent/skills/

# Test it works
Analyse metadata for https://docs.example.com/
```

### Install Dependencies

```bash
cd doc-metadata-analyzer
pip install -r requirements.txt
```

### Required Packages

- `requests>=2.31.0` - HTTP requests
- `beautifulsoup4>=4.12.0` - HTML parsing (uses built-in html.parser)




### Result Structure

The `CheckResult` object contains:

```python
result.url           # str: The checked URL
result.success       # bool: Whether check completed successfully
result.error         # str | None: Error message if success=False
result.title         # TitleCheck: Title validation result
result.description   # DescriptionCheck: Description validation result
```

**TitleCheck / DescriptionCheck attributes:**
```python
result.title.value    # str | None: The title/description text
result.title.exists   # bool: Whether tag exists
result.title.length   # int: Character count
result.title.status   # str: "ideal", "warning", or "missing"
result.title.issues   # list[str]: List of validation issues
```

### Serialization

Convert results to dictionary for JSON output:

```python
import json

result = check_documentation_metadata("https://docs.example.com")
result_dict = result.to_dict()
json_output = json.dumps(result_dict, indent=2)
print(json_output)
```

**Output format:**
```json
{
  "url": "https://docs.example.com",
  "title": {
    "value": "Example Documentation",
    "exists": true,
    "length": 21,
    "status": "warning",
    "issues": ["Title too short (21 chars, recommended: 50-60)"]
  },
  "description": {
    "value": "Learn how to use our platform...",
    "exists": true,
    "length": 145,
    "status": "ideal",
    "issues": []
  },
  "success": true,
  "error": null
}
```

## SEO Guidelines

### Meta Title

- **Ideal Length**: 50-60 characters
- **Warning Threshold**: <30 or >65 characters
- **Why**: Search engines display ~50-60 characters in results

### Meta Description

- **Ideal Length**: 140-160 characters
- **Warning Threshold**: <70 or >165 characters
- **Why**: Search engines display ~140-160 characters in results

## Project Structure

```
doc-metadata-analyzer/
├── scripts/                # Package directory
│   ├── __init__.py         # Public API
│   ├── checker.py          # Metadata checking logic
│   ├── models.py           # Data models
│   └── constants.py        # SEO thresholds
├── check_metadata.py       # Standalone CLI script
├── SKILL.md                # Agent skill documentation
├── README.md               # README
└── requirements.txt        # Python dependencies
```

## Troubleshooting

### Import Errors

**Issue**: `ModuleNotFoundError: No module named 'scripts'`

**Solution**: Ensure the package is in your Python path:
```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
```

Or install the package in development mode:
```bash
pip install -e .
```

### Missing Dependencies

**Issue**: `ModuleNotFoundError: No module named 'requests'` (or beautifulsoup4, lxml)

**Solution**: Install dependencies:
```bash
pip install -r requirements.txt
```

### URL Fetch Errors

**Issue**: "Failed to fetch URL" errors

**Solution**:
- Verify the URL is accessible in a browser
- Check that the URL uses HTTP or HTTPS (not FTP, file://, etc.)
- Ensure you have internet connectivity
- Some sites may block automated requests
- Try increasing the timeout parameter
