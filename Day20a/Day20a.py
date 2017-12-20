#!/usr/bin/python3

import sys
import re

# particle swarm

# each particle has position, velocity, and acceleration
# each tick, update velocity by acceleration and position by velocity
# which particle is closest to origin in the long term?
# use dist distance (sum of absolute values of position)


def buildParts(lines):
    elempat = r"([a-z])=<([^,]*),([^,]*),([^,]*)>"
    parts = []
    for line in lines:
        part = {}
        for elem in line.rstrip().split(", "):
            m = re.search(elempat, elem, )
            if m:
                part[m.group(1)] = [int(m.group(2)), int(m.group(3)), int(m.group(4))]
            else:
                print("OH NO elem=", elem)
        part['d'] = sum([abs(x) for x in part['p']])
        parts.append(part)
    return parts


def newParts(parts):
    newparts = []
    for part in parts:
        part['v'] = [a+b for a, b in zip(part['v'], part['a'])]
        part['p'] = [a+b for a, b in zip(part['p'], part['v'])]
        part['d'] = sum([abs(x) for x in part['p']])
        newparts.append(part)
    return newparts


def work(lines):
    parts = buildParts(lines)
    smalla = [sum(abs(x) for x in part['a']) for part in parts]
    val, idx = min((val, idx) for (idx, val) in enumerate(smalla))
    indexes = [i for i, x in enumerate(smalla) if x == val]
    if len(indexes) == 1:
        return indexes[0]
    else:
        return None
    # while True:
    #     newparts = newParts(parts)
    #     delta = [x['d'] - y['d'] for x, y in zip(parts, newparts)]
    #     if all(d < 0 for d in delta):
    #         print("all are negative")
    #         val, idx = max((val, idx) for (idx, val) in enumerate(delta))
    #         print("the least negative value is {}".format(val))
    #         indexes = [i for i, x in enumerate(delta) if x == val]
    #         print("parts with this value: ", indexes)
    #         if len(indexes) == 1:
    #             return indexes[0]
    #         val, idx = min((val['d'], idx) for (idx, val['d']) in enumerate(newparts))
    #         print("the smallest dist value is {}".format(val))
    #         indexes = [i for i, x in enumerate(newparts) if x['d'] == val]
    #         print("parts with this value: ", indexes)
    #         if len(indexes) == 1:
    #             return indexes[0]
    #         return None
    #     parts = newparts


# Unit tests for work.
tt = {
    'x': ([
        'p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>\n',
        'p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>\n'
    ], 0)
}

for k, v in tt.items():
    result = work(v[0])
    if result != v[1]:
        print("FAIL: input ", v[0], ": expected ", v[1], ", got ", result, sep="")

# The input is not checked for sanity, just existence.
lines = sys.stdin.readlines()
if len(lines) == 0:
    print("lines missing!")
    sys.exit(1)

print(work(lines))
