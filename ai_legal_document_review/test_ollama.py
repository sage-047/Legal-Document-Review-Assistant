from review_engine import review_contract

print("Testing Ollama connection...")
try:
    response = review_contract("Hello, are you working?")
    print("Response received:")
    print(response)
except Exception as e:
    print(f"Failed: {e}")
