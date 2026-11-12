# Workflow, artifacts and re-entry

This contract is shared by exactly three draft skills. Discovery owns the design brief; prototyping owns alternative sketches and the prototype; evaluation owns the evidence-linked assessment. Stages are useful capabilities, not a mandatory waterfall. Choose from current intent and evidence; do not automatically run all three.

## Shared research and portability

The bundle is the deployment unit: keep `skills/<name>/SKILL.md` and `references/` in their declared relative layout. The reference links resolve inside the bundle, use no machine paths/symlinks, and are tested after archive extraction to a different directory. One current copy of each research reference serves all three entrypoints. Do not copy only an entrypoint directory and leave broken references. A future host supporting standalone skills only needs an authorized packaging adapter that materializes dependencies from this one source; do not maintain three divergent research copies. No host installation is included here.

Read branch references only when relevant: data meaning for observation/comparison questions; monitoring-interaction for live attention/exploration; verification for observable rendering/runtime checks; service-semantics only for service status; sources for attribution and evidence qualifications. The source register identifies public influences and reading limits. No full Few/Tufte book reading or proven skill efficacy is implied.

## Minimal durable artifacts

Use project-authorized durable locations for briefs, rationale, reports, prototypes and evaluation evidence. Follow the owner’s existing organization. Never create a competing brain or write externally solely because a stage completes. These fields are a portable information contract, not a forced file format.

**Design brief** (suggested `design-brief.md`): `brief_id`, revision/date, status (`provisional` or `ready_for:<named next step>`), owner/audience; one to three decisions and success observations; viewing/use context; scope and authorization; evidence/data locators with versions/as-of; grain, units, populations, denominators, windows, coverage, quality and freshness; information groups/priorities/comparison contracts; interaction/state needs; existing successful workflows and explicit must-preserve affordances with evidence locators; identified noise versus useful density; user acceptance observations or pending checks; constraints; decisions versus assumptions; consequential open questions and what each blocks. A ready brief may retain nonblocking questions. “Ready for sketching” is not “ready for production.”

**Prototype handoff** (suggested `prototype-manifest.json` plus artifacts): `prototype_id`, revision/date; brief ID/revision (or recovered provisional brief); fixture/data identities and hashes/as-of; artifact paths; fidelity and purpose; supported interactions/states; exact local run/view instructions; known omissions; scope; author-check evidence. Keep sketch alternatives and selection rationale as author materials. A local run command must not silently access external systems.

**Evaluation report** (suggested `evaluation-report.md`): `evaluation_id`, revision/date; exact brief/prototype/data identities; evaluator and independence limits; task questions; checks run with environment/viewport/evidence locations; findings with observation, consequence, severity, repair and recheck; subjective judgments; must-preserve workflow checks and direct user acceptance evidence (or explicitly pending); untested checks and blocked conclusions; disposition for a named purpose; stage/owner for each next action. A report is not a work-status tracker or a production authorization.

## Identity, destination and readiness checks

Resolve the actual durable destination from the applicable project instructions/README or a user-supplied owner. The bundle deliberately has no universal vault path. If that destination cannot be accessed, preserve authorized local work as explicitly noncanonical and report the missing route rather than claiming central persistence.

Reuse existing artifact identities and the project's revision convention. When none exists, choose a collision-checked project-local descriptive ID and record that namespace; use incrementing revisions or an existing content-hash convention consistently. These are artifact references, not tracker IDs or authorizations. For an unversioned supplied screenshot, a stable locator/content hash can identify the evidence without pretending an upstream version exists. Illustrative placeholders in a template are never a completed handoff.

Before marking a handoff ready for a named step, verify required identity/evidence locators resolve, material fields for that step are present, assumptions are labelled, consequential blockers for that step are resolved, and claimed supported behaviors/checks match evidence. This is an explicit review checklist, not a claimed automated readiness validator. Unavailable evidence stays unresolved; a ready sketch brief does not imply production approval.

Use dependency status precisely: **current** means assessed against the named versions; **affected** means a change may alter named conclusions and requires checking; **superseded** means a newer decision/artifact replaces named content for future work. Retain unaffected evidence where justified. Never change these labels merely to make a stage look complete.

## Independent review packet

