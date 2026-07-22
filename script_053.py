documents
def chunk_text(text: str, size: int = 2000, overlap: int = 300) -> list[str]:
    # size/overlap in characters here (~512/~75 tokens) for a minimal example;
    # production code uses a token-aware recursive splitter.
    chunks, start = [], 0
    while start < len(text):
        chunks.append(text[start:start + size])
        start += size - overlap
    return chunks
 
all_chunks = [c for doc in documents for c in chunk_text(doc)]
sentence-transformers
from sentence_transformers import SentenceTransformer
import chromadb
 
embedder = SentenceTransformer("BAAI/bge-small-en-v1.5")   # a strong small open model
client = chromadb.PersistentClient(path="./rag_store")
collection = client.get_or_create_collection("docs")
 
collection.add(
    ids=[f"chunk-{i}" for i in range(len(all_chunks))],
    documents=all_chunks,
    embeddings=embedder.encode(all_chunks).tolist(),   # same model used for queries below
)
