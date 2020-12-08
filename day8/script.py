

F = open("input", "r")

def flip(inst):
    if inst[0] == "nop":
        return ("jmp", inst[1])
    if inst[0] == "jmp":
        return ("nop", inst[1])
    if inst[0] == "acc":
        return ("acc", inst[1])
    raise Exception("Unexpected instruction: ", inst)

operations = {
    'acc': lambda p, a, v: (p+1, a+v),
    'nop': lambda p, a, v: (p+1, a),
    'jmp': lambda p, a, v: (p+v, a),
}

instructions = [(s.split(" ")[0], int(s.split(" ")[1])) for s in F]

def call(set, ptr, acc):
    return operations[set[0]](ptr, acc, set[1])

def detect_infinite(instructions, ptr, acc, visited):
    if ptr >= len(visited):
        return False, ptr, acc, visited
    if visited[ptr]:
        return True, ptr, acc, visited
    visited[ptr] = True
    ptr, acc = call(instructions[ptr], ptr, acc)
    return detect_infinite(instructions, ptr, acc, visited)

yay, ptr, acc, _ = detect_infinite(instructions, 0, 0, [False]*len(instructions))
print("Part 1: ", acc)

for i in range(len(instructions)):
    instructions[i] = flip(instructions[i])
    yay, ptr, acc, _ = detect_infinite(instructions, 0, 0, [False]*len(instructions))
    if yay:
        instructions[i] = flip(instructions[i])
    else:
        print("Part 2: ", acc)
        break
