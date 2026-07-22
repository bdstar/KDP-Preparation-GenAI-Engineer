# Streaming: yield each token as it is produced (integrates with the FastAPI SSE
# endpoint of Chapter 23), so the user sees output begin immediately.
for token in llm.generate_stream(prompt, params):
    yield token                                # time-to-first-token stays low
