from utils import get_input

data = get_input(4)

total = 0
for line in data:
    _, nums = line.split(": ")
    win, mine = nums.split(" | ")
    win = [n for n in win.split(" ") if n]
    mine = [n for n in mine.split(" ") if n]
    score = 0
    for num in win:
        if num in mine:
            score = 1 if score == 0 else score * 2
    total += score
print(total)

arr = [1] * (len(data) + 1)
for idx, line in enumerate(data, start=1):
    _, nums = line.split(": ")
    win, mine = nums.split(" | ")
    win = [n for n in win.split(" ") if n]
    mine = [n for n in mine.split(" ") if n]
    c = sum(1 for n in win if n in mine)
    for i in range(idx + 1, idx + c + 1):
        arr[i] += arr[idx]
print(sum(arr) - 1)
