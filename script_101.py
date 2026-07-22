import time
 
def benchmark(generate_fn, prompts):
    start = time.time()
    first_token_time, total_tokens = None, 0
    for token in generate_fn(prompts):
        if first_token_time is None:
            first_token_time = time.time() - start     # TTFT
        total_tokens += 1
    elapsed = time.time() - start
    print(f"TTFT={first_token_time*1000:.0f}ms  "
          f"throughput={total_tokens/elapsed:.0f} tok/s")
