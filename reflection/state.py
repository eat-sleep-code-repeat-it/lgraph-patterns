from dataclasses import dataclass
from enum import Enum
from typing import Literal

from langgraph.graph import MessagesState

@dataclass
class ContextSchema:
    user_name: str

class Decision(str, Enum):
    """Enumeration for reviewer decision types."""
    APPROVE = "APPROVE"
    REVISE = "REVISE"

class NodeName(str, Enum):
    """Enumeration for node names in the graph."""
    WRITER = "writer_node"
    REVIEWER = "reviewer_node"
    PUBLISHER = "publisher_node"

@dataclass
class AIReviewerResponse:
    """Represents the AI reviewer's decision.
    Attributes:
        decision: The reviewer's decision, either APPROVE or REVISE.
    """
    decision: Literal["APPROVE", "REVISE"]

class MessageResponseState(MessagesState):
    """Extended state for tracking reflection workflow.
    Attributes:
        revision_count: Number of revisions made to the content.
        origional_customer_message: The original message or content before any revisions.
        latest_feedback_for_reviewer: Most recent feedback from reviewer.
        latest_message_response_by_writer: Most recent response writtern.
        latest_reviewer_decision: Current decision from reviewer (APPROVE/REVISE).
        continue_revision: Flag to indicatig whether to continue revisions or not.       
    """
    revision_count: int = 0
    origional_customer_message: str = ""
    latest_feedback_for_reviewer: str = ""
    latest_message_response_by_writer: str = ""
    latest_reviewer_decision: str = Decision.APPROVE.value
    continue_revision: bool = False