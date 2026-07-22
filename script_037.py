import time
from transformers import AutoTokenizer, AutoModelForCausalLM
 
def query_hf(model, tok, prompt: str, max_new_tokens: int = 80) -> tuple[str, float]:
    inputs = tok(prompt, return_tensors="pt").to(model.device)
    start = time.perf_counter()
    out = model.generate(**inputs, max_new_tokens=max_new_tokens,
                         do_sample=True, temperature=0.7, top_p=0.9)
    elapsed = time.perf_counter() - start
    text = tok.decode(out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)
    return text, elapsed
requests
import requests, time
 
def query_ollama(model_name: str, prompt: str) -> tuple[str, float]:
    start = time.perf_counter()
    resp = requests.post("http://localhost:11434/api/generate", json={
        "model": model_name,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.7, "top_p": 0.9},
    })
    elapsed = time.perf_counter() - start
    return resp.json()["response"], elapsed
