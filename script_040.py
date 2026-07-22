from pydantic import BaseModel, Field
 
class Sentiment(BaseModel):
    reasoning: str = Field(description="Brief justification, written before the label")
    label: str = Field(description="One of: positive, negative, neutral")
    confidence: float = Field(description="Model confidence from 0.0 to 1.0")
 
# The schema derived from this model is compiled into a grammar that the
# decoder is constrained to follow, so the returned object is guaranteed
# to have exactly these fields and types — reasoning first, so it informs
# the label. Validating that the *values* make sense is still your job.
