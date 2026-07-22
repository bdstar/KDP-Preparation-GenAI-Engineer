def should_continue(state: AgentState) -> str:
    return "tools" if state["messages"][-1].tool_calls else END
 
graph = StateGraph(AgentState)
graph.add_node("agent", agent_node)
graph.add_node("tools", tool_node)
graph.add_edge(START, "agent")
graph.add_conditional_edges("agent", should_continue, {"tools": "tools", END: END})
graph.add_edge("tools", "agent")                       # loop back — the cycle
app = graph.compile()
