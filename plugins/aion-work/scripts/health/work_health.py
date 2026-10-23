#!/usr/bin/env python3
"""Read-only folder diagnostics for AION WORK. Python 3.10+, standard library only."""

import argparse
import codecs
from collections import Counter
from datetime import datetime, timezone
import html
import json
import os
from pathlib import Path
import re
import stat
import sys
import time
from urllib.parse import unquote, urlsplit

VERSION = 1
SKIP = {".git", "aion_local", ".ssh", ".aws", ".azure", ".gnupg", ".kube", ".codex", ".claude", ".agents", "node_modules", ".venv", "venv", "__pycache__", ".next"}
BINARY = {".pdf", ".zip", ".gz", ".bz2", ".xz", ".7z", ".rar", ".png", ".jpg", ".jpeg", ".webp", ".gif", ".mp4", ".mov", ".mp3", ".wav", ".sqlite", ".db", ".parquet", ".docx", ".xlsx", ".pptx", ".exe", ".dll", ".so", ".dylib", ".wasm", ".bin"}
MAX_ENTRIES = 100000
MAX_FINDINGS = 200
MAX_MARKDOWN = 2 * 1024 * 1024
MAX_READ = 64 * 1024 * 1024
MAX_LINKS = 20000
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
DEFINITION = re.compile(r"^ {0,3}\[([^\]\n]+)\]:\s*(.*)$")
LINK = re.compile(r"!?\[((?:\\.|[^\]\\\n])*)\](\(|\[([^\]\n]*)\])")
REFERENCE = re.compile(r"(?<!!)\[([^\]\n]+)\](?![\[(])")


def hidden(part):
    return part.casefold() in SKIP or part.casefold().startswith(".env")


def linked(info):
    return stat.S_ISLNK(info.st_mode) or bool(getattr(info, "st_file_attributes", 0) & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0))


def identity(info):
    return info.st_dev, info.st_ino, info.st_size, info.st_mtime_ns


def normalize_label(label):
    return " ".join(label.split()).casefold()


def destination(value):
    value = value.lstrip()
    if value.startswith("<"):
        end = value.find(">")
        return value[1:end] if end >= 0 else None
    depth = 0
    result = []
    escaped = False
    for character in value:
        if escaped:
            result.append(character)
            escaped = False
            continue
        if character == "\\":
            escaped = True
            continue
        if character == "(":
            depth += 1
        if character == ")" and depth == 0:
            break
        if character.isspace() and depth == 0:
            break
        if character == ")":
            depth -= 1
        result.append(character)
    return "".join(result) if depth == 0 and not escaped else None


def prose_lines(text):
    """Bounded Markdown subset: skip fenced/indented code and inline code spans."""
    fence = None
    for number, line in enumerate(text.splitlines(), 1):
        if len(line) > 16384:
            continue
        match = FENCE.match(line)
        if fence:
            fence = close_fence(fence, match)
            continue
        if match:
            fence = match.group(1)
            continue
        if line.startswith(("    ", "\t")):
            continue
        yield number, re.sub(r"(`+)(?!`)(.*?)\1(?!`)", "", line)


def close_fence(fence, match):
    if match and match.group(1)[0] == fence[0] and len(match.group(1)) >= len(fence) and not match.group(2).strip():
        return None
    return fence


def markdown_links(text):
    lines = list(prose_lines(text))
    definitions = {}
    for _, line in lines:
        add_definition(definitions, line)
    for number, line in lines:
        if DEFINITION.match(line):
            continue
        yield from line_links(line, number, definitions)


def add_definition(definitions, line):
    match = DEFINITION.match(line)
    if match:
        definitions.setdefault(normalize_label(match.group(1)), destination(match.group(2)))


def line_links(line, number, definitions):
    masked = list(line)
    for match in LINK.finditer(line):
        target = link_target(line, match, definitions)
        yield number, target
        masked[match.start():match.end()] = " " * (match.end() - match.start())
    for match in REFERENCE.finditer("".join(masked)):
        label = normalize_label(match.group(1))
        if label in definitions:
            yield number, definitions[label]


def link_target(line, match, definitions):
    if match.group(2) == "(":
        tail = line[match.end():]
        return destination(tail) if ")" in tail else None
    return definitions.get(normalize_label(match.group(3) or match.group(1)))


