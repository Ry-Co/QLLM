import subprocess
import ollama
import pandas as pd


# we can use this shell() to force ollama to load/unload the model from memory
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


def generate_response(model, query):
    client = ollama.Client()
    response = client.generate(model, query)
    return response["response"]


def run_model_n_times(m, q, n):
    # wrapper to make main more readable - avoiding nested for each
    # m = model name string
    # q = query string
    # n = iterations

    # list for outputs - preallocated for iterations
    model_names = [m] * n
    queries = [q] * n
    responses = [] * n

    for i in range(n):
        try:
            response = generate_response(m, q)
            responses.append(response)
            print(f"Query {i + 1:3d}: {response.strip()}")
        except Exception as e:
            print(f"Query {i + 1:3d}: Error - {e}")

    df = pd.DataFrame(
        {"model_name": model_names, "query": queries, "response": responses}
    )
    return df


def main():
    model = "dolphin3"
    # model = "gemma3"
    query = "Respond with a random digit."
    iterations = 100

    out = run_model_n_times(model, query, iterations)
    print(out)
    
    # df.to_csv(f"{model}_{iterations}_output.csv", index=False)
    # df.to_excel(f"{model}_{iterations}_output.csv", index=False)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye!")
