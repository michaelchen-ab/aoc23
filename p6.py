import math
import sys

file = open(sys.argv[1]).read().strip()
lines = file.split("\n")

times, distances = file.split("\n")
times = [int(x) for x in times.split()[1:]]
distances = [int(x) for x in distances.split()[1:]]
prod = 1
for time, distance in zip(times, distances):
    x1 = (time + (time * time - 4 * distance) ** 0.5) / 2.0
    x2 = (time - (time * time - 4 * distance) ** 0.5) / 2.0
    x1_up = math.ceil(x1)
    x2_down = math.floor(x2)
    ways = x2_down - x1_up + 1
    prod *= ways
print(prod)
