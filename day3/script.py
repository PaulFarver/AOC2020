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