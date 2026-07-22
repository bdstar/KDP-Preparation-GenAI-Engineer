# top-k: sample among the k most likely tokens
out = model.generate(**inputs, max_new_tokens=60, do_sample=True,
                     temperature=0.8, top_k=40)
print("TOP-K 40:\n", tok.decode(out[0], skip_special_tokens=True))
 
# top-p (nucleus): sample from the smallest set with cumulative prob > p
out = model.generate(**inputs, max_new_tokens=60, do_sample=True,
                     temperature=0.8, top_p=0.9)
print("\nTOP-P 0.9:\n", tok.decode(out[0], skip_special_tokens=True))
