"""Core MCP server definition with tools."""
from fastmcp import FastMCP

mcp = FastMCP("MyServer")

@mcp.tool(name="hello", description="Greets a user by name.")
def hello(name: str) -> str:
    return f"Hello, {name}!"

def main():
    """Main entry point for the MCP server."""
    # Run the FastMCP server
    mcp.run()


if __name__ == "__main__":
    main()