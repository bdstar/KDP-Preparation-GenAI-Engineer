from dataclasses import dataclass
 
@dataclass
class Pricing:
    input_per_m: float          # dollars per 1M input tokens
    output_per_m: float         # dollars per 1M output tokens
    cached_input_per_m: float   # dollars per 1M cached input tokens
 
def call_cost(in_tokens, out_tokens, pricing, cached_in_tokens=0):
    fresh_in = in_tokens - cached_in_tokens
    return (fresh_in * pricing.input_per_m
            + cached_in_tokens * pricing.cached_input_per_m
            + out_tokens * pricing.output_per_m) / 1_000_000
