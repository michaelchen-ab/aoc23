from utils import get_input

total = 0
with open(get_input(1), 'r') as f:
    for line in f:
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
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}
with open(get_input(1)) as f:
    for line in f:
        first_num = (-1, float('inf'))
        last_num = (-1, float('inf'))
        for index, char in enumerate(line.rstrip()):
            if char.isdigit():
                if first_num[0] == -1:
                    first_num = (int(char), index)
                last_num = (int(char), index)
        for num, num_str in num_map.items():
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
