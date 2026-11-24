"""Weird job title entry: vet the badge line, then pin it to the gate output."""
import json
import os
import os.path
import sys

BADGE = "entry.txt"
LANYARD_CAP = 60


def vet(text: str) -> dict:
    plain = " ".join(text.split())
    facts = {
        "title_chars": len(plain),
        "badge_printed": bool(plain),
        "one_badge": text.strip().count(chr(10)) == 0,
        "badge_bytes": len(text.encode("utf-8")),
    }
    facts["lanyard_fits"] = 0 < facts["title_chars"] <= LANYARD_CAP and facts["badge_bytes"] < LANYARD_CAP + 2
    return facts


def pin() -> int:
    with open(BADGE, encoding="utf-8") as slot:
        raw = slot.read()
    facts = vet(raw)
    board = os.environ.get("MAKEFUN_OUTPUT_DIR")
    target_dir = board if board else os.path.join(os.path.dirname(os.path.abspath(BADGE)), "board")
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, BADGE), "wb") as slot:
        slot.write(raw.encode("utf-8"))
    print(json.dumps({"weirdo": "sock-loss-investigator", "facts": facts, "board": target_dir}))
    if not (facts["lanyard_fits"] and facts["badge_printed"] and facts["one_badge"]):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(pin())
