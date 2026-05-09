
from tools.mcp_tool import MCPTool

class NpmTool:

    name = "npm"

    category = "development"

    capabilities = ['packages', 'dependencies']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "npm",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
