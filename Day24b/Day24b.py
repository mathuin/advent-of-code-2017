#!/usr/bin/python3

import sys

# electromagnetic moat

# input is a set of ports: a/b in format
# can be a/b or b/a in usage
# first port must be 0
# strength of bridge is sum of port types
# 0/3 3/7 7/4 has strength of 0+3 + 3+7 + 7+4 = 24
# what is the strength of the longest bridge?


def work(lines):
    allports = [tuple(line.rstrip().split('/')) for line in lines]
    ordered = {}
    for port in allports:
        for elem in port:
            if elem not in ordered:
                ordered[elem] = []
            if port not in ordered[elem]:
                ordered[elem].append(port)
    bridges = []
    left = '0'
    for port in ordered[left]:
        right = port[1] if port[0] == left else port[0]
        bridges.append(([port], right))
    lenstrens = []
    while True:
        newbridges = []
        for bridge, left in bridges:
            for port in ordered[left]:
                if port in bridge:
                    continue
                newbridge = list(bridge)
                right = port[1] if port[0] == left else port[0]
                newbridge.append(port)
                newbridges.append((newbridge, right))
            lenstrens.append((len(bridge), sum([int(port[0])+int(port[1]) for port in bridge])))
        if newbridges == []:
            break
        bridges = newbridges
    maxlen, _ = map(max, zip(*lenstrens))
    return max(stren for len, stren in lenstrens if len == maxlen)


# Test case for work.
tt = {'x': (['0/2\n', '2/2\n', '2/3\n', '3/4\n', '3/5\n', '0/1\n', '10/1\n', '9/10\n'], 19)}

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
