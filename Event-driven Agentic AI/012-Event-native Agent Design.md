## 4.Designing Real-time Agent Workflows
8m 37s

### Event-native Agent Design

In event‑driven systems, an event makes an AI agent do something. Then, certain steps happen inside the agent. 

I'll show you what these steps are. 

The first step is the trigger. This is what wakes the agent up when an event is sent to it. It can be a HTTP endpoint if the event was sent via webhook, or it can be a different type of a trigger, such as an Event Grid listener. 

Then we have guardrails, these are the rules that decide whether or not the agent should even run. For example, such a guardrail can act as a protection against a malicious prompt. We don't always need guardrails inside agents in event‑driven systems, as we can subscribe to only those events that we need and apply subscription filters. In this case, event router will act as a guardrail. 

Next, we have tool selection. An agent may execute different functions to solve different problems, it may use various technologies to connect to external data sources. These are collectively known as tools in the context of an agent. 

Finally, agent needs to work with memory attachment to keep track of the context. 

Different types of memories serve different purposes. 
Semantic memory fuels reasoning. It consists of vectorized documents that can be searched during the agent execution. In an example of an incident triage agent, this may be runbooks or past incidents. 

Episodic memory captures session‑specific facts, such as recent steps, idempotency keys, and outcomes. To use this memory most optimally, you need the context windows tight, retrieve the minimum semantic snippets, and summarize episodic state rather than always pass the entire conversation history around. 

I will show you some concrete examples of these concepts I just described. We will go back to the AutoGen‑based incident triage function. This function is invoked via a HTTP POST request. This POST endpoint is its trigger. When an incident occurs, a webhook is generated, which then triggers this function, then the guardrails. In this specific example, we are using basic deterministic guardrail. If no title or symptoms of the incident are specified, the function returns early with an error. Then the agent selects the tools. 

In this example, there's only one tool, search_runbooks. This is the name of the Python function which searches the runbooks in a vector store. Tool names in AutoGen match the names of the available functions. The tool searches the runbook in vector store, which is a type of a semantic memory. The episodic memory is then used by internal agents as they discuss the approach to solve the incident in a group chat. 

Here are the takeaways. Triggers wake the agent, guards keep it safe, the right tool does the work, and semantic and episodic memories keep the model sharp without blowing the context window.