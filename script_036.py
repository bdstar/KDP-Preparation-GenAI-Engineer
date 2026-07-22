out = model.generate(**inputs, max_new_tokens=60, do_sample=True,
                     temperature=0.7, top_p=0.9, repetition_penalty=1.2)
print("PRODUCTION-STYLE:\n", tok.decode(out[0], skip_special_tokens=True))
