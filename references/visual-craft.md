# Visual craft for decision surfaces

A refined dashboard makes the important comparison and next action easier to find. It is not a landing page with charts added. Respect an existing design system before introducing a new aesthetic.

## Establish a visual thesis

Record the primary decision, viewing conditions, intended density, and one sentence describing the hierarchy: for example, “Exceptions first, a stable aligned comparison below, optional investigation at the side.” Choose a small token vocabulary for surfaces, text tiers, spacing, type sizes, borders and semantic states. Use the project's tokens when present. Explain intentional departures. Do not turn these into a mandatory new design-system project.

## Compose around the job

1. Put scope, time window and freshness where their associated claims can be interpreted. Avoid a tall decorative header that pushes all evidence below the initial viewport.
2. Assign each region a job: orient, compare, detect, investigate or act. Regions with no job should earn their space or disappear.
3. Use alignment, proximity and whitespace before adding containers. Cards are useful for discrete entities and actions; aligned tables for repeated comparisons; timelines for sequence. Do not replace a useful representation just to remove its repeated labels.
4. Make the next likely task visible at the target viewport. Long analytical views may scroll; do not shrink text or hide meaning to enforce one-screen dogma.
5. Resolve navigation, filters, overview and detail as one composition. A pleasing static screenshot with clipped menus or unusable drilldown is unfinished.

## Refine the visual grammar

- Typography: establish readable labels, values and supporting text with a small hierarchy. Align comparable numbers and use tabular numerals when available. Show units and meaningful precision; do not inflate every KPI into a hero headline.
- Spacing: use repeated rhythms within and between groups; relationships should survive without every border. Tighten redundant labels before shrinking targets or text.
- Color: reserve emphasis for selection, meaningful exceptions and the action hierarchy. Define distinct semantics for warning, failure, unknown and stale. Pair color with text or shape; check text and non-text contrast in actual states.
- Surfaces: prefer coherent depth and restrained separators. Shadows, gradients and large corner radii are choices with a purpose, not defaults for “premium.” Avoid nested boxes that obscure comparison.
- Charts: choose encodings for the question. Use clear baselines, comparable scales, direct labels when feasible and units. Decorative sparklines without history and fabricated trends are not polish.
- Controls: unify sizes, labels, states and focus treatment. Ensure loading, empty, filtered-empty, partial, error and disabled states explain what happened and how to recover. Use semantic HTML before custom interactions.
- Motion: use it to explain change without disrupting reading; respect reduced-motion preferences. Live refresh must not move focus, reorder a task under the user or make a frozen view appear current.

## Responsive decisions, not miniature desktops

Specify what reflows, remains comparable, collapses or scrolls. Keep row/column labels programmatically associated with data; visually hidden is different from removed. Do not silently drop critical fields. At narrow widths, prioritize the same decision rather than a different marketing-style summary. Test long labels, localization, zoom and touch/keyboard access.

## Concrete refinement example (synthetic)

Before: four oversized green “Running” cards, identical subtitles, giant greeting, and an unlabeled area chart.
After: compact scope/time controls; a visible collector-failure notice; aligned service rows separating runtime, health and age; a clearly labeled trend only where historical samples exist; accessible details with preserved focus.

The improvement is not “tables beat cards.” It is that the reader can distinguish an actual failure from missing evidence and compare services without repeated ornament. If their task instead requires distinct entity actions, compact cards can be the better choice.

## Review in the browser

Capture initial viewport and full-page views at representative wide and narrow sizes. Inspect hierarchy before micro-details, then alignment/type/spacing/color, then actual keyboard and state transitions. Recheck after repair. Keep factual defects, task friction and subjective visual judgments separate. A visual-craft verdict names the artifact, viewport and tested states; it never implies untested accessibility, correctness or user acceptance.
