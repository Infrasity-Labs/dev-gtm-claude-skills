# Infrasity AI Skills

Production-grade AI skills built for developer GTM, GEO (Generative Engine Optimization), AI discoverability, and technical content workflows.

These skills are designed to help developer-focused companies improve:

- AI visibility
- LLM discoverability
- Documentation quality
- SERP performance
- Technical content operations
- Developer marketing workflows

Compatible with:
- Claude
- Cursor
- Kiro
- Windsurf
- Copilot
- Internal AI agents
- Custom automation pipelines

---
# Current Skills

## doc-metadata-analyzer

Audit technical documentation pages for metadata quality, SERP optimization, and discoverability readiness.

### Capabilities

- Extracts meta titles and descriptions
- Detects missing metadata
- Validates SEO best-practice limits
- Identifies weak or low-information metadata
- Returns structured machine-readable reports
- Designed specifically for developer documentation ecosystems


## Example Output

```json
{
  "url": "https://docs.example.com/auth",
  "meta_title": {
    "value": "Authentication API Documentation",
    "exists": true,
    "length": 34,
    "status": "warning",
    "issues": [
        "Title too short"
    ]
  },
  "meta_description": {
    "value": "Learn how to authenticate with the API.",
    "exists": true,
    "length": 42,
    "status": "warning",
    "issues": [
        "Description too short"
    ]
  }
}
```
---
## DOCX to Markdown Converter

Convert Microsoft Word (.docx) files to clean Markdown (.md) files with proper formatting preservation.

## Status

🚧 **In Development** - This skill is currently being built.

## Planned Features

- ✅ **DOM-based Architecture**: Clean separation between parsing and generation
- ✅ **Format Preservation**: Maintain headings, lists, tables, bold, italic, code
- ✅ **Error Handling**: Graceful handling of unsupported elements
- ✅ **Property-Based Testing**: Comprehensive test coverage with Hypothesis
- 🚧 **Parser Layer**: DOCX file parsing (in progress)
- 🚧 **Generator Layer**: Markdown generation (planned)
- 🚧 **CLI Interface**: Command-line tool (planned)
---

# Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/infrasity-ai-skills.git
```

### 2. Choose a skill

```
cd infrasity-ai-skills/skills/doc-metadata-analyzer
```

### 3. Add skill to your AI agent

```
cp -r doc-metadata-analyzer /path-to-agent/skills/
```