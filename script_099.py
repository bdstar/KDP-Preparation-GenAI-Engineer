# A serving runtime (e.g. vLLM) handles continuous batching and KV-cache paging.
from vllm import LLM, SamplingParams
 
llm = LLM(model="some-open-llm", quantization="awq")   # optimized, quantized serving
params = SamplingParams(max_tokens=256)
# Many concurrent requests are batched dynamically — finished sequences are
# replaced immediately, keeping the GPU fully utilized (Section 29.3).
outputs = llm.generate(list_of_prompts, params)
