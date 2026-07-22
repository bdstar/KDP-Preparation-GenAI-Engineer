# Each row records one query and what the RAG system did with it:
eval_data = [
    {"question": "What is the vanishing gradient problem?",
     "contexts": retrieve("What is the vanishing gradient problem?"),   # Ch. 14 retriever
     "answer":   rag_answer("What is the vanishing gradient problem?"), # Ch. 14 generator
     "ground_truth": "Gradients shrink through many layers, stalling learning in early layers."},
    # ... more cases drawn from your real use case ...
]
