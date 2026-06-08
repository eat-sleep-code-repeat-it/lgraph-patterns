### Orchestration and Durable Workflows

Agents don't always finish in one shot, payments time out, people approve later, this is why we need orchestration that coordinates the agents. 

Durable orchestrators give you a deterministic state, built‑in retries, timers, and external events. 

There are different types of durable orchestrators, primarily depending on what system you use. 

The main durable orchestrator in Azure is Durable Functions. You write your entire coordination logic as code. Because of this, it's typically the developers that build workflows with them. Because these functions consist of code, they are often embedded in cloud‑hosted apps. 

On AWS, the tool of choice would be Step Functions, which use different philosophy. They are operated as drag and drop, definition‑first systems, as such, they're typically built by platform engineers. They also span across services and can coordinate multiple different services directly. 

Regardless of what tool you choose, all durable orchestrators have common features, they work of deterministic state, they can execute compensation steps on failures, they can support human‑in‑the‑loop pattern if manual sign‑off is required in the process. 

Let's look at Durable Functions in Azure to see how these features are configured. If I open the function up that represents our order‑processing saga, the durable state behind the scenes keeps track of what steps have completed in the current run. Therefore, if there's a problem on the host system that causes the orchestrator function to restart, it will skip the steps that it already completed. For example, if it already processed the Charge and Ship steps, it will not do them again, it will move straight to the next step, Notify. The function handles errors because it stores deterministic state, it keeps track of what steps it failed on so it can select the appropriate compensation action. Because our workflow is a custom code, we can write additional logic to retry before we compensate. 

Here's the takeaway. Durable orchestrators make complex agent flow reliable, in Azure, they are managed by Durable Functions. If you need a managed alternative on AWS, map the same patterns of Step Functions.