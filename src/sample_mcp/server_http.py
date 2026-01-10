"""HTTP (Streamable HTTP) transport sample - for network access."""
from sample_mcp.server import mcp


def main():
    """Run the MCP server with HTTP transport."""
    mcp.run(transport="http", host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
