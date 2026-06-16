
# Agentic LLMs for Developers 06/15/2026

1. A developer's autonomous agent's performance is degrading over time. Analysis reveals that the agent's conversational memory is growing linearly with each interaction, causing memory lookups to become progressively slower. Which technique should the developer implement to create a more efficient, condensed representation of past interactions and improve lookup performance?

Summarization

2. An agent frequently misunderstands or forgets parts of a user's multi-part request within a single, ongoing conversation. For example, when asked to "find a hotel in Paris, book a flight for two, and add a rental car," it only books the flight. This indicates a failure in which type of memory?

Working memory

3. A developer designs an agent to provide personalized product recommendations. How does a knowledge graph enhance the agent's ability to explain its recommendations?

The agent can trace the path of relationships and present this path as a logical explanation.

4. Your agent's memory retrieval is suffering from 'context drift,' where it retrieves documents that are only tangentially related to the user's query, leading to off-topic responses. How would you systematically evaluate and tune the pipeline to make retrieval more precise?

Analyze the vector distance scores of retrieved documents and adjust the vector_distance_threshold to be more restrictive.

5. A financial agent must analyze the chain of command and ownership structures to detect potential conflicts of interest. Why is a knowledge graph (KG) strategically superior to a vector database for this task?

A KG excels at multi-hop traversal and path analysis, which is essential for explicitly mapping and analyzing hierarchical relationships.

6. An agentic system manages a distributed service. A network glitch causes the cart agent to deliver and process an AddItemToCart event twice. To prevent the item from being added to the cart two times, what property must the agent's event handler possess?

Idempotency

7. A team is building an enterprise agent to interact with multiple internal data sources, including SQL databases, Confluence pages, and shared drives. The goal is to create a unified memory that the agent can query. What strategic advantage does a data framework such as LlamaIndex provide over using a standalone vector database such as Pinecone or Weaviate for this use case?

It offers high-level APIs and data loaders for ingesting and indexing from diverse data sources.

8. In the publish-subscribe (pub/sub) pattern, what is the relationship between event publishers and subscribers?

Publishers and subscribers are decoupled and do not know about each other's existence.

9. An agent must plan a trip, considering flights, hotels, and activities. How does a knowledge graph's schema (ontology) help the agent perform this task effectively?

It defines the valid types of relationships between entities, guiding the agent's planning process.

10. An agentic system uses a highly normalized database for handling CreateOrder and UpdateOrderStatus operations, but uses a separate, denormalized data store for efficiently fetching order histories. What pattern does this design implement?

Command Query Responsibility Segregation (CQRS)

11. A hybrid retrieval system is designed with a two-stage process:  1. A vector search identifies initial starting nodes in a knowledge graph; 2. A graph traversal algorithm expands from these nodes.  An evaluation establishes two facts about the system's performance on multi-hop questions: first, the knowledge graph is confirmed to contain the correct information; second, the traversal algorithm succeeds if, and only if, it begins from the correct starting nodes. Despite this, the system consistently fails to produce the correct answer for these questions.  Based on this evidence, what is the specific point of failure in the system's architecture?

The initial vector search acts as a single point of failure; if it does not retrieve the correct starting nodes, the subsequent traversal stage cannot recover from the error.

12. A healthcare AI system requires real-time diagnostic capabilities, leading to high read/write volume on its patient data store. The system must also comply with audit trail requirements of the Health Insurance Portability and Accountability Act (HIPAA), which mandate tracking all access to Protected Health Information (PHI). Given the competing needs for high performance and comprehensive auditing, which strategy provides the best balance for this specific use case?

Implement an asynchronous, non-repudiable logging service that batches access records, separating the audit path from the performance-critical data path.

13. Your vector search pipeline is struggling with polysemy (words with multiple meanings). When a user queries for, "how to operate a heavy-duty construction crane," the top results are about the migration patterns of the bird. You need an immediate strategy to improve relevance without the time and expense of retraining the embedding model. Which approach is most effective?

Implementing query expansion to add clarifying terms such as "machine" or "construction" to the original query

14. You are using an agent to build a knowledge graph from both a structured SQL database and unstructured text from emails. How would the agent's approach to information extraction differ between these two sources?

The agent would use predefined mapping rules for the SQL database and an LLM-based extraction model for the emails.

15. In an agentic system that monitors social media, an agent detects a new post mentioning a company's product. The agent then broadcasts this information for other agents to act upon. What role does this agent fulfill in this interaction?

Event producer

16. You are designing a system for a multi-player game where an agent's current status (for example, inventory, health, location) must be auditable and reproducible. To achieve this, your team stores every action a player takes as an immutable event in a log. When the agent's state is needed, the system reads the entire sequence of events for that player and computes the final state. Which architectural pattern are you and your team implementing to manage the agent's state?

Event sourcing

17. An engineering team is designing an agentic system that requires both complex Advanced Message Queuing Protocol (AMQP)-style routing and high-throughput event streaming with long-term data retention.The team prioritizes the routing requirement and selects RabbitMQ for that task. What is the primary architectural trade-off it will face?

RabbitMQ's broker-centric design is not inherently optimized for the high-throughput and durable retention necessary for event streaming.

18. You are designing a long-running order fulfillment process for an ecommerce platform using four independent microservices: Inventory, Payment, Shipping, and Notifications. The design must maintain service autonomy and ensure data consistency across services. A key requirement is that a failure in any step must trigger a series of compensating transactions to programmatically reverse all preceding successful operations. Which architectural pattern does this mechanism of managing a distributed transaction through a sequence of local transactions and their corresponding compensating transactions define?

The saga pattern

19. In the following VertexAiRagMemoryService code, a file is uploaded to the Retrieval-Augmented Generation (RAG) corpus, and the display_name parameter is set to a string such as f"{session.app_name}.{session.user_id}.{session.id}": 

It serves as a workaround to store structured metadata that can filter search results later.

20. A company must comply with the 'right to be forgotten' under the General Data Protection Regulation (GDPR), which allows users to request the deletion of their personal data from an agent's memory. The memory is a large, indexed vector store. What is the primary technical challenge you must analyze and solve to implement this functionality effectively?

Efficiently locating and removing specific data vectors from the index without requiring a complete and costly rebuild






