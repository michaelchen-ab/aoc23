import sys

Pos = tuple[int, int]
Dir = tuple[int, int]
State = tuple[Pos, Dir, int]

file = open(sys.argv[1]).read().strip()
lines = [list(line) for line in file.split("\n")]

I = len(lines)
J = len(lines[0])

pos = next((0, j) for j, c in enumerate(lines[0]) if c == ".")
frontier: list[tuple[Pos, Pos, int]] = [(pos, pos, 0)]
goal_dist = -1

while frontier:
    node, prev_node, dist = frontier.pop()
    if node[0] == I - 1:
        goal_dist = max(goal_dist, dist)

    for di, dj, slope in zip([0, 0, 1, -1], [1, -1, 0, 0], "><v^"):
        nb = ni, nj = node[0] + di, node[1] + dj
        if not (0 <= ni < I and 0 <= nj < J):
            continue
        if nb == prev_node:
            continue
        c = lines[ni][nj]
        if c not in [".", slope]:
            continue
        frontier.append((nb, node, dist + 1))
print(goal_dist)
