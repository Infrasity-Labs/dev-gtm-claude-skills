# Documentation Metadata Analyzer

A Python agent skill that enables AI agents to check documentation pages for proper SEO metadata. Validates meta titles and meta descriptions against SEO best practices.

## Features

- ✅ **Meta Title Validation**: Checks existence and character length (ideal: 50-60 chars)
- ✅ **Meta Description Validation**: Checks existence and character length (ideal: 140-160 chars)
- ✅ **SEO Best Practices**: Validates against search engine optimization guidelines
- ✅ **Simple Python API**: Direct function calls without protocol complexity
- ✅ **Clear Responses**: Structured result objects with actionable recommendations

## Installation

### Method 1: Clone Repository

```bash
# Clone the entire repository
git clone https://github.com/infrasity-labs/dev-gtm-claude-skills.git
cd dev-gtm-claude-skills/skills/doc-metadata-analyzer

# Add skill to Claude
Create a .zip file of /doc-metadata-analyzer
Upload the .zip file to Claude

# Test it works
Analyse metadata for https://docs.example.com/
```

<p align="center">
  <a href="./assets/doc-metadata-analyzer-video.mp4">
    <img 
      src="./assets/doc-metadata-analyzer-video.gif" 
      width="100%" 
      alt="Documentation Metadata Analyzer Demo"
    />
  </a>
</p>

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

