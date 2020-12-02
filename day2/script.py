import re

pattern = "(\d+)-(\d+) ([a-z]): ([a-z]*)"

F = open("input.txt", "r")

amount = 0
for l in F:
    a = re.search(pattern, l)
    # print(a.group(1) + "|" + a.group(2) + "|" + a.group(3) + "|" + a.group(4))
    min = int(a.group(1))
    max = int(a.group(2))
    curr = 0
    for c in a.group(4):
        if c == a.group(3):
            curr = curr+1
    if curr >= min and curr <= max:
        amount = amount + 1
print(amount)
    