import sys
from typing import DefaultDict
from collections import defaultdict
from heapq import heappop, heappush

Pos = tuple[int, int]
Dir = tuple[int, int]
State = tuple[Pos, Dir, int]

file = open(sys.argv[1]).read().strip()
grid = [line for line in file.split("\n")]
lines = [[int(c) for c in line] for line in grid]

I = len(lines)
J = len(lines[0])


def h(p: Pos):
    return end[0] - p[0] + end[1] - p[1]


def check_last(state: State, nmin: int, nmax: int):
    global came_from

    _, dir, _ = state
    counter = 1
    while state in came_from:
        state = came_from[state]
        if state[1] != dir:
            break
        counter += 1
        if counter >= nmax:
            return dir
    if counter < nmin:
        return dir
    return None


MIN, MAX = (4, 10)  # (1, 3) for part 1
start_pos = (0, 0)
end = (I - 1, J - 1)
came_from: dict[State, State] = {}
start_state: State = (start_pos, (0, 0), 0)
start_h = h(start_pos)
g_score: DefaultDict[State, int] = defaultdict(lambda: 999999)
g_score[start_state] = 0
f_score: DefaultDict[State, int] = defaultdict(lambda: 999999)
f_score[start_state] = start_h
open_set: list[tuple[int, State]] = []
heappush(open_set, (start_h, start_state))
best = float("inf")
while open_set:
    cur_f, cur_state = heappop(open_set)
    cur_pos, cur_dir, cur_count = cur_state
    if cur_pos == end:
        if cur_count >= MIN and cur_f < best:
            best = cur_f
            print(cur_f)
        continue
    n_dirs = []
    if cur_dir == (0, 0):
        n_dirs.extend([(0, 1), (1, 0)])
    elif cur_count < MIN:
        n_dirs.append(cur_dir)
    else:
        if cur_dir[0] == 0:
            n_dirs.extend([(1, 0), (-1, 0)])
        else:
            n_dirs.extend([(0, 1), (0, -1)])
        if cur_count < MAX:
            n_dirs.append(cur_dir)

    last_state = came_from.get(cur_state)
    for n_dir in n_dirs:
        di, dj = n_dir
        n_pos = (ni, nj) = (cur_pos[0] + di, cur_pos[1] + dj)
        if not (0 <= ni < I and 0 <= nj < J):
            continue
        n_state = (n_pos, n_dir, cur_count + 1 if n_dir == cur_dir else 1)
        g_tent = g_score[cur_state] + lines[ni][nj]
        if g_tent < g_score[n_state]:
            came_from[n_state] = cur_state
            g_score[n_state] = g_tent
            f_score[n_state] = f = g_tent + h(n_pos)
            heappush(open_set, (f, n_state))
