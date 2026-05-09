
from tools.mcp_tool import MCPTool

class TavilyTool:

    name = "tavily"

    category = "research"

    capabilities = ['search', 'web_research', 'knowledge']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "tavily",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
