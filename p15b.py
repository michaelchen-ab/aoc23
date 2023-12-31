import re
import sys
from collections import defaultdict

file = open(sys.argv[1]).read().strip()


def hash(x: str):
    val = 0
    for c in x:
        val += ord(c)
        val *= 17
        val %= 256
    return val


boxes = defaultdict(dict)
for seq in file.split(","):
    a, b = re.split("=|-", seq)
    box = hash(a)
    if b:
        boxes[box][a] = int(b)
    else:
        boxes[box].pop(a, None)


t = 0
for box, slots in boxes.items():
    for idx, lens in enumerate(slots.values(), start=1):
        t += (box + 1) * idx * lens
print(t)
