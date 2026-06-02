from pathlib import Path
from typing import Optional
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

from state import MessageResponseState, Decision, NodeName, AIReviewerResponse
from config import (
    MAX_REVISIONS,
    DEFAULT_MODEL,
    DEFAULT_TEMPERATURE,
    MAX_REVISIONS_MESSAGE,
)

BASE_DIR = Path(__file__).resolve().parent
PROMPTS_DIR = BASE_DIR / "prompts"


def _create_writer_message(
    state: MessageResponseState, feedback: Optional[str] = None
) -> list:
    """Create message list for writer node invocation
    Args:
        state: Current state containing messages.
        feedback: Optional feedback from reviewer for revision.
    Returns:
        List of messages to be sent to the AI model.
    """

    writer_prompt = open(PROMPTS_DIR / "writer_instructions.md").read()
    messages = [{"role": "system", "content": writer_prompt}] + state["messages"]
    original_message = state.get("original_customer_message", "")
    messages.append(HumanMessage(content=f"\n\nOriginal Customer Message:\n{original_message}\n\n"))

    if feedback:
        feedback_message = (
            f"\n\nFeedback from reviewer:\n{feedback}\n\n"
            "Please revise your response based on this feedback."
        )
        messages.append(HumanMessage(content=feedback_message))
    return messages

def _update_writer_state(
        state: MessageResponseState, response_content: str
) -> MessageResponseState:
    """Update the state after writer node generates response
    Args:
        state: Current state containing messages and revision count.
        response_content: Generated response content from the AI model.
    Returns:
        Updated state dictionary with new messages and incremented revision count if feedback was provided.
    """

    revision_count = state.get("revision_count", 0)    
    return {
        **state,
        "latest_message_response_by_writer": response_content,
        "messages": [
            AIMessage(content=response_content, name=NodeName.WRITER.value)
        ],
        "revision_count": revision_count + 1
    }

def writer_node(
    state: MessageResponseState
) -> MessageResponseState:
    """Writer node that generates a response based on the current state and optional feedback.
    Args:
        state: Current state containing messages and revision count.
        feedback: Optional feedback from reviewer for revision.
    Returns:
        Updated state after generating response and incrementing revision count if feedback was provided.
    """
    revision_count = state.get("revision_count", 0)
    latest_decision = state.get("latest_decision_by_reviewer", Decision.APPROVE)

    # Determine if this is a revision or initial write
    feedback = None
    if revision_count >= 0 and latest_decision == Decision.REVISE.value:
        feedback = state.get("latest_feedback_for_reviewer", "")

    # Generate response 
    messages = _create_writer_message(state, feedback)

    # Initialize the LLM
    llm = ChatOpenAI(
        model=DEFAULT_MODEL, 
        temperature=DEFAULT_TEMPERATURE
    )

    # Invoke the model with reasoning configuration
    response = llm.invoke(messages)

    # Update and return state
    return _update_writer_state(state, response.content)

def reviewer_node(
    state: MessageResponseState
) -> MessageResponseState:
    """Reviewer node that evaluates the writer's response and provides feedback.
    Args:
        state: Current state containing written response.
    Returns:
        Updated state with reviewer feedback and continuation decision.
    """
    revision_count = state.get("revision_count", 0)

    # Check if max revisions reached
    if revision_count >= MAX_REVISIONS:
        return {
            **state,
            "continue_revision": False,
            "latest_reviewer_decision": Decision.APPROVE.value,
            "messages":[
                HumanMessage(content=MAX_REVISIONS_MESSAGE, name=NodeName.REVIEWER.value),
                HumanMessage(content=f"{revision_count} reviewer decision: {Decision.APPROVE.value}", name=NodeName.REVIEWER.value),
                HumanMessage(content=f"{revision_count} continue revision?: {False}", name=NodeName.REVIEWER.value),
            ]
        }

    # Get response and comment for review
    latest_response = state.get("latest_message_response_by_writer", "")
    original_message = state.get("original_customer_message", "")

    # Create review messages
    reviewer_prompt = open(PROMPTS_DIR / "reviewer_instructions.md").read()
    messages = [
        {"role": "system", "content": reviewer_prompt}
    ] + state["messages"]

    review_content = (
        f"\n\nOriginal Customer Message:\n{original_message}\n\n"
        f"\n\nProposed Response:\n{latest_response}\n\n"
    )
    messages.append(HumanMessage(content=review_content))

    # Get reviewer feedback
    # Initialize the LLM
    llm = ChatOpenAI(
        model=DEFAULT_MODEL, 
        temperature=DEFAULT_TEMPERATURE
    )

    response = llm.invoke(messages)
    feedback_text = response.content

    # Extract decision using structured output parsing
    decision_prompt = (
        "Based on the given feedback provided by the agent, idenntify if "
        "the agent suggests revision or approves the content as is."
        f"Here is the feedback: \n{feedback_text}\n\n"
    )
    reviewer_response = llm.with_structured_output(
        AIReviewerResponse,
        ## you need uncomment the below line to fallback to function_calling
        ## for llm models that do not support structured output parsing natively (e.g. gpt-3.5-turbo)
        #method="function_calling"
    ).invoke(decision_prompt)
    decision = reviewer_response.get("decision", Decision.REVISE.value)

    # determin if another revision is needed
    continue_revision = (
        decision == Decision.REVISE.value and
        revision_count < MAX_REVISIONS
    )
    return {
        **state,
        "latest_feedback_for_reviewer": feedback_text,
        "latest_reviewer_decision": decision,
        "continue_revision": continue_revision,
        "messages":[
            HumanMessage(content=f"{revision_count} feedback for writer: {feedback_text}", name=NodeName.REVIEWER.value),
            HumanMessage(content=f"{revision_count} reviewer decision: {decision}", name=NodeName.REVIEWER.value),
            HumanMessage(content=f"{revision_count} continue revision?: {continue_revision}", name=NodeName.REVIEWER.value),
        ]
    }

def publisher_node(
    state: MessageResponseState
) -> MessageResponseState:
    """Final node that publishes the approved response.
    Args:
        state: Final workflow state containing the approved response.
    Returns:
        unchanged state (ready for publication)
    """

    return {**state}