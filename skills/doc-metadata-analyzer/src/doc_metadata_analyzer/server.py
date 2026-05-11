"""MCP Server for Documentation Metadata Checker."""

import json
import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from .checker import MetadataChecker


server = Server("doc-metadata-checker")
checker = MetadataChecker()


@server.list_tools()
async def list_tools() -> list[Tool]:
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
    if name == "check_documentation_metadata":
        if "url" not in arguments:
            raise ValueError("Missing required argument: url")
        
        result = checker.check_url(arguments["url"])
        result_json = json.dumps(result.to_dict(), indent=2)
        
        return [TextContent(type="text", text=result_json)]
    else:
        raise ValueError(f"Unknown tool: {name}")


async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())
