
from tools.mcp_tool import MCPTool

class OnedriveTool:

    name = "onedrive"

    category = "storage"

    capabilities = ['file_storage', 'document_access']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "onedrive",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
