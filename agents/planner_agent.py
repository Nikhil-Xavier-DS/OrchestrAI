import json

class PlannerAgent:
    def __init__(self, llm):
        self.llm = llm

    async def run(self, state):
        prompt = """
        You are a planning agent.

        You MUST output ONLY valid JSON.

        NO explanations.
        NO markdown.
        NO extra text.

        FORMAT:
        {
        "steps": [
            {
            "agent": "comms",
            "task": "..."
            }
        ]
        }

        TASK:
        {task}
        """

        response = await self.llm.chat(
            messages=[
                {"role": "system", "content": "Return ONLY valid JSON. No text."},
                {"role": "user", "content": prompt}
            ]
        )

        print("response")
        print(response)
        plan = json.loads(response)
        return {"plan": plan}