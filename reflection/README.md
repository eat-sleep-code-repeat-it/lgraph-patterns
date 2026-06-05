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

