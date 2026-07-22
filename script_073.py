model_with_tools = model.bind_tools([inventory_lookup, place_order])
 
def agent_node(state: AgentState):
    return {"messages": [model_with_tools.invoke(state["messages"])]}
 
def tool_node(state: AgentState):
    from langchain_core.messages import ToolMessage
    last = state["messages"][-1]
    results = []
    for call in last.tool_calls:                       # execute each requested tool
        output = TOOLS[call["name"]](**call["args"])
        results.append(ToolMessage(content=str(output), tool_call_id=call["id"]))
    return {"messages": results}
