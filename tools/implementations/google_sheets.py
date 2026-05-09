
from tools.mcp_tool import MCPTool

class GoogleSheetsTool:

    name = "google_sheets"

    category = "data"

    capabilities = ['spreadsheet', 'analytics', 'structured_data']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "google_sheets",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
