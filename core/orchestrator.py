from langgraph.graph import StateGraph

class Orchestrator:
    def __init__(self, planner, executor):
        self.planner = planner
        self.executor = executor

    def build(self):
        graph = StateGraph(dict)

        graph.add_node("plan", self.planner.run)
        graph.add_node("execute", self.executor.run)

        graph.set_entry_point("plan")
        graph.add_edge("plan", "execute")

        return graph.compile()