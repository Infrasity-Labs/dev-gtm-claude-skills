"""Document Object Model (DOM) for DOCX to Markdown conversion.

This module defines the intermediate representation used to represent
document structure between parsing and generation phases.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union


class ElementType(Enum):
    """Document element types."""
    DOCUMENT = "document"
    HEADING = "heading"
    PARAGRAPH = "paragraph"
    LIST = "list"
    LIST_ITEM = "list_item"
    TABLE = "table"
    TABLE_ROW = "table_row"
    TABLE_CELL = "table_cell"
    LINK = "link"
    CODE_BLOCK = "code_block"
    TEXT = "text"
    UNSUPPORTED = "unsupported"


class TextStyle(Enum):
    """Inline text formatting styles."""
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    BOLD_ITALIC = "bold_italic"


@dataclass
class DOMElement:
    """Base class for all DOM elements."""
    element_type: ElementType


@dataclass
class Document(DOMElement):
    """Root document element."""
    children: List[DOMElement] = field(default_factory=list)
    element_type: ElementType = field(default=ElementType.DOCUMENT, init=False)
    
    def __post_init__(self):
        if self.children is None:
            self.children = []


@dataclass
class Heading(DOMElement):
    """Heading element (H1-H6)."""
    level: int  # 1-6
    text: str
    element_type: ElementType = field(default=ElementType.HEADING, init=False)
    
    def __post_init__(self):
        if not 1 <= self.level <= 6:
            raise ValueError(f"Heading level must be 1-6, got {self.level}")


@dataclass
class TextRun:
    """Inline text with formatting."""
    text: str
    style: TextStyle = TextStyle.NORMAL


@dataclass
class Paragraph(DOMElement):
    """Paragraph element with inline formatting."""
    runs: List[TextRun] = field(default_factory=list)
    element_type: ElementType = field(default=ElementType.PARAGRAPH, init=False)
    
    def __post_init__(self):
        if self.runs is None:
            self.runs = []


@dataclass
class ListItem(DOMElement):
    """List item with optional nesting."""
    content: List[Union[Paragraph, 'List']] = field(default_factory=list)
    element_type: ElementType = field(default=ElementType.LIST_ITEM, init=False)
    
    def __post_init__(self):
        if self.content is None:
            self.content = []


@dataclass
class List(DOMElement):
    """List element (ordered or unordered)."""
    ordered: bool
    items: List[ListItem] = field(default_factory=list)
    element_type: ElementType = field(default=ElementType.LIST, init=False)
    
    def __post_init__(self):
        if self.items is None:
            self.items = []


@dataclass
class TableCell(DOMElement):
    """Table cell."""
    content: List[Union[Paragraph, List]] = field(default_factory=list)
    element_type: ElementType = field(default=ElementType.TABLE_CELL, init=False)
    
    def __post_init__(self):
        if self.content is None:
            self.content = []


@dataclass
class TableRow(DOMElement):
    """Table row."""
    cells: List[TableCell] = field(default_factory=list)
    element_type: ElementType = field(default=ElementType.TABLE_ROW, init=False)
    
    def __post_init__(self):
        if self.cells is None:
            self.cells = []


@dataclass
class Table(DOMElement):
    """Table element."""
    rows: List[TableRow] = field(default_factory=list)
    has_header: bool = True
    element_type: ElementType = field(default=ElementType.TABLE, init=False)
    
    def __post_init__(self):
        if self.rows is None:
            self.rows = []


@dataclass
class Link(DOMElement):
    """Hyperlink element."""
    url: str
    text: str
    element_type: ElementType = field(default=ElementType.LINK, init=False)


@dataclass
class CodeBlock(DOMElement):
    """Code block element."""
    code: str
    language: Optional[str] = None
    element_type: ElementType = field(default=ElementType.CODE_BLOCK, init=False)


@dataclass
class UnsupportedElement(DOMElement):
    """Placeholder for unsupported elements."""
    description: str
    original_type: str
    element_type: ElementType = field(default=ElementType.UNSUPPORTED, init=False)
