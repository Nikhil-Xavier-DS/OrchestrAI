
from tools.mcp_tool import MCPTool

class GmailTool:

    name = "gmail"

    category = "communication"

    capabilities = ['email', 'messaging', 'drafting', 'search']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "gmail",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
