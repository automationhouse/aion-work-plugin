#!/usr/bin/env python3
"""AION WORK content guard. Reads Git objects; never creates commits or publishes work."""

import argparse
import json
import os
from pathlib import Path
import re
import shlex
import stat
import subprocess
import sys
import tempfile
import time

VERSION = "0.1.0"
MAX_OUTPUT = 16 * 1024 * 1024
MAX_BLOB = 5 * 1024 * 1024
MAX_COMMITS = 10000
MAX_ENTRIES = 100000
MAX_SCANNED_BYTES = 128 * 1024 * 1024
OID = re.compile(r"(?:[0-9a-f]{40}|[0-9a-f]{64})\Z")
RULES = {
    "private_key": re.compile(r"-----BEGIN (?:[A-Z0-9]+ )*PRIVATE KEY-----"),
    "github_token": re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})"),
    "aws_key": re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
    "api_token": re.compile(r"\b(?:sk-(?:proj-|svcacct-)?[A-Za-z0-9_-]{24,}|sk_(?:live|test)_[A-Za-z0-9]{16,}|xox[baprs]-[A-Za-z0-9-]{20,})"),
    "credential_url": re.compile(r"\b(?:https?|postgres(?:ql)?|mysql|mongodb(?:\+srv)?|redis)://[^\s/:@]+:[^\s/@]{4,}@", re.I),
    "jwt": re.compile(r"\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}"),
}
ASSIGNMENT = re.compile(
    r'''(?im)^\s*["']?(?:[a-z0-9]+[_-])*(?:password|passwd|api[_-]?key|access[_-]?token|refresh[_-]?token|client[_-]?secret|service[_-]?role[_-]?key|secret[_-]?access[_-]?key)["']?\s*[:=]\s*(?:["']([^"'\r\n]{8,})["']|([^\s"',;}{]{8,}))'''
)
PLACEHOLDERS = ("${", "{{", "process.env.", "os.environ", "os.getenv(", "env(", "your_", "replace_", "example_", "<")


class Blocked(Exception):
    def __init__(self, code, path=None):
        self.code = code
        self.path = path


def require(condition, code, path=None):
    if not condition:
        raise Blocked(code, path)


def valid_oid(value):
    require(bool(OID.fullmatch(value)), "invalid_object_id")
    return value


def is_zero(value):
    return bool(value) and set(value) == {"0"}


