
from tools.mcp_tool import MCPTool

class AirtableTool:

    name = "airtable"

    category = "data"

    capabilities = ['spreadsheet', 'database']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "airtable",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
