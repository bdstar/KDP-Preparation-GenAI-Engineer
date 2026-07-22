result = app.invoke({"messages": [{"role": "user",
    "content": "Check stock for SKU-4421 and reorder it if it is below 900."}]})
print(result["messages"][-1].content)
# Then open LangSmith/Langfuse: the trace shows agent -> tool (inventory_lookup)
# -> agent -> tool (place_order) -> agent -> final answer, each step inspectable.
