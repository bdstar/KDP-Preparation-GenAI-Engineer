# Stream tokens to the client as Server-Sent Events.
from fastapi.responses import StreamingResponse
 
@app.post("/chat/stream")
async def chat_stream(req: ChatRequest, agent=Depends(get_agent)):
    async def event_generator():
        async for token in agent.astream(req.message):     # tokens as they generate
            yield f"data: {token}\n\n"                       # SSE event format
        yield "data: [DONE]\n\n"                             # signal completion
    return StreamingResponse(event_generator(), media_type="text/event-stream")
