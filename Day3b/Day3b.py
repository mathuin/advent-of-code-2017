#!/usr/bin/python3

import sys


# As a stress test on the system, the programs here clear the grid and then
# store the value 1 in square 1. Then, in the same allocation order as shown
# above, they store the sum of the values in all adjacent squares, including
# diagonals.
#
# So, the first few squares' values are chosen as follows:
#
#  - Square 1 starts with the value 1.
#  - Square 2 has only one adjacent filled square (with value 1), so it
#    also stores 1.
#  - Square 3 has both of the above squares as neighbors and stores the sum
#    of their values, 2.
#  - Square 4 has all three of the aforementioned squares as neighbors and
#    stores the sum of their values, 4.
#  - Square 5 only has the first and fourth squares as neighbors, so it
#    gets the value 5.
#
# Once a square is written, its value does not change. Therefore, the first
# few squares would receive the following values:
#
# 147  142  133  122   59
# 304    5    4    2   57
# 330   10    1    1   54
# 351   11   23   25   26
# 362  747  806--->   ...
#
# What is the first value written that is larger than your puzzle input?
def larger(square):
    # Comes in as a string, need it as a number.
    sq = int(square)

    # Have to step around the array in order:
    # right, up, left, down
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    dirp = len(dirs)-1

    # Neighbors
    neighvals = [-1, 0, 1]
    neighbors = [(i, j) for i in neighvals for j in neighvals]

    # Initial conditions
    currVal = 1
    currLoc = (0, 0)
    grid = {currLoc: currVal}

    # While the current value is less than the desired value:
    while currVal < sq:
        # Is next direction free?
        nextDir = (dirp + 1) % len(dirs)
        if nextLoc(currLoc, dirs[nextDir]) not in grid:
            dirp = nextDir
        # Move in desired direction.
        currLoc = nextLoc(currLoc, dirs[dirp])
        # Calculate new value for this location and store it.
        currVal = sum(grid[nextLoc(currLoc, neighbor)]
                      for neighbor in neighbors
                      if nextLoc(currLoc, neighbor) in grid)
        grid[currLoc] = currVal
    return currVal


# nextLoc returns the next location after stepping in the specified direction.
def nextLoc(loc, dir):
    return (loc[0]+dir[0], loc[1]+dir[1])

# Unit tests for steps.
tt = {'3': 4, '12': 23, '25': 26, '512': 747}
for k, v in tt.items():
    result = larger(k)
    if result != v:
        print("FAIL: input ", k, ": expected ", v, ", got ", result, sep="")


# The input is not checked for sanity, just existence.
square = sys.stdin.readlines()
if len(square) == 0:
    print("square missing!")
    sys.exit(1)

# Only one line, and I don't want the newline character.
print(larger(square[0][:-1]))
