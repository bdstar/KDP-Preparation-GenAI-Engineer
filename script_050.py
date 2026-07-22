# Each training example is a chat with the target behavior demonstrated:
example = {"messages": [
    {"role": "system", "content": "You are a helpful legal-intake assistant."},
    {"role": "user", "content": "I was rear-ended last week. What should I document?"},
    {"role": "assistant", "content": "Start by recording the date, time, and location..."},
]}
# A Hugging Face Dataset of such rows, with a train/validation split, is the input.
