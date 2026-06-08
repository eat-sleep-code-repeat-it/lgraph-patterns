
## 3.Frameworks and Tooling for Event-driven Agents
10m 22s

### Messaging and Streaming

There are different tools for transmitting events, choose the wrong one and everything downstream suffers. 

Let's match the tool to the job. Imagine you need to handle durability and speed in a big‑data scenario, such as managing interactions between users of a large social network, refresh of a large RAG database, complex agentic triage, etc. The best tools for these scenarios are Kafka or Azure Event Hubs, they act as a durable event log that stores the entire event history, they excel at highest throughput fan out, which is about processing many events in parallel, replay in case anything goes wrong, and working with multiple independent consumers. 

The next scenario is when speed matters more than durability, this is especially suited for short‑lived live events, such as reacting to a specific IoT telemetry reading that may change in a few milliseconds. Replay doesn't matter, and neither does the event history. The tools that are best suited for the fast service coordination and load jitter agent‑to‑agent charter are NATS or Azure Service Bus, they come with a request/reply pattern or topic subscriptions, they use lightweight subjects. Persistence can be added if needed. 

The next scenario is when you would need a simple task coordination, using big‑data tools such as Kafka may be overkill. Redis streams live where you already have Redis, a popular in‑memory database technology. They're lightweight, good for local queues and micro streams with consumer groups and simple retention. Or if consumer groups don't matter, you can use Azure Queue Storage. Both tools will give you simple work queues. Neither of these tools is a Kafka replacement for massive multi‑team replay, but both are perfect for small‑scoped pipelines. 

Let's look at how some of these tools are used in Azure. First, let's look at the Event Hubs. Here's how you can set partition count. The more petitions you have, the more events you can process in parallel. Next, here's how you can set up Service Bus topic for low latency event trigger. Whenever an event occurs, all services that subscribe to a topic are instantly notified. 

To recap, pick Kafka or Event Hubs for durable fan‑out and replay, NATS for ultra‑low latency control messaging, and Redis Streams for light local pipelines near upstate.
