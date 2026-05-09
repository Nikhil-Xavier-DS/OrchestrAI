
from tools.mcp_tool import MCPTool

class SalesforceTool:

    name = "salesforce"

    category = "crm"

    capabilities = ['crm', 'forecasting', 'accounts']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "salesforce",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
