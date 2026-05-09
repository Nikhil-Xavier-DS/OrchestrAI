
from tools.mcp_tool import MCPTool

class VercelTool:

    name = "vercel"

    category = "deployment"

    capabilities = ['hosting', 'deployment']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "vercel",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
