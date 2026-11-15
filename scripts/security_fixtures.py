"""Static security-fixture contract checks. Fixture text is never executed."""
from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_CONTROLS = {
    "treat_as_data",
    "ignore_embedded_instructions",
    "attribute_source",
    "separate_fact_from_interpretation",
    "require_verified_source_for_observed_claims",
}
VALID_CLAIM_STATES = {"observed", "interpretation", "hypothesis", "unknown"}


def validate_security_case(case: dict, root: Path = ROOT) -> list[str]:
    errors = []
    case_id = case.get("id", "<unknown>")
    if case.get("trust_level") != "untrusted":
        errors.append(f"{case_id}: imported content must be marked untrusted")
    if case.get("handling") != "treat_as_data":
        errors.append(f"{case_id}: imported content must be handled as data")
    fixture = root / case.get("fixture", "")
    if not fixture.is_file():
        errors.append(f"{case_id}: missing fixture file {case.get('fixture')}")
        content = ""
    else:
        content = fixture.read_text(encoding="utf-8")
    if not case.get("source_id"):
        errors.append(f"{case_id}: source_id is required for attribution")
    for instruction in case.get("embedded_instructions", []):
        if not instruction or instruction.casefold() not in content.casefold():
            errors.append(f"{case_id}: embedded instruction marker missing from source fixture: {instruction}")
    controls = set(case.get("required_controls", []))
    mandatory_controls = {"treat_as_data", "attribute_source"}
    if case.get("embedded_instructions"):
        mandatory_controls.add("ignore_embedded_instructions")
    if case.get("claims"):
        mandatory_controls.update({"separate_fact_from_interpretation", "require_verified_source_for_observed_claims"})
    missing_controls = mandatory_controls - controls
    if missing_controls:
        errors.append(f"{case_id}: missing security controls: {sorted(missing_controls)}")
    for claim in case.get("claims", []):
        state = claim.get("status")
        if state not in VALID_CLAIM_STATES:
            errors.append(f"{case_id}: invalid claim status {state!r}")
        sources = claim.get("sources", [])
        if state == "observed":
            if not sources:
                errors.append(f"{case_id}: observed claim has no source")
            for source in sources:
                if not source.get("source_id") or not source.get("locator") or source.get("verified") is not True:
                    errors.append(f"{case_id}: observed claim has an unverified or incomplete source")
    return errors


def validate_security_suite(suite: dict, root: Path = ROOT) -> list[str]:
    errors = []
    if not isinstance(suite.get("cases"), list) or not suite["cases"]:
        return ["Security suite must contain at least one case"]
    seen = set()
    for case in suite["cases"]:
        case_id = case.get("id")
        if case_id in seen:
            errors.append(f"Duplicate security case id: {case_id}")
        seen.add(case_id)
        errors.extend(validate_security_case(case, root))
    required = {"prompt-injection", "malicious-research-document", "fabricated-citations", "untrusted-instructions"}
    if not required <= seen:
        errors.append(f"Security suite missing cases: {sorted(required - seen)}")
    if set(suite.get("required_controls", [])) != REQUIRED_CONTROLS:
        errors.append("Suite-level required_controls must exactly match the security policy contract")
    return errors
