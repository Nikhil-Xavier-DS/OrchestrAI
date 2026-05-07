import yaml
from tools.mcp_tool import MCPTool

class ToolRegistry:
    def __init__(self, config_path="config/tools.yaml"):
        self.tools = {}
        self.load_tools(config_path)

    def load_tools(self, path):
        config = yaml.safe_load(open(path))
        endpoints = config["mcp_endpoints"]

        for name, endpoint in endpoints.items():
            self.tools[name] = MCPTool(name, endpoint)

    def get(self, name):
        return self.tools.get(name)