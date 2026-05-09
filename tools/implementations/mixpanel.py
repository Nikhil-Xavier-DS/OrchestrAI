
from tools.mcp_tool import MCPTool

class MixpanelTool:

    name = "mixpanel"

    category = "analytics"

    capabilities = ['product_analytics', 'funnels']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "mixpanel",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
