from utils import get_input

data = get_input(1)

total = 0
for line in data:
    first_num = last_num = -1
    for char in line.rstrip():
        if char.isdigit():
            if first_num == -1:
                first_num = int(char)
            last_num = int(char)
    total += 10 * first_num + last_num
print(total)

total = 0
num_map = {
    'one': 1,
    '1': 1,
    'two': 2,
    '2': 2,
    'three': 3,
    '3': 3,
    'four': 4,
    '4': 4,
    'five': 5,
    '5': 5,
    'six': 6,
    '6': 6,
    'seven': 7,
    '7': 7,
    'eight': 8,
    '8': 8,
    'nine': 9,
    '9': 9,
}
for line in data:
    # (num, index)
    first_num = (-1, float('inf'))
    last_num = (-1, -float('inf'))
    for num_str, num in num_map.items():
        first_occurrence = line.find(num_str)
        if first_occurrence == -1:
            continue
        if first_occurrence < first_num[1]:
            first_num = (num, first_occurrence)
        last_occurrence = line.rfind(num_str)
        if last_occurrence > last_num[1]:
            last_num = (num, last_occurrence)
    total += 10 * first_num[0] + last_num[0]
print(total)
