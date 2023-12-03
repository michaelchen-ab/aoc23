from utils import get_input

data = get_input(3)

def next_to_star(num_start_idx, num_end_idx, line_idx, line):
    if num_start_idx > 0 and line[num_start_idx - 1] != '.':
        return (line_idx, num_start_idx - 1)
    if num_start_idx < len(line) - 1 and line[num_end_idx] != '.' and not line[num_end_idx].isdigit():
        return (line_idx, num_end_idx)
    if line_idx > 0:
        for i in range(max(0, num_start_idx - 1), min(num_end_idx + 1, len(line) - 1)):
            if data[line_idx - 1][i] != '.':
                return (line_idx - 1, i)
    if line_idx + 1 < len(data):
        for i in range(max(0, num_start_idx - 1), min(num_end_idx + 1, len(line) - 1)):
            if data[line_idx + 1][i] != '.':
                return (line_idx + 1, i)
    return False

total = 0
gear_touches = {}
for line_idx, line in enumerate(data):
    num_start_idx = None
    for char_idx, char in enumerate(line):
        if (
            (num_start_idx is not None and not char.isdigit()) or
            (num_start_idx is not None and char_idx == len(line) - 1)
        ):
            star_coord = next_to_star(num_start_idx, char_idx, line_idx, line)
            if star_coord:
                num = int(line[num_start_idx:char_idx])
                total += num
                star_symbol = data[star_coord[0]][star_coord[1]]
                if star_symbol == '*':
                    if star_coord not in gear_touches:
                        gear_touches[star_coord] = []
                    gear_touches[star_coord].append(num)
            num_start_idx = None
        if num_start_idx is None and char.isdigit():
            num_start_idx = char_idx
print(total)

# part 2
total = 0
for coord, touches in gear_touches.items():
    if len(touches) == 2:
        total += touches[0] * touches[1]
print(total)
