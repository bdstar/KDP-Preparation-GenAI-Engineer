import tiktoken
 
def make_counter(model="gpt-4o"):
    enc = tiktoken.encoding_for_model(model)
    return lambda text: len(enc.encode(text))
 
count = make_counter()
