## Foundations of Event-driven Agentic Systems

### From Prompts to Event-driven Agents

We will begin by learning the basic terminology of an event‑driven architecture. 

Generative AI tools wait for promises before they do anything, production systems don't, they speak in events, such as purchases, failures, approvals, and sensor spikes. 

The most fundamental concepts are events, commands, facts, streams, and sagas. 

An event is a record of something that already happened, such as payment declined. It's immutable, which means it cannot be changed once it happened. We cannot go back in time. 

A command is an instruction to make something happen, such as refund order. Events tell the story, commands write the story. 

A fact is an event you are willing to keep forever as part of the system's truth, an example of this could be something like order 123 shipped at 10:42 UTC. Facts power auditability, training data, and agent memory. 

A stream is an ordered, append‑only continuous sequence of events. Just like a physical water stream, it keeps flowing indefinitely only that instead of water, what flows in such a stream is data. Agents subscribe to streams, which may include payments, tickets, or IoT device readings. Agents then react as new entries arrive. Streams enable low‑latency processing, they can also be replayed for debugging or retraining. 

A saga coordinates multi‑step workflows across services. If a step fails, a saga issues compensating actions. For example, a shipment is canceled if the charge is reversed. In agentic systems, sagas enable robust long‑running workflows. 

Here's an example of agentic event flow that fits all these concepts together. A payment‑declined event triggers the agent to summarize context, then issues a command to refund. Each step emits new events, which become facts on the stream. A saga coordinates the whole flow and compensates if anything fails. 

A properly implemented event‑driven architecture ensures that events are processed in real time, almost instantly. There are important reasons for this. 

Firstly, there's a latency budget, which is the maximum acceptable delay users are willing to tolerate. Users abandon flows if your agents wait seconds for context, this is why events need to push context to agents immediately. 

Secondly, customers assume that confirmations, alerts, and escalations happen instantly. Events that run in the background of the system enable all of this. 

Thirdly, because individual agents are autonomous, they need a live picture of the world. Event streams plus facts give agents a timely, reliable state. 

With these definitions and the why, you're ready to design agents that react fast, stay consistent, and are easy to audit. Next, you'll map this concept onto real messaging patterns.