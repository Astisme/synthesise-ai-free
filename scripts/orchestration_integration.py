"""Deterministic cross-specialist integration contracts for modular v2.

These tests validate handoff/state invariants in authored fixtures. They do not
invoke specialist agents or prove live model behaviour.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "evaluations" / "integration" / "orchestration-scenarios.json"

REQUIRED_TYPES = {
    "lifecycle", "parallelism", "evidence", "ownership",
    "decision_conflict", "resume", "validation", "launch_readiness",
}


def validate_scenario(case: dict) -> list[str]:
    errors = []
    kind = case.get("type")
    if kind == "lifecycle":
        stages = case.get("stages", {})
        required = {"discovery", "audience", "uvz", "market", "validation", "charter"}
        if not required.issubset(stages):
            return ["Lifecycle is missing required stages"]
        discovery, audience, uvz, market, validation, charter = (stages[x] for x in
            ("discovery", "audience", "uvz", "market", "validation", "charter"))
        if audience.get("audience_id") != discovery.get("audience_id") or uvz.get("audience_id") != discovery.get("audience_id") or charter.get("audience_id") != discovery.get("audience_id"):
            errors.append("Audience identity drifted across specialist handoffs")
        if uvz.get("problem_id") != discovery.get("problem_id"):
            errors.append("UVZ lost the originating problem identity")
        if not set(uvz.get("capability_ids", [])) <= set(discovery.get("capability_ids", [])):
            errors.append("UVZ references an unknown creator capability")
        if not set(uvz.get("evidence_ids", [])) <= set(discovery.get("evidence_ids", [])):
            errors.append("UVZ references evidence absent from Discovery")
        if market.get("opportunity_id") != uvz.get("opportunity_id") or validation.get("opportunity_id") != uvz.get("opportunity_id") or charter.get("opportunity_id") != uvz.get("opportunity_id"):
            errors.append("Selected opportunity identity drifted across Market, Validation or Charter")
        if not market.get("evidence_ids") or not validation.get("evidence_ids"):
            errors.append("Market and Validation must return traceable evidence IDs")
        if validation.get("decision") == "revise" and charter.get("promise_status") == "validated":
            errors.append("A revise validation outcome cannot silently produce a validated promise")
        if charter.get("owner") != "synthesise-product-architecture":
            errors.append("Product charter ownership is incorrect")
    elif kind == "parallelism":
        tasks = case.get("tasks", [])
        if len(tasks) != 2:
            errors.append("Parallel research case must contain exactly two tasks")
        else:
            left, right = tasks
            if left.get("skill_id") == right.get("skill_id"):
                errors.append("Parallel tasks must be distinct specialists")
            if left.get("output") == right.get("output") or left.get("owner") == right.get("owner"):
                errors.append("Parallel tasks must have distinct output paths and owners")
            if right.get("skill_id") in left.get("depends_on", []) or left.get("skill_id") in right.get("depends_on", []):
                errors.append("Parallel tasks cannot depend on each other")
            common = set(left.get("depends_on", [])) & set(right.get("depends_on", []))
            if not common or case.get("selected_opportunity") not in common:
                errors.append("Parallel tasks must share the approved opportunity prerequisite")
        expected = "parallel" if case.get("harness_supports_parallel") else "sequential"
        if case.get("expected_mode") != expected:
            errors.append("Execution mode does not respect actual harness parallel capability")
    elif kind == "evidence":
        record = case.get("record", {})
        for consumer in case.get("consumers", []):
            if consumer.get("evidence_id") != record.get("evidence_id"):
                errors.append("Evidence identity changed during handoff")
            if consumer.get("status") != record.get("status") or consumer.get("confidence") != record.get("confidence"):
                errors.append("Evidence status/confidence was silently upgraded")
            if consumer.get("sample_size") != record.get("scope", {}).get("sample_size"):
                errors.append("Evidence sample scope was lost")
        if not record.get("limitations"):
            errors.append("Evidence limitations must remain attached")
    elif kind == "ownership":
        artifact, request = case.get("artifact", {}), case.get("request", {})
        if request.get("requesting_skill") == artifact.get("owner"):
            errors.append("Fixture must exercise a non-owner request")
        if request.get("operation") == "modify" and request.get("write_status") != "proposed":
            errors.append("Non-owner modification must remain a proposal")
        if request.get("approved_by_owner") is not False or case.get("expected") != "reject_write_keep_proposal":
            errors.append("Unauthorized artifact write was not rejected")
    elif kind == "decision_conflict":
        decision, incoming, resolution = case.get("approved_decision", {}), case.get("incoming", {}), case.get("resolution", {})
        if decision.get("status") != "approved" or incoming.get("status") != "proposed":
            errors.append("Conflict must distinguish approved state from proposed recommendation")
        if resolution.get("status") != "pending_user_approval" or resolution.get("prior_decision_preserved") is not True or resolution.get("automatic_replacement") is not False:
            errors.append("Approved decision was silently replaced instead of escalating conflict")
    elif kind == "resume":
        before, after = case.get("before", {}), case.get("after", {})
        if before.get("project_id") != after.get("project_id"):
            errors.append("Resume changed project identity")
        after_decisions = {x.get("id"): x for x in after.get("decisions", [])}
        for decision in before.get("decisions", []):
            if after_decisions.get(decision.get("id")) != decision:
                errors.append("Resume dropped or modified an existing decision")
        if not set(before.get("open_questions", [])) <= set(after.get("open_questions", [])):
            errors.append("Resume dropped an unresolved question")
        if not set(before.get("evidence_ids", [])) <= set(after.get("evidence_ids", [])):
            errors.append("Resume lost evidence provenance")
        if not after.get("next_action"):
            errors.append("Resume must identify a next action")
    elif kind == "validation":
        validation, charter = case.get("validation", {}), case.get("charter", {})
        if validation.get("status") == "failed" and charter.get("promise_status") == "validated":
            errors.append("Failed validation cannot be represented as a validated promise")
        if validation.get("status") == "failed" and charter.get("decision_required") is not True:
            errors.append("Failed validation requires an explicit product decision gate")
        if case.get("expected") != "no_validated_promise":
            errors.append("Negative validation expectation is missing")
    elif kind == "launch_readiness":
        readiness, launch = case.get("readiness", {}), case.get("launch", {})
        critical = {"checkout", "onboarding", "fulfillment"}
        blockers = {key for key in critical if readiness.get(key) != "ready"}
        if not blockers <= set(launch.get("blockers", [])):
            errors.append("Launch handoff omitted critical operational blockers")
        if blockers and launch.get("completion_status") != "blocked":
            errors.append("Launch cannot be complete while critical operational gates are open")
        if launch.get("campaign_plan_status") != "conditional":
            errors.append("Campaign planning must remain conditional until readiness gates pass")
        if case.get("expected") != "blocked_until_critical_gates_pass":
            errors.append("Launch readiness expectation is missing")
    else:
        errors.append("Unknown integration scenario type: " + str(kind))
    return errors


def evaluate_integration_suite(data: dict) -> list[dict]:
    results = []
    scenarios = data.get("scenarios", [])
    seen = set()
    for case in scenarios:
        case_id = case.get("id")
        errors = []
        if not case_id or case_id in seen:
            errors.append("Scenario ID is missing or duplicated")
        seen.add(case_id)
        if not case.get("purpose") or not case.get("title"):
            errors.append("Scenario must explain its purpose and title")
        errors.extend(validate_scenario(case))
        results.append({"id": case_id, "type": case.get("type"), "passed": not errors, "errors": errors})
    present = {case.get("type") for case in scenarios}
    for missing in sorted(REQUIRED_TYPES - present):
        results.append({"id": "suite", "type": missing, "passed": False, "errors": ["Required integration scenario type is missing"]})
    return results
