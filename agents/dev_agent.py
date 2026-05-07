class DevAgent:
    def __init__(self, registry):
        self.registry = registry

    async def run(self, state):
        github = self.registry.get("github")

        repos = await github.run({"action": "list_repos"})

        return {"repos": repos}