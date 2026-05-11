# Documentation Metadata Analyzer

An MCP (Model Context Protocol) server that enables AI agents to check documentation pages for proper SEO metadata. Validates meta titles and meta descriptions against SEO best practices.

## Features

- ✅ **Meta Title Validation**: Checks existence and character length (ideal: 50-60 chars)
- ✅ **Meta Description Validation**: Checks existence and character length (ideal: 140-160 chars)
- ✅ **SEO Best Practices**: Validates against search engine optimization guidelines
- ✅ **MCP Protocol**: Works with Claude, Kiro, and other MCP-compatible AI agents
- ✅ **Clear Responses**: Structured JSON output with actionable recommendations

## Installation

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Install Dependencies

```bash
cd skills/doc-metadata-analyzer
pip install -r requirements.txt
```

### Required Packages

- `mcp>=1.0.0` - Model Context Protocol SDK
- `requests>=2.31.0` - HTTP requests
- `beautifulsoup4>=4.12.0` - HTML parsing
- `lxml>=4.9.0` - Fast HTML parser

## Usage

### Running the MCP Server

```bash
# From the skill directory
python -m src.doc_metadata_analyzer.server
```

The server will start and listen for MCP protocol messages via stdio.

### Connecting from AI Agents

#### Kiro Configuration

Add to `~/.kiro/settings/mcp.json`:

```json
{
  "mcpServers": {
    "doc-metadata-analyzer": {
      "command": "/path/to/venv/bin/python3",
      "args": ["-m", "src.doc_metadata_analyzer.server"],
      "cwd": "/absolute/path/to/skills/doc-metadata-analyzer",
      "env": {},
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

#### Claude Desktop Configuration

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "doc-metadata-analyzer": {
      "command": "python",
      "args": ["-m", "src.doc_metadata_analyzer.server"],
      "cwd": "/absolute/path/to/skills/doc-metadata-analyzer"
    }
  }
}
```

### Using with AI Agents

Once configured, you can ask your AI agent:

```
Check the metadata for https://docs.python.org/3/
```

Or:

```
Can you analyze the SEO metadata for https://stripe.com/docs/api?
```

## Tool Reference

### check_documentation_metadata

Checks if a documentation page has proper meta title and description with correct character lengths.

**Input:**
```json
{
  "url": "https://docs.example.com/page"
}
```

**Output:**
```json
{
  "url": "https://docs.example.com/page",
  "title": {
    "value": "Page Title",
    "exists": true,
    "length": 10,
    "status": "warning",
    "issues": ["Title too short (10 chars, recommended: 50-60)"]
  },
  "description": {
    "value": "Page description text...",
    "exists": true,
    "length": 150,
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
├── src/
│   └── doc_metadata_analyzer/
│       ├── __init__.py
│       ├── server.py          # MCP server implementation
│       ├── checker.py          # Metadata checking logic
│       ├── models.py           # Data models
│       └── constants.py        # SEO thresholds
├── test_mcp_server.py          # MCP integration tests
├── check_metadata.py           # Standalone test script
├── SKILL.md                    # Agent skill documentation
├── README.md                   # This file
└── requirements.txt            # Python dependencies
```

## Development

### Running Tests

```bash
# Run all tests
pytest test_mcp_server.py -v

# Run with coverage
pytest test_mcp_server.py --cov=src.doc_metadata_analyzer
```

### Testing the Checker

```bash
# Test with a real URL
python check_metadata.py https://docs.python.org/3/
```

## Troubleshooting

### Server Won't Start

**Issue**: `ModuleNotFoundError: No module named 'mcp'`

**Solution**: Install dependencies:
```bash
pip install -r requirements.txt
```

### AI Agent Can't Find the Tool

**Issue**: Tool doesn't appear in AI agent

**Solution**:
1. Check that the path in config is absolute
2. Restart the AI agent after config changes
3. Verify the server starts without errors:
   ```bash
   python -m src.doc_metadata_analyzer.server
   ```

### URL Fetch Errors

**Issue**: "Failed to fetch URL" errors

**Solution**:
- Verify the URL is accessible in a browser
- Check that the URL uses HTTP or HTTPS (not FTP, file://, etc.)
- Ensure you have internet connectivity
- Some sites may block automated requests

## Limitations

- Only checks meta title and description (not other metadata)
- Does not analyze content quality or semantic meaning
- Requires HTTP/HTTPS URLs
- Does not handle JavaScript-rendered content
- No support for batch processing multiple URLs in one call

## License

MIT License

## Related Skills

- **docx-to-md**: DOCX to Markdown converter
- Part of the multi-skill MCP repository
