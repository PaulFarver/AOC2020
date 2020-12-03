F = open("input.txt", "r")

steps = 0
trees = 0
for l in F:
    for c in range(31):
        if c == (3*steps)%31:
            if l[c] == "#":
                trees = trees + 1
                print("X", end="")
            else:
                print("O", end="")
        else:
            print(l[c], end="")

    steps = steps + 1
    print()

print(trees)

F = open("input.txt", "r")

slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
result = [0    ,0    ,0    ,0    ,0    ]

def checkSlope(slope, x, y):
    return y%slope[1] == 0 and (y/slope[1]*slope[0])%31 == x

y = 0
for l in F:
    for x in range(31):
        # if l[x] == "#":
        hit = False
        for s in range(len(slopes)):
            if checkSlope(slopes[s], x, y):
                if l[x] == "#":
                    result[s] += 1
                hit = True
        if hit:
            if l[x] == "#":
                print("X", end="")
            else:
                print("O", end="")
        else:
            print(l[x], end="")
    print()
    y += 1
print(result)
print(result[0]*result[1]*result[2]*result[3]*result[4])

