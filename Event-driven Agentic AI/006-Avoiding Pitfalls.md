
### Avoiding Pitfalls

Real systems can get weird at times when you expect it the least, like 2 a.m., and you cannot build a system that never gets weird, the trick is to expect it to happen and prevent it from causing any damage. 

One of the problems you can expect in an event‑driven system is event storms, which are sudden bursts from retries or cascading failures, without guardrails, they store critical parts. You can mitigate this by using rate limits, prioritize essential consumers, and be willing to shed non‑critical load under stress. 

Hot partitions happen when too much traffic is set to the same partition, the fix is a better a petitioning strategy. You can use a more distributed partition key. You can hash your partition key. Before hashing, you can add some random numbers to it, the process known as sorting. You can also increase partition count. 

Then there are duplicates, which are expected with intermittent failures, retries, and consumer rebalances, they are harmless if your handlers are idempotent. For extra safety, apply the event log to verify that duplicate delivery doesn't cause duplicate effect. 

Poison messages are inputs that always fail because of some error in the system. Don't let them block the line, set bounded retries and route them to a dead‑letter queue with enough context to debug later. You can quarantine these messages until the root cause of the problem is known. 

Closely related is the head‑of‑line blocking. One slow or oversized message freezes a batch, shrink batches set timeouts or split topics by SLA so slow work doesn't hold up fast work. 

Fan‑out bottlenecks appear when many subscribers or slow syncs turn your bus into a traffic jam. To mitigate this, you can stage your topics or event‑first derived events later. You can also use async webhooks rather than waiting on downstream work. 

Finally, cold starts, which is additional latency you experience when the system just launched or a service inside the system restarted. If you're using servers for hot path, consider premium plans, pre‑warmed instances, or a small pool of always‑on workers. 

Designed for the bad day, observe hotspots, quarantine the bad, keep the fast paths fast, and pre‑warm the pieces that must respond immediately.