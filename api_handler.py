# read up on the "Modelfile" use case as a way of customizing the model beforehand
# https://youtu.be/UtSSMs6ObqY

# from ollama import chat

# stream = chat(
#     model='gemma3',
#     messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
#     stream=True,
# )

# for chunk in stream:
#   print(chunk['message']['content'], end='', flush=True)


import asyncio
from ollama import AsyncClient

async def chat():
  message = {
      'role': 'user', 
      'content': 'Why is the sky blue?'
      }
  async for part in await AsyncClient().chat(model='gemma3', messages=[message], stream=True):
    print(part['message']['content'], end='', flush=True)

asyncio.run(chat())


