import numpy as np

n = [int(line) for line in open("input")]

print(len(n), len(np.unique(n)))

def hasPair(s, n):
    for a in n:
        b = s - a
        # Apparently b in n is faster than looping through the numbers manually
        if a != b and b in n:
            return True
    return False

part1 = 0
part1n = 0

for i in range(25, len(n)):
    if not hasPair(n[i], n[i-25:i]):
        part1n = i
        part1 = n[i]
        print(n[i], i, False)
        break


def findSet(target, numbers):
    i = 0
    j = 1
    while True:
        s = sum(numbers[i:j])
        if s > target:
            i += 1
        if s < target:
            j += 1
        if s == target:
            return i, j

i, j = findSet(part1, n[:part1n])
print(n[i:j])
print(sum(n[i:j]))
print(min(n[i:j])+max(n[i:j]))
