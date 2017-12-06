#!/usr/bin/python3

import sys


# Now, the jumps are even stranger: after each jump, if the offset was three
# or more, instead decrease it by 1. Otherwise, increase it by 1 as before.
#
# Using this rule with the above example, the process now takes 10 steps, and
# the offset values after finding the exit are left as 2 3 2 3 -1.
#
# How many steps does it now take to reach the exit?
def steps(maze):
    offsets = [int(x.rstrip('\n')) for x in maze]
    # print("len(offsets): ", len(offsets))
    pos = 0
    count = 0
    while (pos < len(offsets) and pos >= 0):
        # print("count:", count, "pos:", pos, "value:", offsets[pos])
        jump = offsets[pos]
        if jump >=3:
            offsets[pos] -= 1
        else:
            offsets[pos] += 1
        pos += jump
        count += 1
    return count

# Unit tests for steps.
tt = {'x': (['0\n', '3\n', '0\n', '1\n', '-3\n'], 10)}
for k, v in tt.items():
    result = steps(v[0])
    if result != v[1]:
        print("FAIL: input ", v[0], ": expected ", v[1], ", got ", result, sep="")


# The input is not checked for sanity, just existence.
maze = sys.stdin.readlines()
if len(maze) == 0:
    print("maze missing!")
    sys.exit(1)

# Only one line, and I don't want the newline character.
print(steps(maze))
