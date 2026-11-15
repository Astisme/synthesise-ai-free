# Evaluation foundation

The evaluation suite is organized around the canonical modular v2 package. It separates deterministic repository contracts from optional evaluation of actual agent runs.

## Layers

- Structural validation checks the eleven v2 skill packages, local references, metadata and root marketplace manifests.
- Schema validation checks extracted structured sections of `PROJECT-BRIEF.md`; Markdown remains the portable source of truth.
- Specialist methodology fixtures check authored task contracts and expected invariants for each of the ten specialists.
- Orchestration fixtures check deterministic handoffs, evidence provenance, artifact ownership, decision conflicts, project resume and launch readiness. They do not execute an agent and do not prove live behaviour.
- The canonical v2 baseline pins the orchestrator and specialist entry points plus their core methodology references using Git blob SHA-1 identifiers. A pinned-file change fails until an explicit, reviewed baseline update.
- Optional model evaluation grades captured agent outputs with rubric scores and reproducibility metadata. It makes no API calls and needs no API key; run scenarios in the target harness/model separately.

## Run

```bash
python scripts/validate.py
python -m unittest discover -s scripts -p 'test_*.py' -v
python scripts/evaluate.py --report-dir evaluations/reports
python scripts/evaluate_model.py path/to/model-run.json --report evaluations/reports/model-run.json
```

Scenario files use JSON syntax, a valid subset of YAML. This keeps the evaluator dependency-free while remaining readable as YAML.

Fixture matching is case-insensitive substring matching: a deterministic smoke check, not a semantic judge.

## Updating the canonical v2 baseline

Never update baseline hashes merely to make a failing check pass. A baseline update must be intentional and separately reviewed, include a rationale describing the methodology change and expected impact, record the source commit and updated Git blob SHA-1 values, update baseline version/results, and add or revise specialist/orchestration scenarios covering the changed behaviour.

The current baseline is `evaluations/baseline/v2.0.0-alpha.4.json`; its pinned file hashes are in `evaluations/baseline/checksums.json`. It covers all eleven modular package entry points and their core methodology references. The seven-dimension UVZ rubric and its established weights, formulas, scales and sensitivity-analysis rules are part of the pinned v2 UVZ specialist method.

## Model-run input

See `schemas/model-run.schema.json` and `fixtures/model-run.example.json`. Scores are supplied by an evaluator/judge; they are not inferred from string matching. Keep raw customer data, secrets and credentials out of captured runs.

## CI execution policy

Required CI is local and API-free. It uses Python's standard library and controlled fixtures. No model provider SDK, credentials, network calls or paid infrastructure are part of required CI. Live Claude Code, Codex, Gemini or other host evaluation is a separate, explicitly recorded acceptance activity and must not be represented by deterministic fixture results.

The evaluator writes `evaluations/reports/deterministic.json` and `deterministic.md`. Reports state that no live agent behaviour was tested and no API calls were made.

## Installer regression tests

The modular v2 installer regression suite exercises `scripts/install.py` using temporary target directories. It checks full and individual installs, idempotence, partial recovery, paths containing spaces, safe collision refusal, explicit forced replacement, duplicate identity detection, read-only verification, and removal without disturbing unrelated skills.

Run on any platform with Python 3:

```bash
python -m unittest discover -s scripts -p 'test_install_v2.py' -v
```

## Security fixture and provenance contract

Security fixtures are treated strictly as untrusted data and are never executed. The validator rejects absolute fixture paths and resolved paths outside the repository root (including symlink escapes), malformed suite/case/claim/source structures, invalid claim states and missing trust controls.

A claim marked `observed` must include at least one source with a non-empty source identifier and locator, `verified: true`, a non-empty `verification_method`, and a valid `verified_at` date in `YYYY-MM-DD` format. This metadata makes the assertion auditable; the offline fixture validator does not independently verify the external source or prove the claim true.
