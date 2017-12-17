#!/usr/bin/python3

import sys

# permutation promenade

# sixteen programs in total, a through p, in positions 0 through 15.

# three dance steps:
# - spin - sX - move X programs from the end to the front (s3 : abcde -> cdeab)
# - exchange - xA/B - swap programs at positions A and B
# - partner - pA/B - swap programs *named* A and B


def spin(line, count):
    ic = -1*int(count)
    return line[ic:] + line[:ic]


def exchange(line, a, b):
    ia = int(a)
    ib = int(b)
    ll = list(line)
    swap = ll[ia]
    ll[ia] = ll[ib]
    ll[ib] = swap
    return ''.join(ll)

def partner(line, a, b):
    return exchange(line, line.index(a), line.index(b))

opdict = {
    's': spin,
    'x': exchange,
    'p': partner,
}


def work(count, steps):
    if count == 5:
        line = 'abcde'
    else:
        line = 'abcdefghijklmnop'
    dance = steps.rstrip().split(',')
    for step in dance:
        opcode = step[0]
        args = step[1:].split('/')
        line = opdict[step[0]](line, *step[1:].split('/'))
    return line


# Unit tests for dance.
tt = {
    'x': (5, "s1,x3/4,pe/b\n", "baedc")
}
for k, v in tt.items():
    result = work(v[0], v[1])
    if result != v[2]:
        print("FAIL: input ", v[0], v[1], ": expected ", v[2], ", got ", result, sep="")

# The input is not checked for sanity, just existence.
steps = sys.stdin.readlines()
if len(steps) == 0:
    print("steps missing!")
    sys.exit(1)

print(work(16, steps[0]))

