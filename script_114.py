import asyncio
from tenacity import retry, stop_after_attempt, wait_exponential
 
@retry(stop=stop_after_attempt(3), wait=wait_exponential(min=1, max=8))
async def call_model(prompt: str):
    return await asyncio.wait_for(model.generate(prompt), timeout=30)  # always time out
 
async def generate_with_fallback(prompt: str):
    try:
        return await call_model(prompt)
    except Exception:
        return cached_or_simpler_response(prompt)      # degrade, don't fail (Ch. 26.3)
