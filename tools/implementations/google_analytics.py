
from tools.mcp_tool import MCPTool

class GoogleAnalyticsTool:

    name = "google_analytics"

    category = "analytics"

    capabilities = ['traffic', 'web_analytics']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "google_analytics",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
