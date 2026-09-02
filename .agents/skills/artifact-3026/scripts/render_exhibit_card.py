#!/usr/bin/env python3
"""Render a future-museum exhibit JSON record as a self-contained SVG card."""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import mimetypes
import re
import unicodedata
from pathlib import Path
from xml.sax.saxutils import escape


WIDTH = 1080
HEIGHT = 1440
DEFAULT_ACCENT = "#A7432B"
REQUIRED = ("artifact_name", "object_identity", "interpretation", "curator_note")
TEXT_RIGHT_EDGE = 992


def visual_width(text: str) -> int:
    return sum(2 if unicodedata.east_asian_width(char) in "WFA" else 1 for char in text)


def wrap_text(text: str, limit: int) -> list[str]:
    if limit < 1:
        raise ValueError("wrap limit must be positive")
    lines: list[str] = []
    closing_punctuation = set("，。！？；：、）》】〕〉”’」』")
    opening_punctuation = set("（《【〔〈“‘「『")
    for paragraph in str(text).splitlines() or [""]:
        remaining = paragraph.strip()
        while visual_width(remaining) > limit:
            cut = 1
            while cut < len(remaining) and visual_width(remaining[: cut + 1]) <= limit:
                cut += 1

            # Prefer a nearby Latin word boundary, but do not waste most of a
            # line when a short Latin fragment is followed by continuous CJK.
            nearby_spaces = [
                index for index, char in enumerate(remaining[:cut])
                if char.isspace() and visual_width(remaining[:index]) >= limit * 0.6
            ]
            if nearby_spaces:
                cut = nearby_spaces[-1]

            # Keep closing CJK punctuation from beginning a new line and
            # opening punctuation from being stranded at the end of one.
            while cut > 1 and cut < len(remaining) and remaining[cut] in closing_punctuation:
                cut -= 1
            while cut > 1 and remaining[cut - 1] in opening_punctuation:
                cut -= 1

            line = remaining[:cut].rstrip()
            if not line:
                line = remaining[:cut]
            lines.append(line)
            remaining = remaining[cut:].lstrip()
        if remaining:
            lines.append(remaining)
    return lines or [""]


def estimated_text_width(text: str, font_size: int) -> float:
    """Return a conservative cross-platform width estimate in SVG pixels.

    Full-width CJK glyphs are treated as one em. Latin and narrow punctuation
    receive 0.50 em, which leaves safety margin over their observed average
    width in the configured font stack without rejecting valid Latin titles.
    """
    return sum(
        font_size if unicodedata.east_asian_width(char) in "WFA" else font_size * 0.50
        for char in text
    )


def svg_text_lines(
    text: str,
    x: int,
    y: int,
    line_height: int,
    limit: int,
    font_size: int,
    role: str,
    attributes: str,
    right_edge: int = TEXT_RIGHT_EDGE,
) -> tuple[str, int]:
    lines = wrap_text(text, limit)
    overflow = [line for line in lines if x + estimated_text_width(line, font_size) > right_edge]
    if overflow:
        raise ValueError("wrapped text exceeds the card's right edge")
    elements = "".join(
        f'<text data-role="{role}" data-line="{index}" x="{x}" '
        f'y="{y + index * line_height}" {attributes}>{escape(line)}</text>'
        for index, line in enumerate(lines)
    )
    return elements, y + len(lines) * line_height


def image_data_uri(path_value: str | None, base_dir: Path | None = None) -> str | None:
    if not path_value:
        return None
    path = Path(path_value).expanduser()
    if not path.is_absolute() and base_dir is not None:
        path = base_dir / path
    path = path.resolve()
    if not path.is_file():
        raise FileNotFoundError(f"image_path does not exist: {path}")
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    if mime not in {"image/png", "image/jpeg", "image/gif", "image/webp", "image/svg+xml"}:
        raise ValueError(f"unsupported image type: {mime}")
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def accession_number(data: dict[str, object]) -> str:
    supplied = str(data.get("accession_no", "")).strip()
    if supplied:
        return supplied
    year = str(data.get("future_year", "3026"))
    seed = "|".join(str(data.get(key, "")) for key in REQUIRED)
    suffix = int(hashlib.sha256(seed.encode("utf-8")).hexdigest()[:8], 16) % 10000
    return f"FM-{year}-{suffix:04d}"


