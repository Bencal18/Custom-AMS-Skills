#!/usr/bin/env python3
"""Build one zip file for each skill, ready to upload to an AI tool.

Each zip holds the skill folder itself, for example force-plate.zip holds
force-plate/SKILL.md. The zips go in dist/. The test skill in tests/ is
included, so users can confirm the install works.

Run it from the repository root:

    python3 scripts/build_skill_zips.py
"""

import glob
import os
import subprocess
import zipfile

OUT_DIR = "dist"


def tracked(folder):
    """Return the files git tracks in a folder, so local junk files stay out."""
    out = subprocess.run(["git", "ls-files", "-z", folder],
                         capture_output=True, check=True).stdout.decode("utf-8")
    return sorted(f for f in out.split("\0") if f)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    folders = sorted(os.path.dirname(p) for p in
                     glob.glob("skills/*/SKILL.md") + glob.glob("tests/*/SKILL.md"))
    names = [os.path.basename(f) for f in folders]
    repeated = {n for n in names if names.count(n) > 1}
    if repeated:
        raise SystemExit(f"Two skill folders share a name: {', '.join(sorted(repeated))}")
    for folder in folders:
        name = os.path.basename(folder)
        files = tracked(folder)
        if not files:
            print(f"Skipped {name}: no tracked files. Commit the skill first.")
            continue
        target = os.path.join(OUT_DIR, f"{name}.zip")
        with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
            for path in files:
                archive.write(path, os.path.relpath(path, os.path.dirname(folder)))
        print(f"Built {target} with {len(files)} file{'' if len(files) == 1 else 's'}.")


if __name__ == "__main__":
    main()
