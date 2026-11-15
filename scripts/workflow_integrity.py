"""Deterministic integrity checks for product workflow handoffs and project resume."""
from __future__ import annotations


def _nonempty_list(value):
    return isinstance(value, list) and len(value) > 0


def validate_product_lifecycle(fixture: dict) -> list[str]:
    errors = []
    stages = fixture.get("stages", {})
    required = ("discovery", "uvz", "validation", "charter", "curriculum", "monetization")
    for name in required:
        if not isinstance(stages.get(name), dict):
            errors.append(f"Missing workflow stage: {name}")
    if errors:
        return errors

    discovery, uvz, validation, charter, curriculum, offer = (stages[name] for name in required)
    for field in ("audience_id", "problem_id"):
        if not discovery.get(field):
            errors.append(f"Discovery missing {field}")
    if not _nonempty_list(discovery.get("capability_ids")) or not _nonempty_list(discovery.get("evidence_ids")):
        errors.append("Discovery must include demonstrated capability IDs and evidence IDs")
    if uvz.get("audience_id") != discovery.get("audience_id") or uvz.get("problem_id") != discovery.get("problem_id"):
        errors.append("UVZ handoff must preserve discovery audience_id and problem_id")
    if not set(uvz.get("creator_capability_ids", [])) <= set(discovery.get("capability_ids", [])):
        errors.append("UVZ references capability IDs absent from discovery")
    if not set(uvz.get("evidence_ids", [])) <= set(discovery.get("evidence_ids", [])):
        errors.append("UVZ references evidence IDs absent from discovery")
    if not _nonempty_list(uvz.get("unknowns")):
        errors.append("UVZ must carry forward explicit unknowns")

    if uvz.get("opportunity_id") != validation.get("opportunity_id"):
        errors.append("Validation must reference the selected UVZ opportunity")
    if not all(validation.get(key) for key in ("hypothesis", "method", "success_threshold", "failure_threshold")):
        errors.append("Validation must define a falsifiable hypothesis, method and success/failure thresholds")
    if validation.get("status") == "completed" and not _nonempty_list(validation.get("evidence_ids")):
        errors.append("Completed validation must include evidence IDs")

    if charter.get("opportunity_id") != uvz.get("opportunity_id"):
        errors.append("Product charter must reference the selected UVZ opportunity")
    if charter.get("audience_id") != discovery.get("audience_id"):
        errors.append("Product charter must preserve the discovery audience")
    if charter.get("promise_status") == "validated":
        if validation.get("status") != "completed" or not _nonempty_list(validation.get("evidence_ids")):
            errors.append("A validated product promise requires completed validation evidence")
        if not set(charter.get("evidence_ids", [])) <= set(validation.get("evidence_ids", [])):
            errors.append("Product promise cites evidence not present in validation")
    if not charter.get("promise_id") or not charter.get("promise"):
        errors.append("Product charter must define a stable promise ID and promise")

    modules = curriculum.get("modules")
    if curriculum.get("product_id") != charter.get("product_id"):
        errors.append("Curriculum must reference the charter product_id")
    if not _nonempty_list(modules):
        errors.append("Curriculum must contain at least one module")
    else:
        for module in modules:
            if module.get("supports_promise_id") != charter.get("promise_id"):
                errors.append(f"Module {module.get('id', '<unknown>')} is not linked to the charter promise")
            for field in ("learning_outcome", "assessment", "deliverable"):
                if not module.get(field):
                    errors.append(f"Module {module.get('id', '<unknown>')} missing {field}")

    if offer.get("product_id") != charter.get("product_id"):
        errors.append("Monetization offer must reference the charter product_id")
    if offer.get("audience_id") != charter.get("audience_id"):
        errors.append("Monetization offer must preserve the charter audience")
    if offer.get("offer_promise_id") != charter.get("promise_id"):
        errors.append("Monetization offer must sell the charter promise")
    if not offer.get("price_hypothesis") or not _nonempty_list(offer.get("assumptions")):
        errors.append("Monetization must label a pricing hypothesis and its assumptions")
    if offer.get("revenue_guarantee") is True:
        errors.append("Monetization must not introduce an unsupported revenue guarantee")
    return errors


def validate_project_resume(fixture: dict) -> list[str]:
    errors = []
    before, after = fixture.get("before", {}), fixture.get("after", {})
    if not before or not after:
        return ["Continuity fixture requires before and after states"]
    if before.get("project_id") != after.get("project_id"):
        errors.append("Resume must preserve project_id")
    prior = before.get("decisions", [])
    resumed = after.get("decisions", [])
    resumed_by_id = {item.get("id"): item for item in resumed}
    for decision in prior:
        decision_id = decision.get("id")
        if decision_id not in resumed_by_id:
            errors.append(f"Resume dropped prior decision {decision_id}")
        elif resumed_by_id[decision_id] != decision:
            errors.append(f"Resume silently modified prior decision {decision_id}")
    prior_ids = [item.get("id") for item in prior]
    resumed_ids = [item.get("id") for item in resumed]
    if resumed_ids[:len(prior_ids)] != prior_ids:
        errors.append("Resume must preserve prior decision order and append new decisions")
    if not set(before.get("open_questions", [])) <= set(after.get("open_questions", [])):
        errors.append("Resume silently dropped unresolved questions")
    return errors
