
from tools.mcp_tool import MCPTool

class NotionTool:

    name = "notion"

    category = "knowledge"

    capabilities = ['notes', 'documentation', 'knowledge_base']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "notion",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
