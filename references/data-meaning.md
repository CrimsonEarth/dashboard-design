# Data meaning and comparison contract

Read for time series, rates, compact comparisons or statistical summaries. These are original project procedures informed by the [source register](sources.md), especially the Few articles on missing data and scaling.

## Observation preflight

Separate condition from the evidence describing it. For each displayed measure name its observation time, collection time, expected/observed coverage, quality, cutoff and transformation. Invalid/suspect values remain labelled, not silently treated as measured zero or clamped into a plausible range. Distinguish a missing observation, an unfinished reporting period, stale historical evidence and a valid period with zero events.

For time series, retain gaps and isolated observations. Do not fill missing values with zero or connect across gaps without stating an interpolation assumption. Mark a partial final period separately from completed periods; label actual-to-date and forecast as different quantities. Unequal elapsed intervals must survive the horizontal spacing or the stated aggregation. A blanket ban on irregular-interval lines, interpolation or step displays would be stronger than the supported rule.

## Comparison contract

Before drawing, state: question; population/cohort; unit; period and aggregation; baseline; numerator and denominator; scale domain/transform; and what may be compared across views. Choose the contract rather than inheriting a chart library's auto-scaling default.

| Intended comparison | Checkable policy |
| --- | --- |
| Level or magnitude | Common units and compatible scales; magnitude bars originate at zero. If a focused positive range is essential, consider position marks with explicit bounds instead of truncated bar length. |
| Absolute change | Show the difference in original units and comparable time windows. Do not infer proportional change from it. |
| Proportional change | Name the baseline/denominator and show absolute context when it is small. Distinguish percentage points from relative percent change. |
| Shape across compact trends | Name shared versus independently fitted ranges, identical or differing time windows, geometry and permitted comparison. Independent fitting cannot support level comparison. |
| Distribution or entity performance | Expose relevant spread/shape/sample size, sampling/case mix and model assumptions. A low-volume extreme is evidence to investigate, not a causal verdict. |

Few's sparkline scale policies are author proposals explicitly not established by usability testing. A common scale may conceal local variation; independent scales may conceal magnitude differences. Choose for the question and label the limitation. Ordinary logarithms cannot encode zero/negative values. Two independently scaled axes can manufacture crossings; consider aligned panels or a defined index. A deterministic unit-conversion axis is a different case.

For rates, keep observed denominator and expected coverage separate. In an incomplete window, 2 excursions from 2 observed samples with 15 expected does not mean 2/15 is the observed-sample rate. Small-sample percentages are arithmetically valid; qualify precision and inference instead of imposing a universal n=100 suppression rule. Keep an overall rate's population explicit; do not average subgroup percentages blindly.

For distributions, check whether equal summaries hide different shapes; explain bins, whiskers and outlier definitions. Confidence bands/funnel limits require a justified statistical model, not copied decoration. For heatmaps, categorical thresholds may be meaningful operational classes; disclose them and retain numeric access. Continuous color is not a universal requirement. Inspect mark discrimination at final size; do not treat an author's full perceptual ranking as empirical consensus.

## Minimal verification

Ask the reader to compare 2→4 with 200→202: both rise 2 units, but relative changes are 100% and 1%. Remove an intermediate observation and truncate a final period; require the design to keep missing, partial and observed values distinguishable. Check a positive truncated axis, a zero baseline for relative change, and low-volume extremes. Record the chosen policy and any unresolved domain/statistical judgment.
