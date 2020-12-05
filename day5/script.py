import numpy as np

F = open("input")

def searchRow(s):
    rows = np.array(range(128))
    for c in s:
        if c == "F":
            rows = np.array_split(rows, 2)[0]
        if c == "B":
            rows = np.array_split(rows, 2)[1]
    return rows[0]

def searchColumn(s):
    columns = np.array(range(8))
    for c in s:
        if c == "L":
            columns = np.array_split(columns, 2)[0]
        if c == "R":
            columns = np.array_split(columns, 2)[1]
    return columns[0]

ids = [ searchRow(l[:7]) * 8 + searchColumn(l[7:]) for l in F ]
print(max(ids))

last = min(ids)-1
for i in sorted(ids):
    if i == last + 2:
        print(i-1)
    last = i