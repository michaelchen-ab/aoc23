import sys
from collections import defaultdict, OrderedDict

file = open(sys.argv[1]).read().strip()


def hash(x: str):
    val = 0
    for c in x:
        val += ord(c)
        val *= 17
        val %= 256
    return val


boxes = defaultdict(OrderedDict)
for seq in file.split(","):
    arr = seq.split("=")
    if len(arr) == 2:
        a, b = arr
        box = hash(a)
        boxes[box][a] = int(b)
    else:
        a = seq[:-1]
        box = hash(a)
        boxes[box].pop(a, None)


t = 0
for box, slots in boxes.items():
    for idx, lens in enumerate(slots.values(), start=1):
        t += (box + 1) * idx * lens
print(t)
