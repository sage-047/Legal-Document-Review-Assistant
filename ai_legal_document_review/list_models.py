import ollama

try:
    with open("models_ollama.txt", "w", encoding="utf-8") as f:
        response = ollama.list()
        
        # Access 'models' attribute if it exists (e.g. ListResponse object)
        # Otherwise try key access if it's a dict
        if hasattr(response, 'models'):
            models = response.models
        elif isinstance(response, dict):
            models = response.get('models', [])
        else:
            # Fallback/Debug: treat response itself as the iterable or handle unknown
            models = response

        for m in models:
            # m should be a Model object or dict
            # Model object usually has 'model' attribute for the name
            # Dict usually has 'name' or 'model'
            if hasattr(m, 'model'):
                name = m.model
            elif isinstance(m, dict):
                name = m.get('model') or m.get('name')
            else:
                name = str(m)
                
            f.write(str(name) + "\n")
            
    print("Models written to models_ollama.txt")
except Exception as e:
    print(f"Error listing models: {e}")