def checked_accent(value: object) -> str:
    accent = str(value or DEFAULT_ACCENT)
    return accent if re.fullmatch(r"#[0-9A-Fa-f]{6}", accent) else DEFAULT_ACCENT


def render(data: dict[str, object], base_dir: Path | None = None) -> str:
    missing = [key for key in REQUIRED if not str(data.get(key, "")).strip()]
    if missing:
        raise ValueError("missing required fields: " + ", ".join(missing))

    accent = checked_accent(data.get("accent"))
    museum = str(data.get("museum_name") or "MUSEUM OF EVERYDAY ANTIQUITIES").upper()
    year = str(data.get("future_year") or "3026")
    artifact = str(data["artifact_name"])
    identity = str(data["object_identity"])
    interpretation = str(data["interpretation"])
    note = str(data["curator_note"])
    accession = accession_number(data)
    image_uri = image_data_uri(
        str(data.get("image_path")) if data.get("image_path") else None,
        base_dir=base_dir,
    )

    title_lines, title_end = svg_text_lines(
        artifact, 86, 812, 74, 27, 61, "artifact-title",
        'class="serif" font-size="61" font-weight="700" fill="#201D19"',
    )
    identity_lines, identity_end = svg_text_lines(
        identity, 88, title_end + 18, 36, 52, 24, "object-identity",
        'font-size="24" fill="#70685D"',
    )
    body_lines, body_end = svg_text_lines(
        interpretation, 88, identity_end + 54, 43, 55, 31, "interpretation",
        'class="serif" font-size="31" fill="#28231E"',
    )
    note_lines, note_end = svg_text_lines(
        note, 88, body_end + 34, 39, 58, 27, "curator-note",
        f'class="serif" font-size="27" font-style="italic" fill="{accent}"',
    )
    if note_end > 1328:
        raise ValueError("card copy is too long; shorten the interpretation or curator_note")

    if image_uri:
        visual = (
            '<clipPath id="photo-clip"><rect x="58" y="174" width="964" height="478" rx="8"/></clipPath>'
            f'<image href="{image_uri}" x="58" y="174" width="964" height="478" '
            'preserveAspectRatio="xMidYMid slice" clip-path="url(#photo-clip)"/>'
        )
    else:
        monogram = escape(next((char for char in artifact if not char.isspace()), "?"))
        visual = (
            f'<rect x="58" y="174" width="964" height="478" rx="8" fill="#E8E0D2"/>'
            f'<circle cx="540" cy="405" r="148" fill="{accent}" opacity="0.08"/>'
            f'<text x="540" y="488" text-anchor="middle" class="monogram" fill="{accent}">{monogram}</text>'
        )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">
  <title>{escape(artifact)} — Future Museum exhibit card</title>
  <rect width="1080" height="1440" fill="#F5F0E7"/>
  <rect x="34" y="34" width="1012" height="1372" rx="10" fill="none" stroke="#C7BBA8" stroke-width="2"/>
  <style>
    text {{ font-family: "Noto Sans CJK SC", "PingFang SC", "Helvetica Neue", Arial, sans-serif; }}
    .serif {{ font-family: "Noto Serif CJK SC", "Songti SC", Georgia, serif; }}
    .monogram {{ font-family: "Noto Serif CJK SC", "Songti SC", Georgia, serif; font-size: 270px; font-weight: 700; }}
  </style>
  <text x="58" y="98" font-size="22" font-weight="700" letter-spacing="2.4" fill="{accent}">{escape(museum)}</text>
  <text x="1022" y="98" text-anchor="end" font-size="19" fill="#756C60">ARCHIVE / {escape(year)}</text>
  {visual}
  {title_lines}
  {identity_lines}
  <rect x="88" y="{identity_end + 18}" width="82" height="5" fill="{accent}"/>
  {body_lines}
  {note_lines}
  <line x1="88" y1="1330" x2="992" y2="1330" stroke="#C7BBA8" stroke-width="2"/>
  <text x="88" y="1372" font-size="18" letter-spacing="1.2" fill="#756C60">{escape(accession)}</text>
</svg>
'''


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="UTF-8 exhibit JSON file")
    parser.add_argument("--output", type=Path, required=True, help="output SVG path")
    args = parser.parse_args()
    data = json.loads(args.input.read_text(encoding="utf-8"))
    svg = render(data, base_dir=args.input.parent)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(svg, encoding="utf-8")
    print(args.output.resolve())


if __name__ == "__main__":
    main()
