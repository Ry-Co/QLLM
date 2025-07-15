# hello world :D

import asyncio
import api_handler
from api_handler import chat


def main():
    user_input: str = input("Please input your query: ")
    # TODO: parse user input for valid query
    asyncio.run(chat(user_input))


main()
