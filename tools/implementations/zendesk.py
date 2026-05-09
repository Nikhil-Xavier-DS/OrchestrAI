
from tools.mcp_tool import MCPTool

class ZendeskTool:

    name = "zendesk"

    category = "support"

    capabilities = ['tickets', 'customer_support']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "zendesk",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
