
from tools.mcp_tool import MCPTool

class GoogleCalendarTool:

    name = "google_calendar"

    category = "productivity"

    capabilities = ['calendar', 'scheduling', 'meetings']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "google_calendar",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
