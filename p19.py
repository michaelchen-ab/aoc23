import sys
from collections import defaultdict

file = open(sys.argv[1]).read().strip()
rules, parts = file.split("\n\n")

rule_map = defaultdict(list)
for line in rules.split("\n"):
    rule_name, rest = line.split("{")
    rest = rest[:-1]
    for rule in rest.split(","):
        if "<" in rule:
            a, b = rule.split("<")
            num, dest = b.split(":")
            func = lambda x, dest=dest, a=a, num=num: dest if x[a] < int(num) else None
        elif ">" in rule:
            a, b = rule.split(">")
            num, dest = b.split(":")
            func = lambda x, dest=dest, a=a, num=num: dest if x[a] > int(num) else None
        else:
            func = lambda _, rule=rule: rule
        rule_map[rule_name].append(func)

total = 0
for part in parts.split("\n"):
    part = part[1:-1]
    map = {}
    for var in part.split(","):
        a, b = var.split("=")
        map[a] = int(b)
    cur = "in"
    while cur not in "AR":
        rules = rule_map[cur]
        for rule in rules:
            next = rule(map)
            if next:
                cur = next
                break
    if cur == "A":
        total += sum(map.values())
print(total)
