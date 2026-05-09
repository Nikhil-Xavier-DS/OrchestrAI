
from tools.mcp_tool import MCPTool

class PostgresTool:

    name = "postgres"

    category = "data"

    capabilities = ['database', 'sql', 'analytics']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "postgres",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
