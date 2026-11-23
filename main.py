"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line (1-200 characters) to /output/entry.txt.
Python standard library only, no network, fully deterministic.
"""

import os
from pathlib import Path

ROAST = (
    "My earbuds case shows 100% while both earbuds are dead, "
    "blinking green like everything is fine: "
    "a power bank that refuses to share."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ROAST + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
