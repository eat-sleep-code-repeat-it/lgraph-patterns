### Inter-agent Protocols

When agents collaborate, they need language, lanes, and rules, that's your protocol. 

Firstly, there are topics. Topics define where events go, they allow agents to subscribe to specific types of events. Multiple agents can listen to the same events. 

Further per‑agent filtering can then be done based on event subject, file extension, or any custom event data. 

Different agents have roles, they define which agents do what. They are needed for multi‑agent interactions, this way, different responsibilities are handled by different agents. Each agent has its own focused context to work with. 

The shape of the data agents work with is defined by message schema, this is a pre‑agreed communication format an agent expects. Schemas are important because they prevent hallucinated fields, allow deterministic validation during message ingestion, enable versioning and evolution of agentic system, and support replay and audit. 

Agents can also share a scratch pad, this is what agents remember together, it may consist of intermediate reasoning artifacts, partial plans, decisions already made, and facts discovered so far. 

Then, once a decision is made, delegation contracts allow for it to be handed over to other agents. This contract defines what is delegated, it provides the input schema along with the expected output. It can define constraints such as the time limits for the task. If this time limit is exceeded, the escalation path can be provided. Finally, the contract will have the authority boundaries which define what the agent the task has been handed over to can and cannot do. 

Here's an example of how these concepts are applied. The trigger into the incident triage agentic‑orchestrator function expects the input in a specific format. It fails the validation if it has fields missing, that's the event schema. Then, there are different agents with different roles. Each agent has its role defined by the system prompt. This prompt tells the LLM what the scope of responsibility for this agent is. It will not do anything outside of its scope of responsibility, that's what the other agents will do. Agents then collaborate in a group chat. The group chat has its own scope defined by a prompt template which includes placeholders for the data from a specific incident. This is an example of a shared scratch pad. In this case, once the solution to the incident is found, the instructions on how to solve it are delegated back to the user. 

Things to remember. Agent protocols reduce chaos, topics define lanes, schemas define language, scratch pads share context, and delegation contracts set expectations.