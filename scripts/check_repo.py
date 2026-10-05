#!/usr/bin/env python3
"""Check the repository before a change is merged.

Runs three checks:

1. Links: every relative link and heading anchor in a Markdown file resolves
   to a file in the repository.
2. Skills: every SKILL.md has a valid name that matches its folder, and a
   one-line description under 200 characters.
3. Blocked terms: no file name or file content contains a term listed in the
   BLOCKED_TERMS environment variable. List terms separated by commas. Matching
   ignores case and finds the term anywhere, including inside longer words.

Output never shows a blocked term. Every printed line has blocked terms
replaced with [blocked], and a match is named by the term's position only.

When BLOCKED_TERMS is not set, the blocked-term check is skipped on a local
run, fails on GitHub Actions, and gives a warning on a pull request from a
fork, because GitHub does not pass secrets to those runs.

Run it from the repository root:

    python3 scripts/check_repo.py

Exits with status 1 if any check fails.
"""

import os
import re
import subprocess
import sys
import unicodedata
from urllib.parse import unquote

MAX_DESCRIPTION = 199
NAME_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_PATTERN = re.compile(r"\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)|href=\"([^\"]+)\"")
FENCE_PATTERN = re.compile(r"^ {0,3}(```|~~~).*?^ {0,3}\1", re.S | re.M)

TERMS = [t.strip() for t in os.environ.get("BLOCKED_TERMS", "").split(",") if t.strip()]
TERM_PATTERNS = [re.compile(r"\s+".join(map(re.escape, t.split())), re.I) for t in TERMS]


def redact(text):
    """Replace every blocked term in text with [blocked]."""
    for pattern in TERM_PATTERNS:
        text = pattern.sub("[blocked]", text)
    return text


def tracked_files():
    """Return the files git tracks, plus new files that are not ignored."""
    out = subprocess.run(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
        capture_output=True, check=True,
    ).stdout.decode("utf-8")
    return sorted(f for f in out.split("\0") if f and os.path.isfile(f))


def read_text(path):
    """Return a file's text, or None for a binary file."""
    data = open(path, "rb").read()
    if data.startswith((b"\xff\xfe", b"\xfe\xff")):
        return data.decode("utf-16", errors="replace")
    if b"\0" in data:
        return None
    return data.decode("utf-8", errors="replace")


def slug(heading):
    """Turn a heading into the anchor GitHub generates for it."""
    text = heading.strip().lower()
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    kept = "".join(c for c in text if c.isalnum() or c in "_- "
                   or unicodedata.category(c).startswith("M"))
    return kept.replace(" ", "-")


_anchor_cache = {}


def anchors(path):
    """Return every heading anchor in a Markdown file."""
    if path not in _anchor_cache:
        text = FENCE_PATTERN.sub("", read_text(path) or "")
        seen = {}
        found = set()
        for heading in re.findall(r"^ {0,3}#{1,6} (.*?)#*\s*$", text, re.M):
            base = slug(heading)
            count = seen.get(base, 0)
            found.add(base if count == 0 else f"{base}-{count}")
            seen[base] = count + 1
        _anchor_cache[path] = found
    return _anchor_cache[path]


def check_links(files):
    known = set(files)
    folders = {os.path.dirname(f) for f in files}
    for f in list(folders):
        while f:
            f = os.path.dirname(f)
            folders.add(f)
    errors = []
    for f in files:
        if not f.endswith(".md"):
            continue
        text = FENCE_PATTERN.sub("", read_text(f) or "")
        for match in LINK_PATTERN.finditer(text):
            target = match.group(1) or match.group(2)
            if re.match(r"[a-z]+:", target) or "<" in target:
                continue
            path, _, fragment = target.partition("#")
            path = unquote(path.split("?")[0])
            fragment = unquote(fragment)
            if path.startswith("/"):
                resolved = os.path.normpath(path.lstrip("/"))
            elif path:
                resolved = os.path.normpath(os.path.join(os.path.dirname(f), path))
            else:
                resolved = f
            if resolved not in known and resolved not in folders:
                errors.append(f"{f}: broken link to {target}")
            elif fragment and resolved.endswith(".md") and fragment.lower() not in anchors(resolved):
                errors.append(f"{f}: missing anchor in {target}")
    return errors


def frontmatter(path):
    """Return the top-level fields, and the names of fields that span lines."""
    match = re.match(r"---\n(.*?)\n---\n", read_text(path) or "", re.S)
    if not match:
        return None, set()
    fields = {}
    multiline = set()
    last = None
    for line in match.group(1).splitlines():
        if line[:1] in (" ", "\t"):
            if last:
                multiline.add(last)
            continue
        key, sep, value = line.partition(":")
        if sep:
            last = key.strip()
            fields[last] = value.strip().strip('"')
    return fields, multiline


def check_skills(files):
    errors = []
    skill_files = [f for f in files if f.endswith("/SKILL.md")
                   and f.startswith(("skills/", "tests/"))]
    for f in skill_files:
        folder = os.path.basename(os.path.dirname(f))
        fields, multiline = frontmatter(f)
        if fields is None:
            errors.append(f"{f}: no frontmatter block")
            continue
        name = fields.get("name", "")
        description = fields.get("description", "")
        if name != folder:
            errors.append(f"{f}: name '{name}' does not match folder '{folder}'")
        if not NAME_PATTERN.match(name) or len(name) > 64:
            errors.append(f"{f}: name must be lowercase letters, digits, and single hyphens, at most 64 characters")
        if not description or description[:1] in (">", "|") or "description" in multiline:
            errors.append(f"{f}: description is missing, or not on one line")
        elif len(description) > MAX_DESCRIPTION:
            errors.append(f"{f}: description is {len(description)} characters; keep it under 200")
    return errors


def check_blocked_terms(files):
    if not TERM_PATTERNS:
        return None
    errors = []
    for f in files:
        for index, pattern in enumerate(TERM_PATTERNS, 1):
            if pattern.search(f):
                errors.append(f"{f}: file name contains blocked term {index}")
        text = read_text(f)
        if text is None:
            continue
        for number, line in enumerate(text.splitlines(), 1):
            for index, pattern in enumerate(TERM_PATTERNS, 1):
                if pattern.search(line):
                    errors.append(f"{f}:{number}: contains blocked term {index}")
        for index, pattern in enumerate(TERM_PATTERNS, 1):
            if " " in TERMS[index - 1] and pattern.search(text) and not any(
                    pattern.search(line) for line in text.splitlines()):
                errors.append(f"{f}: contains blocked term {index} across a line break")
    return errors


def blocked_terms_missing():
    """Say what to do when BLOCKED_TERMS is not set. Return True to fail."""
    if os.environ.get("GITHUB_ACTIONS") != "true":
        print("Blocked terms: skipped, because BLOCKED_TERMS is not set.")
        return False
    if os.environ.get("FORK_PR") == "true":
        print("::warning::Blocked terms: skipped on a pull request from a fork. "
              "A maintainer must run the check before merging.")
        return False
    print("Blocked terms: failed, because the BLOCKED_TERMS secret is not set.")
    return True


def main():
    files = tracked_files()
    failed = False
    for label, check in [("Links", check_links), ("Skills", check_skills),
                         ("Blocked terms", check_blocked_terms)]:
        errors = check(files)
        if errors is None:
            failed = blocked_terms_missing() or failed
            continue
        for error in errors:
            print(redact(f"{label}: {error}"))
        if errors:
            failed = True
        else:
            print(f"{label}: passed.")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
