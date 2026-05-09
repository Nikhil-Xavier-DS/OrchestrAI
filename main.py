import asyncio
from tools.registry import ToolRegistry
from agents.comms_agent import CommsAgent
from agents.data_agent import DataAgent
from agents.dev_agent import DevAgent
from agents.research_agent import ResearchAgent
from core.orchestrator import Orchestrator

async def main():
    registry = ToolRegistry()

    agents = {
        "comms": CommsAgent(registry),
        "data": DataAgent(registry),
        "dev": DevAgent(registry),
        "research": ResearchAgent(registry),
    }

    orchestrator = Orchestrator(agents)
    app = orchestrator.build()

    result = await app.ainvoke({
        "task": "Check emails and analyze sales data"
    })

    print(result)

if __name__ == "__main__":
    asyncio.run(main())