from collections import defaultdict
from typing import DefaultDict
from utils import get_input

data = get_input(3)


def next_to_star(num_start_idx, num_end_idx, line_idx, line):
    for i in range(line_idx - 1, line_idx + 2):
        for j in range(num_start_idx - 1, num_end_idx + 1):
            if 0 <= i < len(line) and 0 <= j < len(data):
                c = data[i][j]
                if c != "." and not c.isdigit():
                    return (c, (i, j))
    return None


total = 0
Coord = tuple[int, int]
gear_touches: DefaultDict[Coord, list[int]] = defaultdict(list)
for line_idx, line in enumerate(data):
    num_start_idx: int | None = None
    for char_idx, c in enumerate(line):
        if (num_start_idx is not None and not c.isdigit()) or (
            num_start_idx is not None and char_idx == len(line) - 1
        ):
            res = next_to_star(num_start_idx, char_idx, line_idx, line)
            if res:
                symbol, coord = res
                num = int(line[num_start_idx:char_idx])
                total += num
                if symbol == "*":
                    gear_touches[coord].append(num)
            num_start_idx = None
        elif num_start_idx is None and c.isdigit():
            num_start_idx = char_idx
print(total)

# part 2
total = 0
for touches in gear_touches.values():
    if len(touches) == 2:
        total += touches[0] * touches[1]
print(total)
