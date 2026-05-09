import json

class PlannerAgent:
    def __init__(self, llm):
        self.llm = llm

    async def run(self, state):
        prompt = f"""
        You are an AI planner.

        Break the task into steps and assign agents:
        Available agents:
        - comms (email, slack)
        - data (databases)
        - dev (code, infra)
        - research (web)

        Return JSON:
        [
          {{ "agent": "...", "task": "..." }}
        ]

        Task: {state["task"]}
        """

        response = await self.llm.chat([
            {"role": "user", "content": prompt}
        ])

        plan = json.loads(response)
        return {"plan": plan}