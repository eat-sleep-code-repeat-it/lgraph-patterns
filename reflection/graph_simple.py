from typing import Dict, Any, Optional
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import StateGraph, START, END

from state import MessageResponseState, Decision, NodeName
from nodes import writer_node, reviewer_node, publisher_node

def should_continue(state: MessageResponseState) -> str:
    """Determine whether to continue the revision process based on the current state.
    Args:
        state: Current state containing messages, revision count, and reviewer decision.
    Returns:
        Name of the next node to execute(writer_node or publisher_node).
    """
    if state.get("continue_revision", False):
        return NodeName.WRITER.value    
    return NodeName.PUBLISHER.value

def create_reflection_graph() -> StateGraph:
    """Create a state graph for the reflection workflow.
    Returns:
        A StateGraph object representing the workflow with defined nodes and transitions.
    """
    
    workflow = StateGraph(MessageResponseState)
    workflow.add_node(NodeName.WRITER.value, writer_node)
    workflow.add_node(NodeName.REVIEWER.value, reviewer_node)
    workflow.add_node(NodeName.PUBLISHER.value, publisher_node)

    workflow.add_edge(START, NodeName.WRITER.value)
    workflow.add_edge(NodeName.WRITER.value, NodeName.REVIEWER.value)
    workflow.add_conditional_edges(
        NodeName.REVIEWER.value,
        should_continue,
        {
            NodeName.WRITER.value: NodeName.WRITER.value,
            NodeName.PUBLISHER.value: NodeName.PUBLISHER.value,
        },
    )
    workflow.add_edge(NodeName.PUBLISHER.value, END)
    return workflow

async def process_customer_message(
    customer_message: str,
    thread_id: str = "message_112233",
    checkpointer: Optional[InMemorySaver] = None
) -> Dict[str, Any]:
    """Process a customer message through the reflection workflow.
    Args:
        customer_message: The original message from the customer to be processed.
        thread_id: Unique identifier for the message thread, used for state tracking.
        checkpointer: Optional InMemorySaver instance for checkpointing state.
    Returns:
        Final state after processing the message through the workflow.
    """

    workflow = create_reflection_graph()
    app = (
        workflow.compile(checkpointer=checkpointer)
        if checkpointer 
        else workflow.compile()
    )

    # Initialize workflow state
    initial_state = {
        "messages":[HumanMessage(content=customer_message)],
        "original_customer_message": customer_message,
        "revision_count": 0,
        "latest_feedback_for_reviewer": "",
        "latest_message_response_by_writer": "",
        "latest_reviewer_decision": Decision.REVISE.value,
        "continue_revision": True
    }
    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }
    final_state = await app.ainvoke(
        initial_state, 
        config=config
    )
    return final_state

async def main() -> None:
    print("Customer comment response system - Reflection Pattern Demo\n")

    # sample customer comment
    sample_comment = (
        "I recently purchased a product from your store and I am very disappointed with the quality. "
        "The item arrived damaged and does not work as advertised. I would like a refund or a replacement."
    )

    # Process the comment
    checkpointer = InMemorySaver()
    result = await process_customer_message(
        customer_message=sample_comment,
        checkpointer=checkpointer,
        thread_id="message_112233"
    )

    # Display result
    print(f"\n Comment: {sample_comment}")
    print(f"\n Response: {result.get('latest_message_response_by_writer', 'N/A')}")
    print("-"*80)

    print("\n Status: Response ready to send!")
    print("\n Demo completed. All customer comments have been processed.\n")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())