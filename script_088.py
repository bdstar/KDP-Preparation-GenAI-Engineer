from pydantic import BaseModel, Field
 
class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=4000, description="The user's prompt")
 
class ChatResponse(BaseModel):
    answer: str = Field(description="The model's generated answer")
    sources: list[str] = Field(default=[], description="Citations, if from a RAG system")
