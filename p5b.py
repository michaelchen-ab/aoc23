from typing import Tuple
from typing_extensions import TypedDict
from utils import get_input

data = get_input(5)

Permutation = TypedDict("permutation", {"min": int, "max": int, "offset": int})
ranges: list[Tuple[int, int]] = []
mapping: list[Permutation] = []
for line in data:
    if line.startswith("seeds"):
        raw = [int(x) for x in line.split(":")[-1].split()]
        ranges = [(raw[i], raw[i + 1]) for i in range(0, len(raw) - 1, 2)]
    elif line.endswith("map:"):
        mapping = []
    elif line:
        dest_min, src_min, r = [int(x) for x in line.split()]
        src_max = src_min + r - 1
        offset = dest_min - src_min
        mapping.append({"min": src_min, "max": src_max, "offset": offset})
    elif not line and mapping:
        next_ranges = []
        while ranges:
            r = ranges.pop()
            r_min, r_range = r
            r_max = r_min + r_range - 1
            for permutation in mapping:
                lower = max(r_min, permutation["min"])
                upper = min(r_max, permutation["max"])
                if lower <= upper:
                    next_ranges.append(
                        (lower + permutation["offset"], upper - lower + 1)
                    )
                    if lower > r_min:
                        ranges.append((r_min, lower - r_min))
                    if upper < r_max:
                        ranges.append((upper + 1, r_max - upper))
                    break
            else:
                next_ranges.append(r)
        ranges = next_ranges
print(min(r[0] for r in ranges))
