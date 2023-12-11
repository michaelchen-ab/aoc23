import sys
import itertools

file = open(sys.argv[1]).read().strip()
lines = [list(line) for line in file.split("\n")]

empty_rows = []
for i in range(len(lines) - 1, -1, -1):
    line = lines[i]
    if all(c == "." for c in line):
        empty_rows.append(i)

empty_cols = []
for j in range(len(lines[0]) - 1, -1, -1):
    col = [line[j] for line in lines]
    if all(c == "." for c in col):
        empty_cols.append(j)

stars = [
    (i, j) for i, line in enumerate(lines) for j, char in enumerate(line) if char == "#"
]
mult = 1_000_000  # 1 for part 1
total = 0
for (a, b), (c, d) in itertools.combinations(stars, 2):
    empty_c = sum(1 for col in empty_cols if b < col < d or d < col < b)
    empty_r = sum(1 for row in empty_rows if a < row < c or c < row < a)
    total += abs(a - c) + abs(b - d) + (mult - 1) * (empty_c + empty_r)
print(total)
