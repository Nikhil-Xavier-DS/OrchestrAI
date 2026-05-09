
from tools.mcp_tool import MCPTool

class AwsTool:

    name = "aws"

    category = "cloud"

    capabilities = ['cloud', 'infrastructure', 'storage']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "aws",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
