
from tools.mcp_tool import MCPTool

class ExcelTool:

    name = "excel"

    category = "documents"

    capabilities = ['spreadsheet', 'excel_processing']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "excel",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
