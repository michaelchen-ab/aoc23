import math
import sys

file = open(sys.argv[1]).read().strip()
lines = file.split("\n")

times, distances = file.split("\n")
time = int("".join(times.split()[1:]))
distance = int("".join(distances.split()[1:]))
x1 = (time + (time * time - 4 * distance) ** 0.5) / 2.0
x2 = (time - (time * time - 4 * distance) ** 0.5) / 2.0
(x1, x2) = (x1, x2) if x1 < x2 else (x2, x1)
x1_up = math.ceil(x1)
x2_down = math.floor(x2)
ways = x2_down - x1_up + 1
print(ways)
