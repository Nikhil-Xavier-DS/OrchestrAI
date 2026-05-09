
from tools.mcp_tool import MCPTool

class DockerTool:

    name = "docker"

    category = "devops"

    capabilities = ['containers', 'deployment']

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "docker",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
