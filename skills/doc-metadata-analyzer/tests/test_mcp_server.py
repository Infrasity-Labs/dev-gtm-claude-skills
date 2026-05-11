"""MCP integration tests for Documentation Metadata Checker."""

import json
import pytest
from unittest.mock import patch
from doc_metadata_analyzer.server import list_tools, call_tool
from doc_metadata_analyzer.models import CheckResult, TitleCheck, DescriptionCheck


@pytest.mark.asyncio
async def test_list_tools():
    tools = await list_tools()
    
    assert len(tools) == 1
    assert tools[0].name == "check_documentation_metadata"
    assert "meta title" in tools[0].description.lower()
    assert "meta description" in tools[0].description.lower()
    
    schema = tools[0].inputSchema
    assert schema["type"] == "object"
    assert "url" in schema["properties"]
    assert schema["properties"]["url"]["type"] == "string"
    assert "url" in schema["required"]


@pytest.mark.asyncio
async def test_call_tool_with_valid_url():
    mock_result = CheckResult(
        url="https://example.com",
        title=TitleCheck(
            value="Example Title",
            exists=True,
            length=13,
            status="warning",
            issues=["Title too short (13 chars, recommended: 50-60)"]
        ),
        description=DescriptionCheck(
            value="This is an example description that is long enough to be in the ideal range for SEO purposes.",
            exists=True,
            length=95,
            status="warning",
            issues=["Description slightly short (95 chars, ideal: 140-160)"]
        ),
        success=True,
        error=None
    )
    
    with patch('doc_metadata_analyzer.server.checker.check_url', return_value=mock_result):
        result = await call_tool(
            name="check_documentation_metadata",
            arguments={"url": "https://example.com"}
        )
    
    assert len(result) == 1
    assert result[0].type == "text"
    
    response_data = json.loads(result[0].text)
    assert response_data["url"] == "https://example.com"
    assert response_data["success"] is True
    assert response_data["error"] is None
    assert response_data["title"]["exists"] is True
    assert response_data["title"]["value"] == "Example Title"
    assert response_data["description"]["exists"] is True


@pytest.mark.asyncio
async def test_call_tool_with_missing_url_argument():
    with pytest.raises(ValueError, match="Missing required argument: url"):
        await call_tool(
            name="check_documentation_metadata",
            arguments={}
        )


@pytest.mark.asyncio
async def test_call_tool_with_unknown_tool():
    with pytest.raises(ValueError, match="Unknown tool"):
        await call_tool(
            name="unknown_tool",
            arguments={"url": "https://example.com"}
        )


@pytest.mark.asyncio
async def test_call_tool_with_invalid_url():
    mock_result = CheckResult(
        url="ftp://example.com",
        title=TitleCheck(
            None, False, 0, "missing",
            ["Invalid URL protocol (must be HTTP or HTTPS)"]
        ),
        description=DescriptionCheck(None, False, 0, "missing", []),
        success=False,
        error="Invalid URL protocol (must be HTTP or HTTPS)"
    )
    
    with patch('doc_metadata_analyzer.server.checker.check_url', return_value=mock_result):
        result = await call_tool(
            name="check_documentation_metadata",
            arguments={"url": "ftp://example.com"}
        )
    
    response_data = json.loads(result[0].text)
    assert response_data["success"] is False
    assert "Invalid URL protocol" in response_data["error"]


@pytest.mark.asyncio
async def test_call_tool_with_network_error():
    mock_result = CheckResult(
        url="https://nonexistent.example.com",
        title=TitleCheck(None, False, 0, "missing", []),
        description=DescriptionCheck(None, False, 0, "missing", []),
        success=False,
        error="Failed to fetch URL: Connection error"
    )
    
    with patch('doc_metadata_analyzer.server.checker.check_url', return_value=mock_result):
        result = await call_tool(
            name="check_documentation_metadata",
            arguments={"url": "https://nonexistent.example.com"}
        )
    
    response_data = json.loads(result[0].text)
    assert response_data["success"] is False
    assert "Failed to fetch URL" in response_data["error"]


@pytest.mark.asyncio
async def test_call_tool_response_structure():
    mock_result = CheckResult(
        url="https://example.com",
        title=TitleCheck("Test Title", True, 10, "warning", ["Too short"]),
        description=DescriptionCheck("Test Description", True, 16, "warning", ["Too short"]),
        success=True,
        error=None
    )
    
    with patch('doc_metadata_analyzer.server.checker.check_url', return_value=mock_result):
        result = await call_tool(
            name="check_documentation_metadata",
            arguments={"url": "https://example.com"}
        )
    
    response_data = json.loads(result[0].text)
    
    assert "url" in response_data
    assert "title" in response_data
    assert "description" in response_data
    assert "success" in response_data
    assert "error" in response_data
    
    assert "value" in response_data["title"]
    assert "exists" in response_data["title"]
    assert "length" in response_data["title"]
    assert "status" in response_data["title"]
    assert "issues" in response_data["title"]
    
    assert "value" in response_data["description"]
    assert "exists" in response_data["description"]
    assert "length" in response_data["description"]
    assert "status" in response_data["description"]
    assert "issues" in response_data["description"]
