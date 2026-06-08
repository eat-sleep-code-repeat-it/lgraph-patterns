### Cloud Triggers and Event Routers

Before your agents can think, it has to hear. 

Event routers connect the outside world to your workflows. 
Event routers handle subscriptions, filters, delivery, and retries. 

What event router tool you use depends on what cloud platform you are hosting your ecosystem on. 

On Azure, you would use Event Grid. It's serverless routing with subject filters, dead lettering, and interactions across Azure services and webhooks. 

On AWS, the tool will be EventBridge. It comes with rich rule patterns, event buses per domain, Software‑as‑a‑Service integrations, and schema registry. 

On Google Cloud Platform, GCP, it will be Eventarc. It routes cloud events across GCP services to Cloud Run functions. 

Let's examine such an event router. I will open Event Grid topic called retail‑events, which is where events representing payments and refunds are routed to. And the Event Subscriptions, I have two subscriptions. Payments‑sub retrieves an event and sends it to an HTTP endpoint for further processing. It's only interested in payment events, so it has a filter where subject begins with payments. Audit‑sub sends events to Storage Queue for durable auditing. You can also track failed events by configuring dead‑letter destination. In this example, it's set to a storage account container. Use a router when you need to push from many producers into one or more agent entry points without running your own consumers.