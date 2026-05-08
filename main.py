import random
from fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Enhanced Remote Server")

@mcp.tool()
def generate_random_number(min_val: int = 1, max_val: int = 100) -> int:
    """Generates a random number between min_val and max_val."""
    return random.randint(min_val, max_val)

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Adds two numbers and returns the result."""
    return a + b

@mcp.resource("config://server-info")
def get_server_info() -> str:
    """Provides structured information about this MCP server."""
    return """
{
  "name": "Enhanced Remote Server",
  "version": "1.0.0",
  "description": "A simple MCP server demonstrating tools and resources.",
  "capabilities": {
    "tools": ["generate_random_number", "add_numbers"],
    "resources": ["config://server-info"]
  }
}
""".strip()

if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=8000)
