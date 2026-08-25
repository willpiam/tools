#!/usr/bin/env python3
"""Build emojiData.js from Unicode CLDR annotations and emoji-test groups."""

from __future__ import annotations

import argparse
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "emojiData.js"
DEFAULT_SOURCE = ROOT / "emojiData.js"
EMOJI_TEST_URL = "https://www.unicode.org/Public/17.0.0/emoji/emoji-test.txt"
ANNOTATIONS_URL = (
    "https://raw.githubusercontent.com/unicode-org/cldr/main/common/annotations/en.xml"
)
ANNOTATIONS_DERIVED_URL = (
    "https://raw.githubusercontent.com/unicode-org/cldr/main/common/annotationsDerived/en.xml"
)

EXTRA_ALIASES: dict[str, list[str]] = {
    "🇺🇸": ["usa", "america", "american", "united states"],
    "🇬🇧": ["uk", "britain", "british", "england", "united kingdom"],
    "👋": ["hello", "hi", "wave"],
    "💡": ["idea"],
    "👍": ["thumbsup", "thumbs-up"],
    "🤝": ["deal", "agreement"],
    "🎉": ["party", "celebrate", "celebration"],
    "☕": ["coffee"],
    "🍕": ["pizza"],
    "🐕": ["dog", "puppy"],
    "🐈": ["cat", "kitty"],
}


def fetch_text(url: str, cache_path: Path | None = None) -> str:
    if cache_path and cache_path.is_file():
        return cache_path.read_text(encoding="utf-8")
    with urllib.request.urlopen(url, timeout=60) as response:
        text = response.read().decode("utf-8")
    if cache_path:
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(text, encoding="utf-8")
    return text


def norm_key(value: str) -> str:
    return " ".join(f"{ord(ch):X}" for ch in value if ord(ch) != 0xFE0F)


def zwj_key(value: str) -> str | None:
    codepoints = [ord(ch) for ch in value if ord(ch) != 0xFE0F]
    if len(codepoints) <= 1:
        return None
    parts: list[str] = []
    for index, codepoint in enumerate(codepoints):
        if index:
            parts.append("200D")
        parts.append(f"{codepoint:X}")
    return " ".join(parts)


def lookup_keys(value: str) -> list[str]:
    keys: list[str] = []
    for candidate in (value, value.replace("\uFE0F", ""), norm_key(value), zwj_key(value)):
        if candidate and candidate not in keys:
            keys.append(candidate)
    return keys


def js_escape(value: str) -> str:
    return (
        value.replace("\\", "\\\\")
        .replace("'", "\\'")
        .replace("\n", "\\n")
        .replace("\r", "\\r")
    )


def load_base_rows(source_path: Path) -> list[tuple[str, str]]:
    text = source_path.read_text(encoding="utf-8")
    rows = re.findall(r"\['((?:\\'|[^'])*)','((?:\\'|[^'])*)'(?:,[^]]*)?\]", text)
    if not rows:
        raise SystemExit(f"No emoji rows found in {source_path}")
    return [(char, name) for char, name in rows]


def parse_cldr_keywords(*urls: str, cache_dir: Path | None = None) -> dict[str, list[str]]:
    keywords: dict[str, list[str]] = {}
    for index, url in enumerate(urls):
        cache = cache_dir / f"cldr-{index}.xml" if cache_dir else None
        root = ET.fromstring(fetch_text(url, cache))
        for element in root.findall(".//annotation"):
            if element.get("type") == "tts":
                continue
            cp = element.get("cp")
            if not cp:
                continue
            words = [
                word.strip().lower()
                for word in (element.text or "").split("|")
                if word.strip()
            ]
            if not words:
                continue
            for key in lookup_keys(cp):
                bucket = keywords.setdefault(key, [])
                for word in words:
                    if word not in bucket:
                        bucket.append(word)
    return keywords


def parse_emoji_test(text: str) -> dict[str, tuple[str, str]]:
    group = ""
    subgroup = ""
    meta: dict[str, tuple[str, str]] = {}
    line_re = re.compile(r"#\s*(\S+)\s+E[\d.]+\s+(.+)$")

    for line in text.splitlines():
        if line.startswith("# group:"):
            group = line.split(":", 1)[1].strip()
            continue
        if line.startswith("# subgroup:"):
            subgroup = line.split(":", 1)[1].strip()
            continue
        if line.startswith("#") or ";" not in line:
            continue

        status = line.split(";", 1)[1].strip().split()[0]
        if status not in {"fully-qualified", "component"}:
            continue

        match = line_re.search(line)
        if not match:
            continue

        emoji = match.group(1)
        for key in lookup_keys(emoji):
            meta[key] = (group, subgroup)

    return meta


def lookup_keywords(char: str, keyword_map: dict[str, list[str]]) -> list[str]:
    words: list[str] = []
    for key in lookup_keys(char):
        for word in keyword_map.get(key, []):
            if word not in words:
                words.append(word)
    for word in EXTRA_ALIASES.get(char, []):
        lowered = word.lower()
        if lowered not in words:
            words.append(lowered)
    return words


def lookup_group(char: str, group_map: dict[str, tuple[str, str]]) -> tuple[str, str]:
    for key in lookup_keys(char):
        if key in group_map:
            return group_map[key]
    return ("", "")


def build_rows(
    base_rows: list[tuple[str, str]],
    keyword_map: dict[str, list[str]],
    group_map: dict[str, tuple[str, str]],
) -> list[list[str]]:
    output: list[list[str]] = []
    for char, name in base_rows:
        keywords = lookup_keywords(char, keyword_map)
        group, subgroup = lookup_group(char, group_map)
        output.append([char, name, "|".join(keywords), group, subgroup])
    return output


def write_emoji_data(rows: list[list[str]], out_path: Path) -> None:
    lines = [
        "/** Auto-generated by scripts/build-emoji-data.py — do not edit by hand. */",
        "window.EMOJI_DATA = [",
    ]
    for char, name, keywords, group, subgroup in rows:
        lines.append(
            "  ['"
            + js_escape(char)
            + "','"
            + js_escape(name)
            + "','"
            + js_escape(keywords)
            + "','"
            + js_escape(group)
            + "','"
            + js_escape(subgroup)
            + "'],"
        )
    lines.append("];")
    lines.append("")
    tmp_path = out_path.with_suffix(out_path.suffix + ".tmp")
    tmp_path.write_text("\n".join(lines), encoding="utf-8")
    tmp_path.replace(out_path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source",
        type=Path,
        default=DEFAULT_SOURCE,
        help="Existing emojiData.js used to preserve emoji characters and display names",
    )
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=ROOT / "scripts" / "cache",
        help="Optional directory for downloaded Unicode/CLDR source files",
    )
    args = parser.parse_args()

    cache_dir = args.cache_dir
    base_rows = load_base_rows(args.source)
    keyword_map = parse_cldr_keywords(
        ANNOTATIONS_URL,
        ANNOTATIONS_DERIVED_URL,
        cache_dir=cache_dir,
    )
    emoji_test = fetch_text(
        EMOJI_TEST_URL,
        cache_dir / "emoji-test.txt" if cache_dir else None,
    )
    group_map = parse_emoji_test(emoji_test)
    rows = build_rows(base_rows, keyword_map, group_map)
    write_emoji_data(rows, args.out)

    missing_keywords = sum(1 for row in rows if not row[2])
    missing_groups = sum(1 for row in rows if not row[3])
    print(
        f"Wrote {len(rows)} rows to {args.out} "
        f"({missing_keywords} without keywords, {missing_groups} without groups)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
