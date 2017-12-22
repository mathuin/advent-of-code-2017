#!/usr/bin/python3

import sys

# sporifica virus

# read lines as grid
# # is infected, . is clean
# new: W is weakened, F is flagged
# virus carrier has node and direction
# initial position is center of grid, direction is up
# once every burst:
# - turns:
#   - clean: left
#   - weakened: no turn
#   - infected: right
#   - flagged: reverse
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

turns = {
    '.': -1,
    'W': 0,
    '#': +1,
    'F': +2,
}

nodes = {
    '.': 'W',
    'W': '#',
    '#': 'F',
    'F': '.'
}


def work(lines):
    grid = {}
    midptval = (len(lines)+1)//2-1
    for i, line in enumerate(lines):
        for j, elem in enumerate(list(line)):
            if elem in nodes:
                grid[(i, j)] = elem
    viruspt = (midptval, midptval)
    virusdir = "up"
    infections = 0
    for iter in range(0, 10000000):
        node = grid[viruspt] if viruspt in grid else '.'
        if node == 'W':
            infections += 1
        virusdir = dirs[(dirs.index(virusdir)+turns[node]) % len(dirs)]
        grid[viruspt] = nodes[node]
        viruspt = go[virusdir](viruspt)
    return infections


# Test case for work.
tt = {'x': (['..#\n', '#..\n', '...\n'], 2511944)}

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
