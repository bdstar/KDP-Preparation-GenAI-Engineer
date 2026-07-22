def batch_count_tokens(texts: list[str]) -> list[int]:
    """Return the whitespace-token count for each string in `texts`."""
    return [count_tokens(t) for t in texts]
