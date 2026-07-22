def retrieve(question: str, k: int = 5) -> list[str]:
    q_vec = embedder.encode([question]).tolist()
    hits = collection.query(query_embeddings=q_vec, n_results=k)
    return hits["documents"][0]
call_model
def answer(question: str, call_model) -> str:
    chunks = retrieve(question)
    context = "\n\n".join(f"[{i+1}] {c}" for i, c in enumerate(chunks))
    prompt = (
        "Answer the question using ONLY the context below. "
        "Cite sources by their [number]. If the context does not contain "
        "the answer, say you don't know.\n\n"
        f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
    )
    return call_model(prompt)
