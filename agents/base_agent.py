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
        self.validate_decision(decision, available_tools)
        
        print("decision")
        print(decision)
        tool = self.registry.get(
            decision["tool"]
        )
        
        if tool is None:
            return {
                "error": "tool_not_found",
                "requested_tool": decision["tool"],
                "available_tools": list(self.registry.tools.keys())
            }

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

        tool_names = [t["name"] for t in tools]

        return f"""
        TASK:
        {state["task"]}

        AVAILABLE TOOLS (choose ONLY from this list):
        {tool_names}

        CRITICAL RULE:
        You MUST select exactly ONE tool from the list above.

        Return ONLY valid JSON:

        {{
        "tool": "one_of_the_above_tools",
        "input": {{}}
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
        
    def validate_decision(self, decision, tools):

        if not decision.get("tool"):
            raise Exception("No tool selected by LLM")

        valid_tools = {t["name"] for t in tools}

        if decision["tool"] not in valid_tools:
            raise Exception(
                f"Invalid tool selected: {decision['tool']}"
            )