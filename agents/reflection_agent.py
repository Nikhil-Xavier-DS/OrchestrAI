class ReflectionAgent:
    def __init__(self, llm):
        self.llm = llm

    async def run(self, state):
        prompt = f"""
        Evaluate the results and suggest improvements.

        Results:
        {state["results"]}
        """

        return await self.llm.chat([
            {"role": "user", "content": prompt}
        ])