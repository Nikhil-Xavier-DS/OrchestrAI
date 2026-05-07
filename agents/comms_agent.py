class CommsAgent:
    def __init__(self, registry):
        self.registry = registry

    async def run(self, state):
        gmail = self.registry.get("gmail")
        slack = self.registry.get("slack")

        emails = await gmail.run({"action": "fetch"})
        messages = await slack.run({"action": "recent"})

        return {
            "emails": emails,
            "messages": messages
        }