# read up on the "Modelfile" use case as a way of customizing the model beforehand
# https://youtu.be/UtSSMs6ObqY


import asyncio
from ollama import AsyncClient


async def chat(user_query):
    message = {"role": "user", "content": user_query}
    async for part in await AsyncClient().chat(
        model="gemma3", messages=[message], stream=True
    ):
        print(part["message"]["content"], end="", flush=True)


# asyncio.run(chat())
