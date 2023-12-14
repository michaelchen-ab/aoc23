import sys

file = open(sys.argv[1]).read().strip()
lines = [list(line) for line in file.split("\n")]

transposed = [list(line) for line in zip(*lines)]

damage = 0
for l, line in enumerate(transposed):
    for i in range(len(line)):
        if line[i] != "O":
            continue
        latest_block = next(
            j for j in range(i - 1, -2, -1) if j == -1 or line[j] != "."
        )
        if latest_block + 1 != i:
            transposed[l][latest_block + 1] = "O"
            transposed[l][i] = "."
        damage += len(line) - (latest_block + 1)
print(damage)
