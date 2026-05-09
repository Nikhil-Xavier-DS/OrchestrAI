
from tools.mcp_tool import MCPTool

class SharepointTool:

    name = "sharepoint"

    category = "enterprise"

    capabilities = ['document_management', 'enterprise_search']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "sharepoint",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
