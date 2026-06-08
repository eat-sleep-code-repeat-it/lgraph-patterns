## Architectural Patterns for Event-driven Agents
10m 48s

### Event Buses and Pub/Sub Topologies

Most agentic systems fail or fly based on one decision, how you design your infrastructure. Do you centralize everything through one backbone or do you decentralize it by domain? 

A central bus gives you a strong governance, a single place to observe, and consistent security. But it also concentrates risks, one outage can ripple everywhere. 

A federated, decentralized approach breaks the problem into smaller, safer, failure domains. Each domain owns its bus, its performance targets, and its evolution, thus local autonomy with a thinner blast radius. 

Kafka is a popular tool for building event‑driven systems. When Kafka logs events, those logs are durable, which means that events are available for replay and for further examination. Kafka also supports consumer groups, which allows different events to be sent to different parts of business. Each team or department can be connected to its own consumer group. 

If your main priority is making sure that events get delivered and reacted to fast and you don't care about consumer groups, then Neural Atomic Transport System, or NATS, may be a better suitable tool than Kafka. Think of NATS as a high‑performance walkie talkie, one service transmits the event and another service reacts to it immediately. By default, NATS does not persist events, it's a fire‑and‑forget request and reply pattern. 

However, persistence can be added with a tool called JetStream if you want to examine the events after they occurred. In Azure, the common trio is Event Hubs for Kafka‑style streams, Service Bus for enterprise messaging pattern, and Event Grid for serverless push and Software‑as‑a‑Service webhook routing. Topic design is your street map. Names and routing keys should communicate intent and help distribute load. With this in place, none of your topics act as a junk drawer where everything lands. Partition based on unique keys can spread traffic evenly and place related events on the same partition when ordering matters. You can pair that with schema governance, which is a registry, compatibility rules and version and discipline, so you can evolve without breaking consumers silently. 

Let's see how these concepts apply in the real world. In Azure portal, I'm opening Event Hubs. You'll see a namespace with two hubs, orders and payments. Under Consumer groups, I've created agent‑triage‑cg consumer group for an issue triage agent and fraud‑scorer‑cg for a fraud detection agent, this allows different teams to scale independently. Pick the topology to match your organization shape, use the right bus for the job, and let topics plus schema carry meaning and safety as your system evolves.