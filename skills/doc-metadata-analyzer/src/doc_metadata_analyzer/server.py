"""
MCP Server for Documentation Metadata Checker.

This module implements the Model Context Protocol server that exposes
the check_documentation_metadata tool to AI agents.
"""

import json
import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from .checker import MetadataChecker


# Initialize the MCP server
server = Server("doc-metadata-checker")

# Initialize the metadata checker
checker = MetadataChecker()


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools for AI agents.
    
    Returns:
        List of Tool definitions that agents can invoke
    """
    return [
        Tool(
            name="check_documentation_metadata",
            description=(
                "Check if a documentation page has proper meta title and meta description, "
                "and validate their character lengths against SEO best practices. "
                "Returns validation results including existence checks and length analysis. "
                "Ideal title length: 50-60 characters. Ideal description length: 140-160 characters."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "The documentation page URL to check (must be HTTP or HTTPS)"
                    }
                },
                "required": ["url"]
            }
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool invocation from AI agents.
    
    Args:
        name: Name of the tool to invoke
        arguments: Tool arguments provided by the agent
    
    Returns:
        List of TextContent with tool results
    
    Raises:
        ValueError: If tool name is unknown or arguments are invalid
    """
    if name == "check_documentation_metadata":
        # Validate arguments
        if "url" not in arguments:
            raise ValueError("Missing required argument: url")
        
        url = arguments["url"]
        
        # Check the metadata
        result = checker.check_url(url)
        
        # Convert result to JSON
        result_json = json.dumps(result.to_dict(), indent=2)
        
        return [
            TextContent(
                type="text",
                text=result_json
            )
        ]
    else:
        raise ValueError(f"Unknown tool: {name}")


async def main():
    """Main entry point for the MCP server.
    
    Starts the server and handles stdio communication with AI agents.
    """
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())
