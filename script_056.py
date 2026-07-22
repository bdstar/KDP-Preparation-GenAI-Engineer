import chromadb
 
client = chromadb.PersistentClient(path="./chroma_store")   # survives restarts
col = client.get_or_create_collection("handbook")
 
# Chroma stores documents, metadata, and (optionally) computes embeddings for you:
col.add(documents=["Attention scales quadratically with sequence length.",
                   "RAG grounds a model in retrieved evidence."],
        metadatas=[{"source": "ch8"}, {"source": "ch14"}],
        ids=["c1", "c2"])
 
hits = col.query(query_texts=["Why is long context expensive?"], n_results=2)
