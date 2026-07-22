# Index both versions and compare retrieval on a table-specific question:
q = "What was the revenue reported for the third quarter?"
for label, structured in [("naive", False), ("structured", True)]:
    chunks = ingest("financial_report.pdf", use_structured=structured)
    top = retrieve(q, chunks)                 # your Chapter 14 retriever
    print(f"[{label}] top chunk:\n{top[0]['text'][:200]}\n")
