import itertools
import sys
import numpy as np

from numpy.linalg import LinAlgError

Pos = tuple[int, int]
Dir = tuple[int, int]
State = tuple[Pos, Dir, int]

file = open(sys.argv[1]).read().strip()
lines = [(line) for line in file.split("\n")]

amin = 200000000000000
amax = 400000000000000
total = 0
for lineA, lineB in itertools.combinations(lines, 2):
    posA, velA = lineA.split(" @ ")
    posB, velB = lineB.split(" @ ")
    posA = np.array([int(x) for x in posA.split(", ")][:2])
    velA = np.array([int(x) for x in velA.split(", ")][:2])
    posB = np.array([int(x) for x in posB.split(", ")][:2])
    velB = np.array([int(x) for x in velB.split(", ")][:2])
    a = np.array([[-velA[0], velB[0]], [-velA[1], velB[1]]])
    b = posA - posB
    try:
        s, t = np.linalg.solve(a, b)
    except LinAlgError:
        print("parallel lines", a, b)
        continue
    if s < 0 or t < 0:
        continue
    point = posA + velA * s
    if amin <= point[0] <= amax and amin <= point[1] <= amax:
        total += 1
print(total)
