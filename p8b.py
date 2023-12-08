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
rounds_agg = []
for pos in poses:
    for rounds in itertools.count(1):
        for step in instruction:
            pos = mapp[pos][step]
        if pos.endswith("Z"):
            rounds_agg.append(rounds)
            break

print(len(instruction) * math.lcm(*rounds_agg))
