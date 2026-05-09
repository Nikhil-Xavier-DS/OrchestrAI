from agents.base_agent import BaseAgent
import json

class ReflectionAgent(BaseAgent):

    capabilities = []

    system_prompt = """
    You are a reflection and critique agent.

    Your job:
    - evaluate execution quality
    - detect failures
    - suggest improvements
    - recommend retries
    """

    async def run(self, state):

        prompt = f"""
        TASK:
        {state["task"]}

        EXECUTION RESULTS:
        {json.dumps(state["results"], indent=2)}

        Evaluate:
        1. Was the task completed successfully?
        2. Were the right tools used?
        3. What failed?
        4. What can improve?
        5. Should the task retry?

        Return ONLY valid JSON:
        {{
            "success": true,
            "issues": [],
            "improvements": [],
            "retry": false
        }}
        """

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

        return self.safe_json_parse(response)