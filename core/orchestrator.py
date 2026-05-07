from langgraph.graph import StateGraph
from core.router import route_task

class Orchestrator:
    def __init__(self, agents):
        self.agents = agents

    def build(self):
        graph = StateGraph(dict)

        graph.add_node("router", route_task)
        graph.add_node("comms", self.agents["comms"].run)
        graph.add_node("data", self.agents["data"].run)
        graph.add_node("dev", self.agents["dev"].run)
        graph.add_node("research", self.agents["research"].run)

        graph.set_entry_point("router")

        return graph.compile()