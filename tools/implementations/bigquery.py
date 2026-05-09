
from tools.mcp_tool import MCPTool

class BigqueryTool:

    name = "bigquery"

    category = "data"

    capabilities = ['analytics', 'sql', 'warehouse']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "bigquery",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
