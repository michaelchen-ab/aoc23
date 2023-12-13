import sys

file = open(sys.argv[1]).read().strip()
lines = [line for line in file.split("\n")]

grids = file.split("\n\n")
grids = [g.split("\n") for g in grids]


def count_diff(a: str, b: str):
    return sum(1 for i, j in zip(a, b) if i != j)


def check_rows(grid: list[str]):
    SMUDGE_REQ = 1  # 0 for part 1
    # 0: [(0,1)]
    # 1: [(1,2),(0,3)]
    # 2: [(2,3),(1,4),(0,5)]
    # 3: [(3,4),(2,5),(1,6),(0,7)]
    for i in range(len(grid) - 1):
        s = i * 2 + 1
        smudges = sum(
            count_diff(grid[j], grid[s - j]) for j in range(i + 1) if s - j < len(grid)
        )
        if smudges == SMUDGE_REQ:
            return i + 1


def check_cols(grid: list[str]):
    transposed = list(zip(*grid))
    return check_rows(transposed)


total = 0
for g in grids:
    row = check_rows(g)
    if row:
        total += 100 * row
    else:
        col = check_cols(g)
        if col:
            total += col
print(total)
