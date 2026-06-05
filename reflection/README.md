## Demo: Extending the App with Memory and Context

### Key Concepts

#### Context

**Context** is the information available to the agent at any given moment. It typically includes:

- Current user input
- Recent conversation history
- Retrieved documents (e.g., via RAG)
- System instructions
- Environmental signals (tool outputs, API responses, etc.)

#### Memory

**Memory** is what the agent retains over time to improve future responses and personalization — the agent's long-term knowledge built from previous interactions or stored information.

Memory comes in two categories:

| Type | Scope | How It Works in LangGraph |
|------|-------|--------------------------|
| **Short-term** | Single session | Managed as part of agent state, persisted via the checkpointer |
| **Long-term** | Across sessions | Stored and retrieved using the memory store |

In most real-world applications, both types are combined to build rich context for the LLM.

---

### The Memory Store

The **memory store** allows persisting and retrieving information across different sessions. This demo uses an in-memory store.

**Basic usage:**

1. **Define a namespace** — a tuple of any length representing an identifier (e.g., `user_id`)
2. **Save memories** — use `store.put(namespace, key, value)` to store data
3. **Retrieve memories** — use `store.search(namespace, query)` to query stored data

**Enhancing with semantic search:**

Attach an embedding model when creating the store. This enables the store to index memories and perform **semantic search** — recalling the most relevant memories based on a query.

---

### Code Walkthrough

#### Graph Compilation

Both long-term and short-term memory contribute to the overall context. Additionally, **runtime context** can be passed to the agent via a context schema.

- **Context schema** — defines runtime inputs (e.g., a `username` field used to create a user-specific memory namespace)
- **Graph compilation** — requires both a `checkpointer` and a `store`
- **Graph invocation** — pass the runtime context alongside the input

#### `main` Function

- Creates an `InMemoryStore` with an attached embedding model (from LangChain) to enable semantic search
- Defines a namespace using a hardcoded `user_id` and a label (e.g., `"memories"`)
- Stores JSON objects into that namespace via `store.put`

#### Inside the Node

The node receives both **runtime context** and the **store** as inputs:

1. Extracts `username` from the runtime context
2. Calls `store.search(namespace, query)` to retrieve relevant memories
3. Includes retrieved memories in the message history
4. Passes the enriched message history to the LLM

This is how the model becomes aware of past interactions and user-specific data.

---

### Running the Code

```bash
python graph_simple.py
```
