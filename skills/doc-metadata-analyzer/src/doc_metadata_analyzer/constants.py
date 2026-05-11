"""
Constants for Documentation Metadata Checker MCP Server.

This module defines character length thresholds for SEO metadata validation.
"""

# ============================================================================
# Title Length Thresholds
# ============================================================================

IDEAL_TITLE_MIN = 50
"""Minimum character length for an ideal meta title."""

IDEAL_TITLE_MAX = 60
"""Maximum character length for an ideal meta title."""

TITLE_WARNING_MIN = 30
"""Minimum character length before issuing a warning for meta title."""

TITLE_WARNING_MAX = 65
"""Maximum character length before issuing a warning for meta title."""


# ============================================================================
# Description Length Thresholds
# ============================================================================

IDEAL_DESC_MIN = 140
"""Minimum character length for an ideal meta description."""

IDEAL_DESC_MAX = 160
"""Maximum character length for an ideal meta description."""

DESC_WARNING_MIN = 70
"""Minimum character length before issuing a warning for meta description."""

DESC_WARNING_MAX = 165
"""Maximum character length before issuing a warning for meta description."""
