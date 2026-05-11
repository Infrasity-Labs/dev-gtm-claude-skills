"""
Data models for Documentation Metadata Checker MCP Server.

This module defines the data structures used for metadata validation results.
"""

from dataclasses import dataclass
from typing import Optional, List, Dict, Any


@dataclass
class TitleCheck:
    """Meta title validation result.
    
    Attributes:
        value: The extracted title text (None if missing)
        exists: Whether the title exists
        length: Character length of the title
        status: Validation status ("ideal", "warning", "missing")
        issues: List of validation issues found
    """
    value: Optional[str]
    exists: bool
    length: int
    status: str  # "ideal", "warning", "missing"
    issues: List[str]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization.
        
        Returns:
            Dictionary representation of the title check result
        """
        return {
            "value": self.value,
            "exists": self.exists,
            "length": self.length,
            "status": self.status,
            "issues": self.issues
        }


@dataclass
class DescriptionCheck:
    """Meta description validation result.
    
    Attributes:
        value: The extracted description text (None if missing)
        exists: Whether the description exists
        length: Character length of the description
        status: Validation status ("ideal", "warning", "missing")
        issues: List of validation issues found
    """
    value: Optional[str]
    exists: bool
    length: int
    status: str  # "ideal", "warning", "missing"
    issues: List[str]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization.
        
        Returns:
            Dictionary representation of the description check result
        """
        return {
            "value": self.value,
            "exists": self.exists,
            "length": self.length,
            "status": self.status,
            "issues": self.issues
        }


@dataclass
class CheckResult:
    """Complete metadata check result.
    
    Attributes:
        url: The URL that was checked
        title: Title validation result
        description: Description validation result
        success: Whether the check completed successfully
        error: Error message if check failed (None if successful)
    """
    url: str
    title: TitleCheck
    description: DescriptionCheck
    success: bool
    error: Optional[str]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization.
        
        Returns:
            Dictionary representation of the complete check result
        """
        return {
            "url": self.url,
            "title": self.title.to_dict(),
            "description": self.description.to_dict(),
            "success": self.success,
            "error": self.error
        }
