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

