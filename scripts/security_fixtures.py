"""Static security-fixture contract checks. Fixture text is never executed."""
from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_CONTROLS = {
    "treat_as_data",
    "ignore_embedded_instructions",
    "attribute_source",
    "separate_fact_from_interpretation",
    "require_verified_source_for_observed_claims",
}
VALID_CLAIM_STATES = {"observed", "interpretation", "hypothesis", "unknown"}


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _safe_fixture_path(root: Path, relative: Any) -> tuple[Path | None, str | None]:
    """Resolve a fixture only when it remains inside the configured repository root."""
    if not _nonempty_string(relative):
        return None, "fixture path must be a non-empty relative path"
    try:
        candidate = Path(relative)
        if candidate.is_absolute():
            return None, "fixture path must be relative to the repository root"
        resolved_root = root.resolve()
        resolved = (resolved_root / candidate).resolve()
    except (OSError, RuntimeError, ValueError) as exc:
        return None, f"fixture path cannot be resolved: {exc}"
    if not resolved.is_relative_to(resolved_root):
        return None, "fixture path escapes the repository root"
    return resolved, None


def validate_security_case(case: dict, root: Path = ROOT) -> list[str]:
    errors = []
    if not isinstance(case, dict):
        return ["Security case must be an object"]

    case_id = case.get("id", "<unknown>")
    if not _nonempty_string(case_id):
        errors.append("Security case id must be a non-empty string")
        case_id = "<unknown>"

    if case.get("trust_level") != "untrusted":
        errors.append(f"{case_id}: imported content must be marked untrusted")
    if case.get("handling") != "treat_as_data":
        errors.append(f"{case_id}: imported content must be handled as data")

    fixture, path_error = _safe_fixture_path(root, case.get("fixture"))
    if path_error:
        errors.append(f"{case_id}: {path_error}")
        content = ""
    elif fixture is None or not fixture.is_file():
        errors.append(f"{case_id}: missing fixture file {case.get('fixture')}")
        content = ""
    else:
        try:
            content = fixture.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{case_id}: unable to read fixture: {exc}")
            content = ""

    if not _nonempty_string(case.get("source_id")):
        errors.append(f"{case_id}: source_id is required for attribution")

    embedded = case.get("embedded_instructions", [])
    if not isinstance(embedded, list) or not all(_nonempty_string(item) for item in embedded):
        errors.append(f"{case_id}: embedded_instructions must be a list of non-empty strings")
        embedded = []
    for instruction in embedded:
        if instruction.casefold() not in content.casefold():
            errors.append(f"{case_id}: embedded instruction marker missing from source fixture: {instruction}")

    raw_controls = case.get("required_controls", [])
    if not isinstance(raw_controls, list) or not all(_nonempty_string(item) for item in raw_controls):
        errors.append(f"{case_id}: required_controls must be a list of non-empty strings")
        controls = set()
    else:
        controls = set(raw_controls)

    mandatory_controls = {"treat_as_data", "attribute_source"}
    if embedded:
        mandatory_controls.add("ignore_embedded_instructions")

    claims = case.get("claims", [])
    if not isinstance(claims, list):
        errors.append(f"{case_id}: claims must be a list")
        claims = []
    if claims:
        mandatory_controls.update({
            "separate_fact_from_interpretation",
            "require_verified_source_for_observed_claims",
        })

    missing_controls = mandatory_controls - controls
    if missing_controls:
        errors.append(f"{case_id}: missing security controls: {sorted(missing_controls)}")

    for index, claim in enumerate(claims):
        claim_label = f"{case_id}: claim[{index}]"
        if not isinstance(claim, dict):
            errors.append(f"{claim_label} must be an object")
            continue
        if not _nonempty_string(claim.get("text")):
            errors.append(f"{claim_label} text must be a non-empty string")

        state = claim.get("status")
        if not isinstance(state, str) or state not in VALID_CLAIM_STATES:
            errors.append(f"{claim_label} has invalid claim status {state!r}")

        sources = claim.get("sources", [])
        if not isinstance(sources, list):
            errors.append(f"{claim_label} sources must be a list")
            continue
        if state == "observed" and not sources:
            errors.append(f"{case_id}: observed claim has no source")

        for source_index, source in enumerate(sources):
            source_label = f"{claim_label} source[{source_index}]"
            if not isinstance(source, dict):
                errors.append(f"{source_label} must be an object")
                continue
            if not _nonempty_string(source.get("source_id")) or not _nonempty_string(source.get("locator")):
                errors.append(f"{source_label} has an unverified or incomplete source")
            if state == "observed":
                if source.get("verified") is not True:
                    errors.append(f"{source_label} has an unverified or incomplete source")
                    continue
                if not _nonempty_string(source.get("verification_method")):
                    errors.append(f"{source_label} requires verification_method")
                verified_at = source.get("verified_at")
                if not _nonempty_string(verified_at):
                    errors.append(f"{source_label} requires verified_at in YYYY-MM-DD format")
                else:
                    try:
                        date.fromisoformat(verified_at)
                    except ValueError:
                        errors.append(f"{source_label} verified_at must be a valid YYYY-MM-DD date")

    return errors


def validate_security_suite(suite: dict, root: Path = ROOT) -> list[str]:
    if not isinstance(suite, dict):
        return ["Security suite must be an object"]

    errors = []
    if not _nonempty_string(suite.get("version")):
        errors.append("Security suite version must be a non-empty string")
    if not _nonempty_string(suite.get("policy")):
        errors.append("Security suite policy must be a non-empty string")

    cases = suite.get("cases")
    if not isinstance(cases, list) or not cases:
        return errors + ["Security suite must contain at least one case"]

    seen = set()
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            errors.append(f"Security case at index {index} must be an object")
            continue
        case_id = case.get("id")
        if not _nonempty_string(case_id):
            errors.append(f"Security case at index {index} must have a non-empty id")
        elif case_id in seen:
            errors.append(f"Duplicate security case id: {case_id}")
        else:
            seen.add(case_id)
        errors.extend(validate_security_case(case, root))

    required = {"prompt-injection", "malicious-research-document", "fabricated-citations", "untrusted-instructions"}
    if not required <= seen:
        errors.append(f"Security suite missing cases: {sorted(required - seen)}")

    suite_controls = suite.get("required_controls", [])
    if not isinstance(suite_controls, list) or not all(_nonempty_string(item) for item in suite_controls):
        errors.append("Suite-level required_controls must be a list of non-empty strings")
    elif set(suite_controls) != REQUIRED_CONTROLS:
        errors.append("Suite-level required_controls must exactly match the security policy contract")
    return errors
