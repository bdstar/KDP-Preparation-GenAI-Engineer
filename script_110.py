# The core is assembled from what you have already built. For the RAG assistant:
pipeline = RAGPipeline(
    ingestion=DocumentIngestion(parser=structured_parser, chunker=chunker),  # Part V
    retriever=HybridRetriever(vector_store=store, reranker=reranker),         # Ch 14
    generator=GroundedGenerator(model=model, cite_sources=True),             # Part V
)
# For the automation platform: a Crew / LangGraph multi-agent system (Ch 21).
# For the voice product: a voice pipeline (Ch 22) over an agent (Part VI).
