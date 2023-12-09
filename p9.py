import sys
import itertools

file = open(sys.argv[1]).read().strip()
lines = file.split("\n")

total = 0
for line in lines:
    rows = [[int(x) for x in line.split()]]
    while any(x != 0 for x in rows[-1]):
        rows.append([b - a for a, b in itertools.pairwise(rows[-1])])
    total += sum(l[-1] for l in rows)
print(total)
