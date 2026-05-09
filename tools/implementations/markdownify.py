
from tools.mcp_tool import MCPTool

class MarkdownifyTool:

    name = "markdownify"

    category = "documents"

    capabilities = ['markdown_conversion', 'document_processing']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "markdownify",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
