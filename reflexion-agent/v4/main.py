from typing import List, TypedDict

from langchain_core.messages import BaseMessage, ToolMessage, HumanMessage
from langgraph.graph import END, StateGraph, add_messages

from chains import revisor_node, first_responder_node
from tool_executor import execute_tools


class AgentState(TypedDict):
    messages: List[BaseMessage]


MAX_ITERATIONS = 2
builder = StateGraph(state_schema=AgentState)
builder.add_node("draft", first_responder_node)
builder.add_node("execute_tools", execute_tools)
builder.add_node("revise", revisor_node)
builder.add_edge("draft", "execute_tools")
builder.add_edge("execute_tools", "revise")


def event_loop(state: AgentState) -> str:
    count_tool_visits = sum(isinstance(item, ToolMessage) for item in state["messages"])
    num_iterations = count_tool_visits
    if num_iterations > MAX_ITERATIONS:
        return END
    return "execute_tools"


builder.add_conditional_edges("revise", event_loop)
builder.set_entry_point("draft")
graph = builder.compile()

print(graph.get_graph().draw_mermaid())


res = graph.invoke(
    {"messages": [HumanMessage(content="Write about AI-Powered SOC / autonomous soc  problem domain, list startups that do that and raised capital.")]}
)
print(res["messages"][-1].tool_calls[0]["args"]["answer"])
print(res)