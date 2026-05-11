# Dev GTM Claude Skills

A collection of MCP servers I built to extend Claude and other AI agents with useful capabilities for developers and technical writers.

## What's Here

### doc-metadata-analyzer

Checks documentation pages for SEO metadata. I got tired of manually inspecting meta tags, so I built this to let Claude do it for me.

**What it does:**
- Fetches any documentation URL
- Extracts meta title and description
- Validates against SEO best practices (50-60 chars for titles, 140-160 for descriptions)
- Returns structured results with specific recommendations

**Status:** Working and tested  
**Details:** [skills/doc-metadata-analyzer](skills/doc-metadata-analyzer)

<!-- ### docx-to-md

Converts Word documents to Markdown. Still working on this one.

**Status:** In progress  
**Details:** [skills/docx-to-md](skills/docx-to-md) -->

## Using These Skills

Each skill is an MCP server that works with Claude Desktop, Kiro, and other MCP-compatible agents.

### Quick setup for doc-metadata-analyzer:

1. Install dependencies:
```bash
cd skills/doc-metadata-analyzer
pip install -r requirements.txt
```

2. Add to your MCP config:

**For Claude Desktop** (`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):
```json
{
  "mcpServers": {
    "doc-metadata-analyzer": {
      "command": "python3",
      "args": ["-m", "src.doc_metadata_analyzer.server"],
      "cwd": "/absolute/path/to/dev-gtm-claude-skills/skills/doc-metadata-analyzer"
    }
  }
}
```

3. Restart your agent and ask it to check a URL:
```
Check the metadata for https://docs.python.org/3/
```

See individual skill directories for detailed setup instructions.

## Why MCP?

MCP (Model Context Protocol) lets you extend AI agents with custom tools. Instead of copy-pasting URLs and manually checking things, you can ask Claude to do it and get structured results back.

These skills are things I needed for my own work. If they're useful to you too, great.

## Requirements

- Python 3.9+
- An MCP-compatible AI agent (Claude Desktop, Kiro, etc.)

## Structure

```
dev-gtm-claude-skills/
├── skills/
│   ├── doc-metadata-analyzer/     # SEO metadata checker
│   └── docx-to-md/                # Word to Markdown converter
├── README.md                      # Setup guides
```

## Contributing

Found a bug? Have an idea? Open an issue or PR.

