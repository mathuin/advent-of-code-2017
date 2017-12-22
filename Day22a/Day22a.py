#!/usr/bin/python3

import sys

# sporifica virus

# read lines as grid
# # is infected, . is clean
# virus carrier has node and direction
# initial position is center of grid, direction is up
# once every burst:
# - if current node is infected, it turns to the right,
#   otherwise turns to the left
# - if current node is clean, it becomes infected, else
#   it becomes clean
# - moves forward one node
# after 10000 bursts, how many resulted in an infection?


dirs = ["up", "right", "down", "left"]


def goUp(pt):
    return (pt[0]-1, pt[1])


def goRight(pt):
    return (pt[0], pt[1]+1)


def goDown(pt):
    return (pt[0]+1, pt[1])


def goLeft(pt):
    return (pt[0], pt[1]-1)

go = {
    "up": goUp,
    "right": goRight,
    "down": goDown,
    "left": goLeft,
}


def work(lines):
    grid = {}
    midptval = (len(lines)+1)//2-1
    for i, line in enumerate(lines):
        for j, elem in enumerate(list(line)):
            if elem == '#':
                grid[(i, j)] = elem
    viruspt = (midptval, midptval)
    virusdir = "up"
    infections = 0
    for iter in range(0, 10000):
        if viruspt in grid:
            turn = 1
            del grid[viruspt]
        else:
            turn = -1
            grid[viruspt] = '#'
            infections += 1
        virusdir = dirs[(dirs.index(virusdir)+turn) % len(dirs)]
        viruspt = go[virusdir](viruspt)
    return infections


# Test case for work.
tt = {'x': (['..#\n', '#..\n', '...\n'], 5587)}

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
