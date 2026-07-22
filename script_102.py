# Pydantic as a guardrail: output that violates structure or constraints is caught.
from pydantic import BaseModel, Field, ValidationError
 
class ModerationDecision(BaseModel):
    category: str = Field(pattern="^(safe|unsafe|needs_review)$")   # allowed values only
    confidence: float = Field(ge=0.0, le=1.0)                       # must be in [0,1]
    reason: str = Field(min_length=1)
 
def validate_output(raw: str) -> ModerationDecision | None:
    try:
        return ModerationDecision.model_validate_json(raw)   # conforms, or is rejected
    except ValidationError:
        return None      # malformed/invalid output is caught, not silently propagated
