
from tools.mcp_tool import MCPTool

class PlaywrightTool:

    name = "playwright"

    category = "automation"

    capabilities = ['browser_automation', 'testing']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "playwright",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
