# Documentation Metadata Checker

## Overview

This MCP server provides AI agents with the ability to check documentation pages for proper SEO metadata. It validates whether meta titles and meta descriptions exist and whether they meet recommended character length guidelines for optimal search engine visibility.

## When to Use This Skill

Use this skill when:
- A user asks to check if a documentation page has proper metadata
- A user wants to validate SEO metadata for documentation
- A user asks about meta title or meta description length
- A user wants to know if their documentation follows SEO best practices
- A user provides a documentation URL and asks about its metadata quality

## Tool: check_documentation_metadata

### Purpose

Checks if a documentation page has proper meta title and meta description, and validates their character lengths against SEO best practices.

### Input

```json
{
  "url": "https://docs.example.com/page"
}
```

**Parameters:**
- `url` (string, required): The documentation page URL to check. Must use HTTP or HTTPS protocol.

### Output

Returns a JSON object with validation results:

```json
{
  "url": "https://docs.example.com/page",
  "title": {
    "value": "Getting Started Guide",
    "exists": true,
    "length": 21,
    "status": "warning",
    "issues": ["Title too short (21 chars, recommended: 50-60)"]
  },
  "description": {
    "value": "Learn how to get started with our platform. This comprehensive guide covers installation, configuration, and your first steps.",
    "exists": true,
    "length": 142,
    "status": "ideal",
    "issues": []
  },
  "success": true,
  "error": null
}
```

**Response Fields:**
- `url`: The URL that was checked
- `title`: Title validation results
  - `value`: The extracted title text (null if missing)
  - `exists`: Whether the title exists (boolean)
  - `length`: Character count
  - `status`: "ideal", "warning", or "missing"
  - `issues`: Array of validation issues
- `description`: Description validation results (same structure as title)
- `success`: Whether the check completed successfully
- `error`: Error message if check failed (null if successful)

### SEO Best Practices

**Meta Title:**
- **Ideal length**: 50-60 characters
- **Warning threshold**: <30 or >65 characters
- **Why it matters**: Search engines typically display 50-60 characters in search results. Titles that are too short may not be descriptive enough, while titles that are too long get truncated.

**Meta Description:**
- **Ideal length**: 140-160 characters
- **Warning threshold**: <70 or >165 characters
- **Why it matters**: Search engines typically display 140-160 characters in search results. Descriptions that are too short don't provide enough context, while descriptions that are too long get cut off.

## Example Usage

### Example 1: Checking a Documentation Page

**User**: "Can you check the metadata for https://docs.stripe.com/api?"

**Agent Action**: Invoke `check_documentation_metadata` with `{"url": "https://docs.stripe.com/api"}`

**Agent Response**: 
```
I checked the metadata for the Stripe API documentation page:

✓ **Title**: "Stripe API Reference" (21 characters)
  - ⚠️ Warning: Title is too short (recommended: 50-60 characters)
  - Suggestion: Consider a more descriptive title like "Stripe API Reference - Complete Payment Integration Documentation"

✓ **Description**: "Complete reference documentation for the Stripe API..." (145 characters)
  - ✅ Ideal length

The page has both title and description, but the title could be more descriptive to improve SEO.
```

### Example 2: Missing Metadata

**User**: "Check https://example.com/docs"

**Agent Action**: Invoke `check_documentation_metadata` with `{"url": "https://example.com/docs"}`

**Agent Response**:
```
I checked the metadata for that page:

❌ **Title**: Missing
  - The page doesn't have a meta title tag

❌ **Description**: Missing
  - The page doesn't have a meta description tag

Both the title and description are missing. I recommend adding:
- A descriptive title (50-60 characters)
- A clear description (140-160 characters)
```

### Example 3: Invalid URL

**User**: "Check ftp://example.com/docs"

**Agent Action**: Invoke `check_documentation_metadata` with `{"url": "ftp://example.com/docs"}`

**Agent Response**:
```
I couldn't check that URL because it uses the FTP protocol. This tool only works with HTTP and HTTPS URLs. Please provide a web URL (starting with http:// or https://).
```

## Error Handling

The tool handles various error scenarios gracefully:

- **Invalid protocol**: Returns error if URL doesn't use HTTP/HTTPS
- **Network errors**: Returns error if page cannot be fetched (404, timeout, etc.)
- **Parse errors**: Returns error if HTML cannot be parsed
- **Missing metadata**: Returns validation results with "missing" status

All errors are returned in a structured format with clear error messages.

## Integration

### Claude Desktop Configuration

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "doc-metadata-checker": {
      "command": "python",
      "args": ["-m", "doc_metadata_analyzer.server"],
      "cwd": "/path/to/docx-to-md"
    }
  }
}
```

### Running the Server

```bash
# From the project directory
python -m doc_metadata_analyzer.server
```

## Limitations

- Only checks meta title and meta description (not other metadata)
- Does not analyze content quality or semantic meaning
- Does not check for generic terms or keyword optimization
- Requires HTTP/HTTPS URLs (no FTP, file://, etc.)
- Does not handle JavaScript-rendered content (checks static HTML only)

## Use Cases

1. **Documentation Audits**: Check multiple documentation pages for metadata compliance
2. **SEO Optimization**: Validate metadata before publishing documentation
3. **Quality Assurance**: Ensure all documentation pages have proper metadata
4. **Competitive Analysis**: Compare metadata across different documentation sites
5. **Migration Validation**: Verify metadata after documentation platform migrations

## Tips for AI Agents

- Always present results in a user-friendly format (not raw JSON)
- Highlight issues with clear visual indicators (✓, ⚠️, ❌)
- Provide specific, actionable recommendations
- Explain why metadata length matters for SEO
- Offer to check multiple pages if the user has a list
- Suggest improvements based on the validation results
