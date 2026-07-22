from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
 
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]   # accumulates across nodes
