<!-- # MCP Skills Repository

A collection of MCP (Model Context Protocol) skills for AI agents like Claude, Kiro, and other MCP-compatible agents.

## Available Skills

### 1. Documentation Metadata Analyzer ✅

Check documentation pages for proper SEO metadata (meta title and description).

**Status**: Production Ready  
**Location**: `skills/doc-metadata-analyzer/`  
**Documentation**: [README](skills/doc-metadata-analyzer/README.md) | [SKILL.md](skills/doc-metadata-analyzer/SKILL.md)

**Features:**
- Meta title validation (ideal: 50-60 chars)
- Meta description validation (ideal: 140-160 chars)
- SEO best practices checking
- Structured JSON responses

**Quick Start:**
```bash
cd skills/doc-metadata-analyzer
pip install -r requirements.txt
python -m src.doc_metadata_analyzer.server
```

---

### 2. DOCX to Markdown Converter 🚧

Convert Microsoft Word (.docx) files to clean Markdown (.md) files.

**Status**: In Development  
**Location**: `skills/docx-to-md/`  
**Documentation**: [README](skills/docx-to-md/README.md)

**Planned Features:**
- DOM-based architecture
- Format preservation (headings, lists, tables, bold, italic, code)
- Error handling for unsupported elements
- Property-based testing

**Quick Start:**
```bash
cd skills/docx-to-md
pip install -r requirements.txt
pytest tests/ -v
```

---

## Repository Structure

```
mcp-skills/
├── skills/                          # All skills
│   ├── doc-metadata-analyzer/       # ✅ Production ready
│   │   ├── src/
│   │   ├── README.md
│   │   ├── SKILL.md
│   │   └── requirements.txt
│   │
│   └── docx-to-md/                  # 🚧 In development
│       ├── src/
│       ├── tests/
│       ├── README.md
│       └── requirements.txt
│
├── .kiro/                           # Kiro workspace config
│   ├── specs/                       # Skill specifications
│   └── settings/                    # MCP server configs
│
├── docs/                            # Shared documentation
│   ├── MCP_SUPPORTED_AI_AGENTS.md
│   └── KIRO_MCP_SETUP.md
│
├── README.md                        # This file
└── venv/                            # Shared virtual environment
```

## Getting Started

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- An MCP-compatible AI agent (Claude Desktop, Kiro, Cline, Continue, Cursor, etc.)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd mcp-skills
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate  # On Windows
   ```

3. **Install a skill:**
   ```bash
   cd skills/doc-metadata-analyzer
   pip install -r requirements.txt
   ```

### Configuration

Each skill can be configured as an MCP server in your AI agent. See:
- [Kiro Setup Guide](docs/KIRO_MCP_SETUP.md)
- [Supported AI Agents](docs/MCP_SUPPORTED_AI_AGENTS.md)

**Example Kiro Configuration** (`~/.kiro/settings/mcp.json`):

```json
{
  "mcpServers": {
    "doc-metadata-analyzer": {
      "command": "/path/to/venv/bin/python3",
      "args": ["-m", "src.doc_metadata_analyzer.server"],
      "cwd": "/absolute/path/to/skills/doc-metadata-analyzer",
      "disabled": false
    }
  }
}
```

## Development

### Adding a New Skill

1. Create a new directory in `skills/`
2. Follow the structure:
   ```
   skills/your-skill/
   ├── src/
   │   └── your_skill/
   │       ├── __init__.py
   │       └── server.py
   ├── tests/
   ├── README.md
   ├── SKILL.md
   └── requirements.txt
   ```
3. Implement the MCP server in `server.py`
4. Add tests
5. Document in README.md and SKILL.md

### Testing

Each skill has its own test suite:

```bash
# Test doc-metadata-analyzer
cd skills/doc-metadata-analyzer
pytest test_mcp_server.py -v

# Test docx-to-md
cd skills/docx-to-md
pytest tests/ -v
```

### Spec-Driven Development

This repository uses spec-driven development methodology. Specifications are in `.kiro/specs/`:

- `requirements.md` - Feature requirements
- `design.md` - Technical design and architecture
- `tasks.md` - Implementation task list

## Documentation

- **[MCP Supported AI Agents](docs/MCP_SUPPORTED_AI_AGENTS.md)** - List of AI agents that support MCP
- **[Kiro MCP Setup](docs/KIRO_MCP_SETUP.md)** - How to configure skills in Kiro
- **Individual Skill READMEs** - See each skill's directory

## Contributing

1. Follow the existing skill structure
2. Add comprehensive tests
3. Document your skill (README.md and SKILL.md)
4. Use spec-driven development for complex features
5. Ensure all tests pass before submitting

## License

MIT License

## Support

For issues or questions:
1. Check the skill-specific README
2. Review the shared documentation in `docs/`
3. Check the MCP protocol documentation

## Roadmap

- ✅ Documentation Metadata Analyzer (v1.0)
- 🚧 DOCX to Markdown Converter (in progress)
- 📋 Future skills: TBD

## Related Projects

- [Model Context Protocol](https://modelcontextprotocol.io/) - Official MCP documentation
- [Claude Desktop](https://claude.ai/download) - AI agent with MCP support
- [Kiro](https://kiro.ai/) - AI-powered development environment -->
