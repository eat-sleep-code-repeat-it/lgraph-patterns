### Human-in-the-loop and SLAs

While AI can do a lot, some decisions need a human, this especially applies to critical decisions where the consequences of a mistake are severe. 

This is where a human‑in‑the‑loop pattern comes in. 

This pattern allows agents to receive a sign‑off or information from a real person before the workflow can proceed any further. 

Here's an example of how it may work. A refund‑approval process has a time limit of 15 minutes. Once the workflow gets to this stage, it informs an appropriate person and starts a timer. If time runs out, it escalates. More team members can be pinged via PagerDuty, email, or other means of communication. If this doesn't work, the system can apply safe fallback, like issuing a partial refund or pausing fulfillment. Rate caps can be added per tenant so a burst of approvals doesn't overwhelm reviewers. 

This is how it can be implemented in the code. This durable function has two time Windows, a 15‑minute initial approval window and 30‑minute post‑escalation window. The orchestrator proposes a refund, then it asks a human to approve it. It then listens to appropriate event, which indicates that an appropriate team member has responded to the refund proposal. There are two tasks running in parallel, approval_even listener and the timeout task set to the approval time window. The further workflow then depends on which of these completes first. If the approval_event comes first, the orchestrator selects an appropriate step based on whether the refund was approved or rejected. And that's it. However, if the approval_event didn't come before the time window expired, escalation is triggered. The orchestrator then waits for the approval_event once again for the duration of the escalation window. If nothing is received within the escalation window, fallback step is executed. 

Human‑in‑the‑loop allows real humans to cooperate with AI. In human‑in‑the‑loop, you would typically define the SLA, codify it with timers, make escalation a first‑class path, and provide safe fallbacks, your agents stay fast without cutting people out of critical decisions.
