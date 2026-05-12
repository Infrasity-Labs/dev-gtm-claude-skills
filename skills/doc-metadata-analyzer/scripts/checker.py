"""Metadata checker for documentation pages."""

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
    def __init__(self, timeout: int = 30, user_agent: str = "DocMetadataChecker/1.0"):
        self.timeout = timeout
        self.user_agent = user_agent
    
    def check_url(self, url: str) -> CheckResult:
        if not self._validate_url(url):
            return CheckResult(
                url=url,
                title=TitleCheck(None, False, 0, "missing", ["Invalid URL protocol (must be HTTP or HTTPS)"]),
                description=DescriptionCheck(None, False, 0, "missing", []),
                success=False,
                error="Invalid URL protocol (must be HTTP or HTTPS)"
            )
        
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
        try:
            parsed = urlparse(url)
            return parsed.scheme in ('http', 'https')
        except Exception:
            return False
    
    def _fetch_html(self, url: str) -> str:
        headers = {'User-Agent': self.user_agent}
        response = requests.get(url, headers=headers, timeout=self.timeout)
        response.raise_for_status()
        return response.text
    
    def _extract_metadata(self, html: str) -> Tuple[Optional[str], Optional[str]]:
        soup = BeautifulSoup(html, 'html.parser')
        
        title = None
        title_tag = soup.find('title')
        if title_tag:
            title = self._normalize_whitespace(title_tag.get_text())
        
        description = None
        desc_tag = soup.find('meta', attrs={'name': 'description'})
        if desc_tag and desc_tag.get('content'):
            description = self._normalize_whitespace(desc_tag['content'])
        
        return title, description
    
    def _normalize_whitespace(self, text: str) -> str:
        if not text:
            return ""
        return ' '.join(text.split()).strip()
    
    def _validate_title(self, title: Optional[str]) -> TitleCheck:
        if not title:
            return TitleCheck(
                value=None,
                exists=False,
                length=0,
                status="missing",
                issues=["Title is missing"]
            )
        
        length = len(title)
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
        if not description:
            return DescriptionCheck(
                value=None,
                exists=False,
                length=0,
                status="missing",
                issues=["Description is missing"]
            )
        
        length = len(description)
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
