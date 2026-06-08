# Generative AI: Engineering and Architecture: Proficient Above Average

1. A team manages a GenAI code completion tool. A postmortem from a recent incident identifies a memory leak in the model serving component. Concurrently, user feedback tickets consistently complain about slow and irrelevant suggestions. Monitoring data confirms a gradual increase in GPU memory usage over time, which correlates with a rise in p99 inference latency. How should the team synthesize this data to prioritize its next action?
Fix the memory leak in the model serving component, as it is the likely root cause of both the high latency and degraded suggestion quality.

2. You are developing a GenAI chatbot for an e-commerce platform. Users submit a mix of precise queries with specific attributes (such as brand, color, size) and broad, descriptive queries (such as "outfits for a beach wedding"). To maximize both relevance for specific filters and discovery for vague concepts, what retrieval approach offers the most robust solution?
A hybrid retrieval system combining keyword-based search for filtering attributes and vector-based search for semantic understanding

3. You are designing a Generative AI (GenAI) service that creates detailed, multi-page financial reports, a process that can take several minutes to complete. The primary business goals are to ensure a reliable user experience without browser timeouts and to allow users to close their browser or perform other tasks while a report generates. Which architectural strategy best satisfies these requirements?
Implement an asynchronous architecture using a message queue and background workers for report generation.

4. A team's GenAI tool uses a RAG pattern to answer questions from internal documents. The tool cannot handle requests like "Summarize our top three security incidents from last quarter and email the summary to the security lead." To enable the system to perform this type of multi-step task, what architectural change should the team implement?

Integrate an agentic framework with tool-use capabilities.

5. A team is developing a new GenAI application that requires complex filtering on structured metadata alongside vector similarity search. The team has deep expertise in SQL and prefers to manage a single, unified database system. What vector database option best fits these requirements?

PostgreSQL with the pg_vector extension

6. You are architecting a serving system for a GenAI application that provides real-time text summarization. Traffic analysis reveals two key patterns: 1) a small number of news articles are requested for summarization thousands of times by different users, and 2) individual users often make several small edits to their text and request a new summary each time. How should you design the caching strategy to most effectively reduce both cost and latency?

Combine a global request-level cache with a session-specific Key-Value (KV) cache.

7. In a standard tool use architecture, what is the application's responsibility immediately after the Large Language Model (LLM) returns a function call request?

Execute the specified function using the arguments provided by the LLM.

8. A monitoring system flags a sudden spike in factually incorrect hallucinations from a new Generative AI (GenAI) chatbot. What is the initial stage in the incident management lifecycle for this GenAI system failure?

Detection and Alerting

9. Within a GenAI agentic framework like GAIA, what is the primary role of a ToolManager class?

Define, manage, and execute external capabilities for the agent.

10. A financial services company deploys a new Generative AI model trained on sensitive, proprietary customer transaction data to classify spending habits. As a security architect, you must evaluate the system's vulnerability to a model inversion attack, where an adversary attempts to reconstruct parts of the training data. What is the most direct and effective strategy to assess this specific vulnerability?

Design a red team exercise that queries the model with specific inputs and analyzes its output confidence scores to attempt to reconstruct sensitive training data points.

11. What kind of diagram do architects use to show the main components and data flows of a GenAI system at a high level?

A system architecture diagram

12. A development team observes that their deployed Large Language Model (LLM) for summarizing financial news is showing degraded performance, particularly with new economic terms. How should the team apply a continuous evaluation strategy to automatically detect and address this issue?

Implement an automated evaluation job that tests the model against an updated set of recent news and summaries.

13. A GenAI-powered code completion tool has an internal Service Level Objective (SLO) for suggestion latency of 99% of requests being faster than 400ms. Its customer-facing Service Level Agreement (SLA) guarantees 99.9% API uptime per month. An issue causes suggestion latency to exceed 400ms for 3% of users, but the API remains fully available. What is the appropriate action based on these metrics?

Declare an internal incident to address the SLO breach, even though the SLA is not violated.

14. A GenAI-powered code generation tool has an error budget for its suggestion acceptance rate Service Level Objective (SLO). With only one week left in the quarter, the monitoring dashboard shows that 90% of the error budget has been consumed due to a series of minor bugs. A new feature update is ready for deployment. How should the team apply the error budget policy in this scenario?

Postpone the new feature deployment and prioritize work on improving service reliability.

15. An engineer is evaluating a new Retrieval-Augmented Generation (RAG) system against a baseline. The new system shows a 15% improvement in recall@10 but a 40% decrease in Mean Reciprocal Rank (MRR). Analysis of the retrieval logs confirms that for most queries, the correct document is present within the top 10 results. What debugging strategy should the engineer prioritize based on this data?

Implement or tune a re-ranking model to improve the position of the most relevant documents in the retrieved set.

16. What is the primary purpose of the function calling feature in a Large Language Model (LLM)?

To allow the model to interact with external systems and APIs

17. A team deploys a new version of a prompt designed to summarize customer feedback, but soon observes a significant decline in the quality of the summaries. To address this issue effectively, what initial action should the team take based on established prompt versioning practices?

Roll back to the last known stable prompt version within the prompt management system.

18. An agent team is executing a multi-step plan. A logic flaw in the orchestrator's progress-tracking model causes it to repeatedly decide that a step is not complete (is_current_step_complete is False) and that no replan is needed (need_to_replan is False). It then re-issues the same instruction to the same agent. This creates a functional loop where the current_step_idx never advances. What feature of the orchestrator's design serves as the ultimate safeguard to terminate this stagnant execution?

The max_turns configuration parameter terminates the entire process after a predefined number of agent interactions.

19. A developer is building a hybrid search system that uses both a sparse method, like BM25, and a dense retrieval method. To merge the outputs, the developer must select a fusion technique that properly combines the ranked lists. What is an effective method for this task?

Use Reciprocal Rank Fusion (RRF) to merge the two ranked lists.

20. A GenAI application queries a third-party Large Language Model (LLM) API for text generation. During peak traffic, the API frequently returns 429 Too Many Requests errors. To handle these transient failures gracefully without overwhelming the API, what resilience strategy should the engineer implement?

Implement retries with exponential backoff.
