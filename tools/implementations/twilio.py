
from tools.mcp_tool import MCPTool

class TwilioTool:

    name = "twilio"

    category = "communication"

    capabilities = ['sms', 'voice']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "twilio",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
