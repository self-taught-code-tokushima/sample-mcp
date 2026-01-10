"""SSE transport sample - legacy, for backward compatibility."""
from sample_mcp.server import mcp


def main():
    """Run the MCP server with SSE transport."""
    mcp.run(transport="sse", host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
