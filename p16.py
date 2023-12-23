import sys

file = open(sys.argv[1]).read().strip()
lines = file.split("\n")

initial_ray = ((0, -1), (0, 1))
cache = set()  # tuple of ((i,j), direction), encountered rays
rays = [initial_ray]
while rays:
    pos, dir = rays.pop()
    new_pos = pos[0] + dir[0], pos[1] + dir[1]
    if not (0 <= new_pos[0] < len(lines) and 0 <= new_pos[1] < len(lines[0])):
        continue
    new_rays = []
    match lines[new_pos[0]][new_pos[1]]:
        case "|":
            if dir[0] == 0:  # moving horizontal
                new_rays.append((new_pos, (1, 0)))
                new_rays.append((new_pos, (-1, 0)))
            else:
                new_rays.append((new_pos, dir))
        case "-":
            if dir[1] == 0:  # moving vertical
                new_rays.append((new_pos, (0, 1)))
                new_rays.append((new_pos, (0, -1)))
            else:
                new_rays.append((new_pos, dir))
        case "/":
            if dir == (0, 1):
                new_rays.append((new_pos, (-1, 0)))
            elif dir == (0, -1):
                new_rays.append((new_pos, (1, 0)))
            elif dir == (1, 0):
                new_rays.append((new_pos, (0, -1)))
            else:
                new_rays.append((new_pos, (0, 1)))
        case "\\":
            if dir == (0, 1):
                new_rays.append((new_pos, (1, 0)))
            elif dir == (0, -1):
                new_rays.append((new_pos, (-1, 0)))
            elif dir == (1, 0):
                new_rays.append((new_pos, (0, 1)))
            else:
                new_rays.append((new_pos, (0, -1)))
        case ".":
            new_rays.append((new_pos, dir))
    for ray in new_rays:
        if ray not in cache:
            cache.add(ray)
            rays.append(ray)
print(len(set(pos for pos, _ in cache)))
