import os

from tools.tool_metadata import TOOLS_METADATA

BASE_DIR = "tools/implementations"

TEMPLATE = """
from tools.mcp_tool import MCPTool

class {class_name}Tool:

    name = "{tool_name}"

    category = "{category}"

    capabilities = {capabilities}

    def __init__(self, endpoint: str):

        self.tool = MCPTool(
            "{tool_name}",
            endpoint
        )

    async def run(self, input: dict):

        return await self.tool.run(input)
"""


def to_class_name(name):

    return "".join(
        word.capitalize()
        for word in name.split("_")
    )


def main():

    os.makedirs(BASE_DIR, exist_ok=True)

    for tool_name, metadata in TOOLS_METADATA.items():

        class_name = to_class_name(tool_name)

        content = TEMPLATE.format(
            class_name=class_name,
            tool_name=tool_name,
            category=metadata["category"],
            capabilities=metadata["capabilities"]
        )

        path = os.path.join(
            BASE_DIR,
            f"{tool_name}.py"
        )

        with open(path, "w") as f:
            f.write(content)

        print(f"✅ Generated {path}")


if __name__ == "__main__":
    main()