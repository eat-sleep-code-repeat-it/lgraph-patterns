from typing import Annotated, List, TypedDict

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from langchain_core.messages import BaseMessage, ToolMessage, HumanMessage
from langgraph.graph import END, START, StateGraph, add_messages

from chains import first_responder_node, revisor_node
from tool_executor import tool_node

class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

from chains import revisor, first_responder
def draft_node(state: AgentState):
    """Draft the initial response."""
    response = first_responder.invoke({"messages": state["messages"]})
    return {"messages": [response]}

def revise_node(state: AgentState):
    """Revise the answer based on tool results."""
    response = revisor.invoke({"messages": state["messages"]})
    return {"messages": [response]}

def event_loop(state: AgentState) -> str:
    """Determine whether to continue or end based on iteration count."""
    count_tool_visits = sum(
        isinstance(item, ToolMessage) for item in state["messages"]
    )
    num_iterations = count_tool_visits
    if num_iterations > MAX_ITERATIONS:
        return END
    return "execute_tools"


MAX_ITERATIONS = 2
builder = StateGraph(state_schema=AgentState)
builder.add_node("draft", first_responder_node)
builder.add_node("execute_tools", tool_node)
builder.add_node("revise", revisor_node)

builder.add_edge("draft", "execute_tools")
builder.add_edge("execute_tools", "revise")
builder.add_conditional_edges("revise", event_loop, ["execute_tools", END])

#builder.add_edge(START, "draft")
builder.set_entry_point("draft")

graph = builder.compile()


print(graph.get_graph().draw_mermaid())
print(graph.get_graph().draw_ascii())
print("\ngoto: https://mermaid.live/")


graph.get_graph().draw_mermaid_png(output_file_path="graph.png")

"""
res = graph.invoke(
    {
    "messages": [HumanMessage(content="Write about AI-Powered SOC / autonomous soc  problem domain, list startups that do that and raised capital.")]}
)
print(res["messages"][-1].tool_calls[0]["args"]["answer"])
print(res)
"""