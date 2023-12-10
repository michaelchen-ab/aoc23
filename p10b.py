import sys

file = open(sys.argv[1]).read().strip()
lines = [list(line) for line in file.split("\n")]

(line_idx, char_idx) = s_pos = next(
    (i, j) for i, line in enumerate(lines) for j, char in enumerate(line) if char == "S"
)

res = []
dirs = []
if line_idx - 1 >= 0:
    c = lines[line_idx - 1][char_idx]
    if c in "|F7":
        res.append((line_idx - 1, char_idx))
        dirs.append((-1, 0))
if line_idx + 1 < len(lines):
    c = lines[line_idx + 1][char_idx]
    if c in "|LJ":
        res.append((line_idx + 1, char_idx))
        dirs.append((1, 0))
if char_idx - 1 >= 0:
    c = lines[line_idx][char_idx - 1]
    if c in "-LF":
        res.append((line_idx, char_idx - 1))
        dirs.append((0, -1))
if char_idx + 1 < len(lines[0]):
    c = lines[line_idx][char_idx + 1]
    if c in "-J7":
        res.append((line_idx, char_idx + 1))
        dirs.append((0, 1))
[a, b] = res

symbol_map = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "F": [(1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    "7": [(1, 0), (0, -1)],
}

dirs_to_symbol_map = {tuple(sorted(v)): k for k, v in symbol_map.items()}
lines[line_idx][char_idx] = dirs_to_symbol_map[tuple(sorted(dirs))]
prev_a = prev_b = s_pos
pipes = set([s_pos, a, b])


def go(pos: tuple[int, int], prev_pos: tuple[int, int]):
    (line_idx, char_idx) = pos
    c = lines[line_idx][char_idx]
    dirs = symbol_map[c]
    next_pos = [(line_idx + a, char_idx + b) for (a, b) in dirs]
    return next(pos for pos in next_pos if pos != prev_pos)


while a != b:
    a, prev_a = go(a, prev_a), a
    b, prev_b = go(b, prev_b), b
    pipes.add(a)
    pipes.add(b)


def num_segments_to_left(pos: tuple[int, int]):
    (line_idx, char_idx) = pos
    num_segments = 0
    idx = 0
    while idx < char_idx:
        pos = (line_idx, idx)
        if pos not in pipes:
            idx += 1
            continue
        c = lines[line_idx][idx]
        if c == "|":
            idx += 1
            num_segments += 1
            continue
        assert c in "LF", c
        start = c
        while True:
            idx += 1
            end = lines[line_idx][idx]
            if end in "J7":
                if (start == "L" and end == "7") or (start == "F" and end == "J"):
                    num_segments += 1
                idx += 1
                break
    return num_segments


total = 0
for line_idx, line in enumerate(lines):
    for char_idx, c in enumerate(line):
        if (line_idx, char_idx) in pipes:
            continue
        pipes_going_left = num_segments_to_left((line_idx, char_idx))
        if pipes_going_left % 2 == 1:
            total += 1
print(total)
