
from tools.mcp_tool import MCPTool

class SlackTool:

    name = "slack"

    category = "communication"

    capabilities = ['messaging', 'team_chat', 'search']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "slack",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
