"""Data models for metadata validation results."""

from dataclasses import dataclass
from typing import Optional, List, Dict, Any


@dataclass
class TitleCheck:
    value: Optional[str]
    exists: bool
    length: int
    status: str
    issues: List[str]
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "value": self.value,
            "exists": self.exists,
            "length": self.length,
            "status": self.status,
            "issues": self.issues
        }


@dataclass
class DescriptionCheck:
    value: Optional[str]
    exists: bool
    length: int
    status: str
    issues: List[str]
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "value": self.value,
            "exists": self.exists,
            "length": self.length,
            "status": self.status,
            "issues": self.issues
        }


@dataclass
class CheckResult:
    url: str
    title: TitleCheck
    description: DescriptionCheck
    success: bool
    error: Optional[str]
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "url": self.url,
            "title": self.title.to_dict(),
            "description": self.description.to_dict(),
            "success": self.success,
            "error": self.error
        }
