import faiss
import numpy as np
 
# Build a flat (exact) index over normalized embeddings, then an HNSW index.
d = 768                                   # embedding dimension
flat = faiss.IndexFlatIP(d)               # inner product = cosine on normalized vectors
hnsw = faiss.IndexHNSWFlat(d, 32)         # 32 = M, the links-per-node parameter
hnsw.hnsw.efConstruction = 200            # build-time search width
 
vectors = np.random.rand(100_000, d).astype("float32")
faiss.normalize_L2(vectors)               # normalize so inner product = cosine
hnsw.add(vectors)                         # index 100k vectors
 
query = vectors[:1]                       # a query vector (already normalized)
hnsw.hnsw.efSearch = 64                   # query-time recall/latency dial
scores, ids = hnsw.search(query, k=5)     # find the 5 nearest neighbors
