# read up on the "Modelfile" use case as a way of customizing the model beforehand
# https://youtu.be/UtSSMs6ObqY


import asyncio
from ollama import AsyncClient

async def chat():
    messages = []  # Store conversation history
    
    while True:
        user_input = input("\nYou: ")
        
        # Exit conditions
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        
        # Skip empty input
        if not user_input.strip():
            continue
        
        # Add user message to history
        messages.append({"role": "user", "content": user_input})
        
        print("Bot: ", end="", flush=True)
        
        # Get bot response
        bot_response = ""
        async for part in await AsyncClient().chat(
            model="gemma3", messages=messages, stream=True
        ):
            content = part["message"]["content"]
            print(content, end="", flush=True)
            bot_response += content
        
        # Add bot response to history
        messages.append({"role": "assistant", "content": bot_response})