Provide the brief's tasks, domain rules, user-stated successful workflows/must-preserve constraints and provenance; raw data/fixtures; artifact revision and neutral run instructions. User constraints belong in the review packet even when they express a preferred existing representation; do not strip them out as evaluator bias. Withhold builder rationale, unsupported builder preferences, author self-grades and hidden expected-answer keys from a genuinely independent evaluator. Derive expected facts from raw evidence; use domain-owner rules as inputs, not as guessed answers. Keep optional author reasoning available after the independent pass if needed to explain tradeoffs. Record packet contents and disclosure limits. If the same agent must review its own work, label it self-review; do not pretend context can be erased.

## Entry and re-entry table

| Situation | Start / continue | Artifact behavior and stopping boundary |
| --- | --- | --- |
| New need or changed audience/task/data meaning | Discovery | Inspect available evidence, resolve consequential questions, issue/revise brief. Do not build by default. |
| Settled brief; requested sketches/build | Prototyping | Use current revision; explore only unresolved structure, build at required fidelity, give manifest and author checks. |
| Prototype requested without formal discovery | Prototyping | Recover minimal brief from supplied evidence; proceed with explicit safe assumptions. Route material unknown semantics to discovery; do not invent them. |
| Existing dashboard or sketch supplied for review, no brief | Evaluation | Recover stated tasks, inspect artifact/data; deliver bounded findings and identify missing task evidence. Do not demand a full discovery cycle or apply fixes. |
| Evaluation finds a local interaction/layout defect | Prototyping, if repair authorized | Keep raw evidence unchanged; issue a new prototype revision, then evaluation rechecks affected paths. |
| Evaluation reveals ambiguous denominator/changed policy | Discovery | Resolve/revise semantics; mark impacted prototype/report conclusions superseded, then prototype and evaluate affected parts. |
| Cosmetic-only adjustment within a settled design | Prototyping | Reuse brief/choice; do not manufacture competing sketches. Check affected layout/accessibility. |
| Request for engineering specification or ticket slicing | Existing to-spec, then to-tickets as appropriate | Pass current brief/prototype/evaluation evidence and open decisions. Do not duplicate their architecture/test contract, ticket graph or publication policy. |
| Unrelated backend, mascot, landing-page or definition request | None of these unless a distinct dashboard stage is also requested | Do the requested work with the appropriate capability; no forced dashboard ceremony. |

## Revision discipline and authority

Every artifact names the versions it relies on. Preserve earlier evidence; never overwrite evaluated artifacts to make a previous report appear to pass. A changed brief names affected prototypes/evaluations; a changed prototype triggers only affected checks plus justified regression coverage. Do not silently carry forward a review after the underlying data/semantics changes.

Use to-spec and to-tickets when available and requested. If unavailable, supply the artifact handoff and report that boundary; do not reimplement their procedures inside these skills. These stages do not install tools, initialize trackers, create/publish tickets, deploy, or contact others. Local drafting and review remain distinct from those actions.

## Redesign preservation and acceptance

Before replacing a working dashboard, inspect authorized examples or the user's account of how it is used. Record the successful decision path, explicit must-preserve affordances, evidence source and proposed change. If inspection is unavailable, say so; do not invent a baseline. Preserve the useful task outcome, not legacy UI unconditionally. A failing or inefficient component may be replaced when the evidence and authorized scope support it; explicitly resolve conflicts with user-stated preservation requirements before dependent work. Record what changes, the expected task benefit and how it will be checked. A complaint about repeated metadata alone is not evidence that the representation itself fails. Compare useful information per view separately from redundant labels and visual clutter; preserve compact cards, tables, timelines or other forms when they support the job.

For each consequential change, evaluation checks whether the existing task remains possible and whether an explicit preservation constraint was met. A missing required workflow blocks acceptance for that daily-use purpose even when synthetic data/runtime checks pass. Record those checks as valid within their scope and user acceptance as failed or pending; do not average the failure away. User rejection is evidence about this user/task, not proof of universal design failure or proof of which stage caused it. Route missing requirements to discovery and authorized local repairs to prototyping.

Progressive details may use click/tap and keyboard-accessible disclosure; hover can supplement them. Keep decision-critical facts and meaningful status visible. Do not interpret a request for hover details as permission to make essential information hover-only.
