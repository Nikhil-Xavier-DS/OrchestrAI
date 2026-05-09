
from tools.mcp_tool import MCPTool

class IntercomTool:

    name = "intercom"

    category = "support"

    capabilities = ['customer_support', 'chat']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "intercom",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
