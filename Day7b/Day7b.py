#!/usr/bin/python3

import sys
from collections import Counter


# One program at bottom supports entire tower.
# List of programs:
# Program name (weight) [-> programs above them]
# NB: programs above not required to be listed before!
# Which program is at the bottom?
def buildStructure(programs):
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
    return structure


def findRoot(structure):
    root = [x for x in structure if structure[x]['root'] == ''][0]
    return root


def weight(structure, node):
    if node in structure:
        if 'fullweight' not in structure[node]:
            structure[node]['fullweight'] = structure[node]['weight'] + sum([weight(structure, x) for x in structure[node]['children']])
        return structure[node]['fullweight']
    else:
        return 0



def findImbalance(structure, node):
    fullweight = weight(structure, node)
    freq = Counter([weight(structure, child) for child in structure[node]['children']]).most_common()
    if len(freq) == 1:
        # children are balanced
        # therefore issue is this node 
        # it is not the same weight as its peers
        parent = structure[node]['root']
        peerfreq = Counter([weight(structure, peer) for peer in structure[parent]['children']]).most_common()
        # return the weight it should be to balance
        return structure[node]['weight'] + (peerfreq[0][0]-fullweight)
    else:
        # children are not balanced
        # issue is further down
        target = freq[1][0]
        for child in structure[node]['children']:
            if weight(structure, child) == target:
                return findImbalance(structure, child)


# Unit tests for findRoot.
tt = {'x': (['pbga (66)\n', 'xhth (57)\n', 'ebii (61)\n', 'havc (66)\n', 'ktlj (57)\n', 'fwft (72) -> ktlj, cntj, xhth\n', 'qoyq (66)\n', 'padx (45) -> pbga, havc, qoyq\n', 'tknk (41) -> ugml, padx, fwft\n', 'jptl (61)\n', 'ugml (68) -> gyxo, ebii, jptl\n', 'gyxo (61)\n', 'cntj (57)\n']
, 60)}
for k, v in tt.items():
    structure = buildStructure(v[0])
    root = findRoot(structure)
    result = findImbalance(structure, root)
    if result != v[1]:
        print("FAIL: input ", v[0], ": expected ", v[1], ", got ", result, sep="")

# The input is not checked for sanity, just existence.
programs = sys.stdin.readlines()
if len(programs) == 0:
    print("programs missing!")
    sys.exit(1)

structure = buildStructure(programs)
root = findRoot(structure)
print(findImbalance(structure, root))
