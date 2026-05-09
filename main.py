import asyncio
from tools.registry import ToolRegistry
from agents.comms_agent import CommsAgent
from agents.data_agent import DataAgent
from agents.dev_agent import DevAgent
from agents.research_agent import ResearchAgent
from agents.reflection_agent import ReflectionAgent
from agents.planner_agent import PlannerAgent
from core.orchestrator import Orchestrator
from core.executor import Executor
from core.llm import LLM

async def main():
    registry = ToolRegistry()
    llm = LLM()

    agents = {
        "comms": CommsAgent(registry, llm),
        "data": DataAgent(registry, llm),
        "dev": DevAgent(registry, llm),
        "research": ResearchAgent(registry, llm),
        "reflect": ReflectionAgent(registry, llm)
    }

    planner = PlannerAgent(llm)
    executor = Executor(agents)
    reflection = ReflectionAgent(registry, llm)

    orchestrator = Orchestrator(planner, executor, reflection)
    app = orchestrator.build()

    result = await app.ainvoke({
        "task": "Check emails and analyze sales data"
    })

    print(result)

if __name__ == "__main__":
    asyncio.run(main())