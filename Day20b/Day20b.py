#!/usr/bin/python3

import sys
import re
from collections import Counter

# particle swarm

# each particle has position, velocity, and acceleration
# each tick, update velocity by acceleration and position by velocity
# when particles collide, they are removed
# how many particles are left after collisions are resolved?


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
    while True:
        precoll = newParts(parts)
        pcounts = Counter([str(part['p']) for part in precoll])
        collisions = [k for k, v in pcounts.items() if v > 1]
        if len(collisions) > 0:
            print("smash {} locations".format(len(collisions)))
            newparts = [part for part in precoll if str(part['p']) not in collisions]
            print("now {} parts".format(len(newparts)))
        else:
            newparts = precoll
        delta = [x['d'] - y['d'] for x, y in zip(parts, newparts)]
        if all(d < 0 for d in delta):
            return len(delta)
        parts = newparts


# Unit tests for work.
tt = {
    'x': ([
        'p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>\n',
        'p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>\n',
        'p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>\n',
        'p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>\n',
    ], 1)
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
