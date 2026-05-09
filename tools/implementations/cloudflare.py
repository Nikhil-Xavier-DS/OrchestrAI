
from tools.mcp_tool import MCPTool

class CloudflareTool:

    name = "cloudflare"

    category = "cloud"

    capabilities = ['cdn', 'dns', 'edge_computing']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "cloudflare",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
