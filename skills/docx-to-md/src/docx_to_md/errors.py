"""
Error handling module for docx-to-md converter.

This module defines custom exceptions and error handling utilities for the
document conversion process.
"""

import sys
import traceback
from pathlib import Path
from typing import List


# Custom Exceptions

class DocxToMdError(Exception):
    """Base exception for all converter errors."""
    pass


class FileNotFoundError(DocxToMdError):
    """
    Raised when the input file doesn't exist.
    
    This exception is raised during file validation when the specified
    input DOCX file path does not exist on the filesystem.
    """
    pass


class InvalidDocxError(DocxToMdError):
    """
    Raised when the file is not a valid DOCX format.
    
    This exception is raised when:
    - The file is not a ZIP archive (DOCX files are ZIP-based)
    - The file doesn't contain required DOCX structure
    - The file has a .docx extension but is not a valid Word document
    """
    pass


class CorruptedDocxError(DocxToMdError):
    """
    Raised when the DOCX file is corrupted or incomplete.
    
    This exception is raised when:
    - The ZIP structure is damaged
    - Required XML files are missing or malformed
    - The document cannot be parsed by python-docx
    """
    pass


class PermissionError(DocxToMdError):
    """
    Raised when file permissions prevent reading or writing.
    
    This exception is raised when:
    - The input file cannot be read due to insufficient permissions
    - The output file cannot be written due to insufficient permissions
    - The output directory cannot be accessed
    """
    pass


class ParsingError(DocxToMdError):
    """
    Raised when an unexpected error occurs during DOCX parsing.
    
    This exception is raised when:
    - An unexpected exception occurs while parsing document structure
    - Element extraction fails unexpectedly
    - DOM construction encounters an error
    """
    pass


class GenerationError(DocxToMdError):
    """
    Raised when an unexpected error occurs during Markdown generation.
    
    This exception is raised when:
    - An unexpected exception occurs while formatting elements
    - Markdown syntax generation fails
    - File writing encounters an error
    """
    pass


# Error Handler

class ErrorHandler:
    """
    Centralized error handling for the converter.
    
    This class provides methods for handling different error types with
    appropriate user messages, logging, and exit codes.
    """
    
    def __init__(self, verbose: bool = False):
        """
        Initialize error handler.
        
        Args:
            verbose: If True, display detailed error information and stack traces
        """
        self.verbose = verbose
        self.warnings: List[str] = []
    
    def handle_file_not_found(self, path: Path) -> None:
        """
        Handle missing file error.
        
        Args:
            path: Path to the missing file
            
        Exit Code: 1
        """
        print(f"Error: File not found: '{path}'", file=sys.stderr)
        print("Please check the file path and try again.", file=sys.stderr)
        sys.exit(1)
    
    def handle_invalid_docx(self, path: Path) -> None:
        """
        Handle invalid DOCX format error.
        
        Args:
            path: Path to the invalid file
            
        Exit Code: 2
        """
        print(f"Error: Invalid DOCX format: '{path}'", file=sys.stderr)
        print("The file is not a valid Word document.", file=sys.stderr)
        sys.exit(2)
    
    def handle_corrupted_docx(self, path: Path, details: str = "") -> None:
        """
        Handle corrupted DOCX error.
        
        Args:
            path: Path to the corrupted file
            details: Optional details about the corruption
            
        Exit Code: 2
        """
        print(f"Error: Corrupted DOCX file: '{path}'", file=sys.stderr)
        if details:
            print(f"Details: {details}", file=sys.stderr)
        print("Try opening and repairing the file in Microsoft Word.", file=sys.stderr)
        sys.exit(2)
    
    def handle_permission_error(self, path: Path, operation: str) -> None:
        """
        Handle permission error.
        
        Args:
            path: Path to the file with permission issues
            operation: Description of the operation (e.g., "read", "write")
            
        Exit Code: 1
        """
        print(f"Error: Permission denied: Cannot {operation} '{path}'", file=sys.stderr)
        print("Please check file permissions.", file=sys.stderr)
        sys.exit(1)
    
    def handle_parsing_error(self, error: Exception) -> None:
        """
        Handle parsing error.
        
        Args:
            error: The exception that occurred during parsing
            
        Exit Code: 3
        """
        print(f"Error: Failed to parse document", file=sys.stderr)
        if self.verbose:
            print(f"Details: {str(error)}", file=sys.stderr)
            traceback.print_exc()
        sys.exit(3)
    
    def handle_generation_error(self, error: Exception) -> None:
        """
        Handle generation error.
        
        Args:
            error: The exception that occurred during generation
            
        Exit Code: 4
        """
        print(f"Error: Failed to generate Markdown output", file=sys.stderr)
        if self.verbose:
            print(f"Details: {str(error)}", file=sys.stderr)
            traceback.print_exc()
        sys.exit(4)
    
    def add_warning(self, message: str) -> None:
        """
        Add a warning message to the warning list.
        
        Warnings are accumulated during conversion and displayed at the end.
        They indicate non-critical issues that don't prevent conversion.
        
        Args:
            message: Warning message to add
        """
        self.warnings.append(message)
        if self.verbose:
            print(f"Warning: {message}", file=sys.stderr)
    
    def print_summary(self) -> None:
        """
        Print warning summary at the end of conversion.
        
        This method displays all accumulated warnings to inform the user
        about non-critical issues encountered during conversion.
        """
        if self.warnings:
            print(f"\nConversion completed with {len(self.warnings)} warning(s):", file=sys.stderr)
            for warning in self.warnings:
                print(f"  - {warning}", file=sys.stderr)
