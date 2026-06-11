from dotenv import load_dotenv

load_dotenv()

import os
import requests
from langchain_core.tools import StructuredTool
from langgraph.prebuilt import ToolNode

from schemas import AnswerQuestion, ReviseAnswer


class SearxngTool:
    def __init__(self, base_url: str | None = None, max_results: int = 5, engine: str | None = None):
        self.base_url = (base_url or os.getenv("SEARXNG_URL") or "https://searxng.org").rstrip("/")
        self.max_results = max_results
        self.engine = engine

    def _search(self, q: str):
        params = {"q": q, "format": "json", "categories": "general"}
        if self.engine:
            params["engines"] = self.engine
        try:
            resp = requests.get(f"{self.base_url}/search", params=params, timeout=10)
            resp.raise_for_status()
            data = resp.json()
            results = []
            for hit in data.get("results", [])[: self.max_results]:
                results.append({"title": hit.get("title"), "content": hit.get("content"), "url": hit.get("url")})
            return results
        except Exception as e:
            return [{"error": str(e)}]

    def batch(self, queries: list[dict]):
        return [self._search(q.get("query") if isinstance(q, dict) else q) for q in queries]


searx_tool = SearxngTool(max_results=5)


def run_queries(search_queries: list[str], **kwargs):
    """Run the generated queries."""
    return searx_tool.batch([{"query": query} for query in search_queries])


execute_tools = ToolNode(
    [
        StructuredTool.from_function(run_queries, name=AnswerQuestion.__name__),
        StructuredTool.from_function(run_queries, name=ReviseAnswer.__name__),
    ]
)