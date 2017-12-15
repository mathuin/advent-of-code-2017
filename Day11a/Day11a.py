#!/usr/bin/python3

import sys

# hex ed

# n, ne, se, s, sw, nw

# given path child took, calculate fewest steps to reach them.

# 1. remove opposing steps (n<-->s)
# 2. merge two-away steps (n + se = ne, etc)
# 3. remove opposing steps again?

stepOrder = ['n', 'ne', 'se', 's', 'sw', 'nw']


def removeOpposing(path):
    half = len(stepOrder)//2

    for dir in range(0, half):
        cancelled = min(path[stepOrder[dir]], path[stepOrder[dir+half]])
        path[stepOrder[dir]] -= cancelled
        path[stepOrder[dir+half]] -= cancelled

    return path


def mergeSemiAdjacent(path):
    numSteps = len(stepOrder)

    for dir in range(0, numSteps):
        merged = min(path[stepOrder[dir]], path[stepOrder[(dir+2) % numSteps]])
        path[stepOrder[dir]] -= merged
        path[stepOrder[(dir+1) % numSteps]] += merged
        path[stepOrder[(dir+2) % numSteps]] -= merged

    return path


def buildPath(stepstr):
    path = {key: 0 for key in stepOrder}

    for step in stepstr.rstrip().split(','):
        path[step] += 1

    return path


def lenPath(path):
    return sum(path[dir] for dir in stepOrder)


def getShortestPath(stepstr):
    path = buildPath(stepstr)
    oldpath = 999999999
    while True:
        path = removeOpposing(path)
        path = mergeSemiAdjacent(path)
        lenpath = lenPath(path)
        if lenpath == oldpath:
            break
        oldpath = lenpath
    return lenpath


tt = {
    'ne,ne,ne': 3,
    'ne,ne,sw,sw': 0,
    'ne,ne,s,s': 2,
    'se,sw,se,sw,sw': 3
}
for k, v in tt.items():
    result = getShortestPath(k)
    if result != v:
        print("FAIL: input ", k, ": expected ", v, ", got ", result, sep="")

# The input is not checked for sanity, just existence.
stepstrs = sys.stdin.readlines()
if len(stepstrs) == 0:
    print("stepstrs missing!")
    sys.exit(1)

print(getShortestPath(stepstrs[0]))
