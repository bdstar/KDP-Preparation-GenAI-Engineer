import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
 
model_name = "some-org/some-7b-base"
bnb = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",           # 4-bit NormalFloat
    bnb_4bit_use_double_quant=True,      # quantize the quantization constants
    bnb_4bit_compute_dtype=torch.bfloat16,
)
model = AutoModelForCausalLM.from_pretrained(model_name, quantization_config=bnb, device_map="auto")
tok = AutoTokenizer.from_pretrained(model_name)
