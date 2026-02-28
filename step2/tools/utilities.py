def get_server_status(server_id: str) -> str:
    servers = {
        "server-0": "Status: CORRUPTED",
        "server-1": "Status: Healthy",
        "server-2": "Status: Deploying"
    }
    return servers.get(server_id, "NOT FOUND")