import httpx


class LLM:

    def __init__(
        self,
        model="llama3.2:1b",
        host="http://localhost:11434"
    ):

        self.model = model
        self.host = host

    async def chat(self, messages):

        if isinstance(messages, str):

            messages = [
                {
                    "role": "user",
                    "content": messages
                }
            ]

        timeout = httpx.Timeout(120.0)

        async with httpx.AsyncClient(
            timeout=timeout
        ) as client:
            response = await client.post(

                f"{self.host}/api/chat",

                json={
                    "model": self.model,
                    "messages": messages,
                    "stream": False
                }

            )

        data = response.json()

        # DEBUG
        print(data)

        # Handle Ollama chat response
        if "message" in data:

            return data["message"]["content"]

        # Handle errors
        if "error" in data:

            raise Exception(data["error"])

        raise Exception(
            f"Unexpected Ollama response: {data}"
        )