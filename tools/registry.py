import yaml
import importlib

class ToolRegistry:
    def __init__(self, config_path="config/tools.yaml"):
        self.tools = {}
        self.load_tools(config_path)

    def load_tools(self, path):
        config = yaml.safe_load(open(path))
        endpoints = config["mcp_endpoints"]

        for name, endpoint in endpoints.items():

            module = importlib.import_module(
                f"tools.implementations.{name}"
            )

            class_name = (
                "".join(word.capitalize() for word in name.split("_"))
                + "Tool"
            )

            tool_class = getattr(module, class_name)

            self.tools[name] = tool_class(endpoint)

    def get(self, name):
        return self.tools.get(name)

    def get_by_category(self, category):
        return [
            tool for tool in self.tools.values()
            if tool.category == category
        ]

    def get_by_capability(self, capability):
        return [
            tool for tool in self.tools.values()
            if capability in tool.capabilities
        ]