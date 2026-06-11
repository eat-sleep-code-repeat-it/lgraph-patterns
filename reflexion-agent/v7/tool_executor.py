from langchain_community.tools import DuckDuckGoSearchResults
from langchain_core.tools import StructuredTool
from langgraph.prebuilt import ToolNode

from schemas import AnswerQuestion, ReviseAnswer

ddg_tool = DuckDuckGoSearchResults()


def run_queries(search_queries: list[str], **kwargs):
    """Run the generated queries."""
    return [ddg_tool.invoke(query) for query in search_queries]


execute_tools = ToolNode(
    [
        StructuredTool.from_function(
            run_queries,
            name=AnswerQuestion.__name__,
        ),
        StructuredTool.from_function(
            run_queries,
            name=ReviseAnswer.__name__,
        ),
    ]
)