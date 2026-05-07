class BaseAgent:
    def __init__(self, tools, memory):
        self.tools = tools
        self.memory = memory

    async def run(self, state: dict):
        raise NotImplementedError