
from tools.mcp_tool import MCPTool

class JiraTool:

    name = "jira"

    category = "project_management"

    capabilities = ['issues', 'tickets', 'task_tracking']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "jira",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
