from agents.base_agent import BaseAgent

class DevAgent(BaseAgent):

    capabilities = [
        "code",
        "deployment",
        "infra",
        "testing",
        "monitoring"
    ]

    system_prompt = """
    You are a software engineering agent.
    """