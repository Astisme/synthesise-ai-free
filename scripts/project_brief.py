#!/usr/bin/env python3
"""Parse structured JSON sections embedded in a portable PROJECT-BRIEF.md.

Markdown remains the human-readable source of truth. Each supported level-two
section contains exactly one fenced JSON value, extracted for schema validation.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
import sys

SECTION_NAMES = {
    "metadata": "metadata",
    "status": "status",
    "creator profile": "creator_profile",
    "audience problem": "audience_problem",
    "uvz opportunities": "uvz_opportunities",
    "market findings": "market_findings",
    "experiments": "experiments",
    "product": "product",
    "commercial": "commercial",
    "launch": "launch",
    "open questions": "open_questions",
    "risks": "risks",
    "next actions": "next_actions",
    "decision log": "decision_log",
}
HEADING = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
JSON_FENCE = re.compile(r"~~~json\s*\n(.*?)\n~~~", re.IGNORECASE | re.DOTALL)


class ProjectBriefError(ValueError):
    pass


def parse_project_brief(markdown: str) -> dict:
    matches = list(HEADING.finditer(markdown))
    extracted = {}
    errors = []
    for index, match in enumerate(matches):
        heading = match.group(1).strip().casefold()
        key = SECTION_NAMES.get(heading)
        if key is None:
            continue
        if key in extracted:
            errors.append(f"Duplicate section: {match.group(1)}")
            continue
        end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        section_body = markdown[match.end():end]
        blocks = list(JSON_FENCE.finditer(section_body))
        if len(blocks) != 1:
            errors.append(f"Section '{match.group(1)}' must contain exactly one fenced json block; found {len(blocks)}")
            continue
        try:
            extracted[key] = json.loads(blocks[0].group(1))
        except json.JSONDecodeError as exc:
            errors.append(f"Section '{match.group(1)}' has invalid JSON at line {exc.lineno}: {exc.msg}")
    missing = sorted(set(SECTION_NAMES.values()) - set(extracted))
    if missing:
        errors.append("Missing or unparsable sections: " + ", ".join(missing))
    if errors:
        raise ProjectBriefError("; ".join(errors))
    return extracted


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("brief", type=Path, help="Path to PROJECT-BRIEF.md")
    parser.add_argument("--output", type=Path, help="Write extracted JSON to this path")
    args = parser.parse_args()
    try:
        value = parse_project_brief(args.brief.read_text(encoding="utf-8"))
        rendered = json.dumps(value, indent=2, ensure_ascii=False) + "\n"
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(rendered, encoding="utf-8")
        else:
            print(rendered, end="")
        return 0
    except (OSError, ProjectBriefError) as exc:
        print(f"PROJECT-BRIEF parse failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
