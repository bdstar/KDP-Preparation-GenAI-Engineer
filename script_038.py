def compare(prompt, hf_model, hf_tok, hf_name, ollama_name):
    hf_text, hf_t = query_hf(hf_model, hf_tok, prompt)
    ol_text, ol_t = query_ollama(ollama_name, prompt)
    print(f"PROMPT: {prompt}\n")
    print(f"[{hf_name} · {hf_t:.1f}s]\n{hf_text}\n")
    print(f"[{ollama_name} · {ol_t:.1f}s]\n{ol_text}\n")
 
# compare("Explain what a transformer is in two sentences.",
#         hf_model, hf_tok, "HF-small-llm", "llama3.2")
