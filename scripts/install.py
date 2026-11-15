#!/usr/bin/env python3
"""Install, verify or remove the canonical modular Synthesise v2 package."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
PACKAGES = (
    "synthesise-orchestrator", "synthesise-discovery", "synthesise-audience",
    "synthesise-uvz", "synthesise-market-intelligence", "synthesise-validation",
    "synthesise-product-architecture", "synthesise-curriculum",
    "synthesise-monetization", "synthesise-launch", "synthesise-project",
)
MANIFEST = ".synthesise-v2.json"
PLUGIN_VERSION = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))["version"]


def skill_checksum(path: Path) -> str:
    return hashlib.sha256((path / "SKILL.md").read_bytes()).hexdigest()


def skill_metadata(path: Path) -> str:
    text = (path / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        raise ValueError(f"Invalid SKILL.md frontmatter: {path}")
    name = re.search(r"(?m)^name:\s*([^\s]+)\s*$", match.group(1))
    if not name:
        raise ValueError(f"Missing skill name metadata: {path}")
    return name.group(1)


def load_manifest(path: Path) -> dict:
    if not path.exists():
        return {"schema_version": 1, "channel": "v2", "packages": {}}
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1 or data.get("channel") != "v2" or not isinstance(data.get("packages"), dict):
        raise ValueError(f"Unrecognized install manifest: {path}")
    return data


def write_manifest(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    temp.replace(path)


def installed_skill_names(target: Path) -> dict[str, Path]:
    found = {}
    if not target.is_dir():
        return found
    for child in target.iterdir():
        skill_file = child / "SKILL.md"
        if child.is_dir() and skill_file.is_file():
            name = skill_metadata(child)
            if name in found:
                raise ValueError(f"Duplicate installed skill name '{name}': {found[name]} and {child}")
            found[name] = child
    return found


def verify_installation(target: Path, selected: tuple[str, ...], manifest: dict, single_package: bool) -> None:
    records = manifest["packages"]
    unknown = sorted(set(records) - set(PACKAGES))
    if unknown:
        raise ValueError("Install manifest contains unknown package IDs: " + ", ".join(unknown))
    installed = installed_skill_names(target)
    errors = []
    for package in selected:
        record = records.get(package)
        destination = target / package
        if not isinstance(record, dict) or not isinstance(record.get("version"), str) or not record["version"]:
            errors.append(f"{package}: missing or invalid install-manifest record")
            continue
        if not destination.is_dir() or not (destination / "SKILL.md").is_file():
            errors.append(f"{package}: installed package or SKILL.md is missing")
            continue
        try:
            name = skill_metadata(destination)
        except (OSError, ValueError) as exc:
            errors.append(f"{package}: cannot read skill metadata ({exc})")
            continue
        if name != package:
            errors.append(f"{package}: skill identity is '{name}'")
        if record["version"] != PLUGIN_VERSION:
            errors.append(f"{package}: install-manifest version {record['version']} does not match plugin version {PLUGIN_VERSION}")
        expected_checksum = record.get("sha256")
        if not isinstance(expected_checksum, str) or skill_checksum(destination) != expected_checksum:
            errors.append(f"{package}: SKILL.md content checksum does not match installed package")
    if not single_package:
        for package in PACKAGES:
            if (target / package).exists() and package not in records:
                errors.append(f"{package}: directory exists but is not tracked by the install manifest")
    if errors:
        raise ValueError("Install verification failed:\n- " + "\n- ".join(errors))
    print("Install verification passed (read-only).")
    for package in selected:
        record = records.get(package)
        if record:
            print(f"Verified {package} ({record['version']})")


def replace_directory(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="synthesise-v2-", dir=destination.parent) as temp_dir:
        staged = Path(temp_dir) / destination.name
        shutil.copytree(source, staged)
        backup = destination.with_name(destination.name + ".synthesise-backup")
        if backup.exists():
            shutil.rmtree(backup)
        if destination.exists():
            destination.rename(backup)
        try:
            staged.rename(destination)
        except Exception:
            if backup.exists():
                backup.rename(destination)
            raise
        if backup.exists():
            shutil.rmtree(backup)


def main() -> int:
    parser = argparse.ArgumentParser(description="Install, verify or remove the modular Synthesise v2 package.")
    parser.add_argument("--target", default=".agents/skills", help="Agent skills directory (default: .agents/skills)")
    parser.add_argument("--package", choices=PACKAGES, help="Install/verify/remove one package; default is the complete v2 set")
    parser.add_argument("--force", action="store_true", help="Replace an existing managed or unmanaged package")
    actions = parser.add_mutually_exclusive_group()
    actions.add_argument("--remove", action="store_true", help="Remove selected v2 package(s)")
    actions.add_argument("--verify", action="store_true", help="Verify installed package identities and versions without writing files")
    args = parser.parse_args()

    target = Path(args.target).expanduser().resolve()
    selected = (args.package,) if args.package else PACKAGES
    manifest_path = target / MANIFEST

    try:
        if args.verify and args.force:
            raise ValueError("--force cannot be combined with --verify")
        manifest = load_manifest(manifest_path)
        if args.verify:
            if not manifest_path.is_file():
                raise ValueError(f"Install manifest not found: {manifest_path}")
            verify_installation(target, selected, manifest, bool(args.package))
            return 0
        if args.remove:
            for package in selected:
                destination = target / package
                if package in manifest["packages"] and destination.exists():
                    shutil.rmtree(destination)
                manifest["packages"].pop(package, None)
            if manifest["packages"]:
                write_manifest(manifest_path, manifest)
            elif manifest_path.exists():
                manifest_path.unlink()
            print("Removed selected v2 package(s).")
            return 0

        target.mkdir(parents=True, exist_ok=True)
        installed = installed_skill_names(target)
        for package in selected:
            source = SKILLS / package
            if not (source / "SKILL.md").is_file():
                raise ValueError(f"Source package is incomplete: {source}")
            name = skill_metadata(source)
            version = PLUGIN_VERSION
            checksum = skill_checksum(source)
            if name != package:
                raise ValueError(f"Package identity mismatch: directory={package}, skill={name}")
            destination = target / package
            existing = installed.get(name)
            if existing and existing != destination:
                raise ValueError(f"Duplicate skill identity '{name}' already installed at {existing}")
            record = manifest["packages"].get(package)
            if destination.exists() and not args.force:
                if record and record.get("version") == version and record.get("sha256") == checksum:
                    print(f"Already installed: {package} ({version})")
                    continue
                if record:
                    raise ValueError(f"{package} is installed at another version; use --force to upgrade")
                raise ValueError(f"Unmanaged destination exists: {destination}; use --force to replace")
            replace_directory(source, destination)
            manifest["packages"][package] = {"version": version, "sha256": checksum}
            write_manifest(manifest_path, manifest)
            print(f"Installed {package} ({version})")
        print(f"v2 installation complete: {target}")
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"v2 installer error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
