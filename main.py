import subprocess  # we can use this to force ollama to load/unload the model from memory
import ollama
import pandas as pd
import openpyxl

# shell('ollama ps')
def shell(command_string):
    try:
        result: subprocess.CompletedProcess[str] = subprocess.run(command_string, shell=True, capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")    

def generate_response(model, query):
    client = ollama.Client()
    response = client.generate(model, query)
    return response["response"]


def main():
    # model = "dolphin3"
    model = "gemma3"
    query = "Respond with a random digit and only a digit. There should be no additional characters beyond the number itself."
    iterations = 10
    
    
    # list for outputs
    model_names = [model] * iterations
    queries = [query] * iterations
    responses = [] * iterations
    
    for i in range(iterations):
        try:
            response = generate_response(model, query)
            responses.append(response)
            print(f"Query {i + 1:3d}: {response.strip()}")
        except Exception as e:
                print(f"Query {i + 1:3d}: Error - {e}")


    df = pd.DataFrame({
        'model_name': model_names,
        'query': queries,
        'response': responses
    })
    
    
    df.to_csv('output.csv', index=False)
    # df.to_excel('output.xlsx', index=False)



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        
