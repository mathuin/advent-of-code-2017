#!/usr/bin/python3

import sys

# a series of tubes

# trace the line drawing from the top of the screen to its end.
# report the letters encountered along the way.


def moveUp(pt):
    return (pt[0]-1, pt[1])


def moveDown(pt):
    return (pt[0]+1, pt[1])


def moveLeft(pt):
    return (pt[0], pt[1]-1)


def moveRight(pt):
    return (pt[0], pt[1]+1)


move = {
    "up": moveUp,
    "down": moveDown,
    "left": moveLeft,
    "right": moveRight
}


def pipeMove(grid, pt, dir):
    nxt = move[dir](pt)
    if nxt in grid:
        return nxt
    return None


def plusMove(grid, pt, dir):
    dirs = ["up", "left", "down", "right"]
    back = dirs[(dirs.index(dir)+2) % len(dirs)]
    for mdir in move:
        if mdir == back:
            continue
        nxt = move[mdir](pt)
        if nxt in grid:
            return (nxt, mdir)
    return (None, None)


def readGrid(lines):
    grid = {}
    for i, line in enumerate(lines):
        for j, char in enumerate(list(line.rstrip())):
            if char == ' ':
                continue
            grid[(i, j)] = char
    return grid


def work(lines):
    waypoints = ""
    dir = "down"

    grid = readGrid(lines)
    for k, v in grid.items():
        if k[0] == 0:
            pt = k

    while True:
        if grid[pt] == '|' or grid[pt] == '-':
            nxt = pipeMove(grid, pt, dir)
            if nxt:
                pt = nxt
            else:
                break
        elif grid[pt] == '+':
            nxt, newdir = plusMove(grid, pt, dir)
            if nxt:
                pt = nxt
                dir = newdir
            else:
                break
        else:
            waypoints += grid[pt]
            nxt = pipeMove(grid, pt, dir)
            if nxt:
                pt = nxt
            else:
                break

    return waypoints


# Unit tests for work.
tt = {
    'x': ([
        '     |          \n',
        '     |  +--+    \n',
        '     A  |  C    \n',
        ' F---|----E|--+ \n',
        '     |  |  |  D \n',
        '     +B-+  +--+ \n',
        ], 'ABCDEF'),
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
