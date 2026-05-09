
from tools.mcp_tool import MCPTool

class MongodbTool:

    name = "mongodb"

    category = "data"

    capabilities = ['nosql', 'documents']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "mongodb",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
