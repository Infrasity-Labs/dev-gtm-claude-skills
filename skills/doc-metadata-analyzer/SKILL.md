---
name: doc-metadata-analyzer
version: 1.0.0
description: Check documentation pages for SEO metadata compliance
author: Dev GTM
tags: [seo, metadata, documentation, validation]
mcp_server: true
---

# Documentation Metadata Analyzer

Checks documentation pages for proper meta title and description tags, validating them against SEO best practices.

## When to Use

Use this skill when you need to:
- Check if a documentation page has meta title and description
- Validate metadata character lengths for SEO
- Audit documentation sites for metadata compliance
- Get specific recommendations for improving metadata

## Tool: check_documentation_metadata

### Input

```json
{
  "url": "https://docs.example.com"
}
```

**Parameters:**
- `url` (string, required): Documentation page URL (HTTP/HTTPS only)

### Output

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

**Status values:**
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

### Check a single page

```
Check the metadata for https://docs.python.org/3/
```

### Audit multiple pages

```
Check the metadata for these URLs:
- https://docs.stripe.com/api
- https://docs.github.com/en
- https://docs.aws.amazon.com/
```

### Get recommendations

```
What's wrong with the metadata on https://example.com/docs?
```

## Response Format

When presenting results to users:
- Show title and description values
- Highlight character counts
- Explain status (ideal/warning/missing)
- Provide specific recommendations
- Use clear visual indicators (✓, ⚠️, ❌)

## Limitations

- Only checks meta title and description (not other tags)
- Requires HTTP/HTTPS URLs
- Does not handle JavaScript-rendered content
- Does not analyze content quality or keyword optimization
- No batch processing in single call

## Error Handling

**Invalid protocol:**
```json
{
  "success": false,
  "error": "Invalid URL protocol (must be HTTP or HTTPS)"
}
```

**Network error:**
```json
{
  "success": false,
  "error": "Failed to fetch URL: Connection timeout"
}
```

**Parse error:**
```json
{
  "success": false,
  "error": "Failed to parse HTML: Invalid document"
}
```
