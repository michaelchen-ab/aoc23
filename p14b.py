import itertools
import sys

file = open(sys.argv[1]).read().strip()
lines = [list(line) for line in file.split("\n")]


def move(y: int, x: int):
    global lines
    y_start = 0 if y == -1 else len(lines) - 1
    y_end = len(lines) if y == -1 else -1
    y_step = 1 if y == -1 else -1
    x_start = 0 if x == -1 else len(lines[0]) - 1
    x_end = len(lines) if x == -1 else -1
    x_step = 1 if x == -1 else -1

    for l in range(y_start, y_end, y_step):
        line = lines[l]
        for i in range(x_start, x_end, x_step):
            if lines[l][i] != "O":
                continue
            c, r = l, i
            did_move = False
            while (
                len(lines) > c + y >= 0
                and len(line) > r + x >= 0
                and lines[c + y][r + x] == "."
            ):
                c += y
                r += x
                did_move = True
            if did_move:
                lines[c][r] = "O"
                lines[l][i] = "."


def get_cache_key(grid: list[list[str]]):
    return tuple(tuple(line) for line in grid)


def get_damage(grid: list[list[str]]):
    return sum(len(grid) - i for i, line in enumerate(grid) for c in line if c == "O")


cache = {}
for i in itertools.count(1):
    move(-1, 0)
    move(0, -1)
    move(1, 0)
    move(0, 1)
    cache_key = get_cache_key(lines)
    if cache_key in cache:
        first_seen = cache[cache_key]
        cycle_len = i - first_seen
        final = 1e9 % cycle_len
        if final < first_seen:
            final += cycle_len
        pos = next(key for key, val in cache.items() if val == final)
        print(get_damage(pos))
        break
    cache[cache_key] = i
