
from tools.mcp_tool import MCPTool

class CodebaseMemoryTool:

    name = "codebase_memory"

    category = "memory"

    capabilities = ['knowledge_graph', 'code_memory']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "codebase_memory",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
