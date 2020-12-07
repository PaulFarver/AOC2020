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
print("Dependency tree generated")

def recurseTree(key):
    if key not in tree:
        return []
    l = []
    for parent in tree[key]:
        l.append(parent)
        l.extend(recurseTree(parent))
    return l
        
masterlist = np.array(recurseTree("shiny gold "))
print(masterlist)

print(np.unique(masterlist))
print(len(np.unique(masterlist)))
