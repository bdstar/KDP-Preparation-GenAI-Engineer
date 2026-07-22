# src/genai_scaffold/tokens.py
"""Small text utilities for GenAI pipelines."""
 
def count_tokens(text: str) -> int:
    """Return a whitespace-token count for `text` (a cheap proxy for length)."""
    return len(text.split())
 
def truncate_to_tokens(text: str, max_tokens: int) -> str:
    """Truncate `text` to at most `max_tokens` whitespace tokens."""
    if max_tokens < 0:
        raise ValueError("max_tokens must be non-negative")
    return " ".join(text.split()[:max_tokens])
