import sys
import math
import itertools

file = open(sys.argv[1]).read().strip()
lines = file.split("\n")

instruction, steps = file.split("\n\n")

mapp = {}
for s in steps.split("\n"):
    key, _, l, r = s.split()
    l = l[1:-1]
    r = r[:-1]
    mapp[key] = {"L": l, "R": r}

poses = [k for k in mapp if k.endswith("A")]
times_agg = []
for pos in poses:
    times = 0
    while not pos.endswith("Z"):
        for step in instruction:
            pos = mapp[pos][step]
            times += 1
    times_agg.append(times)

print(math.lcm(*times_agg))
