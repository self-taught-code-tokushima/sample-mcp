"""Stdio transport sample - default for Claude Desktop."""
from sample_mcp.server import mcp


def main():
    """Run the MCP server with stdio transport."""
    mcp.run()


if __name__ == "__main__":
    main()
