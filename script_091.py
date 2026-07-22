from fastapi.responses import StreamingResponse
 
@app.post("/chat/stream")
async def chat_stream(req: ChatRequest, user: str = Depends(current_user), agent=Depends(get_agent)):
    async def events():
        try:
            async for token in agent.astream(req.message):
                yield f"data: {token}\n\n"
            yield "data: [DONE]\n\n"
        except Exception as e:
            yield f'event: error\ndata: {e}\n\n'
    return StreamingResponse(events(), media_type="text/event-stream")
