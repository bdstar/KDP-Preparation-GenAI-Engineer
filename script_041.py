from dataclasses import dataclass, field
 
@dataclass
class PromptVersion:
    name: str
    version: str                 # e.g. "1.0.0" — pin this in production
    template: str                # uses {placeholders}
    notes: str = ""
 
    def render(self, **kwargs) -> str:
        return self.template.format(**kwargs)
 
classify_v1 = PromptVersion(
    name="classify_sentiment", version="1.0.0",
    template="Classify the sentiment of this review as positive, negative, "
             "or neutral. Review: {review}\nSentiment:",
    notes="Baseline zero-shot.")
 
classify_v2 = PromptVersion(
    name="classify_sentiment", version="2.0.0",
    template="You are a precise sentiment classifier.\n"
             "Examples:\n'A dazzling triumph.' -> positive\n"
             "'The plot dragged badly.' -> negative\n"
             "Now classify. Review: {review}\nSentiment:",
    notes="Few-shot variant with a system-style preamble.")
