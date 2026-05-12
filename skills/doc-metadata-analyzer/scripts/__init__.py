"""
Documentation Metadata Checker

A Python agent skill to validate SEO metadata on documentation pages.
"""

__version__ = "1.0.0"

from .checker import MetadataChecker
from .models import CheckResult, TitleCheck, DescriptionCheck

__all__ = [
    'check_documentation_metadata',
    'CheckResult',
    'TitleCheck',
    'DescriptionCheck',
]


def check_documentation_metadata(
    url: str,
    timeout: int = 30,
    user_agent: str = "DocMetadataChecker/1.0"
) -> CheckResult:
    """
    Check documentation page metadata for SEO compliance.
    
    Validates meta title and meta description tags against SEO best practices.
    Returns structured results including existence checks, character length analysis,
    and specific recommendations for improvement.
    
    Args:
        url: The documentation page URL to check (must be HTTP or HTTPS)
        timeout: Request timeout in seconds (default: 30)
        user_agent: User agent string for HTTP requests (default: "DocMetadataChecker/1.0")
    
    Returns:
        CheckResult object containing validation results for title and description.
        The result includes:
        - url: The checked URL
        - title: TitleCheck with value, length, status, and issues
        - description: DescriptionCheck with value, length, status, and issues
        - success: Boolean indicating if check completed successfully
        - error: Error message if success is False, None otherwise
    
    SEO Guidelines:
        Meta Title:
        - Ideal: 50-60 characters
        - Warning: <30 or >65 characters
        
        Meta Description:
        - Ideal: 140-160 characters
        - Warning: <70 or >165 characters
    
    Example:
        >>> from doc_metadata_analyzer import check_documentation_metadata
        >>> result = check_documentation_metadata("https://docs.python.org/3/")
        >>> if result.success:
        ...     print(f"Title: {result.title.value}")
        ...     print(f"Title Status: {result.title.status}")
        ...     print(f"Description: {result.description.value}")
        ...     print(f"Description Status: {result.description.status}")
        ...     if result.title.issues:
        ...         for issue in result.title.issues:
        ...             print(f"Title Issue: {issue}")
        ... else:
        ...     print(f"Error: {result.error}")
    
    Raises:
        No exceptions are raised. All errors are returned in the CheckResult object
        with success=False and an error message.
    """
    checker = MetadataChecker(timeout=timeout, user_agent=user_agent)
    return checker.check_url(url)
