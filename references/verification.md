# Verification by observable task

Use for initial-view, responsive, accessible and implementation checks. The [source register](sources.md) identifies design influences; WCAG is the relevant accessibility standard. Keep source type and untested behavior explicit.

## Initial view and component feasibility

Render the intended desktop and narrow viewports with real-length labels and representative density. Name the first actionable condition and its evidence in each initial viewport. If the initial screen contains only aggregate counts, branding and normal rows, provide a short named action path (for example, a meaningful overview entry or reachable filter/jump), or document why another task takes priority. Do not impose a universal pixel height, no-scroll rule or exception-first sort. Test whether the intended reader can locate the condition without unnecessary traversal.

Keep exact values aligned for comparison; place related facts together. Test follow-one-entity, compare-one-measure and overview-to-detail paths. Check the selected component library supports required labels, scales, placement, interactions and semantics before committing to it. Fixed grids and equal panels are tools, not evidence of a useful hierarchy. Dense content must remain legible and operable at final size.

## Responsive data relationships

When transforming a table into cards or another narrow layout, preserve entity/measure/value/unit relationships programmatically. Do not simply hide the only column headers with display:none and assume the visual grouping preserves accessibility. Use appropriate table headers or equivalent accessible labels/grouping without duplicated or misleading readings. Check actual browser semantics at every changed breakpoint, followed by accessibility-client navigation. A native table is one solution, not a blanket layout requirement.

## Evidence tiers

- Static/source checks can establish syntax, expected mappings and the presence of labels; they do not demonstrate actual keyboard behavior.
- Rendered viewport images show clipping, grouping, legibility and first-view content. Full-page captures are useful for the whole layout but can distort modal framing; use viewport captures too.
- Browser interaction checks should exercise keyboard open/return, filtering/highlighting, background update, paused/resumed state and focus/scroll retention where applicable. Test active detail and other focus targets, not only one happy path.
- Actual browser accessibility-tree inspection can detect inert/missing content. DOM-derived accessibility snapshots are not equivalent to the platform tree. Neither proves real screen-reader speech, timing or usability.
- Screen-reader, keyboard, contrast and zoom checks establish only tested criteria; do not claim full WCAG conformance from a subset. Reader studies or observed tasks are needed for claims about effectiveness, speed or adoption.

For each finding record location/state, observed behavior, decision consequence, severity, repair and smallest regression check. Label design taste separately. Keep old failed artifacts immutable; a new instruction cannot retroactively pass an old experiment. Where execution is unavailable, deliver the test contract with “not run” instead of invented success.
