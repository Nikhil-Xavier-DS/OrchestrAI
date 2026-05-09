import json
from core.logger import get_logger

logger = get_logger()

class BaseAgent:

    capabilities = []

    system_prompt = "You are an AI agent."

    def __init__(self, registry, llm):
        self.registry = registry
        self.llm = llm

    async def run(self, state):

        logger.info(
            f"{self.__class__.__name__} started task"
        )

        available_tools = self.get_available_tools()

        prompt = self.build_prompt(
            state,
            available_tools
        )

        response = await self.llm.chat([
            {
                "role": "system",
                "content": self.system_prompt
            },
            {
                "role": "user",
                "content": prompt
            }
        ])

        decision = self.safe_json_parse(response)

        tool = self.registry.get(
            decision["tool"]
        )

        result = await tool.run(
            decision["input"]
        )

        logger.info(
            f"{self.__class__.__name__} used {decision['tool']}"
        )

        return {
            "agent": self.__class__.__name__,
            "tool_used": decision["tool"],
            "result": result
        }

    def get_available_tools(self):

        tools = []

        for capability in self.capabilities:

            matched = self.registry.get_by_capability(
                capability
            )

            for tool in matched:

                tools.append({
                    "name": tool.name,
                    "capabilities": tool.capabilities
                })

        return tools

    def build_prompt(self, state, tools):

        return f"""
        TASK:
        {state["task"]}

        AVAILABLE TOOLS:
        {json.dumps(tools, indent=2)}

        Return ONLY valid JSON:
        {{
            "tool": "...",
            "input": {{...}}
        }}
        """

    def safe_json_parse(self, text):

        try:
            return json.loads(text)

        except Exception as e:

            logger.error(
                f"JSON parse failed: {e}"
            )

            return {
                "tool": None,
                "input": {}
            }