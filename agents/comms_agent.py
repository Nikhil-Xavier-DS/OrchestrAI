from agents.base_agent import BaseAgent

class CommsAgent(BaseAgent):

    capabilities = [
        "email",
        "messaging",
        "crm",
        "support"
    ]

    system_prompt = """
    You are a communication agent.

    You specialize in:
    - email
    - messaging
    - CRM workflows
    - support systems
    """