# The high-level constructor assembles a full agent; middleware adds control.
from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware, SummarizationMiddleware
 
agent = create_agent(
    model="claude-opus-4-8",
    tools=[inventory_lookup, place_order],
    system_prompt="You are a careful order-management assistant.",
    middleware=[
        SummarizationMiddleware(max_tokens_before_summary=4000),  # manage context
        HumanInTheLoopMiddleware(interrupt_on=["place_order"]),   # approve sensitive actions
    ],
)
result = agent.invoke({"messages": [{"role": "user", "content": "Reorder SKU-4421."}]})
