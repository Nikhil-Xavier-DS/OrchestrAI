import json

class DevAgent:
    def __init__(self, registry, llm):
        self.registry = registry
        self.llm = llm

    async def run(self, state):
        prompt = f"""
        You are a Dev assistant.

        Task: {state["task"]}

        Available tools:
        - github

        Decide:
        1. Which tool to use
        2. What input to send

        Return JSON:
        {{
          "tool": "...",
          "input": {{...}}
        }}
        """

        decision = await self.llm.chat([
            {"role": "user", "content": prompt}
        ])

        decision = json.loads(decision)

        tool = self.registry.get(decision["tool"])
        result = await tool.run(decision["input"])

        return result