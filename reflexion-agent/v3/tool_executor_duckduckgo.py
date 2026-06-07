from dotenv import load_dotenv

load_dotenv()

# pip install ddgs

from ddgs import DDGS
from langchain_core.tools import StructuredTool
from langgraph.prebuilt import ToolNode

from schemas import AnswerQuestion, ReviseAnswer


def search_ddg(query: str, max_results: int = 5):
    """Search DuckDuckGo and return structured results."""
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=max_results))

    return [
        {
            "title": result.get("title"),
            "url": result.get("href"),
            "content": result.get("body"),
        }
        for result in results
    ]

def run_queries(search_queries: list[str], **kwargs):
    all_results = []

    for query in search_queries:
        all_results.extend(search_ddg(query))

    return all_results

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