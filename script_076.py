# LlamaIndex builds a retrieval system directly from data.
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
 
documents = SimpleDirectoryReader("./corpus").load_data()   # connectors load data
index = VectorStoreIndex.from_documents(documents)          # chunk, embed, index
query_engine = index.as_query_engine(similarity_top_k=5)    # retrieval + generation
answer = query_engine.query("What does the handbook say about refunds?")
