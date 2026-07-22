# An AI endpoint: a Pydantic contract, an async handler, injected dependencies.
from fastapi import FastAPI, Depends
from pydantic import BaseModel
 
app = FastAPI()
 
class ChatRequest(BaseModel):
    message: str
    temperature: float = 0.7
 
class ChatResponse(BaseModel):
    answer: str
    tokens_used: int
 
@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest, agent=Depends(get_agent)):   # dependency injected
    result = await agent.arun(req.message, temperature=req.temperature)
    return ChatResponse(answer=result.text, tokens_used=result.tokens)
