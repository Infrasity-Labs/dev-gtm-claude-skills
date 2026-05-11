"""
Metadata checker for Documentation Metadata Checker MCP Server.

This module provides the core logic for fetching documentation pages,
extracting metadata, and validating character lengths.
"""

from typing import Optional, Tuple
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

from .models import CheckResult, TitleCheck, DescriptionCheck
from .constants import (
    IDEAL_TITLE_MIN,
    IDEAL_TITLE_MAX,
    TITLE_WARNING_MIN,
    TITLE_WARNING_MAX,
    IDEAL_DESC_MIN,
    IDEAL_DESC_MAX,
    DESC_WARNING_MIN,
    DESC_WARNING_MAX
)


class MetadataChecker:
    """Checks documentation metadata for SEO compliance.
    
    This class fetches HTML from URLs, extracts meta title and description,
    and validates them against SEO best practices for character length.
    """
    
    def __init__(self, timeout: int = 30, user_agent: str = "DocMetadataChecker/1.0"):
        """Initialize the metadata checker.
        
        Args:
            timeout: Request timeout in seconds (default: 30)
            user_agent: User agent string for HTTP requests
        """
        self.timeout = timeout
        self.user_agent = user_agent
    
    def check_url(self, url: str) -> CheckResult:
        """Check metadata for a documentation URL.
        
        This is the main entry point that orchestrates the entire checking process:
        1. Validate URL protocol
        2. Fetch HTML content
        3. Extract metadata
        4. Validate metadata
        5. Return structured result
        
        Args:
            url: The documentation page URL to check
        
        Returns:
            CheckResult with validation results or error information
        """
        # Validate URL protocol
        if not self._validate_url(url):
            return CheckResult(
                url=url,
                title=TitleCheck(None, False, 0, "missing", ["Invalid URL protocol (must be HTTP or HTTPS)"]),
                description=DescriptionCheck(None, False, 0, "missing", []),
                success=False,
                error="Invalid URL protocol (must be HTTP or HTTPS)"
            )
        
        # Fetch HTML
        try:
            html = self._fetch_html(url)
        except Exception as e:
            return CheckResult(
                url=url,
                title=TitleCheck(None, False, 0, "missing", []),
                description=DescriptionCheck(None, False, 0, "missing", []),
                success=False,
                error=f"Failed to fetch URL: {str(e)}"
            )
        
        # Extract metadata
        try:
            title, description = self._extract_metadata(html)
        except Exception as e:
            return CheckResult(
                url=url,
                title=TitleCheck(None, False, 0, "missing", []),
                description=DescriptionCheck(None, False, 0, "missing", []),
                success=False,
                error=f"Failed to parse HTML: {str(e)}"
            )
        
        # Validate metadata
        title_check = self._validate_title(title)
        description_check = self._validate_description(description)
        
        return CheckResult(
            url=url,
            title=title_check,
            description=description_check,
            success=True,
            error=None
        )
    
    def _validate_url(self, url: str) -> bool:
        """Validate that URL uses HTTP or HTTPS protocol.
        
        Args:
            url: URL to validate
        
        Returns:
            True if URL uses HTTP or HTTPS, False otherwise
        """
        try:
            parsed = urlparse(url)
            return parsed.scheme in ('http', 'https')
        except Exception:
            return False
    
    def _fetch_html(self, url: str) -> str:
        """Fetch HTML content from URL.
        
        Args:
            url: URL to fetch
        
        Returns:
            HTML content as string
        
        Raises:
            requests.RequestException: If fetch fails
        """
        headers = {
            'User-Agent': self.user_agent
        }
        
        response = requests.get(url, headers=headers, timeout=self.timeout)
        response.raise_for_status()
        
        return response.text
    
    def _extract_metadata(self, html: str) -> Tuple[Optional[str], Optional[str]]:
        """Extract meta title and description from HTML.
        
        Args:
            html: HTML content to parse
        
        Returns:
            Tuple of (title, description), either can be None if not found
        """
        soup = BeautifulSoup(html, 'lxml')
        
        # Extract title from <title> tag
        title = None
        title_tag = soup.find('title')
        if title_tag and title_tag.string:
            title = self._normalize_whitespace(title_tag.string)
        
        # Extract description from <meta name="description"> tag
        description = None
        desc_tag = soup.find('meta', attrs={'name': 'description'})
        if desc_tag and desc_tag.get('content'):
            description = self._normalize_whitespace(desc_tag['content'])
        
        return title, description
    
    def _normalize_whitespace(self, text: str) -> str:
        """Normalize whitespace in text.
        
        Removes leading/trailing whitespace and collapses multiple
        whitespace characters into single spaces.
        
        Args:
            text: Text to normalize
        
        Returns:
            Normalized text
        """
        if not text:
            return ""
        
        # Replace all whitespace (including newlines, tabs) with single spaces
        normalized = ' '.join(text.split())
        
        return normalized.strip()
    
    def _validate_title(self, title: Optional[str]) -> TitleCheck:
        """Validate meta title.
        
        Checks:
        - Existence
        - Character length against SEO thresholds
        
        Args:
            title: Title to validate (can be None)
        
        Returns:
            TitleCheck with validation results
        """
        # Handle missing title
        if not title:
            return TitleCheck(
                value=None,
                exists=False,
                length=0,
                status="missing",
                issues=["Title is missing"]
            )
        
        # Calculate length
        length = len(title)
        
        # Determine status and issues
        issues = []
        
        if IDEAL_TITLE_MIN <= length <= IDEAL_TITLE_MAX:
            status = "ideal"
        elif length < TITLE_WARNING_MIN:
            status = "warning"
            issues.append(f"Title too short ({length} chars, recommended: {IDEAL_TITLE_MIN}-{IDEAL_TITLE_MAX})")
        elif length > TITLE_WARNING_MAX:
            status = "warning"
            issues.append(f"Title too long ({length} chars, recommended: {IDEAL_TITLE_MIN}-{IDEAL_TITLE_MAX})")
        else:
            # Length is in warning range but not ideal
            status = "warning"
            if length < IDEAL_TITLE_MIN:
                issues.append(f"Title slightly short ({length} chars, ideal: {IDEAL_TITLE_MIN}-{IDEAL_TITLE_MAX})")
            else:
                issues.append(f"Title slightly long ({length} chars, ideal: {IDEAL_TITLE_MIN}-{IDEAL_TITLE_MAX})")
        
        return TitleCheck(
            value=title,
            exists=True,
            length=length,
            status=status,
            issues=issues
        )
    
    def _validate_description(self, description: Optional[str]) -> DescriptionCheck:
        """Validate meta description.
        
        Checks:
        - Existence
        - Character length against SEO thresholds
        
        Args:
            description: Description to validate (can be None)
        
        Returns:
            DescriptionCheck with validation results
        """
        # Handle missing description
        if not description:
            return DescriptionCheck(
                value=None,
                exists=False,
                length=0,
                status="missing",
                issues=["Description is missing"]
            )
        
        # Calculate length
        length = len(description)
        
        # Determine status and issues
        issues = []
        
        if IDEAL_DESC_MIN <= length <= IDEAL_DESC_MAX:
            status = "ideal"
        elif length < DESC_WARNING_MIN:
            status = "warning"
            issues.append(f"Description too short ({length} chars, recommended: {IDEAL_DESC_MIN}-{IDEAL_DESC_MAX})")
        elif length > DESC_WARNING_MAX:
            status = "warning"
            issues.append(f"Description too long ({length} chars, recommended: {IDEAL_DESC_MIN}-{IDEAL_DESC_MAX})")
        else:
            # Length is in warning range but not ideal
            status = "warning"
            if length < IDEAL_DESC_MIN:
                issues.append(f"Description slightly short ({length} chars, ideal: {IDEAL_DESC_MIN}-{IDEAL_DESC_MAX})")
            else:
                issues.append(f"Description slightly long ({length} chars, ideal: {IDEAL_DESC_MIN}-{IDEAL_DESC_MAX})")
        
        return DescriptionCheck(
            value=description,
            exists=True,
            length=length,
            status=status,
            issues=issues
        )
