# DOCX to Markdown Converter

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

## Installation

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Install Dependencies

```bash
cd skills/docx-to-md
pip install -r requirements.txt
```

## Project Structure

```
docx-to-md/
├── src/
│   └── docx_to_md/
│       ├── __init__.py
│       ├── dom.py              # Document Object Model
│       ├── errors.py           # Error handling
│       ├── utils.py            # Utility functions
│       └── handlers/           # Format handlers (planned)
├── tests/
│   ├── __init__.py
│   └── test_formatting_properties.py
├── README.md                   # This file
└── requirements.txt            # Python dependencies
```

## Development

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src.docx_to_md

# Run property-based tests
pytest tests/test_formatting_properties.py -v
```

### Current Implementation

**Completed:**
- ✅ DOM structure (Node, TextNode, ElementNode)
- ✅ Error handling (ConversionError, UnsupportedElementError)
- ✅ Configuration system
- ✅ Utility functions (escape_markdown)
- ✅ Property-based tests for utilities

**In Progress:**
- 🚧 Parser layer implementation
- 🚧 Generator layer implementation

## Specification

This skill is being developed following the spec-driven development methodology. See `.kiro/specs/docx-to-md/` for:
- `requirements.md` - Feature requirements
- `design.md` - Technical design and architecture
- `tasks.md` - Implementation task list

## License

MIT License

## Related Skills

- **doc-metadata-analyzer**: Documentation metadata checker
- Part of the multi-skill MCP repository
