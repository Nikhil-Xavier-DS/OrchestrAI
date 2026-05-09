class Executor:
    def __init__(self, agents):
        self.agents = agents

    async def run(self, state):
        results = []

        for step in state["plan"]:
            agent_name = step["agent"]
            agent = self.agents[agent_name]

            output = await agent.run({
                "task": step["task"],
                "context": results
            })

            results.append({
                "agent": agent_name,
                "output": output
            })

        return {"results": results}