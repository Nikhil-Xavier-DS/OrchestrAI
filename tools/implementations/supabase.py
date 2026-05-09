
from tools.mcp_tool import MCPTool

class SupabaseTool:

    name = "supabase"

    category = "data"

    capabilities = ['database', 'auth', 'storage']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "supabase",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
