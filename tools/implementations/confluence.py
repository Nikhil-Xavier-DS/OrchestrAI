
from tools.mcp_tool import MCPTool

class ConfluenceTool:

    name = "confluence"

    category = "knowledge"

    capabilities = ['wiki', 'documentation', 'knowledge_base']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "confluence",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
