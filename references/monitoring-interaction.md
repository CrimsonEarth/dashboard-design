# Monitoring, attention and exploration

Read for live monitoring or interactive investigation. See the monitoring and accessibility sources in the [register](sources.md). These are design procedures to test, not claims of improved task performance.

## Model separate facts

Keep condition, observation quality, attention need, permitted response and presentation state separate. Distinguish enduring importance from temporary urgency. For every alert candidate, name the affected entity, evidence/cutoff, why it matters, expected response, permitted actor and recovery/acknowledgment behavior. If no useful response is known, label an informative condition rather than inventing an urgent alarm. Calibrate severity/escalation with the domain owner; opportunities can also warrant attention.

Avoid importing historical flashing/sound advice or a fixed number of alert levels. Non-color cues and accessible status delivery matter more than copied alarm styling. A change in past-period exposure is not automatically a current alarm.

## Pause, inspect and resume

Offer pause/freeze when continuous updates would disrupt necessary inspection; it is not mandatory on every static display. State what pauses: presentation, collection, or both. If presentation freezes, keep a visible and accessible frozen/as-of label and explicit resume control. Define how the frozen view warns when it has been left behind, without flashing or silently taking control. The domain owner must set a useful threshold; no universal timeout is prescribed.

While frozen, do not imply that evidence is current merely because collection continues. Keep source freshness and presentation age distinguishable. Define whether response-worthy alerts continue independently and how they reach the active context. Resume deliberately applies pending changes and reassesses freshness while retaining selection, filters, focus, scroll and investigation context where possible. If retention is impossible, explain the change and offer recovery.

## Stable overview and reversible exploration

Monitoring needs a stable overview, but stability does not require alphabetical order or hiding current exceptions. Give a named actionable path while keeping targets stable during background updates. Separate initial organization from update reordering.

Specify the views affected by each interaction. Filtering removes items from a defined scope; linked highlighting marks a subset while preserving its comparison context. State which denominator and summary scope change, keep shared scopes synchronized when intended, and label deliberate scope differences. Return from exploration restores the prior view, selection and focus. Avoid silent filter resets or unexplained summary changes.

## Active-detail updates

Place response-worthy update information in the actual active detail surface when a native modal makes the background inert. Keep the inspected entity and focus intact; do not replace its detail with the new entity automatically. Include an accessible way to inspect the new condition and return. A background live region may exist in the DOM yet be absent from the browser accessibility tree.

Verify a background event with detail open at desktop and narrow sizes: selected entity, search, scope, scroll and focused node persist; new condition is discoverable; unrelated period counts stay unchanged. Inspect the actual browser AX tree with the modal open, then test an accessibility client for announcements and operation. A DOM-derived snapshot alone does not prove exposure.
