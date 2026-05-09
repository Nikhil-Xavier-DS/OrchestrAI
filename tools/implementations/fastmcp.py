
from tools.mcp_tool import MCPTool

class FastmcpTool:

    name = "fastmcp"

    category = "mcp"

    capabilities = ['mcp_creation']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "fastmcp",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
