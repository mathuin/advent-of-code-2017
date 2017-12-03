#!/usr/bin/python3

import sys
import math


# Each square on the grid is allocated in a spiral pattern starting at a
# location marked 1 and then ringing up while spiraling outward. For
# example, the first few squares are allocated like this:
#
# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23---> ...
#
# While this is very space-efficient (no squares are skipped), requested data
# must be carried back to square 1 (the location of the only access port for
# this memory system) by programs that can only move up, down, left, or
# right. They always take the shortest path: the Manhattan Distance between
# the location of the data and square 1.
def steps(square):
    # Comes in as a string, need it as a number.
    sq = int(square)
    # Square 1 is a special case.
    if sq == 1:
        return 0
    # Rings are numbered by odd squares, counting from zero.
    # 1 is in ring 0, because 1 (sqrt(1)) is the zeroth odd square.
    # 2-9 are in ring 1, because 3 (sqrt(9)) is the second odd square.
    root = math.ceil(math.sqrt(sq))
    # If the square is even, must add one!
    oddsq = root+1 if root % 2 == 0 else root
    # Ring is nth odd square.
    ring = (oddsq-1)//2

    # Rings are composed of four equal sequences.
    # Counting backwards from the maximum, the sequences:
    # start at 2*ring,
    # decrement 1 to ring, then
    # increment to 2*ring-1

    inseq = (oddsq*oddsq - sq) % (2*ring)
    if inseq < ring:
        return 2*ring - inseq
    else:
        return inseq


# Unit tests for steps.
tt = {'1': 0, '12': 3, '23': 2, '1024': 31}
for k, v in tt.items():
    result = steps(k)
    if result != v:
        print("FAIL: input ", k, ": expected ", v, ", got ", result, sep="")


# The input is not checked for sanity, just existence.
square = sys.stdin.readlines()
if len(square) == 0:
    print("square missing!")
    sys.exit(1)

# Only one line, and I don't want the newline character.
print(steps(square[0][:-1]))
