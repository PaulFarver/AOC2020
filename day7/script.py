import re
import numpy as np

F = open("input", "r")

bagPattern = " ((\d) ((\w+ )+))bags?"
pattern = "((\w+ )+)bags contain(( (\d+ (\w+ )+)+bag(s)?[,.])+)"
noPattern = "((\w+ )+)bags contain no other bags."

tree = {}

for line in F:
    m = re.match(pattern, line)
    if m == None:
        m = re.match(noPattern, line)
    parent = m.groups()[0]
    if len(m.groups()) >= 3:
        for g in m.groups()[2].split(","):
            color = re.match(bagPattern, g).groups()[2]
            if color not in tree:
                tree[color] = []
            tree[color].append(parent)

def recurseTree(key):
    if key not in tree:
        return []
    l = []
    for parent in tree[key]:
        l.append(parent)
        l.extend(recurseTree(parent))
    return l
        
masterlist = np.array(recurseTree("shiny gold "))

print(len(np.unique(masterlist)))

F = open("input", "r")

tree = {}
for line in F:
    m = re.match(pattern, line)
    if m == None:
        m = re.match(noPattern, line)
    parent = m.groups()[0]
    if parent not in tree:
        tree[parent] = []
    if len(m.groups()) >= 3:
        for g in m.groups()[2].split(","):
            l = re.match(bagPattern, g) 
            tree[parent].append((int(l.groups()[1]), l.groups()[2]))

def recurseTree2(key):
    if key not in tree:
        return 1
    s = 1
    for b in tree[key]:
        s += b[0] * recurseTree2(b[1])
    return s

print(recurseTree2("shiny gold ")-1)