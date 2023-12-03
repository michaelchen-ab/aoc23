from utils import get_input

data = get_input(2)
maxes = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

def is_valid(turns):
    for turn in turns.split('; '):
        for quantity in turn.split(', '):
            [num, col] = quantity.split(' ')
            if int(num) > maxes[col]:
                return False
    return True

total = 0
for line in data:
    game_turn, turns = line.split(': ')
    if is_valid(turns):
        id = game_turn.split(' ')[-1]
        total += int(id)
print(total)

total = 0
for line in data:
    _, turns = line.split(': ')
    maxes = {}
    for turn in turns.split('; '):
        for quantity in turn.split(', '):
            [num, col] = quantity.split(' ')
            maxes[col] = max(int(num), maxes.get(col, 0))
    power = 1
    for num in maxes.values():
        power *= num
    total += power
print(total)