class Health:
    def __init__(self, args):
        self.root = args.root.resolve(strict=True)
        if not self.root.is_dir():
            raise ValueError("directory_required")
        self.args = args
        self.deadline = time.monotonic() + 30
        self.previous = self.baseline()
        self.result = {
            "schemaVersion": VERSION, "root": str(self.root),
            "createdAt": datetime.now(timezone.utc).isoformat(),
            "complete": True, "readOnly": True, "networkUsed": False,
            "thresholds": {"binaryBytes": args.binary_mib * 1024 * 1024, "markdownBytes": args.markdown_kib * 1024, "growthBytes": args.growth_kib * 1024},
            "entriesScanned": 0, "files": 0, "bytes": 0, "bytesRead": 0,
            "largestFiles": [], "markdown": [], "findings": [], "findingCounts": {},
            "findingsTruncated": False, "skippedEntries": [], "skippedEntriesCount": 0,
            "links": {"checked": 0, "broken": 0, "skipped": 0, "syntax": "single-line-markdown-inline-images-and-references", "anchorsChecked": False},
        }

    def baseline(self):
        if not self.args.baseline:
            return {}
        with self.args.baseline.open("rb") as handle:
            raw = handle.read(4 * 1024 * 1024 + 1)
        if len(raw) > 4 * 1024 * 1024:
            raise ValueError("baseline_too_large")
        data = json.loads(raw)
        if not isinstance(data, dict) or data.get("schemaVersion") != VERSION or data.get("root") != str(self.root):
            raise ValueError("baseline_scope_mismatch")
        items = data.get("markdown")
        if not isinstance(items, list) or not all(valid_measurement(item) for item in items):
            raise ValueError("invalid_baseline")
        return {item["path"]: item for item in items}

    def finding(self, code, path, **details):
        counts = self.result["findingCounts"]
        counts[code] = counts.get(code, 0) + 1
        if len(self.result["findings"]) < MAX_FINDINGS:
            self.result["findings"].append({"code": code, "path": path, **details})
            return
        self.result["findingsTruncated"] = True

    def incomplete(self, code, path):
        self.result["complete"] = False
        self.finding(code, path)

    def relative(self, path):
        return path.relative_to(self.root).as_posix()

    def path_info(self, path):
        relative = path.relative_to(self.root)
        current = self.root
        if linked(current.lstat()):
            raise ValueError("linked_root_not_followed")
        for part in relative.parts:
            current = current / part
            info = current.lstat()
            if linked(info):
                raise ValueError("linked_path_not_followed")
        return path.lstat()

    def read(self, path, limit):
        before = self.path_info(path)
        if not stat.S_ISREG(before.st_mode):
            raise ValueError("special_file_not_read")
        remaining = MAX_READ - self.result["bytesRead"]
        if remaining <= 0:
            raise ValueError("read_budget_exceeded")
        amount = min(limit, remaining)
        flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0)
        with os.fdopen(os.open(path, flags), "rb") as handle:
            if identity(os.fstat(handle.fileno())) != identity(before):
                raise ValueError("file_changed")
            data = handle.read(amount)
            if identity(os.fstat(handle.fileno())) != identity(before):
                raise ValueError("file_changed")
        self.result["bytesRead"] += len(data)
        return data, before.st_size

    def scan(self):
        pending = [self.root]
        while pending:
            if time.monotonic() >= self.deadline or self.result["entriesScanned"] >= MAX_ENTRIES:
                self.incomplete("scan_limit", ".")
                break
            self.directory(pending.pop(), pending)
        return self.result

    def directory(self, path, pending):
        try:
            self.path_info(path)
            with os.scandir(path) as entries:
                self.directory_entries(entries, pending)
        except (OSError, ValueError):
            self.incomplete("directory_unreadable_or_linked", self.relative(path))

    def directory_entries(self, entries, pending):
        for entry in entries:
            if time.monotonic() >= self.deadline or self.result["entriesScanned"] >= MAX_ENTRIES:
                self.incomplete("scan_limit", ".")
                return
            self.result["entriesScanned"] += 1
            self.inspect(entry, pending)

    def inspect(self, entry, pending):
        path = Path(entry.path)
        try:
            self.inspect_info(path, entry.stat(follow_symlinks=False), pending)
        except (OSError, ValueError):
            self.incomplete("file_unreadable_or_changed", self.relative(path))

    def inspect_info(self, path, info, pending):
        relative = self.relative(path)
        if hidden(path.name):
            self.skip(relative)
            return
        if linked(info) or not (stat.S_ISDIR(info.st_mode) or stat.S_ISREG(info.st_mode)):
            self.incomplete("linked_or_special_entry_skipped", relative)
            return
        if stat.S_ISDIR(info.st_mode):
            pending.append(path)
            return
        self.result["files"] += 1
        self.result["bytes"] += info.st_size
        self.result["largestFiles"] = sorted([*self.result["largestFiles"], {"path": relative, "bytes": info.st_size}], key=lambda item: (-item["bytes"], item["path"]))[:20]
        if path.suffix.casefold() in {".md", ".markdown", ".mdx"}:
            self.markdown(path, info)
            return
        if info.st_size >= self.result["thresholds"]["binaryBytes"]:
            self.large_file(path, info)

    def skip(self, path):
        self.result["skippedEntriesCount"] += 1
        if len(self.result["skippedEntries"]) < 50:
            self.result["skippedEntries"].append(path)

    def large_file(self, path, info):
        if path.suffix.casefold() in BINARY:
            self.finding("large_binary", self.relative(path), bytes=info.st_size, classification="extension")
            return
        data, _ = self.read(path, 8192)
        binary = b"\0" in data
        try:
            codecs.getincrementaldecoder("utf-8")().decode(data, final=False)
        except UnicodeDecodeError:
            binary = True
        self.finding("large_binary" if binary else "large_file", self.relative(path), bytes=info.st_size, classification="sample")

    def markdown(self, path, info):
        relative = self.relative(path)
        if len(self.result["markdown"]) >= 5000:
            self.incomplete("markdown_count_limit", relative)
            return
        size = info.st_size
        item = {"path": relative, "bytes": size, "readBytes": 0, "contentComplete": False}
        self.result["markdown"].append(item)
        self.growth(item)
        if size >= self.result["thresholds"]["markdownBytes"]:
            self.finding("large_markdown", relative, bytes=size)
        data, current_size = self.read(path, MAX_MARKDOWN)
        if current_size != size:
            raise ValueError("file_changed")
        text = codecs.getincrementaldecoder("utf-8")().decode(data, final=len(data) == size)
        lines = text.splitlines()
        item.update({"readBytes": len(data), "contentComplete": len(data) == size, "linesRead": len(lines), "longestLineCharacters": max(map(len, lines), default=0)})
        if len(data) < size:
            self.incomplete("markdown_partially_read", relative)
        if any(len(line) > 16384 for line in lines):
            self.incomplete("markdown_long_lines_not_parsed", relative)
        self.repetition(relative, lines)
        for line, href in markdown_links(text):
            if self.result["links"]["checked"] + self.result["links"]["skipped"] >= MAX_LINKS or time.monotonic() >= self.deadline:
                self.incomplete("link_scan_limit", relative)
                break
            self.link(path, line, href)

    def repetition(self, path, lines):
        counts = Counter(line.strip() for line in lines if len(line.strip()) >= 80)
        repeated = sum(count - 1 for count in counts.values() if count >= 3)
        if repeated >= 10:
            self.finding("repeated_markdown_lines", path, duplicateLines=repeated)

    def growth(self, item):
        old = self.previous.get(item["path"])
        if not old:
            return
        delta = item["bytes"] - old["bytes"]
        item["previousBytes"] = old["bytes"]
        item["growthBytes"] = delta
        if delta >= self.args.growth_kib * 1024:
            self.finding("markdown_growth", item["path"], previousBytes=old["bytes"], bytes=item["bytes"], growthBytes=delta)

    def link(self, source, line, href):
        relative = self.relative(source)
        if href is None:
            self.result["links"]["skipped"] += 1
            self.incomplete("unresolved_markdown_link", relative)
            return
        href = html.unescape(href)
        is_file_url = href.lower().startswith("file:")
        external_scheme = re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", href) and not is_file_url
        if not href or href.startswith(("#", "//")) or external_scheme:
            self.result["links"]["skipped"] += 1
            return
        url = urlsplit(href)
        if is_file_url and url.netloc not in ("", "localhost"):
            self.result["links"]["skipped"] += 1
            self.finding("link_outside_scope", relative, line=line)
            return
        raw = unquote(url.path)
        if not raw:
            self.result["links"]["skipped"] += 1
            return
        target = Path(os.path.abspath(source.parent / raw))
        if not target.is_relative_to(self.root):
            self.result["links"]["skipped"] += 1
            self.finding("link_outside_scope", relative, line=line)
            return
        if any(hidden(part) for part in target.relative_to(self.root).parts):
            self.result["links"]["skipped"] += 1
            self.finding("link_to_excluded_path", relative, line=line)
            return
        self.check_target(source, line, target)

    def check_target(self, source, line, target):
        self.result["links"]["checked"] += 1
        try:
            self.path_info(target)
        except (FileNotFoundError, NotADirectoryError):
            self.result["links"]["broken"] += 1
            self.finding("broken_file_link", self.relative(source), line=line, target=self.relative(target))
        except (OSError, ValueError):
            self.incomplete("link_target_not_checked", self.relative(source))


def valid_measurement(item):
    return isinstance(item, dict) and isinstance(item.get("path"), str) and type(item.get("bytes")) is int and item["bytes"] >= 0


def positive(value):
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError("Use a positive integer.")
    return number


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    parser.add_argument("--baseline", type=Path)
    parser.add_argument("--binary-mib", type=positive, default=10)
    parser.add_argument("--markdown-kib", type=positive, default=64)
    parser.add_argument("--growth-kib", type=positive, default=32)
    result = Health(parser.parse_args()).scan()
    print(json.dumps(result, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError, TypeError):
        print(json.dumps({"ok": False, "code": "health_unavailable"}), file=sys.stderr)
        sys.exit(1)
