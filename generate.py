import asyncio
import ollama

async def generate_response(model_name, query):
    """
    Generate a response using the specified model and query.
    
    Args:
        model_name (str): The name of the model to use (e.g., 'llama3.2')
        query (str): The query/prompt to send to the model
        
    Returns:
        str: The generated response from the model
    """
    client = ollama.AsyncClient()
    response = await client.generate(model_name, query)
    return response['response']