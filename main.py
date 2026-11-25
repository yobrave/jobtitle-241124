import json
import os
from pathlib import Path

BAR = 60
BRAND = "jbt-r2-auditor"
CARD = {"shift": "night", "coin": "two-headed", "form": "1099-N"}


def comb(panel):
    rows = [r.strip() for r in panel.read_text(encoding="utf-8").splitlines() if r.strip()]
    if len(rows) != 1:
        raise SystemExit("exactly one title wanted on the card")
    if len(rows[0]) > BAR:
        raise SystemExit(f"title is {len(rows[0])} wide, badge holds {BAR}")
    return rows[0]


def post(line, shell):
    shell.mkdir(parents=True, exist_ok=True)
    out = shell / "entry.txt"
    ink = line.encode("utf-8")
    out.write_bytes(ink)
    assert out.read_bytes() == ink, "posted card came back different"
    return out


def main():
    root = Path(__file__).resolve().parent
    line = comb(root / "entry.txt")
    env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    shell = Path(env) if env else root / "output"
    out = post(line, shell)
    print(json.dumps({"title_ok": True, "n": len(line), "bar": BAR, "out": str(out), "shift": CARD["shift"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
