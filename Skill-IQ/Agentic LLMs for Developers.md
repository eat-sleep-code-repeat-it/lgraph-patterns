
# Agentic LLMs for Developers

1. An agent must understand the complex network of collaborations between different research institutions. How does the structure of a knowledge graph (KG) directly enable this type of reasoning?

It explicitly models institutions as nodes and collaborations as edges, allowing the agent to traverse and analyze relationship paths.

2. An AI coding assistant uses a knowledge graph (a form of semantic memory) to answer factual questions about code libraries. It consistently fails when asked to perform a developer's three-step debugging process of running tests, analyzing the stack trace, and suggesting a fix. To enable the agent to reliably carry out this workflow, which implementation should the developer prioritize?

Implement a state machine or a sequential action model to encode the step-by-step debugging process.

3. An event-driven system uses multiple agents to process images from a message queue. To prevent the system from processing the same image multiple times, especially during high traffic, which architectural solution ensures exactly-once processing while supporting horizontal scaling?

Use a transactional outbox or deduplication store to coordinate the message processing state with message acknowledgment while allowing multiple consumer instances.

4. An AI agent is designed to answer complex user queries. It can use two hybrid retrieval strategies: 1. Graph-First: Traverse a knowledge graph using entities from the query, then use the retrieved entity information to seed a vector search for nuanced context; 2. Vector-First: Perform a broad vector search using the initial query, then use entities found in the top results to refine and filter using a knowledge graph. As the system designer, you must create a rule that determines which strategy to use. In which situation would you justify choosing the graph-first strategy over the vector-first strategy for optimal precision and reliability?

When the query has a specific, unambiguous entity and seeks interconnected facts that require several relational steps, like finding capitals located along the Danube River's banks

5. An AI agent relies on a knowledge graph (KG) for high-accuracy structured queries and a separate vector database for semantic search. A new mandate requires consolidating these functions onto a single, existing technology stack to reduce operational overhead. The strategy must preserve the KG's built-in capability for high-fidelity, structured graph queries. Which strategy satisfies all stated constraints?

Generating vector embeddings from the KG's node and relationship text and integrating a vector search index within the graph database ecosystem to support both query types

6. An engineering team is selecting an open-source platform for a global system. The platform must satisfy three mandatory technical requirements:  1. A unified architecture that natively supports both message queuing and event streaming patterns.  2. Built-in, first-class functionality for geo-replicating data between distinct geographic regions.  3. Avoidance of vendor lock-in through an open-source license.  Which framework meets all these requirements?

Apache Pulsar

7. An engineering team's platform uses RabbitMQ for low-latency, transactional messaging between microservices. A new requirement mandates that a data science team must be able to replay the complete, ordered history of all events over the past three years. The current RabbitMQ setup cannot meet this retention demand. The team must preserve the existing low-latency transactional messaging flow, enable replay of a complete and ordered three-year event history, and use a system explicitly designed for durable, large-scale event log management. How can the team accomplish this?

Integrate Apache Kafka alongside RabbitMQ, with producers also sending events to Kafka for long-term storage and replay while RabbitMQ handles existing transactional messaging.

8. An agent is designed to function as an expert on a specific subject, like corporate law. It needs to access a vast, stable repository of facts, definitions, and legal precedents to answer user queries accurately. Which type of memory is the foundational component for this capability?

Semantic memory

9. When constructing a pipeline for an agentic knowledge graph, you must decide where to execute reasoning logic: within the graph database using graph algorithms or in the application layer using the agent's LLM capabilities. What key trade-off should guide this decision?

The database's suitability for well-defined structural analysis versus the LLM's capacity for semantic understanding

10. An IoT system requires an architectural component to ingest a continuous, high-volume flow of time-ordered sensor events. The requirements state that the events must be stored durably in an append-only log, preserving their original sequence, and must be replayable by multiple, independent consumer applications. Which component is specifically designed to meet all these requirements?

An event stream

