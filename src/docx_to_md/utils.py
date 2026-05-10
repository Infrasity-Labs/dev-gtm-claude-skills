"""Utility functions and configuration for the DOCX to Markdown converter."""

from dataclasses import dataclass
from typing import Any


@dataclass
class ConverterConfig:
    """Configuration for converter behavior.
    
    Attributes:
        max_line_length: Maximum line length for wrapping (default: 120)
        list_indent_spaces: Number of spaces for list indentation (default: 2)
        use_fenced_code_blocks: Use fenced (```) vs indented code blocks (default: True)
        escape_special_chars: Escape special Markdown characters (default: True)
        line_ending: Line ending character(s) to use (default: LF)
        blank_lines_between_blocks: Number of blank lines between block elements (default: 1)
        log_unsupported_elements: Log warnings for unsupported elements (default: True)
    """
    max_line_length: int = 120
    list_indent_spaces: int = 2
    use_fenced_code_blocks: bool = True
    escape_special_chars: bool = True
    line_ending: str = "\n"  # LF
    blank_lines_between_blocks: int = 1
    log_unsupported_elements: bool = True


def escape_markdown(text: str) -> str:
    """Escape special Markdown characters in plain text.
    
    Escapes the following characters: \\ ` * _ { } [ ] ( ) # + - . ! |
    
    Args:
        text: The text to escape
        
    Returns:
        Text with special Markdown characters escaped
        
    Note:
        Backslash is escaped first to avoid double-escaping.
    """
    # Characters that need escaping in Markdown
    # Escape backslash first to avoid double-escaping
    special_chars = ['\\', '`', '*', '_', '{', '}', '[', ']', '(', ')', '#', '+', '-', '.', '!', '|']
    
    result = text
    for char in special_chars:
        result = result.replace(char, f'\\{char}')
    
    return result


def wrap_line(text: str, max_length: int = 120) -> str:
    """Wrap long lines at word boundaries.
    
    Args:
        text: The text to wrap
        max_length: Maximum line length (default: 120)
        
    Returns:
        Text wrapped at word boundaries
        
    Note:
        Does not wrap lines that contain Markdown syntax like tables or code.
        Does not break URLs or inline code.
    """
    # Don't wrap if line is already short enough
    if len(text) <= max_length:
        return text
    
    # Don't wrap lines with Markdown syntax that shouldn't be broken
    if any(marker in text for marker in ['|', '```', '    ']):
        return text
    
    # Don't wrap if line contains URLs (simple heuristic)
    if 'http://' in text or 'https://' in text:
        return text
    
    # Split at word boundaries
    words = text.split()
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        word_length = len(word)
        # +1 for the space
        if current_length + word_length + 1 > max_length and current_line:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_length = word_length
        else:
            current_line.append(word)
            current_length += word_length + (1 if current_line else 0)
    
    if current_line:
        lines.append(' '.join(current_line))
    
    return '\n'.join(lines)


def extract_text(element: Any) -> str:
    """Extract plain text from a DOCX element for fallback handling.
    
    This is a fallback function for extracting text from elements
    that have complex formatting or are not fully supported.
    
    Args:
        element: A DOCX element (from python-docx)
        
    Returns:
        Extracted plain text content
    """
    try:
        # Try to get text attribute directly
        if hasattr(element, 'text'):
            return element.text
        
        # Try to iterate through runs
        if hasattr(element, 'runs'):
            return ''.join(run.text for run in element.runs)
        
        # Try to iterate through paragraphs
        if hasattr(element, 'paragraphs'):
            return '\n'.join(para.text for para in element.paragraphs)
        
        # Fallback to string representation
        return str(element)
    except Exception:
        # If all else fails, return empty string
        return ''
