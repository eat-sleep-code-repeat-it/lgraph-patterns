### Agent Stacks and Integrations

LLM agents are only as smart as the tools and memory you wire in. There are different tools that allow your agents to interact with LLMs, and they are used for different purposes. 

Event‑driven agents respond to incoming events and use LLMs to interpret those events and decide on actions in real time. 

Memory‑augmented agents extend our LLMs with short and long‑term memory so past interactions and knowledge can inform current reasoning. 

Integrating these approaches enable agents that are both reactive to new events and capable of context aware, informed decision making over time. 

Semantic Kernel is a Microsoft tool that allows you to get any arbitrary codes to interact directly with an LLM. It's perfect for .NET shops and Azure integration, although it is also available in other languages such as Python. 

LangChain and LangGraph are used for orchestrating an agentic flow, they're similar to durable orchestration tools and can be integrated with them. However, they are Python first and are used specifically for building multi‑step agentic AI workflow processes, not just any arbitrary workflows. 

AutoGen is a great for multi‑agent conversations and role orchestration. 

Let's look at how these tools work. 

First, this is how Semantic Kernel is used inside a .NET application. In this example, I am building a custom chatbot. Here's how Semantic Kernel instance is configured to connect to a locally‑hosted Ollama container with a small language model, but it can be connected to an online‑hosted Frontier LLM, too. The endpoint hosted on a server receives a chat message from user's web browser. It then adds this message to the chat history and keeps track of the context. At the end, it streams the response back to the user. 

Let's now move on to LangChain. In this example, LangChain is used to orchestrate agentic flow in a response to an incident. The agent is triggered by a webhook when an incident occurs. It has some system prompts that tell the agents what to do. There is also another prompt template that is populated by the Incident information, it performs all the steps by invoking appropriate functions such as search runbooks. The agent searches appropriate runbooks in a RAG store to figure out how to deal with the incident, it then summarizes the incident to the user and drafts the instruction. While we can add steps to the process, this process still works as a single agent going through a sequence of tasks. 

AutoGen, on the other hand, coordinates multiple agents together, so they try to collaboratively come up with a solution. Different agents have different roles, such as TriageLead, RunbookResearcher, FixPlanner, and RiskReviewer. Each uses its own connection to an LLM, each has a role within a team defined by its system prompt. AutoGen then coordinates these agents so they collaborate with one another without any hard‑coded logic. They work together in a group chat. Once they reach the consensus, it's written into the results. 

No matter the framework, the loop is consistent, Event, Retrieve, Reason, Act, Event. 

Semantic Kernel, LangGraph, and AutoGen differ in ergonomics, but not the fundamentals.