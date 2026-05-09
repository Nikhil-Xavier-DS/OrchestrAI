
from tools.mcp_tool import MCPTool

class SnowflakeTool:

    name = "snowflake"

    category = "data"

    capabilities = ['warehouse', 'analytics']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "snowflake",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
