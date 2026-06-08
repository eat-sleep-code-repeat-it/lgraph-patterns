### Retries Done Right

Retries can heal or hammer, done right, they speed recovery, done wrong, they trigger a storm. 

Because incorrectly done, retries can cause more problems than they solve, it's important to come up with an appropriate retry strategy. 

You wouldn't just keep retrying at the same short intervals, use exponential backoff to space retries, wait one second before the first retry, two seconds before the next attempt, four seconds before the next, and so on, up to a configurable maximal retry count. 

You can also add jitter to avoid synchronized thundering herds, i.e., prevent many clients from retrying simultaneously. Jitters are randomized wait times between retries. 

Retries should not continue forever. What if it's not a blip and the service is genuinely down, therefore you must cap max attempts so you don't grind hardware. If a message still fails, mark it as poison so it doesn't block the main lane. 

For routers like Event Grid, understand built‑in retry and add dead‑letter destination so nothing disappears silently. The failed message will still be available for further examination. 

Here are different ways of implementing retries. Some infrastructure services already come with a pre‑build retry strategy. 

Event Grid has its own built‑in retry mechanism so you don't have to do anything. You still need to add a dead‑letter destination if you want to examine messages that still failed after an exhausting retry attempt, a storage account is a commonly‑used service for such a purpose. In Service Bus, max delivery attempts can be configured on a per‑subscription basis on a topic. 

Service bus comes with built‑in dead‑letter queue that the messages are sent to when delivery attempts are exceeded. 

Retries can also be added to the application code, this would be relevant in a durable Azure Function. In this example, instead of going to the compensation stage right away when order processing fails, the function retries to execute a failing step five times with exponential backoff, this prevents transient connection problems from canceling the order. 

Space out retries, randomize them, cap them, and quarantine the hopeless, your queues and your neighbors will thank you.
