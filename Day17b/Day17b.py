#!/usr/bin/python3

import sys 

# spinlock

# starts with circular buffer containing only 0
# current position is 0
# step forward X steps (puzzle input defines X)
# insert next value (which is 1)
# this new value is current position
# repeat until 50000000 is inserted (really)
# return the value *after* 0 was inserted
# hah -- that's whenever the position becomes 0

def work(steps):
    ist = int(steps)
    lenbuf = 1
    pos = 0
    recent = -1
    for i in range(0, 50000000):
        pos = (pos + ist + 1) % lenbuf
        if pos == 0:
            recent = i + 1
        lenbuf += 1
    return recent

# Unit tests for work.
tt = {
#    'x': ('3\n', 638),
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
