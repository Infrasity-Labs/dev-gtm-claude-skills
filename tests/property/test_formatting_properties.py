"""Property-based tests for Markdown formatting properties."""

from hypothesis import given, settings, strategies as st
import pytest

from docx_to_md.utils import escape_markdown


# Configure Hypothesis settings
settings.register_profile("default", max_examples=100, deadline=None)
settings.load_profile("default")


# Feature: docx-to-md, Property 25: Special Character Escaping
# **Validates: Requirements 14.4**
@given(text=st.text(alphabet=r"\`*_{}[]()#+-.!|", min_size=1, max_size=100))
def test_special_character_escaping(text: str):
    """For any text with special Markdown characters, the generator escapes them.
    
    Property 25: Special Character Escaping
    Validates: Requirements 14.4
    
    Tests that all Markdown special characters are properly escaped to prevent
    unintended formatting in the output.
    """
    escaped = escape_markdown(text)
    
    # Verify that each special character in the original text is escaped
    special_chars = r"\`*_{}[]()#+-.!|"
    for char in text:
        if char in special_chars:
            # The escaped version should contain the escaped form
            assert f'\\{char}' in escaped, f"Character '{char}' was not properly escaped"
    
    # Verify the escaped text is longer or equal (due to added backslashes)
    assert len(escaped) >= len(text), "Escaped text should be at least as long as original"


@given(text=st.text(min_size=0, max_size=100))
def test_escape_markdown_returns_string(text: str):
    """Escape markdown should always return a string."""
    result = escape_markdown(text)
    assert isinstance(result, str), "escape_markdown must return a string"


@given(text=st.text(alphabet=st.characters(blacklist_categories=('Cs',)), min_size=0, max_size=100))
def test_escape_markdown_preserves_non_special_chars(text: str):
    """Non-special characters should be preserved in the escaped output."""
    special_chars = r"\`*_{}[]()#+-.!|"
    
    # Filter out special characters from the input
    non_special_text = ''.join(c for c in text if c not in special_chars)
    
    if non_special_text:
        escaped = escape_markdown(non_special_text)
        # All non-special characters should appear in the output
        for char in non_special_text:
            assert char in escaped, f"Non-special character '{char}' was not preserved"


@given(text=st.text(min_size=0, max_size=50))
def test_escape_markdown_idempotent_structure(text: str):
    """Escaping twice should add more backslashes but maintain structure."""
    escaped_once = escape_markdown(text)
    escaped_twice = escape_markdown(escaped_once)
    
    # The second escape should be at least as long as the first
    assert len(escaped_twice) >= len(escaped_once), \
        "Double escaping should not reduce length"
