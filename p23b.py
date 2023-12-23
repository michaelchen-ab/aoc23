import sys
from collections import defaultdict
from time import time

t = time()

Pos = tuple[int, int]
Dir = tuple[int, int]
State = tuple[Pos, Dir, int]

file = open(sys.argv[1]).read().strip()
lines = [list(line) for line in file.split("\n")]

I = len(lines)
J = len(lines[0])

start = next((0, j) for j, c in enumerate(lines[0]) if c == ".")
end = next((I - 1, j) for j, c in enumerate(lines[-1]) if c == ".")

# get all junctions (nodes with more than 2 neighbours) so we can run all paths
# between start and end in reasonable time
juncs = []
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == "#":
            continue
        ns = [
            1
            for ni, nj in zip([i, i, i + 1, i - 1], [j + 1, j - 1, j, j])
            if 0 <= ni < I and 0 <= nj < J and lines[ni][nj] != "#"
        ]
        if len(ns) > 2:
            juncs.append((i, j))

# find distances between all junctions
junc_dists = defaultdict(dict)
for j in juncs:
    frontier: list[tuple[Pos, Pos, int]] = [(j, j, 0)]
    while frontier:
        node, prev_node, dist = frontier.pop()
        if node != j and node in [*juncs, start, end]:
            junc_dists[j][node] = dist
            junc_dists[node][j] = dist
            continue
        for di, dj in zip([0, 0, 1, -1], [1, -1, 0, 0]):
            nb = ni, nj = node[0] + di, node[1] + dj
            if not (0 <= ni < I and 0 <= nj < J):
                continue
            if nb == prev_node:
                continue
            if lines[ni][nj] == "#":
                continue
            frontier.append((nb, node, dist + 1))

# find all paths from start to end
frontier2: list[tuple[Pos, set[Pos], int]] = [(start, set([start]), 0)]
goal_dist = -1

while frontier2:
    node, seen_nodes, dist = frontier2.pop()
    for nb, nb_dist in junc_dists[node].items():
        if nb in seen_nodes:
            continue
        ndist = dist + nb_dist
        if nb == end and ndist > goal_dist:
            goal_dist = ndist
            print(goal_dist)
            continue
        frontier2.append((nb, seen_nodes | set([nb]), ndist))
