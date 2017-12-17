#!/usr/bin/python3

import sys 

# spinlock

# starts with circular buffer containing only 0
# current position is 0
# step forward X steps (puzzle input defines X)
# insert next value (which is 1)
# this new value is current position
# repeat until 2017 is inserted
# return the value *after* 2017 was inserted

def work(steps):
    ist = int(steps)
    buf = [0]
    pos = 0
    for i in range(0, 2017):
        pos = (pos + ist + 1) % len(buf)
        buf.insert(pos, i + 1)
    return buf[(pos + 1) % len(buf)]

# Unit tests for work.
tt = {
    'x': ('3\n', 638),
}

for k, v in tt.items():
    result = work(v[0])
    if result != v[1]:
        print("FAIL: input ", v[0], ": expected ", v[1], ", got ", result, sep="")

# The input is not checked for sanity, just existence.
steps = sys.stdin.readlines()
if len(steps) == 0:
    print("lines missing!")
    sys.exit(1)

print(work(steps[0]))
