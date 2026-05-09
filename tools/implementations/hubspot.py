
from tools.mcp_tool import MCPTool

class HubspotTool:

    name = "hubspot"

    category = "crm"

    capabilities = ['crm', 'sales_pipeline']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "hubspot",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
