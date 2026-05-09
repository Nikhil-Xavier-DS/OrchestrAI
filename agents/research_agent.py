from agents.base_agent import BaseAgent

class ResearchAgent(BaseAgent):

    capabilities = [
        "search",
        "documentation",
        "web_scraping",
        "knowledge"
    ]

    system_prompt = """
    You are a research and intelligence agent.
    """