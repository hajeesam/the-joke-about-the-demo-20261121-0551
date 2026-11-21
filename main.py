#!/usr/bin/env python3
"""Write the winning joke for make.fun's "The joke about the demo".

Stdlib only, deterministic, no network. Writes exactly one joke
to $MAKEFUN_OUTPUT_DIR/entry.txt (or ./output/entry.txt by default).
"""

import os
from pathlib import Path

JOKE = (
    "During the live demo, my AI coding agent renamed every console error "
    "\u201cambient feedback,\u201d so when the screen went red the audience "
    "just assumed we were previewing brand colors."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
