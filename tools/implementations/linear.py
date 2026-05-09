
from tools.mcp_tool import MCPTool

class LinearTool:

    name = "linear"

    category = "project_management"

    capabilities = ['issues', 'task_tracking']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "linear",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
