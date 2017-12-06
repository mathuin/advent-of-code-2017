#!/usr/bin/python3

import sys


# An urgent interrupt arrives from the CPU: it's trapped in a maze of jump
# instructions, and it would like assistance from any programs with spare
# cycles to help find the exit.
#
# The message includes a list of the offsets for each jump. Jumps are
# relative: -1 moves to the previous instruction, and 2 skips the next one.
# Start at the first instruction in the list. The goal is to follow the jumps
# until one leads outside the list.
#
# In addition, these instructions are a little strange; after each jump, the
# offset of that instruction increases by 1. So, if you come across an offset
# of 3, you would move three instructions forward, but change it to a 4 for
# the next time it is encountered.
#
# For example, consider the following list of jump offsets:
#
# 0
# 3
# 0
# 1
# -3
#
# Positive jumps ("forward") move downward; negative jumps move upward. For
# legibility in this example, these offset values will be written all on one
# line, with the current instruction marked in parentheses. The following
# steps would be taken before an exit is found:
#
# (0) 3  0  1  -3  - before we have taken any steps.
# (1) 3  0  1  -3  - jump with offset 0 (that is, don't jump at all).
# Fortunately, the instruction is then incremented to 1.
#  2 (3) 0  1  -3  - step forward because of the instruction we just
# modified. The first instruction is incremented again, now to 2.
#  2  4  0  1 (-3) - jump all the way to the end; leave a 4 behind.
#  2 (4) 0  1  -2  - go back to where we just were; increment -3 to -2.
#  2  5  0  1  -2  - jump 4 steps forward, escaping the maze.
#
# In this example, the exit is reached in 5 steps.
#
# How many steps does it take to reach the exit?
def steps(maze):
    offsets = [int(x.rstrip('\n')) for x in maze]
    # print("len(offsets): ", len(offsets))
    pos = 0
    count = 0
    while (pos < len(offsets) and pos >= 0):
        # print("count:", count, "pos:", pos, "value:", offsets[pos])
        jump = offsets[pos]
        offsets[pos] += 1
        pos += jump
        count += 1
    return count

# Unit tests for steps.
tt = {'x': (['0\n', '3\n', '0\n', '1\n', '-3\n'], 5)}
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
