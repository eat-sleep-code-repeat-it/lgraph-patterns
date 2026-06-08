## 5.Making Event-driven Agents Robust
8m 56s

### Failure Taxonomy

Not all failures are equal. Treat every error the same, and you'll either page too often or miss the real fire. 

Transit errors are temporary hiccups, such as network blips, brief throttling, or slowness due to cold caches, they usually recover with a simple retry and back off. 

Systemic errors are widespread, a regional issue, partition hotspots, and dependency outage. They need load shedding, circuit breakers, and escalation, in this case, blind retries won't work. 

Logic errors are bugs or bad assumptions, schema mismatches, null references, or malformed payloads. They won't fix themselves, you can route them to dead letter and quarantine with enough context to debug. Then once you identify the problem, you can solve it by releasing a patch or a standard software update. 

Here's how errors can be monitored in Azure. The same principles apply in other cloud systems too, only the tools are different. The main tool in Azure to monitor errors is application insights. It doesn't only monitor errors, it collects different types of application telemetry. The main type of telemetry are logs, traces, and metrics. I am re‑executing the previously executed union * query, which returns all log data. Logs provide human‑readable description of individual events. They come with different severity levels, such as information, warnings, error, and critical failure. In the raw log data, these are often represented by numbers. For example, in the default log view, number three represents an error, while number one represents an information‑level operation. 

Information‑level log entries describe normal operational events. Several log entries can be linked together by a corresponding ID to form a trace, so all events associated with an operation can be followed sequentially. In Azure Application Insights, full event traces can be examined via the Search blade of the Investigate panel. 

Metrics are simple measures such as counters, durations, and so on. They measure many different things, including the total count of the users in the system, request latency, number of specific errors, etc. In Azure, metrics can be viewed on an ad‑hoc basis or by constructing the spoke dashboards. The dashboards for any custom matrix can be constructed via the dashboards with Grafana blade. Azure also comes with a feature that allows to configure notifications when specific metrics exceed a specific threshold, this is how you can set your team members or AI agents to be notified if anything in the system goes wrong. 

To recap, retry transient errors, mitigate systemic errors, quarantine logic errors. Classification first, reaction second.
