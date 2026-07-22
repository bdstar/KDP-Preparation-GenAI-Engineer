out = model.generate(**inputs, max_new_tokens=60, do_sample=False)
print("GREEDY:\n", tok.decode(out[0], skip_special_tokens=True))
