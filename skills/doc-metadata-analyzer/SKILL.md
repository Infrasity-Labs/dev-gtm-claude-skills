---
name: doc-metadata-analyzer
version: 1.0.0
description: Check documentation pages for SEO metadata compliance
author: Dev GTM
tags: [seo, metadata, documentation, validation, agent-skill]
---

# Documentation Metadata Analyzer

A Python agent skill that checks documentation pages for proper meta title and description tags, validating them against SEO best practices.

## 🤖 FOR AI AGENTS: How to Use This Skill

**Simple usage - just run the CLI script:**

```bash
cd path/to/doc-metadata-analyzer
python check_metadata.py https://docs.example.com
```

**If you get import errors**, install dependencies first:

```bash
cd path/to/doc-metadata-analyzer
pip install -r requirements.txt
python check_metadata.py https://docs.example.com
```

**That's it!** The script will:
- Fetch the URL
- Analyze title and description metadata
- Show results with SEO recommendations

---

## When to Use

Use this skill when you need to:
- Check if a documentation page has meta title and description
- Validate metadata character lengths for SEO
- Audit documentation sites for metadata compliance
- Get specific recommendations for improving metadata
- Analyze multiple pages for SEO optimization

## Function: check_documentation_metadata

### Import

```python
from scripts import check_documentation_metadata
```

### Function Signature

```python
def check_documentation_metadata(
    url: str,
    timeout: int = 30,
    user_agent: str = "DocMetadataChecker/1.0"
) -> CheckResult
```

### Parameters

- `url` (str, required): Documentation page URL (HTTP/HTTPS only)
- `timeout` (int, optional): Request timeout in seconds (default: 30)
- `user_agent` (str, optional): User agent string for HTTP requests (default: "DocMetadataChecker/1.0")

### Return Value

Returns a `CheckResult` object with the following attributes:

```python
result.url           # str: The checked URL
result.success       # bool: Whether check completed successfully
result.error         # str | None: Error message if success=False
result.title         # TitleCheck: Title validation result
result.description   # DescriptionCheck: Description validation result
```

**TitleCheck attributes:**
```python
result.title.value    # str | None: The title text
result.title.exists   # bool: Whether title tag exists
result.title.length   # int: Character count
result.title.status   # str: "ideal", "warning", or "missing"
result.title.issues   # list[str]: List of validation issues
```

**DescriptionCheck attributes:**
```python
result.description.value    # str | None: The description text
result.description.exists   # bool: Whether meta description exists
result.description.length   # int: Character count
result.description.status   # str: "ideal", "warning", or "missing"
result.description.issues   # list[str]: List of validation issues
```

### Status Values

- `ideal` - Length is within recommended range
- `warning` - Length is outside recommended range
- `missing` - Tag not found

### SEO Guidelines

**Meta Title:**
- Ideal: 50-60 characters
- Warning: <30 or >65 characters

**Meta Description:**
- Ideal: 140-160 characters
- Warning: <70 or >165 characters

## Usage Examples

### Basic Usage

```python
from scripts import check_documentation_metadata

# Check a documentation page
result = check_documentation_metadata("https://docs.python.org/3/")

if result.success:
    print(f"Title: {result.title.value}")
    print(f"Status: {result.title.status}")
    print(f"Length: {result.title.length} chars")
    
    if result.title.issues:
        for issue in result.title.issues:
            print(f"Issue: {issue}")
else:
    print(f"Error: {result.error}")
```

### Check Multiple Pages

```python
from scripts import check_documentation_metadata

urls = [
    "https://docs.stripe.com/api",
    "https://docs.github.com/en",
    "https://docs.aws.amazon.com/"
]

for url in urls:
    result = check_documentation_metadata(url)
    print(f"\n{url}")
    print(f"  Title: {result.title.status}")
    print(f"  Description: {result.description.status}")
```

### Custom Parameters

```python
from scripts import check_documentation_metadata

# Custom timeout for slow sites
result = check_documentation_metadata(
    "https://docs.example.com",
    timeout=60
)

# Custom user agent
result = check_documentation_metadata(
    "https://docs.example.com",
    user_agent="MyBot/1.0"
)
```

### Detailed Analysis

```python
from scripts import check_documentation_metadata

result = check_documentation_metadata("https://docs.example.com")

if result.success:
    # Title analysis
    if result.title.exists:
        print(f"✓ Title found: {result.title.value}")
        print(f"  Length: {result.title.length} chars")
        if result.title.status == "ideal":
            print("  ✓ Length is ideal for SEO")
        else:
            print(f"  ⚠️  {', '.join(result.title.issues)}")
    else:
        print("❌ Title is missing")
    
    # Description analysis
    if result.description.exists:
        print(f"\n✓ Description found: {result.description.value}")
        print(f"  Length: {result.description.length} chars")
        if result.description.status == "ideal":
            print("  ✓ Length is ideal for SEO")
        else:
            print(f"  ⚠️  {', '.join(result.description.issues)}")
    else:
        print("\n❌ Description is missing")
```

### JSON Serialization

```python
import json
from scripts import check_documentation_metadata

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

## Response Format Guidelines

When presenting results to users:
- Show title and description values
- Highlight character counts
- Explain status (ideal/warning/missing)
- Provide specific recommendations from the issues list
- Use clear visual indicators (✓, ⚠️, ❌)

## Error Handling

All errors are returned in the `CheckResult` object with `success=False` and an error message. No exceptions are raised.

### Invalid Protocol

```python
result = check_documentation_metadata("ftp://example.com")
# result.success == False
# result.error == "Invalid URL protocol (must be HTTP or HTTPS)"
```

### Network Error

```python
result = check_documentation_metadata("https://nonexistent.example.com")
# result.success == False
# result.error == "Failed to fetch URL: Connection timeout"
```

### Parse Error

```python
result = check_documentation_metadata("https://example.com/invalid")
# result.success == False
# result.error == "Failed to parse HTML: Invalid document"
```

## Limitations

- Only checks meta title and description (not other tags like Open Graph, Twitter Cards)
- Requires HTTP/HTTPS URLs (no file:// or ftp://)
- Does not handle JavaScript-rendered content (requires static HTML)
- Does not analyze content quality or keyword optimization
- No batch processing in single call (use a loop for multiple URLs)

## Data Models

### CheckResult

```python
@dataclass
class CheckResult:
    url: str
    title: TitleCheck
    description: DescriptionCheck
    success: bool
    error: Optional[str]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
```

### TitleCheck

```python
@dataclass
class TitleCheck:
    value: Optional[str]
    exists: bool
    length: int
    status: str
    issues: List[str]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
```

### DescriptionCheck

```python
@dataclass
class DescriptionCheck:
    value: Optional[str]
    exists: bool
    length: int
    status: str
    issues: List[str]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
```

## Importing Models

```python
from scripts import (
    check_documentation_metadata,
    CheckResult,
    TitleCheck,
    DescriptionCheck
)
```

## For Manual Installation (Human Users Only)

**Note for AI Agents:** Skip this section. Dependencies are already installed in your environment.

If you need to manually install this skill for use outside of an AI agent environment, ensure the skill package is in your Python path:

```python
import sys
from pathlib import Path
sys.path.insert(0, "path/to/skills/doc-metadata-analyzer")
```

Then install the required dependencies:

```bash
cd skills/doc-metadata-analyzer
pip install -r requirements.txt
```
