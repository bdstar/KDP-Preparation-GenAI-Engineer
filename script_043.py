tiktokenAutoTokenizer
import tiktoken
enc = tiktoken.encoding_for_model("gpt-4o")     # the model's real tokenizer
n_tokens = len(enc.encode("How many tokens is this sentence?"))
 
# For a Hugging Face model, the model's own tokenizer counts exactly:
# from transformers import AutoTokenizer
# tok = AutoTokenizer.from_pretrained("some-org/some-model")
# n_tokens = len(tok("How many tokens is this sentence?").input_ids)
