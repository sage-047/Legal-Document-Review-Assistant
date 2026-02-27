import ollama

def review_contract(prompt: str) -> str:
    """
    Sends the contract text + playbook prompt to local Ollama and returns the response.
    """
    try:
        response = ollama.chat(model='llama3.2', messages=[
            {
                'role': 'user',
                'content': prompt,
            },
        ])
        return response['message']['content']
    except Exception as e:
        return f"Error during Ollama review: {str(e)}. Make sure Ollama is running and you have run 'ollama pull llama3.2'."
