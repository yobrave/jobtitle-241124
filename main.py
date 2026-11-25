# Weirdest job title: 60-char gate, ship + json line (round 4).
import json
import pathlib

MAX_N = 60
RUN_ID = "jbt4-jobtitle-r4"


def guarded(value, floor=1, top=MAX_N):
    return floor <= len(value) <= top and value.strip() != ""


def forward():
    value = pathlib.Path("entry.txt").read_text(encoding="utf-8").strip()
    if not guarded(value):
        print(json.dumps({"run": RUN_ID, "ok": False, "n": len(value)}))
        return
    pathlib.Path("out").mkdir(exist_ok=True)
    pathlib.Path("out/entry.txt").write_bytes((value + "\n").encode("utf-8"))
    print(json.dumps({"run": RUN_ID, "ok": True, "n": len(value), "top": MAX_N}))


forward()
