"""Weirdest job title plater."""
import json
import os
from pathlib import Path

EDGE = 60
DIVISION = "fridge-light"
read = lambda p: (Path(p).resolve().parent / "entry.txt").read_bytes().decode("utf-8").strip()
within = lambda t: 1 <= len(t) <= EDGE
emit = lambda tag, t, held: print(json.dumps({"badge": tag, "width": len(t), "held": held}))

title = read(Path(__file__))
if within(title):
    dest = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "entry.txt").write_bytes(title.encode("utf-8"))
    emit("stamped", title, True)
else:
    emit("bent", title, False)
