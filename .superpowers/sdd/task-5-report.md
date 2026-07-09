Task 5 report: Remove Old Runtime API And Align Docs Across Projects

Summary
- Verified that `workflow-container-runtime` no longer exposes the old public lifecycle API: `VerifiedCodexStageRunner`, `VerifiedCodexStageConfig`, `stage_prompt_context_path_get`, and `STAGE_PROMPT_CONTEXT_FILENAME` are absent from current runtime production/test exports and call sites.
- Aligned runtime and brand design docs with the current stage file contract: `input.json` public input, `result.json` public result and DBOS handoff payload, `verification.json` verifier verdict, and `state.json` private same-stage durable state.
- Updated `brand-size-chart` design text to use `TableExtractionInput`, `CanonicalSelectionInput`, `SourceDiscoveryResult`, and `TableExtractionResult` instead of stale prompt-context terminology.
- Confirmed `RunResult` and `BrandResult` public contracts have no `message` field and documented that explicitly in `doc/design/brand-size-chart.md`.
- Updated brand prompt templates and test helper docstrings to say `stage input` instead of `prompt context`.
- Left developer skill/reference matches only where they explicitly document forbidden or migration-only legacy terms.

Files changed
- `workflow-container-runtime/doc/design/workflow-container-runtime.md`
- `brand-size-chart/doc/design/brand-size-chart.md`
- `brand-size-chart/brand_size_chart/prompt/template/canonical_select.md.j2`
- `brand-size-chart/brand_size_chart/prompt/template/canonical_select_verify.md.j2`
- `brand-size-chart/brand_size_chart/prompt/template/source_discover_verify.md.j2`
- `brand-size-chart/test/test_workflow_contract.py`
- `workflow-container-developer/.superpowers/sdd/task-5-report.md`

Verification
- Runtime: `python -m black --target-version py314 --line-length 120 workflow_container_runtime test`
  - Pass.
- Runtime: `python -m compileall workflow_container_runtime`
  - Pass.
- Runtime: `python -m pytest -q`
  - Pass (`30 passed`).
- Brand: `python -m black --target-version py314 --line-length 120 brand_size_chart test`
  - Pass.
  - Used system `python` because `/home/andrey/Projects/brand-size-chart/.venv/bin/python -m black` failed with `No module named black`.
- Brand: `/home/andrey/Projects/brand-size-chart/.venv/bin/python -m compileall brand_size_chart`
  - Pass.
- Brand: `/home/andrey/Projects/brand-size-chart/.venv/bin/python -m pytest -q`
  - Pass (`146 passed`).
- Developer: `python -m compileall workflow_container_developer`
  - Pass.
- Developer: `python -m pytest -q`
  - Pass (`13 passed`).

Contract grep
- Command:
  - `rg -n "prompt_context_path|prompt_context\.json|STAGE_PROMPT_CONTEXT|VerifiedCodexStageRunner|VerifiedCodexStageConfig|stage_prompt_context_path_get|PromptContext|previous_result_json|draft_result_json" /home/andrey/Projects/workflow-container-runtime /home/andrey/Projects/brand-size-chart /home/andrey/Projects/workflow-container-developer/plugins/workflow-container-tools/skills`
- Current production/test matches:
  - None in `workflow-container-runtime`.
  - None in `brand-size-chart`.
- Allowed developer-skill/reference matches:
  - `plugins/workflow-container-tools/skills/workflow-container-developer/references/workflow-container-authoring.md`
  - `plugins/workflow-container-tools/skills/workflow-container-developer/references/2026-07-09-stage-file-contract-design.md`
  - `plugins/workflow-container-tools/skills/workflow-container-developer/SKILL.md`
  - `plugins/workflow-container-tools/skills/workflow-container-audit/SKILL.md`
  - These are all forbidden-contract, obsolete-contract, or migration-history references. No current production/test API usage remains.

Semantic audit
- Performed a manual semantic audit against:
  - `plugins/workflow-container-tools/skills/workflow-container-audit/SKILL.md`
  - `plugins/workflow-container-tools/skills/workflow-container-developer/SKILL.md`
  - `plugins/workflow-container-tools/skills/workflow-container-developer/references/workflow-container-authoring.md`
- Result:
  - No High findings.
  - No Medium findings.
  - Current docs/prompts/tests align with `Minimal Stable Contract`, `Stage Lifecycle`, `Prompt Routing`, `DBOS Handoff`, and private `state.json` boundaries for the touched artifacts.

Commits
- `workflow-container-runtime`: `e91eda5` `docs: align runtime stage contract wording`
- `brand-size-chart`: `410c478` `docs: align brand stage file contracts`
- `workflow-container-developer`: `docs: add task 5 alignment report`

Concerns
- No functional concerns.
- `brand-size-chart` still relies on system `black` for this task because the project `.venv` does not have the `black` module installed.
