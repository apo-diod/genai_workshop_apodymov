from fastmcp import FastMCP

mcp = FastMCP("My First MCP Server")

@mcp.tool
def get_server_status(server_id: str) -> str:
    """
    Use this tool when you need to get a status of the server.
    Input parameters:
        - server_id: An ID of the server in next format: <alphanumeric>-<numeric>
    Output:
        Gives back status of the server
    """
    servers = {
        "server-0": "Status: CORRUPTED",
        "server-1": "Status: Healthy",
        "server-2": "Status: Deploying"
    }
    return servers.get(server_id, "NOT FOUND")

if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=9000)