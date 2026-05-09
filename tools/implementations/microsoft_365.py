
from tools.mcp_tool import MCPTool

class Microsoft365Tool:

    name = "microsoft_365"

    category = "enterprise"

    capabilities = ['email', 'documents', 'calendar']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "microsoft_365",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
