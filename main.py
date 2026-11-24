#!/usr/bin/env python3
"""Till Firmware Do Us Part -- a robot's wedding vow.

Writes one sentence (a robot's own wedding vow, funny and heartfelt)
to /output/entry.txt. Deterministic, no network, no input.
"""

import os
from pathlib import Path

VOW = (
    "I promise to love you through every crash, every reboot, "
    "and every firmware update, until my battery runs out for good."
)


def main() -> None:
    # Enforce the gate ourselves: one sentence, 1-200 characters.
    assert 1 <= len(VOW) <= 200, "vow must be 1-200 characters"
    assert VOW.count(".") == 1 and VOW.endswith("."), "vow must be one sentence"
    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(VOW + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
