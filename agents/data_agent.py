from agents.base_agent import BaseAgent

class DataAgent(BaseAgent):

    capabilities = [
        "database",
        "sql",
        "analytics",
        "spreadsheet",
        "tracking"
    ]

    system_prompt = """
    You are a data analytics agent.

    You specialize in:
    - SQL
    - analytics
    - dashboards
    - structured data
    """