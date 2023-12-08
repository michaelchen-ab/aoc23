import sys

file = open(sys.argv[1]).read().strip()
lines = file.split("\n")

instruction, steps = file.split("\n\n")

mapp = {}
for s in steps.split("\n"):
    key, _, l, r = s.split()
    l = l[1:-1]
    r = r[:-1]
    mapp[key] = {"L": l, "R": r}

times = 0
pos = "AAA"
while pos != "ZZZ":
    for step in instruction:
        pos = mapp[pos][step]
        times += 1
print(times)
