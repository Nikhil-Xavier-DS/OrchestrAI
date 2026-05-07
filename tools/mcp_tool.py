from tools.base_tool import BaseTool
from mcp.client import MCPClient
from core.retry import retry_policy

class MCPTool(BaseTool):
    def __init__(self, name: str, endpoint: str):
        self.name = name
        self.client = MCPClient(endpoint)

    @retry_policy()
    async def run(self, input: dict):
        return await self.client.call(input)