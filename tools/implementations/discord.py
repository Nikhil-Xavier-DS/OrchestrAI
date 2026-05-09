
from tools.mcp_tool import MCPTool

class DiscordTool:

    name = "discord"

    category = "communication"

    capabilities = ['messaging', 'community_management']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "discord",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
