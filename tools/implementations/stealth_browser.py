
from tools.mcp_tool import MCPTool

class StealthBrowserTool:

    name = "stealth_browser"

    category = "automation"

    capabilities = ['web_scraping', 'browser_automation']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "stealth_browser",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
