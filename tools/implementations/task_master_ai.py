
from tools.mcp_tool import MCPTool

class TaskMasterAiTool:

    name = "task_master_ai"

    category = "planning"

    capabilities = ['task_planning', 'workflow_management']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "task_master_ai",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
