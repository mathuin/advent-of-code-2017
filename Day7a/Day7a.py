#!/usr/bin/python3

import sys


# One program at bottom supports entire tower.
# List of programs:
# Program name (weight) [-> programs above them]
# NB: programs above not required to be listed before!
# Which program is at the bottom?
def findRoot(programs):
    structure = {}
    for program in programs:
        line = program.split()
        structure[line[0]] = {
            'weight': int(line[1].strip('[()]')),
            'children': [x.strip(', \n') for x in line[3:]],
            'root': ''
        }
    for k in list(structure.keys()):
        for child in structure[k]['children']:
            structure[child]['root'] = k
    root = [x for x in structure if structure[x]['root'] == ''][0]
    return root

# Unit tests for findRoot.
tt = {'x': (['pbga (66)\n', 'xhth (57)\n', 'ebii (61)\n', 'havc (66)\n', 'ktlj (57)\n', 'fwft (72) -> ktlj, cntj, xhth\n', 'qoyq (66)\n', 'padx (45) -> pbga, havc, qoyq\n', 'tknk (41) -> ugml, padx, fwft\n', 'jptl (61)\n', 'ugml (68) -> gyxo, ebii, jptl\n', 'gyxo (61)\n', 'cntj (57)\n']
, 'tknk')}
for k, v in tt.items():
    result = findRoot(v[0])
    if result != v[1]:
        print("FAIL")

# The input is not checked for sanity, just existence.
programs = sys.stdin.readlines()
if len(programs) == 0:
    print("programs missing!")
    sys.exit(1)

# Only one line, and I don't want the newline character.
print(findRoot(programs))
