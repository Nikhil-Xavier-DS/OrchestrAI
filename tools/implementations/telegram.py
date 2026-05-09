
from tools.mcp_tool import MCPTool

class TelegramTool:

    name = "telegram"

    category = "communication"

    capabilities = ['messaging', 'channels']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "telegram",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
