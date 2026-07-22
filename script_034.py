for temp in (0.3, 0.7, 1.2):
    out = model.generate(**inputs, max_new_tokens=60, do_sample=True,
                         temperature=temp, top_k=0, top_p=1.0)
    print(f"\nTEMPERATURE {temp}:\n", tok.decode(out[0], skip_special_tokens=True))
