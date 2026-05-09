from langgraph.graph import StateGraph

class Orchestrator:
    def __init__(self, planner, executor, reflection):
        self.planner = planner
        self.executor = executor
        self.reflection = reflection

    def build(self):
        graph = StateGraph(dict)

        graph.add_node("planner", self.planner.run)
        graph.add_node("executor", self.executor.run)
        graph.add_node("reflection", self.reflection.run)

        graph.set_entry_point("planner")

        graph.add_edge("planner", "executor")
        graph.add_edge("executor", "reflection")

        return graph.compile()