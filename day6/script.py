import re
import numpy as np

F = open("input", "r")

s = 0
for l in re.sub(r'\n(\S)', r'\1', F.read()).splitlines():
    arr = np.array(list(l))
    s += len(np.unique(arr))
print(s)

F = open("input", "r")
s = 0
for l in re.sub(r'\n(\S)', r' \1', F.read()).splitlines():
    groups = [list(h) for h in l.split(" ")[1:]]
    intersection = groups[0]
    for i in range(len(groups)):
        intersection = np.intersect1d(intersection, groups[i])
    s += len(intersection)
print(s)