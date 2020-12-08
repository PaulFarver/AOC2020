

F = open("input", "r")

acc = 0
ptr = 0

def accumulate(value):
    global acc
    acc += int(value)
    return 1

operations = {
    'acc': accumulate,
    'nop': lambda v: 1,
    'jmp': lambda v: int(v),
}

instructions = [(s.split(" ")[0], s.split(" ")[1]) for s in F]

visited = [False]*len(instructions)
while True:
    if visited[ptr]:
        break
    else:
        visited[ptr] = True
    ptr = ptr + operations[instructions[ptr][0]](instructions[ptr][1])

print(acc)
