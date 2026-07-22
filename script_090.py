from fastapi import FastAPI
 
app = FastAPI(title="LLM Inference API", version="1.0")   # docs served automatically at /docs
 
@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest, user: str = Depends(current_user), agent=Depends(get_agent)):
    try:
        result = await agent.arun(req.message)        # authenticated inference
        return ChatResponse(answer=result.text, sources=result.sources)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Generation failed: {e}")
