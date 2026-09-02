#!/usr/bin/env python3
"""Run dependency-free release checks for Future Museum Curator."""

from __future__ import annotations

import importlib.util
import json
import re
import struct
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_PATH = ROOT / ".codex-plugin" / "plugin.json"
SKILL_PATH = ROOT / "skills" / "future-museum-curator" / "SKILL.md"
RENDERER_PATH = ROOT / "skills" / "future-museum-curator" / "scripts" / "render_exhibit_card.py"
EXPECTED = {
    "name": "future-museum-curator",
    "author_name": "WANG ZHEN",
    "author_url": "https://github.com/xxwzkdwz",
    "repository": "https://github.com/xxwzkdwz/future-museum-curator",
    "license": "MIT",
}


def fail(message: str) -> None:
    raise ValueError(message)


def load_renderer():
    spec = importlib.util.spec_from_file_location("future_museum_renderer", RENDERER_PATH)
    if not spec or not spec.loader:
        fail("cannot load render_exhibit_card.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check_plugin() -> None:
    plugin = json.loads(PLUGIN_PATH.read_text(encoding="utf-8"))
    checks = {
        "plugin name": plugin.get("name") == EXPECTED["name"],
        "author name": plugin.get("author", {}).get("name") == EXPECTED["author_name"],
        "author URL": plugin.get("author", {}).get("url") == EXPECTED["author_url"],
        "repository URL": plugin.get("repository") == EXPECTED["repository"],
        "homepage URL": plugin.get("homepage") == EXPECTED["repository"],
        "license": plugin.get("license") == EXPECTED["license"],
        "skills directory": plugin.get("skills") == "./skills/",
    }
    failures = [label for label, passed in checks.items() if not passed]
    if failures:
        fail("plugin metadata mismatch: " + ", ".join(failures))


def check_skill() -> None:
    text = SKILL_PATH.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail("SKILL.md is missing YAML frontmatter")
    frontmatter = text.split("---", 2)[1]
    if not re.search(r"^name:\s*future-museum-curator\s*$", frontmatter, re.MULTILINE):
        fail("SKILL.md name does not match plugin")
    if not re.search(r"^description:\s*\S.+$", frontmatter, re.MULTILINE):
        fail("SKILL.md description is missing")
    if "AI-ASSISTED FICTION" not in (ROOT / "skills" / "future-museum-curator" / "references" / "card-schema.md").read_text(encoding="utf-8"):
        fail("card schema is missing the bilingual fiction disclosure")


def check_license_and_readmes() -> None:
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    if "MIT License" not in license_text or "Copyright (c) 2026 WANG ZHEN" not in license_text:
        fail("LICENSE does not match the declared MIT author metadata")
    for readme in (ROOT / "README.md", ROOT / "README.zh-CN.md"):
        text = readme.read_text(encoding="utf-8")
        if EXPECTED["repository"] not in text:
            fail(f"{readme.name} does not contain the canonical repository URL")
        if "examples/meeting-room-paper-cup.svg" not in text:
            fail(f"{readme.name} does not reference the generated example card")


def check_examples() -> None:
    renderer = load_renderer()
    inputs = sorted((ROOT / "examples").glob("*.json"))
    if len(inputs) != 6:
        fail(f"expected 6 public examples, found {len(inputs)}")
    tones: set[str] = set()
    chinese_examples = 0
    for input_path in inputs:
        data = json.loads(input_path.read_text(encoding="utf-8"))
        tones.add(str(data.get("tone", "")))
        chinese_examples += bool(re.search(r"[\u3400-\u9fff]", str(data.get("artifact_name", ""))))
        image_path = Path(str(data.get("image_path", "")))
        if image_path.is_absolute() or image_path.parts[:1] != ("scenes",):
            fail(f"example image_path must be a portable scenes/ path: {input_path.name}")
        scene_path = input_path.parent / image_path
        if not scene_path.is_file():
            fail(f"missing generated scene: {scene_path.relative_to(ROOT)}")
        if data.get("scene_source") != "AI-generated from text for this repository; see examples/SOURCES.md":
            fail(f"missing scene provenance: {input_path.name}")
        rendered = renderer.render(data, base_dir=input_path.parent)
        output_path = input_path.with_suffix(".svg")
        if not output_path.is_file():
            fail(f"missing generated example: {output_path.relative_to(ROOT)}")
        if output_path.read_text(encoding="utf-8") != rendered:
            fail(f"stale generated example: {output_path.relative_to(ROOT)}")
        if "AI-ASSISTED FICTION · AI辅助虚构内容" not in rendered:
            fail(f"missing disclosure in {output_path.relative_to(ROOT)}")
        card_path = ROOT / "examples" / "cards" / f"{input_path.stem}.png"
        if not card_path.is_file():
            fail(f"missing final PNG card: {card_path.relative_to(ROOT)}")
        payload = card_path.read_bytes()
        if payload[:8] != b"\x89PNG\r\n\x1a\n" or len(payload) < 24:
            fail(f"invalid PNG card: {card_path.relative_to(ROOT)}")
        if struct.unpack(">II", payload[16:24]) != (1080, 1440):
            fail(f"wrong PNG card dimensions: {card_path.relative_to(ROOT)}")
    if tones != {"deadpan", "tender", "absurd"}:
        fail("gallery must cover deadpan, tender, and absurd tones")
    if chinese_examples != 3:
        fail(f"gallery must contain 3 Chinese and 3 English examples, found {chinese_examples} Chinese")
    if not (ROOT / "examples" / "SOURCES.md").is_file():
        fail("example image provenance record is missing")


def check_repository_hygiene() -> None:
    required = [
        ROOT / ".codex-plugin" / "plugin.json",
        ROOT / "LICENSE",
        ROOT / "README.md",
        ROOT / "README.zh-CN.md",
        SKILL_PATH,
        RENDERER_PATH,
    ]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
    if missing:
        fail("missing required files: " + ", ".join(missing))
    ignored = (ROOT / ".gitignore").read_text(encoding="utf-8").splitlines()
    if "output/" not in ignored:
        fail("local trial output must remain excluded from the public repository")
    placeholder_marker = "[TO" + "DO:"
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".md", ".json", ".py", ".yaml", ".yml"}:
            if placeholder_marker in path.read_text(encoding="utf-8"):
                fail(f"unfinished placeholder in {path.relative_to(ROOT)}")


def main() -> int:
    checks = [
        ("plugin metadata", check_plugin),
        ("skill metadata", check_skill),
        ("license and readmes", check_license_and_readmes),
        ("generated examples", check_examples),
        ("repository hygiene", check_repository_hygiene),
    ]
    for label, check in checks:
        check()
        print(f"ok: {label}")
    print("release validation passed")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"release validation failed: {error}", file=sys.stderr)
        raise SystemExit(1)
