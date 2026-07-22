from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
 
app = FastAPI(title="LLM Service", version="1.0.0")
 
class GenerateRequest(BaseModel):
    prompt: str = Field(min_length=1, max_length=8000)
    max_tokens: int = Field(default=256, ge=1, le=2048)
 
class GenerateResponse(BaseModel):
    text: str
    tokens_used: int
 
@app.post("/generate", response_model=GenerateResponse)
async def generate(req: GenerateRequest, user=Depends(current_user)):
    try:
        out = await model.generate(req.prompt, max_tokens=req.max_tokens)
    except TimeoutError:
        raise HTTPException(status_code=504, detail="upstream timeout")
    return GenerateResponse(text=out.text, tokens_used=out.tokens)
 
@app.post("/generate/stream")                 # SSE: first token fast (Ch. 29.3)
async def generate_stream(req: GenerateRequest, user=Depends(current_user)):
    async def events():
        async for token in model.stream(req.prompt, max_tokens=req.max_tokens):
            yield f"data: {token}\n\n"
        yield "data: [DONE]\n\n"
    return StreamingResponse(events(), media_type="text/event-stream")
 
@app.get("/health")                            # liveness for K8s / load balancers
async def health(): return {"status": "ok"}
