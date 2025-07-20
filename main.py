import subprocess
import ollama
import pandas as pd
import time

# ends up ollama will gracefull load & unload models as they're used in memory so we don't need this :D
# --- we can use this shell() to force ollama to load/unload the model from memory---
# shell('ollama ps')
def shell(command_string):
    try:
        result: subprocess.CompletedProcess[str] = subprocess.run(
            command_string, shell=True, capture_output=True, text=True
        )
        print(result.stdout)
        print(result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")


def generate_response(client, model, query):
    response = client.generate(model, query)
    return response["response"]


def run_model_n_times(m, q, n):
    # wrapper to make main more readable - avoiding nested for each
    # m = model name string
    # q = query string
    # n = iterations

    start_time = time.time()

    # list for outputs - preallocated for iterations
    model_names = [m] * n
    queries = [q] * n
    responses = []

    # generate client
    client = ollama.Client()
    for i in range(n):
        try:
            response = generate_response(client, m, q)
            responses.append(response)
            # print(f"Query {i + 1:3d}: {response.strip()}")
        except Exception as e:
            print(f"Query {i + 1:3d}: Error - {e}")

    df = pd.DataFrame(
        {"model_name": model_names, "query": queries, "response": responses}
    )
    
    end_time = time.time()
    print(f"Model {m} took {end_time - start_time:.2f} seconds for {n} iterations")
    
    return df


# why is deepseek taking so much longer?
def main():
    query = "Respond with a single random digit."
    iterations = 10
    models_to_run = ['gemma3','deepseek-r1','dolphin3','qwen3']
    
    # TODO: consider preallocating the combined dataframes since we know the dims & colnames before computations
    all_dataframes = [] 
    first_model = True
    
    for model in models_to_run:
        print(f"Running model: {model}")
        df = run_model_n_times(model, query, iterations)
        
        # Add a column to identify which model generated the results
        df['model'] = model
        
        # write the table to disk
        df.to_csv(f"all_models_{iterations}_output.csv", 
                  mode='w' if first_model else 'a', 
                  header=first_model, 
                  index=False)
        first_model = False
        
        # Add to our list of dataframes
        # all_dataframes.append(df)
        
        print(f"Completed {model}: {len(df)} records")
        # del df
    
    # Combine all dataframes into one
    # combined_df = pd.concat(all_dataframes, ignore_index=True)
    
    # print(f"\nCombined dataframe shape: {combined_df.shape}")
    # print(combined_df.head())
    
    # combined_df.to_csv(f"all_models_{iterations}_output.csv", index=False)
    # df.to_csv(f"{model}_{iterations}_output.csv", index=False)
    # df.to_excel(f"{model}_{iterations}_output.csv", index=False)
    
    

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # ctrl + c
        print("\nGoodbye!")


