# main.py
import asyncio
import api_handler
from api_handler import chat

def main():
    print("Chat with the bot! Type 'quit' or 'exit' to stop.")
    asyncio.run(chat())

main()

# api_handler.py
