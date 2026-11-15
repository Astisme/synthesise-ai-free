#!/usr/bin/env python3
"""Install the modular v2 preview without modifying the stable v1 skill."""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
PACKAGES = (
    "synthesise-orchestrator",
    "synthesise-discovery",
    "synthesise-audience",
    "synthesise-uvz",
    "synthesise-market-intelligence",
    "synthesise-validation",
    "synthesise-product-architecture",
    "synthesise-curriculum",
    "synthesise-monetization",
    "synthesise-launch",
    "synthesise-project",
)
MANIFEST = ".synthesise-v2-preview.json"


def skill_metadata(path: Path) -> tuple[str, str]:
    text = (path / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        raise ValueError(f"Invalid SKILL.md frontmatter: {path}")
    name = re.search(r"(?m)^name:\s*([^\s]+)\s*$", match.group(1))
    version = re.search(r'(?m)^\s+version:\s*["\']?([^\s"\']+)', match.group(1))
    if not name or not version:
        raise ValueError(f"Missing name/version metadata: {path}")
    return name.group(1), version.group(1)


def load_manifest(path: Path) -> dict:
    if not path.exists():
        return {"schema_version": 1, "channel": "v2-preview", "packages": {}}
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1 or data.get("channel") != "v2-preview" or not isinstance(data.get("packages"), dict):
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
            name, _ = skill_metadata(child)
            if name in found:
                raise ValueError(f"Duplicate installed skill name '{name}': {found[name]} and {child}")
            found[name] = child
    return found


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
    parser = argparse.ArgumentParser(description="Install or remove the modular Synthesise v2 preview.")
    parser.add_argument("--target", default=".agents/skills", help="Agent skills directory (default: .agents/skills)")
    parser.add_argument("--package", choices=PACKAGES, help="Install/remove one package; default is the complete v2 set")
    parser.add_argument("--force", action="store_true", help="Replace an existing managed or unmanaged package")
    parser.add_argument("--remove", action="store_true", help="Remove selected v2 preview package(s)")
    args = parser.parse_args()

    target = Path(args.target).expanduser().resolve()
    selected = (args.package,) if args.package else PACKAGES
    manifest_path = target / MANIFEST

    try:
        manifest = load_manifest(manifest_path)
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
            print("Removed selected v2 preview package(s).")
            return 0

        target.mkdir(parents=True, exist_ok=True)
        installed = installed_skill_names(target)
        for package in selected:
            source = SKILLS / package
            if not (source / "SKILL.md").is_file():
                raise ValueError(f"Source package is incomplete: {source}")
            name, version = skill_metadata(source)
            if name != package:
                raise ValueError(f"Package identity mismatch: directory={package}, skill={name}")
            destination = target / package
            existing = installed.get(name)
            if existing and existing != destination:
                raise ValueError(f"Duplicate skill identity '{name}' already installed at {existing}")
            record = manifest["packages"].get(package)
            if destination.exists() and not args.force:
                if record and record.get("version") == version:
                    print(f"Already installed: {package} ({version})")
                    continue
                if record:
                    raise ValueError(f"{package} is installed at another version; use --force to upgrade")
                raise ValueError(f"Unmanaged destination exists: {destination}; use --force to replace")
            replace_directory(source, destination)
            manifest["packages"][package] = {"version": version}
            write_manifest(manifest_path, manifest)
            print(f"Installed {package} ({version})")
        print(f"v2 preview installation complete: {target}")
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"v2 preview installer error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
