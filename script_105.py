from pydantic import BaseModel, Field, ValidationError
 
class AgentResponse(BaseModel):
    answer: str = Field(min_length=1)
    confidence: float = Field(ge=0.0, le=1.0)
    sources: list[str] = []
 
def validate_response(raw: str) -> AgentResponse | None:
    try:
        return AgentResponse.model_validate_json(raw)
    except ValidationError:
        return None       # caught: fall back to a safe default rather than propagate
