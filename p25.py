import sys
from collections import defaultdict

file = open(sys.argv[1]).read().strip()
lines = [(line) for line in file.split("\n")]

# use graphviz to visually find cut points
# dot = graphviz.Graph(engine="neato")
# for line in lines:
#     node, ns = line.split(": ")
#     for n in ns.split():
#         dot.edge(node, n)
# dot.render("asdf", view=True)

# klk - xgz
# vmq - cbl
# bvz - nvf

graph = defaultdict(set)
for line in lines:
    node, ns = line.split(": ")
    for n in ns.split():
        graph[node].add(n)
        graph[n].add(node)

for i, j in [("klk", "xgz"), ("vmq", "cbl"), ("bvz", "nvf")]:
    graph[i].remove(j)
    graph[j].remove(i)

prod = 1
for i in ["klk", "xgz"]:
    seen = {i}
    frontier = [i]
    while frontier:
        node = frontier.pop()
        seen.add(node)
        for n in graph[node]:
            if n not in seen:
                frontier.append(n)
    prod *= len(seen)
print(prod)
