from pathlib import Path
 
def ingest(path: str, use_structured: bool = True) -> list[dict]:
    text = parse_structured(path) if use_structured else parse_naive(path)
    meta = {"source": Path(path).name, "parser": "structured" if use_structured else "naive"}
    chunks = chunk_text(text, size_tokens=512, overlap_tokens=75)   # from Chapter 14
    return [{"text": c, "metadata": {**meta, "chunk": i}} for i, c in enumerate(chunks)]
