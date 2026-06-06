from typing import TypedDict, Annotated

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, StateGraph
from langgraph.graph.message import add_messages

from chains import generate_chain, reflect_chain

REFLECT = "reflect"
GENERATE = "generate"

class MessageGraph(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def generation_node(state: MessageGraph):
    return {"messages": [generate_chain.invoke({"messages": state["messages"]})]}

def reflection_node(state: MessageGraph):
    res = reflect_chain.invoke({"messages": state["messages"]})
    return {"messages": [HumanMessage(content=res.content)]}

def should_continue(state: MessageGraph):
    if len(state["messages"]) > 6:
        return END
    return REFLECT

def main(inputs: any = None):
    builder = StateGraph(state_schema=MessageGraph)
    builder.add_node(GENERATE, generation_node)
    builder.add_node(REFLECT, reflection_node)
    builder.set_entry_point(GENERATE)

    # Must have the third input to draw topology graph correctly
    builder.add_conditional_edges(GENERATE, should_continue, path_map={END:END, REFLECT:REFLECT})
    builder.add_edge(REFLECT, GENERATE)

    graph = builder.compile()
    print(graph.get_graph().draw_mermaid())
    graph.get_graph().print_ascii()


    ### ready to run
    if inputs != None:
        print("Hello LangGraph")        
        response = graph.invoke(inputs)
        print(response)

if __name__ == "__main__":    
    inputs = {
        "messages": [
            HumanMessage(content="""Make this tweet better:
            @LangChainAI — newly Tool Calling feature is seriously underrated.
            After a long wait, it's  here- making the implementation of agents across different models with function calling - super easy.
            Made a video covering their newest blog post
            """)
        ]
    }   
    main()