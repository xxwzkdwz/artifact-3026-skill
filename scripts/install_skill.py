#!/usr/bin/env python3
"""Install the canonical Artifact 3026 skill by copying or symlinking it."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / ".agents" / "skills" / "artifact-3026"


def target_path(platform: str, scope: str, project_dir: Path) -> Path:
    if scope == "user":
        base = Path.home()
    else:
        base = project_dir.resolve()
    if platform == "claude":
        folder = ".claude/skills"
    elif platform == "qwen":
        folder = ".qwen/skills"
    elif platform == "kimi" and scope == "user":
        folder = ".config/agents/skills"
    else:
        folder = ".agents/skills"
    return base / folder / SOURCE.name


def install(source: Path, target: Path, mode: str, dry_run: bool = False) -> str:
    source = source.resolve()
    if target.exists() or target.is_symlink():
        try:
            if target.resolve() == source:
                return f"already installed: {target}"
        except OSError:
            pass
        raise FileExistsError(
            f"target already exists: {target}\n"
            "Remove or rename it after reviewing its contents, then run this command again."
        )
    action = f"{mode} {source} -> {target}"
    if dry_run:
        return f"dry run: {action}"
    target.parent.mkdir(parents=True, exist_ok=True)
    if mode == "copy":
        shutil.copytree(source, target)
    else:
        target.symlink_to(source, target_is_directory=True)
    return action


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Install Artifact 3026 from its canonical .agents/skills directory. "
            "The installer adapts the same source to each host's documented skill path."
        )
    )
    parser.add_argument(
        "--platform",
        choices=("agents", "codex", "cursor", "copilot", "claude", "qwen", "kimi"),
        default="agents",
    )
    parser.add_argument("--scope", choices=("project", "user"), default="user")
    parser.add_argument("--mode", choices=("copy", "symlink"), default="copy")
    parser.add_argument("--project-dir", type=Path, default=Path.cwd())
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    target = target_path(args.platform, args.scope, args.project_dir)
    print(install(SOURCE, target, args.mode, args.dry_run))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