11. A development team is architecting a knowledge system with two competing requirements. The highest priority is performing millisecond-speed, deep, multi-hop traversals across a graph of millions of nodes. A secondary requirement is the ability to run ad-hoc analytical queries on large, unstructured JSON payloads stored within each node. Which architectural solution meets the primary requirement for fast traversal while providing a functional, if not perfectly optimized, solution for the secondary analytical requirement?

Implement a native graph database (for example, Neo4j)

12. You are building a personal assistant agent where user privacy and data control are the highest priorities. The user must have absolute certainty that their data does not leave their personal devices. What architectural choice for the agent's memory system best aligns with this strict requirement?

An architecture that stores all memory data in an encrypted database on the user's local device

13. You are evaluating two memory architectures for a new agent. Architecture A uses a local, file-based vector store (such as Facebook AI Similarity Search (FAISS)), whereas Architecture B uses a managed, cloud-hosted vector database. The agent must be highly available and scale dynamically to support a rapidly growing user base. What is the primary trade-off you must analyze?

Balancing the self-hosting operational burden against the network latency and costs of a managed service

14. An ecommerce system's review submission service saves a review to a database and then publishes a ReviewSubmitted message to a message queue. A separate moderation service subscribes to this queue to begin its content review process. Within this event-driven architecture (EDA), which step represents the event?

The ReviewSubmitted message on the message queue, which serves as a notification of a state change.

15. You are auditing a multi-tenant AI agent that experienced several data leakage incidents where one user's private information appeared in another user's conversation. The current architecture already encrypts all data at rest and uses a Personally Identifiable Information (PII)-scrubbing process on user inputs. Despite this, leaks are still occurring specifically during the retrieval-augmentation step. Which remediation strategy would you prioritize to provide the most architecturally sound solution?

Re-architect the data retrieval process to enforce strict partitioning based on user ID, ensuring that the retrieval context is exclusively built from data associated with the current user's session.

16. What is the primary advantage of using an event-driven architecture to coordinate multiple specialized agents?

It enables loose coupling, allowing agents to operate and evolve independently.

17. You are building a medical diagnosis agent. A doctor asks, "what are the common treatments for patients with Type 2 diabetes and a history of heart disease?". Why is a hybrid retrieval strategy superior to using graph traversal only for this query?

Because it combines graph relationships with semantic retrieval over unstructured medical text.

18. An ecommerce platform uses dozens of asynchronous microservices for order processing. When an order fails, engineers must manually search logs across services, which significantly delays incident resolution. A new solution must meet three primary requirements: 
Automatically propagate a shared request context across both synchronous and asynchronous service boundaries. 
Establish clear causal relationships (for example, parent/child operations) between interactions within a single request's lifecycle. 
Minimize ongoing manual coding effort for developers instrumenting their services. 
Which strategy meets all the specified requirements?

Adopt a distributed tracing framework that instruments services to automatically propagate context and capture operation spans across service calls and event messages.

19. A retrieval-augmented generation (RAG) system processes long research papers using a fixed-size, non-overlapping chunking strategy. A user submits the query, "how do the conclusions in paper X relate to its methodology?" An investigation reveals that the 'methodology' and 'conclusion' sections of paper X were split into separate, non-adjacent chunks, and the retrieval step fails to fetch context from both sections simultaneously. Which modification addresses the root cause of this context loss between chunk boundaries?

Replace the fixed-size strategy with one that creates chunks based on document structure and add overlap between adjacent chunks.

20. A development team is monitoring a distributed system where multiple 'Agent' instances process real-time data from a high-volume stream. Users report that insights derived from the agents' processing are frequently outdated. The team instrumented the system and collected the following data points over the last hour:- The rate of messages that the agents processed (throughput) has been stable;- The time taken for the agent to process a single message, from consumption to output (latency), has not significantly increased;- The number of failed processing attempts (error rate) is near zero;- The difference between the latest event's offset in the stream and the offset of the last event the agents processed is steadily increasing. Given this data, which metric provides the most direct and critical insight into the root cause of the outdated insights?

Consumer lag