def extract(**context):
    """Extract: pull new/changed documents from the source into staging."""
    docs = fetch_new_documents(since=context["prev_execution_date"])  # incremental
    stage_documents(docs)                          # land raw docs (the 'load' of ELT)
    return len(docs)
 
def transform_and_index():
    """Transform: parse, chunk, embed, and upsert into the vector store."""
    for doc in staged_documents():
        text = parse_document(doc)                 # Chapter 16 parsing
        chunks = chunk_text(text, size_tokens=512, overlap_tokens=75)  # Chapter 14
        vectors = embed(chunks)                    # Part V embedding model
        vector_store.upsert(doc.id, chunks, vectors)   # idempotent by doc.id
