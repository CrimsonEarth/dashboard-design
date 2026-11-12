# Dashboard Design

A free, MIT-licensed agent skill bundle for dashboards that are useful, honest and visually refined, not just grids of attractive cards.

**Public preview.** Three focused entrypoints share one workflow:

| Skill | Use it for | Output |
| --- | --- | --- |
| [dashboard-discovery](skills/dashboard-discovery/SKILL.md) | Audience, decisions, data meaning and information architecture | A bounded dashboard brief |
| [dashboard-prototyping](skills/dashboard-prototyping/SKILL.md) | Sketching, building or refining an authorized dashboard | Reviewable prototype and evidence manifest |
| [dashboard-evaluation](skills/dashboard-evaluation/SKILL.md) | Critiquing an existing dashboard or prototype | Evidence-backed findings, not unsolicited changes |

Start at the stage you need. A critique does not require a discovery ceremony, and a spacing fix does not require competing redesigns. This is a coordinated dashboard-specific skill bundle, not a dashboard generator or a UI component library.

## What it emphasizes

- Decisions before KPI decoration; preserve working calendars, comparisons and actions during redesigns.
- Coherent typography, spacing, alignment, semantic color and responsive composition.
- Missing is not zero; collector failure is not service failure; a fresh page is not fresh data.
- Real keyboard, live-update and narrow-screen behavior, not screenshot-only approval.
- Separate correctness, visual judgment, task fit and user acceptance.

[Visual craft](references/visual-craft.md) gives the refinement pass. [Workflow contract](references/workflow-contract.md) defines handoffs. [Sources](references/sources.md) identifies influences and reading limits, including Stephen Few, Tufte, Impeccable and P-Stack. No third-party packages are required or bundled.

## Use and install

For any agent that can read local files, ask it to read the relevant `skills/<name>/SKILL.md` from this checkout. Preserve the **whole repository layout**: skills link to shared `references/` two levels up. Copying just a skill directory breaks those links.

For a host that discovers skill directories under `.agents/skills` and follows symlinks, clone this repository into a durable location and link the three skill directories into the host's skill directory. Review the files before enabling them. Do not overwrite an existing skill with the same name. Host discovery and symlink behavior vary; explicit file loading is the portable fallback. No installation, network access, hooks, credentials or telemetry run automatically.

Examples:

- “Use dashboard-discovery to define a support-queue dashboard for a shift lead.”
- “Use dashboard-prototyping to refine this layout without losing the day timeline.”
- “Use dashboard-evaluation to critique this dashboard; do not modify it.”

To package this as a particular host's plugin, keep all shared references resolvable and validate the packaged result. This preview does not claim a tested marketplace installer or universal plugin compatibility.

## Validate and contribute

```sh
python3 scripts/check_dashboard_bundle.py .
```

The standard-library checker validates frontmatter, local links, the three entrypoints, byte-preserving archive relocation, and rejection of a missing shared reference. It does **not** establish visual quality or model efficacy. See [evaluation notes](evaluation/README.md) for bounded behavioral probes and limitations.

Contributions should include the task, synthetic or explicitly publishable evidence, observed failure and a reproducible check. Do not contribute customer data, private screenshots, credentials or copyrighted book excerpts. Keep the skills short and put specialized guidance in linked references. Avoid universal chart/card bans and unsupported “proven better” claims.
