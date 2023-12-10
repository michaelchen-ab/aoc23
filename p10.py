import sys
import itertools

file = open(sys.argv[1]).read().strip()
lines = file.split("\n")

(line_idx, char_idx) = s_pos = next(
    (i, j) for i, line in enumerate(lines) for j, char in enumerate(line) if char == "S"
)


res = []
if line_idx - 1 >= 0:
    c = lines[line_idx - 1][char_idx]
    if c in "|F7":
        res.append((line_idx - 1, char_idx))
if line_idx + 1 < len(lines):
    c = lines[line_idx + 1][char_idx]
    if c in "|LJ":
        res.append((line_idx + 1, char_idx))
if char_idx - 1 >= 0:
    c = lines[line_idx][char_idx - 1]
    if c in "-LF":
        res.append((line_idx, char_idx - 1))
if char_idx + 1 < len(lines[0]):
    c = lines[line_idx][char_idx + 1]
    if c in "-J7":
        res.append((line_idx, char_idx + 1))
[a, b] = res


symbol_map = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "F": [(1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    "7": [(1, 0), (0, -1)],
}


def go(pos: tuple[int, int], prev_pos: tuple[int, int]):
    (line_idx, char_idx) = pos
    c = lines[line_idx][char_idx]
    dirs = symbol_map[c]
    next_pos = [(line_idx + a, char_idx + b) for (a, b) in dirs]
    return next(pos for pos in next_pos if pos != prev_pos)


prev_a = prev_b = s_pos
for c in itertools.count(2):
    a, prev_a = go(a, prev_a), a
    b, prev_b = go(b, prev_b), b
    if a == b:
        print(c)
        break
