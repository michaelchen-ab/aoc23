from utils import get_input

data = get_input(5)
data = get_input("5e")
data[0] = "seeds: " + " ".join(str(x) for x in range(100))

vals = []
mapping = []
for line_no, line in enumerate(data):
    if line.startswith("seeds"):
        vals = [int(x) for x in line.split(":")[-1].split()]
    elif line.endswith("map:"):
        mapping = []
    elif line:
        dest_min, src_min, range = [int(x) for x in line.split()]
        src_max = src_min + range - 1
        offset = dest_min - src_min
        mapping.append({"min": src_min, "max": src_max, "offset": offset})
    elif not line and mapping:
        print("vals", vals)
        print(mapping)
        new_vals = []
        for v in vals:
            for partition in mapping:
                if partition["min"] <= v <= partition["max"]:
                    new_vals.append(v + partition["offset"])
                    break
            else:
                new_vals.append(v)
        print(new_vals)
        vals = new_vals
print(min(vals))
