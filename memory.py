memory_store = []

def save_to_memory(observation: dict):
    memory_store.append(observation)

def get_memory():
    return memory_store