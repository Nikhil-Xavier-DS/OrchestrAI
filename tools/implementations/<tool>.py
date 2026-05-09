from tools.mcp_tool import MCPTool

class Tool:
    def __init__(self, endpoint: str):
        self.tool = MCPTool("<tool_name>", endpoint)

    async def run(self, input: dict):
        return await self.tool.run(input)