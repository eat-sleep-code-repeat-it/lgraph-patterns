## Demo: Implementing Reflection Pattern Using LangGraph

### Graph Overview

The graph has three nodes: `writer_node`, `reviewer_node`, and `publisher_node`.

- **Starting node:** `writer_node` → passes output to `reviewer_node`
- **Conditional edge:** routes back to `writer_node` for revisions, or forward to `publisher_node` to finalize
- **Shared state** includes:
  - `revision_count`
  - `original_customer_message`
  - Writer's response
  - Reviewer's decision
  - Feedback for the writer

All nodes are defined in `nodes.py` to keep the code clean and manageable.

---

### `writer_node` — Drafting the Reply

The writer is the agent that drafts (or revises) the response. Step by step:

1. Reads the current state and determines whether this is a **first draft** or a **revision**
   - If `revision_count > 0` and reviewer's decision is `REVISE`, the reviewer's feedback is attached to the context
2. Constructs the full LLM prompt using:
   - System instructions from `writer_instructions.md`
   - The original customer message
   - Reviewer feedback (if revision)
3. Builds conversation history from state messages
4. Calls the LLM via `ChatOpenAI` using the default model and temperature from `config.py`
5. Updates workflow state:
   - Increments `revision_count`
   - Stores the latest reply
   - Stores pending messages

> **In short:** `writer_node` reads the customer message, optionally incorporates reviewer feedback, writes/rewrites the reply, and saves it back to shared state.

> **Note on config:** Environment variables and constants are centralized in `config.py`, which loads from the `.env` file. An example `.env` file is included.

---

### `reviewer_node` — Quality Control

Think of `reviewer_node` as the quality control agent. Step by step:

1. **Checks revision count** — if `max_revisions` (from `config.py`) is reached, the reviewer auto-approves
2. Pulls from state:
   - Writer's latest reply
   - Original customer message
3. Builds the reviewer prompt using:
   - System instructions from `reviewer_instructions.md`
   - Previous message history
   - Original customer message
   - Proposed response from the writer
4. Calls the LLM to produce **written feedback** (not just approve/reject)
5. Uses the written feedback to request a **structured response** from the LLM:
   - Schema has one property: `decision`
   - Returns either `APPROVE` or `REVISE`
6. Decides whether another revision loop is needed
7. Updates state with the decision and feedback

> **In short:** `reviewer_node` reads the writer's answer, critiques it, and either sends feedback back to the writer or forwards the response to `publisher_node`.

---

### `publisher_node`

The `publisher_node` is minimal — it receives the approved response and ends the graph.

---

### System Prompts

Prompts are stored in the `prompts/` folder:

- **`writer_instructions.md`** — defines the writer's role with a detailed prompt and examples
- **`reviewer_instructions.md`** — defines the reviewer's role with evaluation criteria and examples

---

### Running the Code

Before running, install the required libraries:

```bash
pip install -r requirements.txt
```

A Python virtual environment is recommended. The code is available in the linked GitHub repository.

---

## Demo: Running the Graph and Enabling LangSmith Tracing

### The `main` Function

- Uses a sample customer comment (positive laptop feedback) as input
- Uses `InMemorySaver` for checkpoint storage (required for later demos)

### `process_customer_message` Function

This is where the reflection workflow runs:

1. Calls `create_reflection_graph()` to build the graph
2. Initializes state with the sample customer message
3. Invokes the graph with a `thread_id` in the config (required when using a checkpointer)

---

### Enabling LangSmith Tracing

Observability is critical for LLM applications. LangSmith provides end-to-end visibility into how requests are processed.

To enable tracing, set these environment variables:

```bash
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=<your-api-key>   # get this by creating an account at smith.langchain.com
```

> **Important:** When invoking a graph with a checkpointer, you must provide a `thread_id` in the `config` dictionary.

---

### Execution Trace

After running the graph and opening the latest trace in LangSmith:

| Step | Node | Action |
|------|------|--------|
| 1 | `writer_node` | Received customer message → generated first draft |
| 2 | `reviewer_node` | Evaluated draft → provided detailed feedback → decision: **APPROVED** |
| 3 | `publisher_node` | No revision needed → workflow complete |

In this run, the writer's first draft was approved on the first attempt — no revision loop was triggered.


## Demo: Extending the App with Human-in-the-Loop

### How Interrupts Work

In LangGraph, **interrupts** are used to implement human-in-the-loop workflows. They allow you to pause graph execution at a specific point and wait for external input before continuing.

When `interrupt()` is called:

1. Graph execution is **immediately suspended** at that exact line
2. LangGraph **saves the current state** using its persistence layer
3. The graph **waits indefinitely** until execution is explicitly resumed