class Guard:
    def __init__(self, root):
        self.root = root
        self.deadline = time.monotonic() + 120
        self.seen = set()
        self.scanned_bytes = 0
        self.entries = 0
        self.policy = json.loads(Path(__file__).with_name("policy.json").read_text())
        require(self.policy["version"] == 1, "unsupported_policy")

    def git(self, *args, missing_ok=False):
        require(time.monotonic() < self.deadline, "scan_timeout")
        env = dict(os.environ, GIT_NO_REPLACE_OBJECTS="1", GIT_NO_LAZY_FETCH="1", GIT_TERMINAL_PROMPT="0")
        command = ["git", "--no-pager", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "protocol.allow=never", "-C", str(self.root), *args]
        with tempfile.TemporaryFile() as output:
            result = subprocess.run(command, stdout=output, stderr=subprocess.DEVNULL, env=env, timeout=min(30, max(1, self.deadline - time.monotonic())))
            output.seek(0)
            data = output.read(MAX_OUTPUT + 1)
        require(len(data) <= MAX_OUTPUT, "output_limit")
        if result.returncode and missing_ok:
            return None
        require(result.returncode == 0, "git_read_failed")
        return data

    def path(self, path):
        parts = path.replace("\\", "/").casefold().split("/")
        require(not any(part in {item.casefold() for item in self.policy["blockedComponents"]} for part in parts), "blocked_folder", path)
        require(not any(part.startswith(tuple(self.policy["blockedPrefixes"])) for part in parts), "environment_file", path)
        require(parts[-1] not in self.policy["privateKeyNames"], "private_key_file", path)
        require(not parts[-1].endswith(tuple(self.policy["privateKeySuffixes"])), "private_key_file", path)

    def content(self, data, path):
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            raise Blocked("unscannable_binary", path) from None
        require("\x00" not in text, "unscannable_binary", path)
        require(not text.startswith("version https://git-lfs.github.com/spec/v1"), "unscanned_lfs_content", path)
        for code, pattern in RULES.items():
            require(not pattern.search(text), code, path)
        for match in ASSIGNMENT.finditer(text):
            value = (match.group(1) or match.group(2)).lower()
            require(value.startswith(PLACEHOLDERS), "secret_assignment", path)

    def object(self, oid, kind, path):
        valid_oid(oid)
        if oid in self.seen:
            return
        size = int(self.git("cat-file", "-s", oid))
        require(size <= MAX_BLOB, "file_size_limit", path)
        self.scanned_bytes += size
        require(self.scanned_bytes <= MAX_SCANNED_BYTES, "scan_size_limit")
        self.content(self.git("cat-file", kind, oid), path)
        self.seen.add(oid)

    def entry(self, mode, oid, path):
        self.entries += 1
        require(self.entries <= MAX_ENTRIES, "entry_limit")
        self.path(path)
        require(mode in ("100644", "100755"), "unsupported_file_mode", path)
        self.object(oid, "blob", path)

    def staged(self):
        # Read the actual index (including GIT_INDEX_FILE), never the working file.
        records = self.git("ls-files", "--stage", "-z").split(b"\0")
        for record in filter(None, records):
            self.index_entry(record)

    def index_entry(self, record):
        metadata, raw_path = record.split(b"\t", 1)
        mode, oid, stage = metadata.decode("ascii").split()
        require(stage == "0", "unmerged_index")
        self.entry(mode, oid, raw_path.decode("utf-8"))

    def tree(self, commit):
        for record in filter(None, self.git("ls-tree", "-r", "-z", commit).split(b"\0")):
            self.tree_entry(record)

    def tree_entry(self, record):
        metadata, raw_path = record.split(b"\t", 1)
        mode, kind, oid = metadata.decode("ascii").split()
        require(kind == "blob", "unsupported_file_mode", raw_path.decode("utf-8"))
        self.entry(mode, oid, raw_path.decode("utf-8"))

    def commit_target(self, oid):
        # Inspect annotated tag messages as well as the eventual commit.
        for _ in range(10):
            kind = self.git("cat-file", "-t", oid).decode().strip()
            if kind == "commit":
                return oid
            require(kind == "tag", "unsupported_push_target")
            self.object(oid, "tag", "<tag metadata>")
            first_line = self.git("cat-file", "tag", oid).splitlines()[0].decode()
            require(first_line.startswith("object "), "invalid_tag")
            oid = valid_oid(first_line.removeprefix("object "))
        raise Blocked("tag_depth_limit")

    def update(self, line):
        fields = line.split()
        require(len(fields) == 4, "invalid_push_input")
        _, local, _, remote = fields
        valid_oid(local)
        valid_oid(remote)
        if is_zero(local):
            return
        target = self.commit_target(local)
        arguments = [target]
        remote_commit = self.remote_commit(remote)
        if remote_commit:
            arguments.append("^" + remote_commit)
        revisions = self.git("rev-list", "--max-count=" + str(MAX_COMMITS + 1), *arguments, "--").decode().splitlines()
        require(len(revisions) <= MAX_COMMITS, "history_limit")
        for commit in dict.fromkeys([target, *revisions]):
            self.commit(commit)

    def remote_commit(self, oid):
        if is_zero(oid):
            return None
        value = self.git("rev-parse", "--verify", oid + "^{commit}", missing_ok=True)
        return valid_oid(value.decode().strip()) if value else None

    def commit(self, oid):
        self.object(oid, "commit", "<commit metadata>")
        self.tree(oid)

    def pre_push(self):
        require(not os.environ.get("GIT_GRAFT_FILE"), "grafted_history")
        require(self.git("rev-parse", "--is-shallow-repository").strip() == b"false", "shallow_history")
        grafts = Path(os.fsdecode(self.git("rev-parse", "--git-path", "info/grafts").strip()))
        require(not (self.root / grafts).exists(), "grafted_history")
        raw = sys.stdin.buffer.read(128 * 1024 + 1)
        require(len(raw) <= 128 * 1024, "push_input_limit")
        for line in raw.decode("utf-8").splitlines():
            self.update(line)


