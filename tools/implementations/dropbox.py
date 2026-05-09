
from tools.mcp_tool import MCPTool

class DropboxTool:

    name = "dropbox"

    category = "storage"

    capabilities = ['file_storage']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "dropbox",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