To **resume**, invoke the graph again and pass a `Command` containing a `resume` value. That value becomes the return value of the original `interrupt()` call — execution continues exactly where it left off, with the human input available.

---

### Updated Graph Structure

The workflow now includes three additional nodes:

- `human_review_node`
- `publisher_node`
- `rejection_node`

---

### `human_review_node` — Routing Based on Human Input

This node dynamically routes execution based on the human reviewer's action.

**Step by step:**

1. Calls `interrupt()` with a message describing the expected input structure:
   - A JSON object with an `action` property
   - Possible values: `approve`, `reject`, or `edit`
   - Also includes the `writer_node` response so the reviewer can evaluate it
2. Extracts the human response and updates state:

| Action | Behavior |
|--------|----------|
| `approve` | No changes — routes to `publisher_node` |
| `reject` | Routes to `rejection_node` |
| `edit` | Updates state with human-modified content → routes to `publisher_node` |

---

### Running the Code with LangGraph Dev Server

This demo uses the **LangGraph dev server** for local testing.

```bash
langgraph dev
```

- Starts the agent server in **in-memory mode** — ideal for development and testing
- Requires the LangGraph CLI (see the official docs for installation)

---

### Testing in LangGraph Studio UI

The Studio UI provides a visual view of all nodes and their connections.

**Scenario 1 — Approve:**

1. Paste a sample input message (this becomes the initial workflow state)
2. Click **Submit**
3. The workflow runs, generates output, and **pauses at `human_review_node`**
4. The AI response is displayed with a prompt for human input
5. Select **Approve** → workflow completes normally

**Scenario 2 — Edit:**

1. Submit the same input message again
2. Select **Edit** and provide a modified response
3. The workflow continues using the **human-edited version** instead of the original AI output


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

## Demo: Extending the App with Streaming

### Streaming Capabilities in LangGraph

LangGraph supports streaming at multiple levels:

| What You Can Stream | Description |
|---------------------|-------------|
| **Graph state updates** | Changes after each node step (`updates` mode) |
| **Full graph state** | Complete state snapshot after each step (`values` mode) |
| **Subgraph states** | State from nested subgraphs as they execute |
| **LLM tokens** | Individual tokens from the LLM as they are generated |
| **Custom events** | User-defined events emitted from inside nodes or tools |

Multiple stream modes can be **combined** in a single call.

---

### Code Walkthrough

#### Enabling Multiple Stream Modes

When calling `stream()`, set `stream_mode` to combine modes:

```python
graph.stream(input, config, stream_mode=["updates", "custom"])
```

- `updates` — emits only the state changes after each node step
- `custom` — emits user-defined events sent from inside nodes

---

#### Emitting Custom Events from `writer_node`

In `nodes.py`, the `writer_node` uses `get_stream_writer` to access a `StreamWriter` and emit custom data during execution:

```python
from langgraph.types import StreamWriter, get_stream_writer

def writer_node(state, ...):
    writer = get_stream_writer()
    writer({"status": "Writer is generating a response..."})
    # ... rest of node logic
```

This lets users see real-time progress while the node is running, before it completes.

---

### Running the Code

```bash
python graph_simple.py
```

The graph emits custom events directly from `writer_node` as it executes.
## Demo: Using the Responses API and Implementing Background Runs

### When to Use Background Mode

Not every graph execution needs to happen in real time. Agents like **Codex** or **Deep Research** can take several minutes to solve complex problems — especially when using reasoning models. Background mode is designed for exactly these long-running scenarios.

---

### Enabling Background Mode

Two small changes are required:

1. **Initialize the LLM** with `use_responses_api=True`:

    ```python
    llm = ChatOpenAI(..., use_responses_api=True)
    ```

2. **Invoke the graph** with `background=True`:

    ```python
    result = graph.invoke(input, config, background=True)
    ```

---

### Retrieving the Result

Once the graph is running in the background, use the **OpenAI client directly** to poll for the response until it completes:

```python
from openai import OpenAI

client = OpenAI()

while True:
    response = client.responses.retrieve(response_id)
    if response.status == "completed":
        print(response.output)
        break
    print(f"Status: {response.status}...")  # intermediate update
```

During the polling loop, intermediate status updates are shown to the user. Once the response is ready, the final output is printed.

> **Note:** You don't always have to rely on LangChain integrations. LangGraph is a low-level orchestration framework — you are free to use external libraries like the OpenAI client directly inside your nodes or tools to unlock additional capabilities.

---

### Running the Code

```bash
python graph_simple.py
```

Output includes:
- Intermediate status updates during polling
- The final response once background execution completes


