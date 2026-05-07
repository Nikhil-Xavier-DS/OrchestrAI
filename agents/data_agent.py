class DataAgent:
    def __init__(self, registry):
        self.registry = registry

    async def run(self, state):
        db = self.registry.get("postgres")

        result = await db.run({
            "query": "SELECT * FROM sales LIMIT 10"
        })

        return {"data": result}