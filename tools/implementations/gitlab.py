
from tools.mcp_tool import MCPTool

class GitlabTool:

    name = "gitlab"

    category = "development"

    capabilities = ['repository', 'ci_cd']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "gitlab",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
