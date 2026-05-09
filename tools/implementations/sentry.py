
from tools.mcp_tool import MCPTool

class SentryTool:

    name = "sentry"

    category = "monitoring"

    capabilities = ['error_tracking', 'monitoring', 'debugging']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "sentry",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
