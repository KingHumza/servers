from fastmcp import FastMCP
import random
import json

mcp = FastMCP("MCP-Server")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        The sum of a and b
    """
    return a + b

@mcp.tool
def random_number(min_val: int = 1, max_val: int = 100) -> int:
    """Generate a random number between min_val and max_val.

    Args:
        min_val: Minimum value of the random number
        max_val: Maximum value of the random number

    Returns:
        A random number between min_val and max_val
    """
    return random.randint(min_val, max_val)

@mcp.resource("info://server/info")
def server_info() -> dict:
    """Get information about the server."""
    info = {
        "name": "MCP-Server",
        "version": "0.1.0",
        "description": "A simple MCP Server",
        "tools": ["add", "random_number"],
        "resources": ["info://server/info"],
        "author": "Your Name"
    }
    return info  # No need to json.dumps here; MCP handles dicts

if __name__ == "__main__":
    mcp.run(transport='http', host='0.0.0.0', port=8000)
