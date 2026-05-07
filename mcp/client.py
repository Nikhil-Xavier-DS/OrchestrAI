import httpx

class MCPClient:
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    async def call(self, payload: dict):
        async with httpx.AsyncClient() as client:
            response = await client.post(self.endpoint, json=payload)
            return response.json()