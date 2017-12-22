#!/usr/bin/python3

import sys
from math import sqrt

# fractal art

# starts with grid:
# .#.
# ..#
# ###
# where # is on and . is off
# this grid is size 3 (3x3)

# if size is evenly divisible by 2:
# break pixels up into 2x2 squares
# convert 2x2 square into 3x3 square following rules
# rotating and flipping 2x2 square as necessary
# if size is evenly divisible by 3:
# break pixels up into 3x3 squares
# convert 3x3 square into 4x4 square following rules
# rotating and flipping 3x3 square as necessary.


def buildRules(lines):
    template = {
        4: [
            # 0 degrees
            [0, 1, 2, 3, ],
            # 90 degrees ccw
            [1, 3, 0, 2, ],
            # 180 degrees ccw
            [3, 2, 1, 0, ],
            # 270 degrees ccw
            [2, 0, 3, 1, ],
            # horizontal flip
            [2, 3, 0, 1, ],
            # vertical flip
            [1, 0, 3, 2, ],
            # 90 degrees ccw horizontal flip
            [0, 2, 1, 3, ],
            # 90 degrees ccw vertical flip
            [3, 1, 2, 0, ],
        ],
        9: [
            # 0 degrees
            [0, 1, 2, 3, 4, 5, 6, 7, 8, ],
            # 90 degrees ccw
            [2, 5, 8, 1, 4, 7, 0, 3, 6, ],
            # 180 degrees ccw
            [8, 7, 6, 5, 4, 3, 2, 1, 0, ],
            # 270 degrees ccw
            [6, 3, 0, 7, 4, 1, 8, 5, 2, ],
            # horizontal flip
            [6, 7, 8, 3, 4, 5, 0, 1, 2, ],
            # vertical flip
            [2, 1, 0, 5, 4, 3, 8, 7, 6, ],
            # 90 degrees ccw horizontal flip
            [0, 3, 6, 1, 4, 7, 2, 5, 8, ],
            # 90 degrees ccw vertical flip
            [8, 5, 2, 7, 4, 1, 6, 3, 0, ],
        ]
    }
    rules = {}
    for line in lines:
        inrule, arrow, outrule = line.rstrip().split()
        elems = list(''.join(inrule.split('/')))
        outelems = list(''.join(outrule.split('/')))
        for pat in template[len(elems)]:
            newin = ''.join([elems[i] for i in pat])
            rules[newin] = outelems
    return rules


def work(lines, iters):
    rules = buildRules(lines)
    start = '.#...####'
    grid = {(i // 3, i % 3): value for i, value in enumerate(start)}
    for iter in range(0, iters):
        newgrid = {}
        if len(grid) % 4 == 0:
            squares = int(sqrt(len(grid)/4))
            side = 2
            nextside = 3
        elif len(grid) % 9 == 0:
            squares = int(sqrt(len(grid)/9))
            side = 3
            nextside = 4
        else:
            print("panic, len(grid) = ", len(grid))
        for row in range(0, squares):
            for col in range(0, squares):
                pat = ''.join([grid[(i, j)] for i in range(row*side, row*side+side) for j in range(col*side, col*side+side)])
                if pat in rules:
                    pass
                else:
                    print("panic, pat {} not in rules".format(pat))
                    return None
                nextgrid = {(row*nextside+(i//nextside), col*nextside+(i % nextside)): value for i, value in enumerate(rules[pat])}
                newgrid.update(nextgrid)
        grid = newgrid
    return len([i for i in grid.values() if i == '#'])

# Test case for work.
tt = {
    'x': (
        ['../.# => ##./#../...\n', '.#./..#/### => #..#/..../..../#..#\n'],
        2, 12
    )
}

for k, v in tt.items():
    result = work(v[0], v[1])
    if result != v[2]:
        print("FAIL: input ", v[0], v[1], ": expected ", v[2], ", got ", result, sep="")

# The input is not checked for sanity, just existence.
lines = sys.stdin.readlines()
if len(lines) == 0:
    print("lines missing!")
    sys.exit(1)

print(work(lines, 18))
