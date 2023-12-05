from typing_extensions import TypedDict
from utils import get_input
from pprint import pprint
import itertools

data = get_input(5)
data = get_input("5e")
# data[0] = "seeds: " + " ".join(str(x) for x in range(100))
seed_ranges = [(i, 1) for i in range(0, 100)]

Permutation = TypedDict("permutation", {"min": int, "max": int, "offset": int})
mappings: list[list[Permutation]] = [[]]
for line_no, line in enumerate(reversed(data)):
    if line.startswith("seeds"):
        mappings = mappings[:-1]
        vals = [int(x) for x in line.split(":")[-1].split()]
        seed_ranges = [(vals[i], vals[i + 1]) for i in range(0, len(vals) - 1, 2)]
        print("got to seeds", vals)
        pprint(mappings)
        for i in itertools.count(0):
            print("checking", i)
            val = i
            for mapping in mappings:
                for permutation in mapping:
                    # print(permutation)
                    if permutation["min"] <= val <= permutation["max"]:
                        val += permutation["offset"]
                        break
            # print(i, val, seed_ranges)
            for min, r in seed_ranges:
                if min <= val <= min + r - 1:
                    print(i, val, min, r)
                    exit(0)

    elif line.endswith("map:"):
        mappings.append([])
    elif not line:
        pass
    elif not line.endswith("map:"):
        dest_min, src_min, r = [int(x) for x in line.split()]
        dest_max = dest_min + r - 1
        offset = src_min - dest_min
        mappings[-1].append({"min": dest_min, "max": dest_max, "offset": offset})
