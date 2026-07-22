generate
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
 
name = "gpt2"  # small, fast, illustrative; swap for any small open model
tok = AutoTokenizer.from_pretrained(name)
model = AutoModelForCausalLM.from_pretrained(name)
 
prompt = "In the year 2050, artificial intelligence had become"
inputs = tok(prompt, return_tensors="pt")