def no_links(path):
    for item in [path, *path.parents]:
        require(not item.is_symlink(), "linked_hook_path")
        attributes = getattr(item.lstat(), "st_file_attributes", 0) if item.exists() else 0
        require(not attributes & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0), "linked_hook_path")


def hook_files(guard):
    require(not guard.git("config", "--get", "core.hooksPath", missing_ok=True), "custom_hooks_require_integration")
    raw = os.fsdecode(guard.git("rev-parse", "--git-path", "hooks").strip())
    hooks = guard.root / raw
    no_links(hooks)
    return hooks


def installation(guard):
    hooks = hook_files(guard)
    destination = hooks / "work-guard"
    python = shlex.quote(Path(sys.executable).as_posix())
    script = shlex.quote((destination / "work_guard.py").absolute().as_posix())
    files = {
        destination / "work_guard.py": Path(__file__).read_bytes(),
        destination / "policy.json": Path(__file__).with_name("policy.json").read_bytes(),
        hooks / "pre-commit": f'#!/bin/sh\n# AION WORK content guard {VERSION}\nexec {python} {script} staged\n'.encode(),
        hooks / "pre-push": f'#!/bin/sh\n# AION WORK content guard {VERSION}\nexec {python} {script} pre-push\n'.encode(),
    }
    return files


def status(guard):
    files = installation(guard)
    return all(matches(path, content) for path, content in files.items())


def matches(path, content):
    no_links(path)
    return path.is_file() and path.read_bytes() == content and (path.suffix != "" or os.access(path, os.X_OK))


def install(guard):
    files = installation(guard)
    for path, content in files.items():
        require(not path.exists() or matches(path, content), "existing_hooks_require_integration")
    for path, content in files.items():
        write_new(path, content)
    require(status(guard), "hook_installation_incomplete")


def write_new(path, content):
    no_links(path)
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(content)
    if path.suffix == "":
        path.chmod(0o755)


class Parser(argparse.ArgumentParser):
    def error(self, message):
        raise Blocked("invalid_arguments")


def main():
    parser = Parser(description=__doc__)
    parser.add_argument("command", choices=["staged", "pre-push", "install", "status"])
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    args = parser.parse_args()
    guard = Guard(args.repo.absolute())
    require(guard.git("rev-parse", "--is-inside-work-tree").strip() == b"true", "working_copy_required")
    guard.root = Path(os.fsdecode(guard.git("rev-parse", "--show-toplevel").strip()))
    if args.command == "install":
        install(guard)
    elif args.command == "status":
        require(status(guard), "guard_not_installed")
    elif args.command == "staged":
        guard.staged()
    else:
        guard.pre_push()
    print(json.dumps({"ok": True, "operation": args.command, "policyVersion": guard.policy["version"]}))


if __name__ == "__main__":
    try:
        main()
    except Blocked as error:
        print(json.dumps({"ok": False, "code": error.code, "path": error.path}), file=sys.stderr)
        sys.exit(1)
    except (OSError, ValueError, KeyError, subprocess.SubprocessError):
        # Never echo Git stderr, matched text, credentials or subprocess arguments.
        print(json.dumps({"ok": False, "code": "scan_unavailable"}), file=sys.stderr)
        sys.exit(1)
