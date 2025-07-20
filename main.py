# main.py
import asyncio
import subprocess
import ollama

async def generate_response(model, query, query_num):
    client = ollama.AsyncClient()
    try:
        response = await client.generate(model, query)
        return f"Query {query_num:3d}: {response['response'].strip()}"
    except Exception as e:
        return f"Query {query_num:3d}: Error - {e}"

async def main():
    model = "gemma3"
    query = "Respond with a random digit and only a digit. There should be no additional characters beyond the number itself."
    
    # Create all tasks at once
    tasks = [
        generate_response(model, query, i + 1) 
        for i in range(100)
    ]
    
    # Run all tasks concurrently
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    # Print results in order
    for result in results:
        print(result)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nGoodbye!")

