def compare_cost(original, optimized, count, pricing, out_tokens=300, cached_in_optimized=0):
    orig = call_cost(count(original), out_tokens, pricing)
    opt  = call_cost(count(optimized), out_tokens, pricing, cached_in_tokens=cached_in_optimized)
    saved = (orig - opt) / orig if orig else 0
    print(f"  original : {count(original):5d} in  -> ${orig:.5f}/call")
    print(f"  optimized: {count(optimized):5d} in  -> ${opt:.5f}/call")
    print(f"  saving   : {saved:.0%} per call")
 
# At scale the per-call saving multiplies: a 40% cut over 1M calls/month is
# real money, which is the entire point of measuring it.
