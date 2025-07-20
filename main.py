# main.py
import asyncio
import subprocess  # we can use this to force ollama to load/unload the model from memory
import ollama


async def generate_response(model, query):
    client = ollama.AsyncClient()
    response = await client.generate(model, query)
    return response["response"]


async def main():
    # model = "dolphin3"
    model = "gemma3"
    query = "Respond with a random digit and only a digit. There should be no additional characters beyond the number itself."

    for i in range(100):
        try:
            response = await generate_response(model, query)
            print(f"Query {i + 1:3d}: {response.strip()}")
        except Exception as e:
            print(f"Query {i + 1:3d}: Error - {e}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nGoodbye!")
