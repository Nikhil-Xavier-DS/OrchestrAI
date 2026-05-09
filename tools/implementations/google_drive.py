
from tools.mcp_tool import MCPTool

class GoogleDriveTool:

    name = "google_drive"

    category = "storage"

    capabilities = ['file_storage', 'document_access', 'search']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "google_drive",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
