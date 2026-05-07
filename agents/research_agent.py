class ResearchAgent:
    def __init__(self, registry):
        self.registry = registry

    async def run(self, state):
        tavily = self.registry.get("tavily")

        results = await tavily.run({"query": state["task"]})

        return {"research": results}