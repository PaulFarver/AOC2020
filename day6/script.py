import re
import numpy as np

F = open("input", "r")

s = 0
for l in re.sub(r'\n(\S)', r'\1', F.read()).splitlines():
    arr = np.array(list(l))
    s += len(np.unique(arr))
print(s)
