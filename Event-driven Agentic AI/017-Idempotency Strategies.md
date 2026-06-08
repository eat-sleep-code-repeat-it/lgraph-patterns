### Idempotency Strategies

The problem with retries is that they can cause duplicate messages to be sent to consumers. 

Idempotency strategies ensure that a duplicate event doesn't result in a repeated action, they ensure effectively once delivery. 

Stamp each request with an idempotency key, which can be an unique per request or per event. You can then use this key to store the outcome of the event in the effect log. Then, once an event with a duplicate key arrives, the action will not be performed again because there is already an entry with the same key in the effect log. This is how, for example, you would prevent your customers from being double charged. 

But not all actions require idempotency key and effect log to be idempotent, some actions are semantically idempotent. For example, a duplicate delete action is safe to perform because the item is already deleted. The same applies to a duplicate update if all updated values are the same as what's already stored. 

Semantic idempotency doesn't require any additional storage, however, it's not possible for operations that have side effects, such as payments. 

Another way to ensure idempotency is a state machine, this is where progress only moves forward, and it's impossible to execute an action that has already been executed. This is what durable orchestrators use to skip the steps that have already been executed. 

State machines are great for human‑in‑the‑loop, they also allow you to easily configure the timeouts. 

There's also outbox pattern, this is when an event and its outcomes are published in the same transaction. Because both of these are done in a transaction, either both or none of these are saved in a database together. This pattern often used in distributed systems and microservices where background workers publish events, this way publisher is idempotent. 

I will now show you some examples of these idempotent strategies. Firstly, I'll open an Azure Cosmos DB database. This database acts as an effect log. This table has an idempotency key as its searchable index. Each key has a stored‑event entry associated with it. For example, this entry here indicates that refund has succeeded. Next, I will open a durable function. What makes this function durable is the state store associated with it. By default, a durable Azure Function stores the state of its invocations in an Azure Storage account. The storage account acts as a state machine, it keeps track of the steps that have already been executed. So if a temporary problem occurs and orchestrator needs to rerun, it will skip the steps it already executed. 

Here's a recap. Keys are used to identify events, effect logs deduplicate, deterministic handlers repeat safely. That's effectively once delivery in a world where events can be lost or delivered twice.

