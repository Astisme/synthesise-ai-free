# Evaluation foundation

This directory separates deterministic checks from optional evaluation of actual agent runs.

## Layers

- Structural validation checks repository files, references, metadata and manifests.
- Schema validation checks extracted structured sections of PROJECT-BRIEF.md; Markdown remains the portable source of truth.
- Scenario/fixture validation checks scenario contracts and authored reference fixtures. It does not execute an agent and does not prove live behaviour.
- Regression baseline pins v1.1.0 canonical skill files to Git blob SHA-1 identifiers. A pinned-file change fails until an explicit, reviewed baseline update.
- Model evaluation optionally grades captured agent outputs with rubric scores and reproducibility metadata. It makes no API calls and needs no API key; run scenarios in the target harness/model separately.

## Run

    python scripts/validate.py
    python scripts/evaluate.py
    python scripts/evaluate_model.py path/to/model-run.json --report evaluations/reports/model-run.json

Scenario files use JSON syntax, a valid subset of YAML. This keeps the evaluator dependency-free while remaining readable as YAML.

Fixture matching is case-insensitive substring matching: a deterministic smoke check, not a semantic judge.

## Updating the frozen baseline

Never update baseline hashes merely to make a failing check pass. A baseline update must be intentional and separately reviewed, include a rationale describing the methodology change and expected impact, record the source commit and updated Git blob SHA-1 values, update baseline version/results, and add or revise scenarios covering the changed behaviour.

The v1.1.0 baseline is anchored to commit 3b70afb997a377fd555e9888cec912c96bf4ebd9. The v1.2.0 foundation does not edit canonical skill files.

## Model-run input

See schemas/model-run.schema.json and fixtures/model-run.example.json. Scores are supplied by an evaluator/judge; they are not inferred from string matching. Keep raw customer data, secrets and credentials out of captured runs.

## Regression metadata

Every scenario stores a role/content input conversation and a regression_status object. The v1.2.0 scenarios are fixture-only because v1.1.0 did not have captured live-agent outputs; they must not be presented as historical behavioural regressions.


The CI model-evaluator smoke test uses an authored sample capture only. It validates the report pipeline and does not execute a model or agent.

## v1.2.x API-free execution policy

The v1.2.1, v1.2.2 and v1.2.3 milestones are local/CI-only. They use Python's standard library and controlled fixtures. No model provider SDK, credentials, network calls or paid infrastructure are part of these milestones. v1.3.0 may add explicitly opt-in live Claude/GPT/Gemini evaluation; that is a separate capability and must not be required by ordinary CI.

Run the complete local QA pipeline:

    python scripts/validate.py
    python -m unittest discover -s scripts -p 'test_*.py' -v
    python scripts/evaluate.py --report-dir evaluations/reports

The evaluator writes evaluations/reports/deterministic.json and deterministic.md. Reports state that no live agent behaviour was tested and no API calls were made.
