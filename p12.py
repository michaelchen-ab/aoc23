import functools
import sys

file = open(sys.argv[1]).read().strip()
lines = [line for line in file.split("\n")]


@functools.lru_cache()
def f(springs: str, groups: tuple[int, ...]):
    if not groups:
        if "#" in springs:
            return 0
        return 1
    if not springs:
        return 0
    g, *g_rest = groups
    if len(springs) < g:
        return 0
    total = 0
    if all(springs[i] in "?#" for i in range(g)):
        if len(springs) == g:
            if g_rest:
                return 0
            else:
                return 1
        if springs[g] in ".?":
            total += f(springs[g + 1 :], tuple(g_rest))

    must_match = springs[0] == "#"
    if must_match:
        return total
    return total + f(springs[1:], groups)


t = 0
MULT = 5  # 1 for part 1
for line in lines:
    springs, groups = line.split()
    springs = "?".join([springs] * MULT)
    groups = tuple(int(g) for g in groups.split(",") * MULT)
    c = f(springs, groups)
    t += c
print(t)
