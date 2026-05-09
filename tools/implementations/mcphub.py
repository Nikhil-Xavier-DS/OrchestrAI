
from tools.mcp_tool import MCPTool

class McphubTool:

    name = "mcphub"

    category = "mcp"

    capabilities = ['mcp_management']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "mcphub",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
