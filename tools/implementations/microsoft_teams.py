
from tools.mcp_tool import MCPTool

class MicrosoftTeamsTool:

    name = "microsoft_teams"

    category = "communication"

    capabilities = ['messaging', 'meetings']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "microsoft_teams",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
