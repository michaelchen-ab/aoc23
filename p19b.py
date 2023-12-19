import sys
import itertools
from collections import defaultdict
from typing import DefaultDict
from math import prod

file = open(sys.argv[1]).read().strip()
rules, parts = file.split("\n\n")

rule_map: DefaultDict[str, list[dict]] = defaultdict(list)
for line in rules.split("\n"):
    rule_name, rest = line.split("{")
    rest = rest[:-1]
    for idx, rule in enumerate(rest.split(",")):
        if "<" in rule:
            a, b = rule.split("<")
            num, dest = b.split(":")
            rule_map[rule_name].append(
                {
                    "c": a,
                    "op": "<",
                    "num": int(num),
                    "dest": f"A{idx}" if dest == "A" else dest,
                }
            )
        elif ">" in rule:
            a, b = rule.split(">")
            num, dest = b.split(":")
            rule_map[rule_name].append(
                {
                    "c": a,
                    "op": ">",
                    "num": int(num),
                    "dest": f"A{idx}" if dest == "A" else dest,
                }
            )
        else:
            rule_map[rule_name].append({"c": "", "op": "", "num": 0, "dest": rule})

paths = []
came_from = {}
nodes = ["in"]
while nodes:
    node = nodes.pop()
    ns = rule_map[node]
    for i, n in enumerate(ns):
        came_from[n["dest"]] = node
        if n["dest"].startswith("A"):
            path = [f"A{i}"]
            cur = node
            while True:
                path.append(cur)
                if cur == "in":
                    break
                cur = came_from[cur]
            paths.append(list(reversed(path)))
        elif n["dest"] == "R":
            pass
        else:
            nodes.append(n["dest"])


total = 0
for path in paths:
    restrictions = {
        "x": {"min": 1, "max": 4001},
        "m": {"min": 1, "max": 4001},
        "a": {"min": 1, "max": 4001},
        "s": {"min": 1, "max": 4001},
    }
    for n1, n2 in itertools.pairwise(path):
        rules = rule_map[n1]
        for rule in rules:
            c = rule["c"]
            op = rule["op"]
            num = rule["num"]
            if rule["dest"] == n2:
                if op == ">":
                    restrictions[c]["min"] = max(restrictions[c]["min"], num + 1)
                elif op == "<":
                    restrictions[c]["max"] = min(restrictions[c]["max"], num)
                break
            else:
                if op == ">":
                    restrictions[c]["max"] = min(restrictions[c]["max"], num + 1)
                elif op == "<":
                    restrictions[c]["min"] = max(restrictions[c]["min"], num)

    ranges = [c["max"] - c["min"] for c in restrictions.values()]
    total += prod(ranges)
print(total)
