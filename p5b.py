import sys
from typing import Tuple
from typing_extensions import TypedDict

file = open(sys.argv[1]).read().strip()
lines = file.split("\n")


Permutation = TypedDict("permutation", {"min": int, "max": int, "offset": int})
ranges: list[Tuple[int, int]] = []

seeds, *maps = file.split("\n\n")
seed_vals = [int(x) for x in seeds.split(":")[-1].split()]
ranges = [
    (seed_vals[i], seed_vals[i] + seed_vals[i + 1] - 1)
    for i in range(0, len(seed_vals) - 1, 2)
]

for m in maps:
    mapping: list[Permutation] = []
    for line in m.split("\n")[1:]:
        dst_min, src_min, r = [int(x) for x in line.split()]
        src_max = src_min + r
        offset = dst_min - src_min
        mapping.append({"min": src_min, "max": src_max, "offset": offset})
    next_ranges = []
    while ranges:
        r = ranges.pop()
        r_min, r_max = r
        for permutation in mapping:
            lower = max(r_min, permutation["min"])
            upper = min(r_max, permutation["max"])
            if lower < upper:
                next_ranges.append(
                    (lower + permutation["offset"], upper + permutation["offset"])
                )
                if lower > r_min:
                    ranges.append((r_min, lower))
                if upper < r_max:
                    ranges.append((upper, r_max))
                break
        else:
            next_ranges.append(r)
    ranges = next_ranges
print(min(r[0] for r in ranges))
