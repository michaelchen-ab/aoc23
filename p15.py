import sys

file = open(sys.argv[1]).read().strip()


def hash(x: str):
    val = 0
    for c in x:
        val += ord(c)
        val *= 17
        val %= 256
    return val


t = 0
for seq in file.split(","):
    t += hash(seq)
print(t)
