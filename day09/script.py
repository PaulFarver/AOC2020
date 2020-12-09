import numpy as np

n = [int(line) for line in open("input")]

print(len(n), len(np.unique(n)))

def hasPair(s, numbers):
    for n1 in numbers:
        for n2 in numbers:
            if n1+n2 == s and n1 != n2:
                return True
    return False



for i in range(25, len(n)):
    print(n[i], hasPair(n[i], n[:i]))
