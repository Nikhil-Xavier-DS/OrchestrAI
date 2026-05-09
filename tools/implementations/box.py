
from tools.mcp_tool import MCPTool

class BoxTool:

    name = "box"

    category = "storage"

    capabilities = ['enterprise_storage']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "box",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
