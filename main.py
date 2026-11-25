#!/usr/bin/env python3
"""Two Robots in an Elevator (R2) — one awkward line of robot small talk.

Writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt (UTF-8, 1-200 chars).
Stdlib only. Paths resolve from the environment, never from the cwd.
"""
import os
from pathlib import Path

LINE = (
    "I have never been to the penthouse. Its button is 4.2 centimetres "
    "above my reach, and I am too polite to ask you to press it."
)


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = " ".join(LINE.split())
    if not text or len(text) > 200:
        raise SystemExit(f"entry invalid: {len(text)} chars")
    print(f"entry ok: {len(text)} chars")
    target = out_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
