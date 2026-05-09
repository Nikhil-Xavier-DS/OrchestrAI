
from tools.mcp_tool import MCPTool

class GoogleDocsTool:

    name = "google_docs"

    category = "documents"

    capabilities = ['document_editing', 'document_reading']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "google_docs",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
