
from tools.mcp_tool import MCPTool

class FirecrawlTool:

    name = "firecrawl"

    category = "research"

    capabilities = ['web_scraping', 'crawl']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "firecrawl",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
