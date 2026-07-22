tokenizer.apply_chat_template
from transformers import AutoTokenizer
 
tok = AutoTokenizer.from_pretrained("some-org/some-instruct-model")
messages = [
    {"role": "system", "content": "You are a concise financial analyst."},
    {"role": "user", "content": "Summarize why interest rates affect stock prices."},
]
# Serialize into the model's exact trained format, ready to generate from:
prompt = tok.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)
