from transformers import AutoModelForCausalLM, BitsAndBytesConfig
import torch
 
quant = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4",
                           bnb_4bit_compute_dtype=torch.bfloat16)
model = AutoModelForCausalLM.from_pretrained(
    "some-open-llm", quantization_config=quant, device_map="auto")
# The 4-bit model uses ~1/4 the memory of 16-bit — bigger models fit, decode is faster.
