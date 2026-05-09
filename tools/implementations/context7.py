
from tools.mcp_tool import MCPTool

class Context7Tool:

    name = "context7"

    category = "development"

    capabilities = ['documentation', 'api_reference', 'libraries']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "context7",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
