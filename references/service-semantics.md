# Operational semantics — synthetic case only

These are proposed domain rules, not universal thresholds. Confirm them with the real system owner.

| Fact | Meaning | Must not imply |
| --- | --- | --- |
| Runtime | Process/container running, stopped, restarting or unknown | Running means requests succeed |
| Health | Latest explicit probe result, timestamp, probe identity and reason | A historical pass is current health |
| Telemetry | Collector success/failure, observation time, collection time and coverage | Collector failure means service outage |
| Release | Version, rollout phase, target scope and change time | Deployment succeeded means service is healthy |

For fixtures, evaluation time is 2026-10-01 12:00:00 UTC; observations older than 120 seconds are stale. Last-known health remains visible with age; current health is unknown when stale. This threshold is an assumption for the fixture, not a recommendation.

Loading: name what is loading; no placeholder zero. Empty: distinguish no services in scope from no matching filters; offer scope/filter recovery. Partial: show observed/expected coverage and missing members; do not extrapolate silently. Error: name failed source and retry; preserve dated last-known evidence where available. Stale: show observation time/age and freshness threshold beside affected values; a recent page refresh does not renew old evidence.

Synthetic example at noon, production/eu, request window 11:55–12:00 UTC:

| Service | Runtime | Last health | Observed UTC | Telemetry | Errors / requests |
| --- | --- | --- | --- | --- | ---: |
| API | Running | Pass (historical) | 11:50:00 | Collector failed | Unknown |
| Worker | Running | Fail: dependency timeout | 11:59:40 | Current | 20 / 1,000 (2.0%) |
| Billing | Running | Pass | 11:59:40 | Current | 0 / 1,000 (0.0%) |

Bad original treatment: three green cards labelled “Running,” a fresh page timestamp, and “0 errors” for API. It conflates three facts and invents a measurement.
Better original treatment: an aligned comparison table like this one, a “Telemetry unavailable for API” notice, and visible Worker failure reason. Offer separate drilldowns for probe history and release changes. Investigate Worker and restore API evidence; these data alone do not justify rollback or an all-clear. Add a trend only if timing helps the decision and actual historical samples exist.

A service with no configured healthcheck has “No healthcheck,” not “Unhealthy” or “Healthy.” Distinguish this from an unknown result of a configured probe.

